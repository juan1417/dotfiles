---
name: SDD Workflow
description: Flujo de trabajo Specification-Driven Development
location: C:\Users\juani\.config\opencode\skills\sdd-workflow\SKILL.md
---

# SDD Workflow

Flujo de trabajo completo de Specification-Driven Development para desarrollo colaborativo entre humano e IA.

## Uso

Activar esta skill cuando el usuario pida implementar una feature, corregir un bug o hacer cambios que requieran planificación y ejecución estructurada. El flujo SDD asegura calidad y trazabilidad.

## Pasos

1. **@sdd-explore** - Explorar el codebase para entender estructura, patrones y dependencias
2. **@sdd-spec** - Escribir especificaciones claras de lo que se va a hacer
3. **@sdd-design** - Diseñar la solución técnica con ADRs si aplica
4. **@sdd-tasks** - Desglosar en tareas concretas y estimar esfuerzo
5. **@sdd-apply** - Implementar los cambios respetando convenciones existentes
6. **@sdd-verify** - Verificar con tests, lint y typecheck

## Ejemplos

- "Necesito agregar autenticación OAuth al proyecto"
- "Hay un bug en el login que no valida email correctamente"
- "Quiero refactorizar el módulo de pagas para usar patrón Repository"

## Referencias

- Cada fase produce artefactos documentados
- El flujo es iterativo: si verify falla, se regresa a la fase correspondiente
- Los sub-agentes se encargan de la ejecución, el humano supervisa
- Seguir el tracking obligatorio después de cada delegación
