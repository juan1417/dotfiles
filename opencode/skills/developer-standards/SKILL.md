---
name: Developer Standards
description: Estándares de desarrollo y buenas prácticas
location: C:\Users\juani\.config\opencode\skills\developer-standards\SKILL.md
---

# Developer Standards

Estándares de desarrollo, convenciones de código y buenas prácticas de programación.

## Uso

Activar cuando el usuario necesite: implementar código, refactorizar, aplicar convenciones, o revisar estándares de desarrollo.

## Convenciones

### Nomenclatura
- **Variables/funciones**: camelCase (`userName`, `getUserData`)
- **Clases/Interfaces**: PascalCase (`UserService`, `IRepository`)
- **Constantes**: UPPER_SNAKE_CASE (`MAX_RETRY_COUNT`)
- **Archivos**: kebab-case (`user-service.ts`)
- **Directorios**: kebab-case (`shared-utils/`)

### Estructura de Proyecto
```
src/
├── core/           # Lógica de negocio
├── infrastructure/ # Adaptadores externos
├── shared/         # Utilidades compartidas
├── types/          # Definiciones de tipos
└── index.ts        # Punto de entrada
```

### Testing
- Tests unitarios para lógica de negocio
- Tests de integración para servicios
- Tests E2E para flujos críticos
- Cobertura mínima: 80%

### Código Limpio
- Funciones pequeñas (máx 30 líneas)
- Nombres descriptivos (no abreviar)
- Un solo nivel de abstracción por función
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)

## Buenas Prácticas

### Git
- Commits atómicos y descriptivos
- Branches feature/bugfix/hotfix
- PRs pequeños y revisionables
- No commitear secrets nunca

### Seguridad
- Validar inputs siempre
- Sanitizar outputs
- Usar HTTPS en producción
- No exponer información sensible en logs

### Performance
- Lazy loading cuando sea posible
- Cache de datos estáticos
- Conexiones a DB pool
- Monitoreo de métricas

## Pasos

1. **Revisar código existente** - Entender patrones actuales
2. **Aplicar convenciones** - Seguir estilo del proyecto
3. **Escribir tests** - Acompañar cambios con pruebas
4. **Documentar** - Comentar solo lo necesario
5. **Revisar** - Self-review antes de PR

## Ejemplos

- "Refactoriza este componente siguiendo clean code"
- "Aplica las convenciones del proyecto a este módulo"
- "Revisa este código y sugiere mejoras"
- "Crea un archivo de estándares para el equipo"

## Referencias

- Seguir estilo del código existente
- Preferir composición sobre herencia
- Manejar errores explícitamente
- No agregar dependencias sin evaluación
