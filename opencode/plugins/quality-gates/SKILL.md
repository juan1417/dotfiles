# Quality Gates Plugin

## Nombre
Quality Gates

## Descripción
Plugin de control de calidad que valida la calidad del código antes de cada transición en el flujo SDD. Verifica tests, coverage, deuda técnica y estándares de código.

## Uso
Se activa cuando el usuario solicita:
- Validar calidad antes de una transición
- Ejecutar quality gates
- Verificar coverage de tests
- Auditar deuda técnica
- Aprobar una fase del flujo SDD

## Capacidades

### 1. Validación por Fase
```markdown
## Quality Gates por Fase

### Exploration → Specification
- [ ] Codebase analizado
- [ ] Dependencias identificadas
- [ ] Puntos de integración mapeados

### Specification → Design
- [ ] Especificación completa
- [ ] Criterios de aceptación definidos
- [ ] Alcance clarificado

### Design → Planning
- [ ] Arquitectura definida
- [ ] Tecnologías seleccionadas
- [ ] Decisiones documentadas (ADR)

### Planning → Implementation
- [ ] Tareas planificadas
- [ ] Estimaciones realizadas
- [ ] Dependencias mapeadas

### Implementation → Verification
- [ ] Tests unitarios pasando
- [ ] Coverage mínimo alcanzado
- [ ] Code review completado
- [ ] Sin errores de linting

### Verification → Deployment
- [ ] Tests E2E pasando
- [ ] Performance aceptable
- [ ] Seguridad verificada
- [ ] Documentación actualizada
```

### 2. Verificación de Tests
```markdown
## Reporte de Tests

### Unit Tests
- **Total**: 150
- **Pasando**: 145 (96.7%)
- **Fallando**: 5 (3.3%)
- **Estado**: ⚠️ Requiere atención

### Integration Tests
- **Total**: 30
- **Pasando**: 30 (100%)
- **Estado**: ✅ Aprobado

### E2E Tests
- **Total**: 20
- **Pasando**: 18 (90%)
- **Fallando**: 2 (10%)
- **Estado**: ⚠️ Requiere atención
```

### 3. Verificación de Coverage
```markdown
## Reporte de Coverage

### General
- **Statements**: 85%
- **Branches**: 78%
- **Functions**: 90%
- **Lines**: 87%

### Por Módulo
| Módulo | Statements | Branches | Functions | Lines |
|--------|------------|----------|-----------|-------|
| auth | 95% | 90% | 100% | 96% |
| users | 88% | 82% | 92% | 89% |
| api | 80% | 75% | 85% | 81% |
| ui | 75% | 68% | 80% | 76% |

### Mínimos Requeridos
- Statements: 80% ✅
- Branches: 75% ✅
- Functions: 85% ✅
- Lines: 80% ✅
```

### 4. Auditoría de Deuda Técnica
```markdown
## Reporte de Deuda Técnica

### Resumen
- **Deuda total**: 45 días
- **Deuda crítica**: 10 días
- **Deuda mayor**: 20 días
- **Deuda menor**: 15 días

### Por Severidad
| Severidad | Deuda | Items |
|-----------|-------|-------|
| Crítica | 10 días | 3 |
| Mayor | 20 días | 8 |
| Menor | 15 días | 15 |

### Top Issues
1. **Duplicación de código** - 5 días
2. **Funciones complejas** - 3 días
3. **Dependencias desactualizadas** - 2 días
```

### 5. Verificación de Estándares
```markdown
## Verificación de Estándares

### Code Style
- **ESLint**: 0 errores, 5 warnings ✅
- **Prettier**: Formateo correcto ✅
- **Naming**: Convenciones seguidas ✅

### Architecture
- **Separación de concerns**: ✅
- **Dependency injection**: ✅
- **Error handling**: ⚠️ 2 pendientes

### Documentation
- **README actualizado**: ✅
- **JSDoc completado**: ⚠️ 80%
- **Changelog**: ✅
```

## Herramientas
- `bash`: Ejecutar tests y linting
- `read`: Leer reportes de coverage
- `codebase-memory`: Almacenar resultados
- `todowrite`: Tracking de issues

## Flujo de Trabajo

### Ejecutar Quality Gates
```markdown
1. Identificar fase actual
2. Ejecutar validaciones correspondientes
3. Recopilar resultados
4. Clasificar por severidad
5. Generar reporte
6. Decidir: Aprobar / Rechazar / Condicional
7. Presentar al usuario
```

### Aprobar Fase
```markdown
1. Verificar que todos los gates pasan
2. Documentar aprobación
3. Actualizar estado en codebase-memory
4. Notificar transición
```

### Rechazar Fase
```markdown
1. Identificar gates que fallaron
2. Clasificar issues por severidad
3. Generar plan de corrección
4. Notificar al usuario
5. Esperar correcciones
6. Re-ejecutar gates
```

## Ejemplos de Uso

### Ejemplo 1: Aprobación Completa
```
Usuario: "¿Paso el código la verificación de calidad?"
Plugin:
1. Ejecuta todos los quality gates
2. Todos pasan al 100%
3. Reporta: "✅ Código aprobado, todos los gates pasan"
```

### Ejemplo 2: Rechazo con Issues
```
Usuario: "¿Paso el código la verificación?"
Plugin:
1. Ejecuta quality gates
2. Falla: tests fallando, coverage bajo
3. Reporta: "❌ Código no aprobado"
4. Detalla: "5 tests fallando, coverage 75% (mínimo 80%)"
5. Sugiere: "Corregir tests y agregar más coverage"
```

### Ejemplo 3: Aprobación Condicional
```
Usuario: "¿Paso el código?"
Plugin:
1. Ejecuta quality gates
2. Pasa con warnings
3. Reporta: "⚠️ Aprobado condicionalmente"
4. Detalla: "3 warnings menores, 1 deuda técnica crítica"
5. Recomienda: "Corregir deuda técnica antes de producción"
```

## Formato de Reporte

```markdown
# Reporte de Quality Gates

**Proyecto**: [Nombre]
**Fecha**: [fecha]
**Fase**: Implementation → Verification
**Verificador**: @qa

---

## Resumen Ejecutivo

| Gate | Estado | Detalles |
|------|--------|----------|
| Tests Unitarios | ✅ | 150/150 pasando |
| Coverage | ✅ | 85% (mínimo 80%) |
| Linting | ⚠️ | 5 warnings |
| Code Review | ✅ | Aprobado |
| Seguridad | ✅ | Sin vulnerabilidades |

**Estado General**: ✅ APROBADO

---

## Detalle por Gate

### 1. Tests Unitarios ✅
- **Total**: 150
- **Pasando**: 150 (100%)
- **Fallando**: 0
- **Duración**: 45s

### 2. Coverage ✅
- **Statements**: 85% (mínimo: 80%)
- **Branches**: 78% (mínimo: 75%)
- **Functions**: 90% (mínimo: 85%)
- **Lines**: 87% (mínimo: 80%)

### 3. Linting ⚠️
- **Errores**: 0
- **Warnings**: 5
  - `line 15: unused variable` - warning
  - `line 23: missing dependency` - warning
  - `line 45: console.log` - warning
  - `line 67: any type` - warning
  - `line 89: magic number` - warning

### 4. Code Review ✅
- **Revisor**: @developer
- **Aprobado**: Sí
- **Comentarios**: 2 menores
- **Cambios solicitados**: Ninguno

### 5. Seguridad ✅
- **Vulnerabilidades**: 0
- **Dependencias con CVE**: 0
- **Secretos expuestos**: 0
- **Hardcoded secrets**: 0

---

## Recomendaciones

1. **Corregir warnings de linting** para limpieza de código
2. **Documentar variables no usadas** o eliminarlas
3. **Reemplazar console.log** con logging apropiado
4. **Tipar variables** correctamente
5. **Extraer magic numbers** a constantes

---

## Aprobación

**Estado**: ✅ APROBADO
**Condiciones**: Corregir warnings antes de merge
**Próxima verificación**: Después de correcciones
```

## Integración con Subagentes

| Gate | Subagente | Responsabilidad |
|------|-----------|-----------------|
| Tests | `@qa` | Ejecutar y validar tests |
| Coverage | `@qa` | Verificar coverage |
| Linting | `@qc` | Ejecutar linting |
| Code Review | `@qc` | Revisar código |
| Seguridad | `@qc` | Auditar seguridad |
| Documentación | `@devops` | Verificar docs |

## Configuración

```json
{
  "quality-gates": {
    "enabled": true,
    "strict_mode": false,
    "min_coverage": 80,
    "max_complexity": 10,
    "auto_fix": false,
    "notify_on_failure": true
  }
}
```

## Convenciones

1. **Siempre ejecutar gates** antes de transiciones
2. **Documentar todas las excepciones** aprobadas
3. **Re-ejecutar después de correcciones**
4. **Mantener historial** de quality gates
5. **No saltar gates** sin aprobación explícita
6. **Priorizar issues** por severidad
