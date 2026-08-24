---
name: DevOps Pipeline
description: Configuración de CI/CD y pipelines de deploy
location: C:\Users\juani\.config\opencode\skills\devops-pipeline\SKILL.md
---

# DevOps Pipeline

Configuración de pipelines CI/CD, estrategias de deploy y automatización de infraestructura.

## Uso

Activar cuando el usuario necesite: configurar CI/CD, crear pipelines de deploy, automatizar builds, o gestionar infraestructura como código.

## Plataformas

### GitHub Actions
- Workflows en YAML
- Triggers: push, PR, schedule
- Marketplace de actions
- Secrets management

### GitLab CI
- `.gitlab-ci.yml`
- Stages: build, test, deploy
- Runners compartidos o dedicados
- Auto DevOps

### Jenkins
- Jenkinsfile (declarative/scripted)
- Pipelines como código
- Plugins extensibles
- Distribuido (master/agent)

## Estrategias de Deploy

### Blue/Green
- Dos ambientes idénticos
- Deploy sin downtime
- Rollback instantáneo
- Costo: duplicar infraestructura

### Canary
- Deploy gradual a subconjunto de usuarios
- Monitoreo de métricas antes de avanzar
- Rollback si hay problemas
- Riesgo controlado

### Rolling
- Actualización incremental de instancias
- Sin downtime
- Rollback más lento
- Balance entre costo y disponibilidad

## Pasos

1. **Analizar proyecto** - Lenguaje, framework, dependencias
2. **Definir stages** - Build, test, lint, security scan, deploy
3. **Crear pipeline** - Configurar para la plataforma elegida
4. **Configurar secrets** - Variables sensibles en vault
5. **Agregar quality gates** - Tests deben pasar, coverage mínimo
6. **Deploy strategy** - Seleccionar estrategia apropiada
7. **Monitoreo** - Configurar alertas y métricas post-deploy

## Ejemplos

- "Crea un pipeline de GitHub Actions para el proyecto Node.js"
- "Configura deploy automático a AWS con estrategia Blue/Green"
- "Agrega security scanning al pipeline"
- "Configura deploy canary para la API"

## Referencias

- Seguir principios de Shift-Left Security
- Mantener pipelines como código (IaC)
- Usar cache para acelerar builds
- Documentar proceso de deploy
