---
name: Architect Design
description: Diseño de arquitectura de software
location: C:\Users\juani\.config\opencode\skills\architect-design\SKILL.md
---

# Architect Design

Diseño de arquitectura de software, patrones de diseño y documentación arquitectónica.

## Uso

Activar cuando el usuario necesite: diseñar sistema, elegir arquitectura, crear ADRs, o documentar decisiones técnicas.

## Patrones Arquitectónicos

### Microservices
- Servicios pequeños y desplegables independientemente
- Comunicación: REST, gRPC,消息 queues
- Bases de datos por servicio
- Complejidad operacional aumentada

### Monolith
- Todo en una sola aplicación
- Despliegue unitario
- Más simple de desarrollar y debuggear
- Riesgo de acoplamiento excesivo

### Serverless
- Functions as a Service (FaaS)
- Auto-escalado automático
- Pay-per-use
- Cold start como limitación

### Modular Monolith
- Monolith con módulos bien definidos
- Mejor de ambos mundos
- Preparado para extracción a microservices
- Balance entre simplicidad y escalabilidad

## Pasos

1. **Entender requerimientos** - Funcionales y no funcionales
2. **Evaluar trade-offs** - Escalabilidad, complejidad, costo
3. **Seleccionar patrón** - Basado en necesidades reales
4. **Diseñar componentes** - Módulos, servicios, interfaces
5. **Documentar** - Crear design.md y ADRs
6. **Revisar** - Validar con stakeholders

## Documentos

### design.md
```markdown
# Diseño del Sistema

## Visión General
[Descripción de alto nivel]

## Componentes
[Diagrama y descripción de componentes]

## Decisiones Técnicas
[Lista de ADRs relevantes]

## trade-offs
[Decisiones tomadas y por qué]
```

### ADRs (Architecture Decision Records)
```markdown
# ADR-[Número]: [Título]

## Estado
[Aceptado/Deprecado/Reemplazado]

## Contexto
[Situación que requiere decisión]

## Decisión
[Qué se decidió]

## Consecuencias
[Impacto positivo y negativo]
```

## Ejemplos

- "Diseña la arquitectura para un e-commerce escalable"
- "Crea un ADR para migrar de monolith a microservices"
- "Evalúa opciones para el sistema de autenticación"
- "Documenta la arquitectura actual del proyecto"

## Referencias

- Preferir simplicidad sobre elegancia
- Documentar el "por qué", no solo el "qué"
- Los ADRs son inmutables (se crean nuevos, no se editan)
- Revisar arquitectura periódicamente
