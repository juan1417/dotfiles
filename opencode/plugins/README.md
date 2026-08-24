# Sistema de Plugins de OpenCode

## Descripción

El sistema de plugins de OpenCode permite extender las capacidades del asistente con módulos especializados. Los plugins se cargan automáticamente cuando el usuario los invoca mediante el nombre del plugin o cuando el contexto lo requiere.

## Estructura

```
plugins/
├── learning-plugin/
│   └── SKILL.md
├── search-plugin/
│   └── SKILL.md
└── README.md
```

## Plugins Disponibles

### Learning Plugin
Plugin de aprendizaje que analiza patrones del codebase para aprender convenciones y generar sugerencias adaptativas.

- **Uso**: Analizar convenciones, detectar inconsistencias, sugerir refactorizaciones
- **Integración**: codebase-memory
- **Documentación**: `learning-plugin/SKILL.md`

### Search Plugin
Plugin de búsqueda mejorada con contexto semántico para encontrar código por significado, estructura o dependencias.

- **Uso**: Buscar código con contexto, analizar dependencias, rastrear relaciones
- **Herramientas**: grep, glob, codebase-memory
- **Documentación**: `search-plugin/SKILL.md`

## Cómo Instalar Plugins

### 1. Crear Directorio
```bash
mkdir plugins/nombre-del-plugin
```

### 2. Crear SKILL.md
Cada plugin debe contener un archivo `SKILL.md` con la siguiente estructura mínima:

```markdown
# Nombre del Plugin

## Nombre
Nombre del Plugin

## Descripción
Descripción breve del plugin.

## Uso
Cuándo y cómo se utiliza el plugin.

## Capacidades
- Capacidad 1
- Capacidad 2
```

### 3. Registrar el Plugin
Los plugins se detectan automáticamente por la presencia del archivo `SKILL.md` en el directorio `plugins/`.

## Cómo Crear Plugins

### Estructura Recomendada

```
plugins/
└── mi-plugin/
    ├── SKILL.md          # Documentación principal (obligatorio)
    ├── config.json       # Configuración opcional
    └── scripts/          # Scripts auxiliares opcionales
        └── helper.sh
```

### Plantilla de SKILL.md

```markdown
# Mi Plugin

## Nombre
Mi Plugin

## Descripción
Descripción detallada de lo que hace el plugin.

## Uso
Cuándo se activa el plugin y cómo se utiliza.

## Capacidades
### Capacidad 1
Descripción de la capacidad.

### Capacidad 2
Descripción de la capacidad.

## Herramientas
- Herramienta 1: Descripción
- Herramienta 2: Descripción

## Ejemplos de Uso

### Ejemplo 1: Título
Descripción del ejemplo con código o instrucciones.

## Configuración
```json
{
  "mi-plugin": {
    "enabled": true
  }
}
```
```

### Convenciones

1. **Nomenclatura**: Usar guiones `-` en nombres de directorio (ej: `mi-plugin`)
2. **Documentación**: Cada plugin debe tener un `SKILL.md` completo
3. **Integración**: Preferir integración con `codebase-memory` para persistencia
4. **Modularidad**: Un plugin debe enfocarse en una funcionalidad específica

## Cómo Usar Plugins

### Invocación Directa
El usuario puede invocar un plugin directamente:
```
Usa el learning-plugin para analizar las convenciones del proyecto.
```

### Invocación por Contexto
El asistente puede sugerir el uso de un plugin cuando el contexto lo requiera:
```
Para esta tarea de búsqueda semántica, recomiendo usar el search-plugin.
```

### Configuración
Los plugins pueden configurarse en `opencode.json` o en su propio archivo `config.json`.

## Ejemplos de Uso

### Ejemplo 1: Análisis de Convenciones
```
Usuario: Analiza las convenciones de código del proyecto.
Asistente: [Usa learning-plugin] He analizado el proyecto y encontré las siguientes convenciones...
```

### Ejemplo 2: Búsqueda Semántica
```
Usuario: Encuentra todas las funciones que manejan errores de base de datos.
Asistente: [Usa search-plugin] He encontrado 15 funciones que manejan errores de base de datos...
```

### Ejemplo 3: Detección de Inconsistencias
```
Usuario: Revisa si hay inconsistencias en el estilo de código.
Asistente: [Usa learning-plugin + search-plugin] He detectado 3 inconsistencias principales...
```

## Desarrollo de Plugins

### Requisitos Mínimos
- Archivo `SKILL.md` con documentación completa
- Estructura de directorio limpia
- Integración con herramientas existentes

### Mejores Prácticas
1. Mantener documentación actualizada
2. Usar integración con `codebase-memory` para persistencia
3. Proporcionar ejemplos claros de uso
4. Incluir configuración por defecto razonable
5. Seguir convenciones de naming del proyecto

### Testing
Para probar un plugin:
1. Crear el directorio y archivos
2. Invocar el plugin desde el asistente
3. Verificar que las capacidades funcionan correctamente
4. Revisar la integración con otras herramientas

## Solución de Problemas

### Plugin no se carga
- Verificar que el archivo `SKILL.md` existe
- Revisar la sintaxis del markdown
- Comprobar que el directorio está en la ubicación correcta

### Integración con codebase-memory
- Verificar que codebase-memory está indexado
- Comprobar que los permisos de lectura/escritura son correctos
- Revisar los logs para errores de integración

## Enlaces

- [Documentación de OpenCode](https://opencode.ai)
- [Guía de Skills](https://opencode.ai/skills)
- [codebase-memory](https://opencode.ai/codebase-memory)
