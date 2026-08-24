---
name: QA Automation
description: Automatización de pruebas de software
location: C:\Users\juani\.config\opencode\skills\qa-automation\SKILL.md
---

# QA Automation

Automatización de pruebas de software: unitarias, integración, E2E y performance.

## Uso

Activar cuando el usuario necesite: crear tests, configurar frameworks de testing, ejecutar pruebas, o mejorar cobertura de tests.

## Tipos de Pruebas

### Unitarias
- Pruebas individuales de funciones/métodos
- Aisladas, rápidas, deterministas
- Frameworks: Jest, Vitest, Mocha

### Integración
- Pruebas de interacción entre módulos
- Base de datos, APIs, servicios externos
- Frameworks: Jest, Vitest, Supertest

### E2E (End-to-End)
- Flujos completos del usuario
- Navegador real o headless
- Frameworks: Playwright, Cypress

### Performance
- Load testing, stress testing
- Métricas: response time, throughput
- Herramientas: k6, Artillery, Locust

## Pasos

1. **Analizar código** - Identificar qué necesita testing
2. **Definir estrategia** - Qué tipo de tests para cada caso
3. **Configurar framework** - Instalar y configurar herramientas
4. **Escribir tests** - Seguir patrones AAA (Arrange, Act, Assert)
5. **Ejecutar** - Correr suite completa
6. **Reportar** - Generar reporte de cobertura

## Herramientas

- Playwright: E2E testing multi-browser
- Jest: Unit testing para JavaScript/TypeScript
- Vitest: Unit testing moderno y rápido
- Supertest: Testing de APIs Express
- k6: Performance testing

## Ejemplos

- "Crea tests unitarios para el servicio de autenticación"
- "Configura Playwright para E2E testing"
- "Genera tests de integración para la API de usuarios"
- "Ejecuta los tests y muestra cobertura"

## Referencias

- Mantener tests limpios y legibles
- Cada test debe ser independiente
- Usar mocks/stubs para dependencias externas
- Cobertura mínima recomendada: 80%
