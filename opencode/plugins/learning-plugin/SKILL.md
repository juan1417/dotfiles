# Learning Plugin

## Nombre
Learning Plugin

## Descripción
Plugin de aprendizaje que analiza patrones del codebase para aprender convenciones, estilos y arquitecturas del proyecto. Genera sugerencias adaptativas basadas en el historial de código.

## Uso
Para aprender convenciones y patrones del proyecto. Se activa cuando el usuario necesita comprender estilos de código existentes, detectar inconsistencias o recibir sugerencias basadas en el historial del proyecto.

## Capacidades

### Análisis de Patrones de Código
- Detección de patrones arquitectónicos (MVC, Clean Architecture, etc.)
- Identificación de convenciones de naming (camelCase, snake_case, etc.)
- Análisis de estructura de directorios
- Detección de patrones de diseño utilizados

### Aprendizaje de Convenciones
- Extracción de reglas de estilo del proyecto
- Identificación de dependencias y frameworks preferidos
- Análisis de convenciones de testing
- Detección de patrones de error handling

### Sugerencias Adaptativas
- Recomendaciones basadas en código existente
- Sugerencias de refactorización según patrones detectados
- Alertas de inconsistencias con el estilo del proyecto
- Propuestas de estructura basadas en convenciones existentes

### Persistencia de Aprendizaje
- Almacenamiento de patrones aprendidos en codebase-memory
- Evolución del aprendizaje a lo largo del tiempo
- Contexto histórico para mejores sugerencias

## Integración

### Herramientas Utilizadas
- `codebase-memory`: Para almacenar y recuperar patrones aprendidos
- `codebase-memory_search_code`: Para analizar código existente
- `codebase-memory_get_architecture`: Para comprender estructura del proyecto
- `codebase-memory_query_graph`: Para consultas complejas de patrones

### Flujo de Trabajo
1. Analizar el codebase actual
2. Extraer patrones y convenciones
3. Almacenar en codebase-memory
4. Generar sugerencias basadas en patrones aprendidos

## Ejemplos de Uso

### Ejemplo 1: Analizar convenciones del proyecto
```
Analiza las convenciones de naming utilizadas en el proyecto y genera una guía de estilos.
```

### Ejemplo 2: Detectar inconsistencias
```
Revisa el código reciente y detecta inconsistencias con los patrones establecidos del proyecto.
```

### Ejemplo 3: Sugerir refactorización
```
Basado en los patrones aprendidos, sugiere refactorizaciones para el archivo src/services/api.ts.
```

### Ejemplo 4: Aprender de cambios recientes
```
Analiza los últimos commits y actualiza los patrones aprendidos del proyecto.
```

## Configuración

```json
{
  "learning-plugin": {
    "enabled": true,
    "auto_analyze": true,
    "persistence": true,
    "update_frequency": "on_change"
  }
}
```
