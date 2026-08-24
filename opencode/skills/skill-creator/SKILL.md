---
name: Skill Creator
description: Creador de skills para opencode
location: C:\Users\juani\.config\opencode\skills\skill-creator\SKILL.md
---

# Skill Creator

Herramienta para crear nuevas skills para el sistema opencode.

## Uso

Activar cuando el usuario quiera crear una nueva skill, modificar una existente, o entender la estructura de skills.

## Estructura de una Skill

```
skill-name/
└── SKILL.md
```

### Frontmatter YAML Obligatorio

```yaml
---
name: Nombre de la Skill
description: Descripción clara y concisa
location: Ruta completa al archivo SKILL.md
---
```

### Secciones del SKILL.md

1. **# Nombre** - Título de la skill
2. **## Uso** - Cuándo activar esta skill
3. **## Pasos** - Flujo de trabajo paso a paso
4. **## Ejemplos** - Casos de uso concretos
5. **## Referencias** - Notas adicionales y mejores prácticas

## Pasos para Crear

1. **Definir propósito** - ¿Qué resuelve esta skill?
2. **Identificar triggers** - ¿Cuándo se activa?
3. **Diseñar flujo** - ¿Qué pasos seguir?
4. **Escribir contenido** - Claro, conciso, accionable
5. **Agregar ejemplos** - Casos de uso reales
6. **Validar** - Probar que funciona
7. **Registrar** - Agregar a available_skills en opencode.json

## Template

```markdown
---
name: [Nombre]
description: [Descripción]
location: C:\Users\juani\.config\opencode\skills\[nombre]\SKILL.md
---

# [Nombre]

[Descripción detallada]

## Uso

Activar cuando [condiciones].

## Pasos

1. **[Paso 1]** - [Descripción]
2. **[Paso 2]** - [Descripción]
3. **[Paso 3]** - [Descripción]

## Ejemplos

- "[Ejemplo 1]"
- "[Ejemplo 2]"

## Referencias

- [Nota 1]
- [Nota 2]
```

## Validación

- [ ] Frontmatter completo (name, description, location)
- [ ] Secciones presentes (Uso, Pasos, Ejemplos, Referencias)
- [ ] Descripción clara y específica
- [ ] Pasos numerados y accionables
- [ ] Ejemplos concretos
- [ ] Sin errores de ortografía
- [ ] Compatible con el sistema de opencode

## Ejemplos

- "Crea una skill para gestión de migraciones de base de datos"
- "Modifica la skill de QA para agregar nuevas herramientas"
- "Crea una skill específica para el stack del proyecto"

## Referencias

- Las skills se cargan automáticamente por el sistema
- Cada skill debe ser independiente
- No duplicar funcionalidad existente
- Mantener actualizado el frontmatter con la ubicación correcta
