from __future__ import annotations

from dataclasses import dataclass
from typing import Any, AsyncIterator

from ollama import AsyncClient

from agent.config import AppConfig


@dataclass(slots=True)
class ModelInfo:
    name: str
    size: int | None = None
    modified_at: str | None = None
    family: str | None = None
    format: str | None = None


class OllamaClient:
    def __init__(self, config: AppConfig):
        self.config = config
        self._client = AsyncClient(host=config.ollama.host)

    async def list_models(self) -> list[ModelInfo]:
        response = await self._client.list()
        models = _response_models(response)
        return [
            ModelInfo(
                name=str(model.get("model", "")),
                size=_as_int(model.get("size")),
                modified_at=_as_text(model.get("modified_at")),
                family=_as_text(_nested_detail(model, "family")),
                format=_as_text(_nested_detail(model, "format")),
            )
            for model in models
            if model.get("model")
        ]

    async def complete(self, messages: list[dict[str, str]], model: str | None = None) -> str:
        response = await self._client.chat(
            model=model or self.config.ollama.model,
            messages=messages,
        )
        return _response_content(response)

    async def stream_chat(
        self,
        messages: list[dict[str, str]],
        model: str | None = None,
    ) -> AsyncIterator[str]:
        stream = await self._client.chat(
            model=model or self.config.ollama.model,
            messages=messages,
            stream=True,
        )
        async for chunk in stream:
            content = _chunk_content(chunk)
            if content:
                yield content


def _response_models(response: Any) -> list[dict[str, Any]]:
    if isinstance(response, dict):
        return list(response.get("models", []))
    models = getattr(response, "models", None)
    return list(models or [])


def _response_content(response: Any) -> str:
    if isinstance(response, dict):
        message = response.get("message", {})
        if isinstance(message, dict):
            return str(message.get("content", ""))
        return str(getattr(message, "content", ""))
    message = getattr(response, "message", None)
    if message is None:
        return ""
    return str(getattr(message, "content", ""))


def _chunk_content(chunk: Any) -> str:
    if isinstance(chunk, dict):
        message = chunk.get("message", {})
        if isinstance(message, dict):
            return str(message.get("content", ""))
        return str(getattr(message, "content", ""))
    message = getattr(chunk, "message", None)
    if message is None:
        return ""
    return str(getattr(message, "content", ""))


def _nested_detail(model: dict[str, Any], key: str) -> Any:
    details = model.get("details", {})
    if isinstance(details, dict):
        return details.get(key)
    return getattr(details, key, None)


def _as_text(value: Any) -> str | None:
    if value is None:
        return None
    return str(value)


def _as_int(value: Any) -> int | None:
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None
