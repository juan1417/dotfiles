---
name: API Project
description: Proyectos de API/Backend
location: C:\Users\juani\.config\opencode\skills\project-type-api\SKILL.md
---

# API Project

Guía para desarrollo de APIs y servicios backend.

## Uso

Activar cuando el usuario trabaje en un proyecto de API REST, GraphQL, o servicio backend.

## Stacks

### Node.js
- **Framework**: Express, Fastify, NestJS
- **ORM**: Prisma, TypeORM, Drizzle
- **Validation**: Zod, Joi, class-validator
- **Auth**: JWT, Passport, Lucia
- **API**: REST, GraphQL (Apollo), tRPC

### Python
- **Framework**: FastAPI (recomendado), Django REST, Flask
- **ORM**: SQLAlchemy, Django ORM, Tortoise
- **Validation**: Pydantic
- **Auth**: JWT, OAuth2
- **API**: REST, GraphQL (Strawberry)

### Go
- **Framework**: Gin, Echo, Fiber
- **ORM**: GORM, sqlx
- **Validation**: go-playground/validator
- **Auth**: JWT, custom middleware
- **API**: REST, gRPC

### Java
- **Framework**: Spring Boot
- **ORM**: JPA/Hibernate
- **Validation**: Bean Validation
- **Auth**: Spring Security
- **API**: REST, GraphQL (Spring GraphQL), gRPC

## Consideraciones

### Seguridad
- Authentication & Authorization
- Rate limiting
- Input validation
- SQL injection prevention
- CORS configuration
- HTTPS enforcement

### Performance
- Connection pooling
- Caching (Redis, in-memory)
- Pagination
- Compression
- Query optimization

### Documentación
- OpenAPI/Swagger
- API versioning
- Changelog
- Postman collections

### Observabilidad
- Structured logging
- Metrics (Prometheus)
- Tracing (OpenTelemetry)
- Health checks

## Pasos

1. **Evaluar stack** - Elegir lenguaje/framework según necesidades
2. **Diseñar API** - Endpoints, request/response schemas
3. **Implementar** - Controllers, services, repositories
4. **Seguridad** - Auth, validation, rate limiting
5. **Testing** - Unit + Integration + E2E
6. **Documentar** - OpenAPI, examples
7. **Deploy** - CI/CD, containerización

## Ejemplos

- "Crea una API REST con FastAPI y PostgreSQL"
- "Implementa autenticación JWT para la API"
- "Configura rate limiting y CORS"
- "Genera documentación OpenAPI"

## Referencias

- Seguir principios REST/GraphQL según corresponda
- Versionar API desde el inicio
- Usar DTOs para separar capas
- Manejar errores de forma consistente
- Monitorear performance en producción
