# Search Plugin

## Nombre
Search Plugin

## Descripción
Plugin de búsqueda mejorada con contexto semántico. Permite buscar código con significado, no solo con patrones de texto. Integra múltiples herramientas de búsqueda para resultados comprehensivos.

## Uso
Para buscar código con contexto semántico. Se activa cuando el usuario necesita encontrar código basado en funcionalidad, estructura o relaciones, no solo por nombre de archivo o contenido textual.

## Capacidades

### Búsqueda Semántica
- Búsqueda por significado del código
- Encontrar funciones por su propósito
- Localizar código relacionado por funcionalidad
- Búsqueda en lenguaje natural

### Búsqueda por Estructura
- Encontrar patrones arquitectónicos
- Localizar puntos de entrada
- Buscar por tipo de archivo
- Encontrar relaciones entre componentes

### Búsqueda por Dependencias
- Rastrear llamadas a funciones
- Encontrar dependencias circulares
- Localizar puntos de acoplamiento
- Análisis de impacto de cambios

### Integración con codebase-memory
- Consultas complejas en el grafo de conocimiento
- Búsqueda enriquecida con contexto histórico
- Resultados priorizados por relevancia

## Herramientas

### grep
- Búsqueda de patrones de texto en archivos
- Soporte para expresiones regulares
- Filtrado por tipo de archivo

### glob
- Búsqueda de archivos por patrones de nombre
- Navegación de estructura de directorios
- Encontrar archivos por extensión

### codebase-memory
- `search_code`: Búsqueda enriquecida con contexto del grafo
- `search_graph`: Búsqueda en el grafo de conocimiento
- `trace_path`: Rastreo de relaciones entre funciones
- `query_graph`: Consultas Cypher complejas

## Ejemplos de Uso

### Ejemplo 1: Buscar por funcionalidad
```
Encuentra todas las funciones que manejan autenticación en el proyecto.
```

### Ejemplo 2: Buscar por estructura
```
Busca todos los archivos de configuración de TypeScript en el proyecto.
```

### Ejemplo 3: Buscar dependencias
```
Encuentra todas las funciones que llaman a la función `processPayment`.
```

### Ejemplo 4: Búsqueda semántica
```
Busca código que implemente lógica de caché en el proyecto.
```

### Ejemplo 5: Análisis de impacto
```
Si cambio la función `getUserById`, ¿qué otros archivos se verán afectados?
```

## Configuración

```json
{
  "search-plugin": {
    "enabled": true,
    "default_mode": "semantic",
    "include_tests": false,
    "max_results": 50,
    "context_lines": 3
  }
}
```
