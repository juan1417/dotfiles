# Backlog Manager Plugin

## Nombre
Backlog Manager

## Descripción
Plugin de gestión inteligente del backlog.md. Maneja historias de usuario, correcciones, mejoras y ajustes con auto-clasificación y reportes de progreso.

## Uso
Se activa cuando el usuario solicita:
- Agregar elementos al backlog
- Corregir o ajustar funcionalidades
- Ver progreso del backlog
- Generar reportes de estado
- Clasificar cambios (FIX/ENH/BUG/ADJUST)

## Capacidades

### 1. Auto-clasificación de Cambios
```markdown
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| FIX | Corrección de error | "El login no funciona" |
| ENH | Mejora adicional | "Agregar validación" |
| BUG | Comportamiento incorrecto | "Los datos no se guardan" |
| ADJUST | Ajuste de requerimientos | "Cambiar color de UI" |
```

### 2. Gestión de Historias de Usuario
```markdown
## Formato Estándar

- [ ] US-[ID]: [Descripción]
  - **Como** [usuario]
  - **Quiero** [funcionalidad]
  - **Para** [beneficio]
  - **Prioridad**: Alta/Media/Baja
  - **Estado**: Pendiente/En Progreso/Completada
  - **Criterios de Aceptación**: [lista]
```

### 3. Gestión de Correcciones
```markdown
## Formato Estándar

- [ ] [TIPO]-[ID]: [Descripción]
  - **Tipo**: Fix/Enhancement/Bug/Adjustment
  - **Prioridad**: Alta/Media/Baja
  - **Estado**: Pendiente
  - **Fecha**: [fecha]
  - **Descripción**: [detalles]
  - **Impacto**: [archivos afectados]
  - **Criterios**: [cómo validar]
```

### 4. Reportes de Progreso
```markdown
## Dashboard del Backlog

### Resumen
- **Total elementos**: 25
- **Completados**: 10 (40%)
- **En progreso**: 5 (20%)
- **Pendientes**: 10 (40%)

### Por Tipo
- Historias de usuario: 15
- Fixes: 5
- Mejoras: 3
- Bugs: 2

### Por Prioridad
- Alta: 8
- Media: 12
- Baja: 5
```

## Herramientas
- `read`: Leer backlog.md existente
- `edit`: Actualizar elementos
- `codebase-memory`: Persistir estado del backlog
- `todowrite`: Tracking de tareas

## Flujo de Trabajo

### Agregar Elemento al Backlog
```markdown
1. Leer backlog.md actual
2. Clasificar el cambio (FIX/ENH/BUG/ADJUST o US)
3. Asignar ID único
4. Agregar al backlog con formato estándar
5. Actualizar métricas
6. Confirmar al usuario
```

### Actualizar Estado
```markdown
1. Identificar elemento por ID
2. Actualizar estado (Pendiente → En Progreso → Completada)
3. Agregar notas si es necesario
4. Actualizar métricas
5. Notificar cambio
```

### Generar Reporte
```markdown
1. Leer backlog.md completo
2. Calcular métricas
3. Generar dashboard
4. Presentar al usuario
```

## Ejemplos de Uso

### Ejemplo 1: Agregar Fix
```
Usuario: "Agregar fix para el bug del login"
Plugin:
1. Clasifica como FIX
2. Asigna ID: FIX-001
3. Agrega al backlog.md
4. Confirma: "FIX-001 agregado al backlog"
```

### Ejemplo 2: Agregar Historia de Usuario
```
Usuario: "Como usuario quiero ver mi perfil"
Plugin:
1. Clasifica como US
2. Asigna ID: US-001
3. Agrega al backlog.md con formato estándar
4. Confirma: "US-001 agregada al backlog"
```

### Ejemplo 3: Ver Progreso
```
Usuario: "¿Cómo va el backlog?"
Plugin:
1. Lee backlog.md
2. Calcula métricas
3. Presenta dashboard
4. Muestra: "40% completado, 5 en progreso, 10 pendientes"
```

### Ejemplo 4: Actualizar Estado
```
Usuario: "Marcar US-001 como completada"
Plugin:
1. Encuentra US-001
2. Actualiza estado a "Completada"
3. Actualiza métricas
4. Confirma: "US-001 marcada como completada"
```

## Formato del Backlog

```markdown
# Backlog - [Nombre del Proyecto]

**Última actualización**: [fecha]
**Estado**: Activo

---

## Historias de Usuario

### Prioridad Alta
- [ ] US-001: Como usuario quiero hacer login para acceder a mi cuenta
  - **Criterios**: Autenticación JWT, manejo de errores
  - **Estado**: Pendiente
  - **Estimación**: 3 días

### Prioridad Media
- [ ] US-002: Como usuario quiero ver mi perfil para managing mis datos
  - **Criterios**: Edición de campos, validación
  - **Estado**: En Progreso
  - **Estimación**: 2 días

### Prioridad Baja
- [ ] US-003: Como usuario quiero cambiar mi contraseña
  - **Criterios**: Email de recuperación, validación
  - **Estado**: Pendiente
  - **Estimación**: 1 día

---

## Correcciones y Ajustes

### Fixes
- [ ] FIX-001: Corregir validación de email
  - **Tipo**: Fix
  - **Prioridad**: Alta
  - **Estado**: Pendiente
  - **Impacto**: RegisterForm.tsx

### Mejoras
- [ ] ENH-001: Agregar recordatorio de contraseña
  - **Tipo**: Enhancement
  - **Prioridad**: Media
  - **Estado**: Pendiente
  - **Impacto**: LoginForm.tsx

### Bugs
- [ ] BUG-001: Los datos no se guardan en Firefox
  - **Tipo**: Bug
  - **Prioridad**: Alta
  - **Estado**: En Progreso
  - **Impacto**: ProfileForm.tsx

### Ajustes
- [ ] ADJUST-001: Cambiar color de botón primario
  - **Tipo**: Adjustment
  - **Prioridad**: Baja
  - **Estado**: Pendiente
  - **Impacto**: theme.ts
```

## Integración con Obsidian

### Sincronización
```bash
# Sincronizar backlog con Obsidian
obsidian:sync-backlog [proyecto]

# Generar reporte en Obsidian
obsidian:generate-report [proyecto] --type=backlog

# Crear vista Kanban
obsidian:create-kanban [proyecto] --from=backlog
```

### Estructura en Obsidian
```
SDD-Vault/
├── 01-Planning/
│   └── backlog.md
├── 02-Proyectos/
│   └── [Nombre]/
│       └── backlog-sync.md
└── 03-Reports/
    └── backlog-report-[fecha].md
```

## Configuración

```json
{
  "backlog-manager": {
    "enabled": true,
    "auto_classify": true,
    "auto_id": true,
    "sync_obsidian": true,
    "notifications": true
  }
}
```

## Convenciones

1. **Siempre usar formato estándar** para elementos
2. **Asignar IDs únicos** automáticamente
3. **Clasificar TODOS los cambios** antes de agregar
4. **Actualizar métricas** después de cada cambio
5. **Sincronizar con Obsidian** cuando sea posible
6. **NUNCA crear archivos nuevos** - SIEMPRE agregar al backlog.md
