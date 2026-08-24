# SDD Workflow Plugin

## Nombre
SDD Workflow

## Descripción
Plugin de automatización del flujo completo de Spec-Driven Development (SDD). Coordina y gestiona todas las fases del desarrollo basado en especificaciones, desde la exploración inicial hasta la verificación final.

## Uso
Se activa cuando el usuario solicita:
- Implementar una nueva feature usando SDD
- Coordinar un flujo de desarrollo completo
- Gestionar transiciones entre fases SDD
- Validar progreso y estado del proyecto

## Capacidades

### 1. Automatización de Flujo SDD
```
Explotation → Specification → Design → Planning → Implementation → Verification
```

### 2. Tracking de Progreso
- Estado actual del proyecto
- Fases completadas vs pendientes
- Bloqueantes activos
- Métricas de progreso

### 3. Validación de Transiciones
- Verificar prerequisitos antes de cambiar de fase
- Asegurar calidad en cada transición
- Prevenir saltos no válidos

### 4. Gestión de Estado
```
┌─────────────────────────────────────────────────────────┐
│  ESTADOS SDD                                            │
├─────────────────────────────────────────────────────────┤
│  exploration → specification → design → planning        │
│       ↓             ↓            ↓          ↓           │
│  development → testing → deployment → completed         │
└─────────────────────────────────────────────────────────┘
```

## Herramientas
- `codebase-memory`: Persistencia de estado del proyecto
- `todowrite`: Tracking de tareas por fase
- `task`: Delegación a subagentes especializados

## Flujo de Trabajo

### Paso 1: Inicializar Proyecto
```markdown
1. Crear estado inicial en codebase-memory
2. Definir fases requeridas
3. Establecer criterios de éxito por fase
4. Inicializar tracking de progreso
```

### Paso 2: Ejecutar Fase
```markdown
1. Validar prerequisitos de la fase
2. Delegar a subagente apropiado
3. Recopilar resultados
4. Validar criterios de éxito
5. Actualizar estado
```

### Paso 3: Transicionar
```markdown
1. Verificar completitud de fase actual
2. Validar calidad del entregable
3. Actualizar estado en codebase-memory
4. Notificar transición
5. Iniciar siguiente fase
```

## Ejemplos de Uso

### Ejemplo 1: Feature Completa
```
Usuario: "Implementar autenticación JWT usando SDD"
Plugin: 
1. Inicializa proyecto en codebase-memory
2. Ejecuta exploration → @architect analiza codebase
3. Ejecuta specification → @po crea especificación
4. Ejecuta design → @architect diseña solución
5. Ejecuta planning → @po planifica tareas
6. Ejecuta implementation → @developer implementa
7. Ejecuta verification → @qa valida
8. Marca proyecto como completado
```

### Ejemplo 2: Bug Fix
```
Usuario: "Corregir bug en login usando SDD"
Plugin:
1. Ejecuta exploration → @developer analiza bug
2. Ejecuta specification → @po define fix
3. Ejecuta implementation → @developer corrige
4. Ejecuta verification → @qa valida fix
```

### Ejemplo 3: Status Check
```
Usuario: "¿Cómo va el proyecto?"
Plugin:
1. Lee estado desde codebase-memory
2. Muestra fase actual
3. Lista tareas completadas
4. Identifica bloqueantes
5. Sugiere próximos pasos
```

## Integración con Subagentes

| Fase | Subagente | Responsabilidad |
|------|-----------|-----------------|
| Exploration | `@architect` | Analizar codebase |
| Specification | `@po` | Crear especificación |
| Design | `@architect` | Diseñar solución |
| Planning | `@po` | Planificar tareas |
| Implementation | `@developer` | Implementar código |
| Verification | `@qa` | Validar calidad |
| Quality Control | `@qc` | Auditar código |

## Métricas de Progreso

```markdown
## Dashboard del Proyecto

### Estado General
- **Fase actual**: Design
- **Progreso**: 45%
- **Bloqueantes**: 0
- **Calidad**: 85%

### Por Fase
- [x] Exploration (100%)
- [x] Specification (100%)
- [ ] Design (75%)
- [ ] Planning (0%)
- [ ] Implementation (0%)
- [ ] Verification (0%)
```

## Configuración

```json
{
  "sdd-workflow": {
    "enabled": true,
    "auto_transitions": true,
    "quality_gates": true,
    "notifications": true
  }
}
```

## Convenciones

1. **Siempre usar codebase-memory** para persistir estado
2. **Validar calidad** antes de cada transición
3. **Documentar decisiones** en cada fase
4. **Notificar cambios** de estado
5. **Mantener tracking** actualizado
