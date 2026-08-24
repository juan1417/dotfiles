---
name: QC Audit
description: Auditoría de código y calidad de software
location: C:\Users\juani\.config\opencode\skills\qc-audit\SKILL.md
---

# QC Audit

Auditoría de código, métricas de calidad y gestión de deuda técnica.

## Uso

Activar cuando el usuario necesite: auditar código, medir calidad, identificar deuda técnica, o generar reportes de estado.

## Métricas

### Deuda Técnica
- **Ratio**: Deuda técnica / Esfuerzo total
- **Tiempo estimado**: Horas para resolver toda la deuda
- **Tendencia**: Mejora o empeora con el tiempo
- **Hotspots**: Archivos con más deuda concentrada

### Cobertura de Código
- **Line coverage**: % de líneas ejecutadas por tests
- **Branch coverage**: % de branches ejecutados
- **Function coverage**: % de funciones probadas
- **Mínimo recomendado**: 80% general, 90% crítico

### Complejidad
- **Cyclomatic**: Número de caminos independientes (máx 10)
- **Cognitive**: Complejidad de comprensión (máx 15)
- **Halstead**: Esfuerzo basado en operadores/operandos
- **Lines of Code**: Tamaño de archivos/métodos

### Code Smells
- Duplicación de código
- Métodos muy largos (>30 líneas)
- Parámetros excesivos (>4)
- Clases con mucha responsabilidad
- Variables globales

## Pasos

1. **Recopilar código** - Analizar estructura completa
2. **Ejecutar métricas** - Usar herramientas de análisis
3. **Identificar problemas** - Clasificar por severidad
4. **Evaluar impacto** - Business impact de cada issue
5. **Generar reporte** - Documentar hallazgos
6. **Priorizar remediación** - Quick wins vs largo plazo

## Herramientas

- ESLint: Análisis estático JavaScript/TypeScript
- SonarQube: Análisis completo de calidad
- TypeScript Compiler: Type checking
- Istanbul: Cobertura de tests
- Dependency-cruiser: Análisis de dependencias

## Reportes

```markdown
# QC Report - [Fecha]

## Resumen Ejecutivo
- Score general: [A-F]
- Deuda técnica: [Horas estimadas]
- Cobertura: [%]

## Hallazgos Críticos
1. [Issue] - [Archivo:Línea] - [Impacto]

## Métricas
| Métrica | Valor | Objetivo | Estado |
|---------|-------|----------|--------|
| Coverage | 75% | 80% | ⚠️ |
| Complexity | 12 | <10 | ❌ |

## Recomendaciones
1. [Acción concreta]
2. [Acción concreta]
```

## Ejemplos

- "Audita la calidad del código del proyecto"
- "Genera un reporte de deuda técnica"
- "Identifica los archivos con más code smells"
- "Evalúa si el código cumple estándares de calidad"

## Referencias

- Enfocarse en issues de alto impacto primero
- No intentar resolver toda la deuda de golpe
- Establecer baseline y medir progreso
- Integrar análisis en CI/CD
