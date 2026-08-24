---
name: Webapp Project
description: Proyectos de aplicación web
location: C:\Users\juani\.config\opencode\skills\project-type-webapp\SKILL.md
---

# Webapp Project

Guía para desarrollo de aplicaciones web con stacks modernos.

## Uso

Activar cuando el usuario trabaje en un proyecto de aplicación web (SPA, SSR, SSG).

## Stacks

### React
- **Framework**: Next.js (SSR/SSG), Vite (SPA)
- **State**: Zustand, Redux Toolkit, Jotai
- **Styling**: Tailwind CSS, CSS Modules, styled-components
- **Data Fetching**: React Query, SWR, Apollo Client

### Vue
- **Framework**: Nuxt.js (SSR/SSG), Vite (SPA)
- **State**: Pinia, Vuex
- **Styling**: Tailwind CSS, scoped CSS
- **Data Fetching**: Vue Query, Apollo Client

### Angular
- **Framework**: Angular CLI
- **State**: NgRx, Akita
- **Styling**: Angular Material, Tailwind CSS
- **Data Fetching**: HttpClient, Apollo Angular

### Svelte
- **Framework**: SvelteKit
- **State**: Svelte stores
- **Styling**: Tailwind CSS, scoped styles
- **Data Fetching**: Built-in fetch

## Consideraciones

### Performance
- Lazy loading de rutas
- Code splitting automático
- Optimización de imágenes
- Core Web Vitals (LCP, FID, CLS)

### SEO
- Meta tags dinámicos
- Sitemap XML
- Structured data
- Server-side rendering cuando aplique

### Accesibilidad
- WCAG 2.1 AA mínimo
- ARIA labels
- Keyboard navigation
- Screen reader testing

### Seguridad
- XSS prevention (CSP headers)
- CSRF protection
- Input sanitization
- Secure cookies

## Pasos

1. **Evaluar stack** - Elegir framework según necesidades
2. **Estructurar proyecto** - Seguir convenciones del framework
3. **Configurar build** - Optimizar para producción
4. **Implementar features** - Componentes reutilizables
5. **Testing** - Unit + E2E
6. **Deploy** - CI/CD + hosting

## Ejemplos

- "Crea un proyecto React con Next.js y Tailwind"
- "Configura SSR para mejorar SEO del e-commerce"
- "Implementa lazy loading para las rutas del dashboard"
- "Optimiza Core Web Vitals del sitio"

## Referencias

- Priorizar UX sobre complejidad técnica
- Usar SSR para contenido que requiere SEO
- Medir performance regularmente
- Mantener dependencias actualizadas
