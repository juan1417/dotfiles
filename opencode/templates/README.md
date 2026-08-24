# Templates para Ejecución Paralela

Este directorio contiene templates para configurar ejecución paralela de Frontend y Backend en proyectos SDD.

## 📁 Archivos Incluidos

| Archivo | Descripción |
|---------|-------------|
| `playwright.config.ts` | Configuración de Playwright para testing E2E |
| `docker-compose.yml` | Docker Compose para servicios paralelos |
| `package.json` | Scripts npm para ejecución paralela |

## 🚀 Inicio Rápido

### 1. Copiar Templates

```bash
# Copiar docker-compose.yml
cp ~/.config/opencode/templates/docker-compose.yml ./docker-compose.yml

# Copiar package.json (fusionar con existente)
cp ~/.config/opencode/templates/package.json ./package.json

# Copiar playwright.config.ts
cp ~/.config/opencode/templates/playwright.config.ts ./apps/frontend/playwright.config.ts
```

### 2. Instalar Dependencias

```bash
# Instalar concurrently
npm install concurrently --save-dev

# Instalar husky (opcional)
npm install husky --save-dev
npx husky install
```

### 3. Ejecutar en Paralelo

```bash
# Frontend + Backend en paralelo
npm run dev

# Con Docker
npm run dev:docker

# Con herramientas de admin
npm run dev:tools
```

## 📋 Scripts Disponibles

### Desarrollo
```bash
npm run dev                    # Frontend + Backend en paralelo
npm run dev:backend            # Solo Backend
npm run dev:frontend           # Solo Frontend
npm run dev:docker             # Con Docker
npm run dev:docker:build       # Con Docker (rebuild)
npm run dev:tools              # Con pgAdmin y Redis Commander
```

### Build
```bash
npm run build                  # Ambos en paralelo
npm run build:backend          # Solo Backend
npm run build:frontend         # Solo Frontend
```

### Testing
```bash
npm run test                   # Tests unitarios en paralelo
npm run test:backend           # Tests del Backend
npm run test:frontend          # Tests del Frontend
npm run test:e2e               # Tests E2E con Playwright
npm run test:e2e:ui            # Playwright con UI
npm run test:e2e:debug         # Playwright en modo debug
npm run test:all               # Todos los tests
```

### Linting
```bash
npm run lint                   # Linting en paralelo
npm run lint:fix               # Auto-fix en paralelo
npm run typecheck              # Type checking en paralelo
```

### Docker
```bash
npm run docker:up              # Iniciar servicios
npm run docker:down            # Detener servicios
npm run docker:restart         # Reiniciar servicios
npm run docker:logs            # Ver logs
```

### Database
```bash
npm run db:migrate             # Ejecutar migraciones
npm run db:seed                # Poblar base de datos
npm run db:reset               # Resetear base de datos
```

## 🎯 Arquitectura Monorepo

```
mi-proyecto/
├── apps/
│   ├── frontend/              # React/Vue/Angular
│   │   ├── src/
│   │   ├── tests/e2e/
│   │   ├── playwright.config.ts
│   │   └── package.json
│   └── backend/               # Node/Python/Go
│       ├── src/
│       ├── tests/
│       └── package.json
├── docker-compose.yml
├── package.json
└── README.md
```

## 🧪 Testing con Playwright

### Ejecutar Tests
```bash
# Todos los tests
npm run test:e2e

# Test específico
npx playwright test tests/e2e/login.spec.ts

# Con UI
npm run test:e2e:ui

# Debug
npm run test:e2e:debug
```

### Ver Reportes
```bash
npm run playwright:report
```

## 🐳 Docker

### Servicios
- **Backend**: Puerto 4000
- **Frontend**: Puerto 3000
- **PostgreSQL**: Puerto 5432
- **Redis**: Puerto 6379
- **Playwright**: Ejecución bajo demanda

### Comandos Útiles
```bash
# Ver logs de un servicio
docker-compose logs -f backend

# Reiniciar un servicio
docker-compose restart backend

# Ver estado
docker-compose ps

# Ejecutar comando en un servicio
docker-compose exec backend npm run migrate
```

## 🔧 Configuración Personalizada

### Variables de Entorno

Crear archivo `.env` en la raíz:

```env
# Backend
PORT=4000
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/myapp
REDIS_URL=redis://localhost:6379
JWT_SECRET=your-secret-key

# Frontend
VITE_API_URL=http://localhost:4000
VITE_WS_URL=ws://localhost:4000

# Playwright
BASE_URL=http://localhost:3000
```

### Personalizar Puertos

Editar `docker-compose.yml`:

```yaml
services:
  backend:
    ports:
      - "4001:4000"  # Cambiar puerto externo
```

## 📚 Documentación Adicional

- [Playwright Docs](https://playwright.dev/docs/intro)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Concurrently Docs](https://github.com/open-cli-tools/concurrently)
