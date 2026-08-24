# Documentation Sync Plugin

## Nombre
Documentation Sync

## Descripción
Plugin de sincronización automática de documentación con código. Actualiza README, CHANGELOG y documentación técnica automáticamente.

## Uso
Se activa cuando el usuario solicita:
- Sincronizar documentación con código
- Actualizar README automáticamente
- Generar CHANGELOG desde commits
- Documentar cambios recientes
- Mantener documentación actualizada

## Capacidades

### 1. Sincronización de README
```markdown
## README Auto-actualizado

### Secciones Actualizadas
- ✅ Descripción del proyecto
- ✅ Instalación
- ✅ Uso
- ✅ API Reference
- ✅ Contributing
- ✅ Changelog

### Detección de Cambios
- Nuevos archivos: 3
- Archivos modificados: 5
- Archivos eliminados: 1
- Dependencias actualizadas: 2
```

### 2. Generación de CHANGELOG
```markdown
## CHANGELOG Generado

### [1.2.0] - 2026-08-11

#### Added
- Autenticación JWT para usuarios
- Endpoints de gestión de perfil
- Tests unitarios para módulo de auth

#### Changed
- Actualizado endpoint de login
- Mejorado manejo de errores
- Refactorizado módulo de usuarios

#### Fixed
- Corregido bug en validación de email
- Solucionado problema de CORS
- Arreglado error en persistencia de datos

#### Removed
- Eliminado endpoint obsoleto /v1/users
- Removida dependencia no utilizada
```

### 3. Documentación de API
```markdown
## API Reference Auto-generada

### Endpoints

#### POST /api/auth/login
**Descripción**: Autenticar usuario
**Request**:
```json
{
  "email": "string",
  "password": "string"
}
```
**Response**:
```json
{
  "token": "string",
  "user": {
    "id": "string",
    "email": "string"
  }
}
```

#### GET /api/users/profile
**Descripción**: Obtener perfil de usuario
**Headers**: Authorization: Bearer [token]
**Response**:
```json
{
  "id": "string",
  "name": "string",
  "email": "string"
}
```
```

### 4. Documentación de Componentes
```markdown
## Component Documentation

### Button Component
**Props**:
- `variant`: 'primary' | 'secondary' | 'danger'
- `size`: 'sm' | 'md' | 'lg'
- `disabled`: boolean
- `onClick`: () => void

**Uso**:
```jsx
<Button variant="primary" size="md" onClick={handleClick}>
  Click me
</Button>
```
```

## Herramientas
- `bash`: Ejecutar git commands
- `read`: Leer archivos de documentación
- `edit`: Actualizar documentación
- `github`: MCP para integración con GitHub

## Flujo de Trabajo

### Sincronización Completa
```markdown
1. Detectar cambios recientes (git log)
2. Actualizar README si es necesario
3. Generar CHANGELOG desde commits
4. Documentar nuevos endpoints/API
5. Documentar nuevos componentes
6. Verificar enlaces rotos
7. Confirmar sincronización
```

### Actualización de README
```markdown
1. Leer README actual
2. Detectar cambios en estructura
3. Actualizar secciones afectadas
4. Verificar que la información sea correcta
5. Guardar cambios
```

### Generación de CHANGELOG
```markdown
1. Obtener commits recientes
2. Clasificar por tipo (Added, Changed, Fixed, Removed)
3. Generar entradas del CHANGELOG
4. Agregar fecha y versión
5. Insertar en CHANGELOG.md
```

## Ejemplos de Uso

### Ejemplo 1: Sincronización Completa
```
Usuario: "Sincroniza la documentación con el código"
Plugin:
1. Detecta 10 commits recientes
2. Actualiza README con nuevos endpoints
3. Genera CHANGELOG con 5 Added, 3 Changed, 2 Fixed
4. Documenta 2 nuevos componentes
5. Confirma: "Documentación sincronizada"
```

### Ejemplo 2: Actualizar README
```
Usuario: "Actualiza el README"
Plugin:
1. Detecta cambios en package.json
2. Actualiza sección de instalación
3. Detecta nuevos scripts
4. Actualiza sección de uso
5. Confirma: "README actualizado"
```

### Ejemplo 3: Generar CHANGELOG
```
Usuario: "Genera el CHANGELOG de esta release"
Plugin:
1. Obtiene commits desde última release
2. Clasifica: 8 Added, 5 Changed, 3 Fixed
3. Genera CHANGELOG.md
4. Confirma: "CHANGELOG generado para v1.2.0"
```

## Formato de CHANGELOG

```markdown
# Changelog

Todas lasNotas de Cambios importantes a este proyecto serán documentadas en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- Nueva funcionalidad 1
- Nueva funcionalidad 2

### Changed
- Cambio en funcionalidad existente

### Fixed
- Corrección de bug 1

## [1.2.0] - 2026-08-11

### Added
- Autenticación JWT para usuarios
- Endpoints de gestión de perfil
- Tests unitarios para módulo de auth

### Changed
- Actualizado endpoint de login
- Mejorado manejo de errores
- Refactorizado módulo de usuarios

### Fixed
- Corregido bug en validación de email
- Solucionado problema de CORS
- Arreglado error en persistencia de datos

### Removed
- Eliminado endpoint obsoleto /v1/users
- Removida dependencia no utilizada

## [1.1.0] - 2026-08-01

### Added
- Sistema de logging
- Rate limiting en endpoints públicos

### Changed
- Mejorado rendimiento de consultas

### Fixed
- Corregido timezone en timestamps
```

## Formato de README

```markdown
# [Nombre del Proyecto]

[Descripción breve del proyecto]

## Instalación

### Prerrequisitos
- Node.js >= 18
- npm >= 9

### Pasos
```bash
# Clonar repositorio
git clone https://github.com/usuario/proyecto.git

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env

# Ejecutar en desarrollo
npm run dev
```

## Uso

### Scripts Disponibles
```bash
npm run dev      # Desarrollo
npm run build    # Construcción
npm run test     # Tests
npm run lint     # Linting
npm run preview  # Preview de construcción
```

### API Reference
Ver [docs/api.md](docs/api.md) para documentación completa de la API.

## Estructura del Proyecto
```
src/
├── components/     # Componentes React
├── hooks/         # Custom hooks
├── services/      # Servicios API
├── utils/         # Utilidades
├── types/         # Tipos TypeScript
└── index.tsx      # Entry point
```

## Contributing
Ver [CONTRIBUTING.md](CONTRIBUTING.md) para guías de contribución.

## Changelog
Ver [CHANGELOG.md](CHANGELOG.md) para historial de cambios.

## Licencia
[MIT](LICENSE)
```

## Integración con GitHub

### Comandos Disponibles
```bash
# Obtener commits recientes
gh api repos/{owner}/{repo}/commits

# Obtener releases
gh api repos/{owner}/{repo}/releases

# Crear release
gh api repos/{owner}/{repo}/releases --method POST

# Actualizar README en GitHub
gh api repos/{owner}/{repo}/contents/README.md --method PUT
```

### Sincronización Automática
```bash
# Configurar hook post-commit
echo "npm run doc-sync" >> .git/hooks/post-commit

# Configurar GitHub Action
name: Documentation Sync
on:
  push:
    branches: [main]
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run doc-sync
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "docs: update documentation"
```

## Configuración

```json
{
  "doc-sync": {
    "enabled": true,
    "auto_readme": true,
    "auto_changelog": true,
    "auto_api_docs": true,
    "sync_on_commit": false,
    "notify_on_update": true
  }
}
```

## Convenciones

1. **Sincronizar después de cambios significativos**
2. **Mantener CHANGELOG actualizado** con cada release
3. **Documentar TODOS los endpoints** públicos
4. **Verificar enlaces rotos** regularmente
5. **Usar formato Keep a Changelog** para CHANGELOG
6. **Incluir ejemplos** en documentación de API
