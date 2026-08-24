---
name: opendesign-integration
description: Integración con OpenDesign para diseño UI/UX y generación de código desde diseños. Use when importing designs, generating UI components from design files, syncing design tokens, or converting OpenDesign prototypes to React/Vue/Angular code.
---

# OpenDesign Integration

Integración completa con OpenDesign para diseño UI/UX y generación automática de código.

## Capacidades

- **Importación de diseños**: Convertir diseños de OpenDesign a código
- **Generación de componentes**: Crear componentes React/Vue/Angular desde diseños
- **Sincronización**: Mantener sincronizado diseño con código
- **Design Tokens**: Exportar tokens de diseño (colores, tipografía, espaciado)
- **Responsive**: Generar diseños responsive automáticamente
- **Accesibilidad**: Incluir estándares de accesibilidad (WCAG)

## Flujo de Integración

1. Diseñador crea prototipo en OpenDesign
2. Arquitecto importa diseño al proyecto
3. Sistema genera código base automáticamente
4. Developer personaliza y extiende el código
5. QA verifica que el código coincida con el diseño

## Comandos Disponibles

```bash
# Importar diseño desde URL
opendesign:import https://opendesign.com/project/123

# Exportar componente creado
opendesign:export src/components/Button.tsx

# Sincronizar cambios
opendesign:sync

# Exportar design tokens
opendesign:tokens --format css

# Generar preview del diseño
opendesign:preview
```

## Formato de Salida

- Componentes de UI generados (React/Vue/Angular)
- Design tokens (JSON/CSS Variables)
- Documentación de componentes
- Guía de estilos

## Integración con Agentes

- **Architect**: Usa OpenDesign para validar diseños
- **Developer**: Importa diseños para implementar
- **QA**: Verifica fidelidad del código al diseño
- **QC**: Audita consistencia de diseño

## Ejemplo de Uso

```bash
# Importar diseño de OpenDesign
opendesign:import https://opendesign.com/project/123

# Exportar componente creado
opendesign:export src/components/Button.tsx

# Sincronizar cambios
opendesign:sync

# Exportar design tokens
opendesign:tokens --format css
```

## Referencias

- Documentación de OpenDesign API: https://opendesign.com/docs
- Ejemplos de integración: https://opendesign.com/examples
- Mejores prácticas: https://opendesign.com/best-practices
