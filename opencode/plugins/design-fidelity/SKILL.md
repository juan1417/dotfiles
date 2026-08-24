# Design Fidelity Plugin

## Nombre
Design Fidelity

## Descripción
Plugin de verificación de fidelidad al diseño. Compara el código implementado con los diseños de OpenDesign y genera reportes de desviación.

## Uso
Se activa cuando el usuario solicita:
- Verificar que el código coincide con el diseño
- Detectar desviaciones de UI/UX
- Generar reportes de fidelidad al diseño
- Auditar implementación visual

## Capacidades

### 1. Comparación de Diseño vs Código
```markdown
## Análisis de Fidelidad

### Diseño (OpenDesign)
- Componente: Button
- Color: #3B82F6
- Tamaño: 44px height
- Border-radius: 8px

### Código Implementado
- Componente: Button
- Color: #3B82F6 ✅
- Tamaño: 44px ✅
- Border-radius: 8px ✅

### Fidelidad: 100%
```

### 2. Detección de Desviaciones
```markdown
## Desviaciones Detectadas

### Críticas (deben corregirse)
- [ ] Botón primario usa color incorrecto
- [ ] Fuente no coincide con diseño

### Menores (pueden aceptarse)
- [ ] Espaciado ligeramente diferente
- [ ] Border-radius 2px mayor

### Sugerencias (mejoras opcionales)
- [ ] Agregar hover state no especificado
- [ ] Mejorar transición de animación
```

### 3. Reportes de Fidelidad
```markdown
## Reporte de Fidelidad al Diseño

**Fecha**: 2026-08-11
**Proyecto**: [Nombre]
**Diseñador**: [Nombre]

### Resumen
- **Componentes verificados**: 15
- **Fidelidad promedio**: 87%
- **Desviaciones críticas**: 2
- **Desviaciones menores**: 5

### Por Componente
| Componente | Fidelidad | Estado |
|------------|-----------|--------|
| Header | 100% | ✅ |
| Button | 95% | ✅ |
| Card | 85% | ⚠️ |
| Modal | 70% | ❌ |
```

### 4. Integración con OpenDesign
```markdown
## Flujo OpenDesign

1. Diseñar en OpenDesign
2. Exportar especificaciones
3. Comparar con código implementado
4. Generar reporte de fidelidad
5. Corregir desviaciones
6. Re-verificar
```

## Herramientas
- `open-design`: MCP para acceder a diseños
- `codebase-memory`: Almacenar comparaciones
- `read`: Leer archivos de diseño
- `grep`: Buscar estilos en código

## Flujo de Trabajo

### Verificación Completa
```markdown
1. Obtener diseño desde OpenDesign
2. Extraer especificaciones de UI
3. Buscar componentes en código
4. Comparar propiedades
5. Clasificar desviaciones
6. Generar reporte
7. Presentar al usuario
```

### Verificación de Componente
```markdown
1. Identificar componente a verificar
2. Obtener diseño del componente
3. Leer código del componente
4. Comparar propiedades específicas
5. Reportar coincidencias/desviaciones
```

## Ejemplos de Uso

### Ejemplo 1: Verificación Completa
```
Usuario: "Verifica que el código coincida con el diseño"
Plugin:
1. Obtiene diseño desde OpenDesign
2. Analiza 15 componentes
3. Detecta 2 desviaciones críticas
4. Genera reporte con 87% fidelidad
5. Presenta: "87% fidelidad, 2 correcciones necesarias"
```

### Ejemplo 2: Verificar Componente
```
Usuario: "Verifica el componente Button"
Plugin:
1. Obtiene diseño de Button
2. Lee código de Button.tsx
3. Compara: color ✅, tamaño ✅, border-radius ✅
4. Reporta: "Button con 100% fidelidad"
```

### Ejemplo 3: Detectar Desviaciones
```
Usuario: "¿Hay desviaciones del diseño?"
Plugin:
1. Analiza todos los componentes
2. Detecta 5 desviaciones menores
3. Clasifica: 2 críticas, 3 menores
4. Presenta lista de correcciones necesarias
```

## Formato de Reporte

```markdown
# Reporte de Fidelidad al Diseño

**Proyecto**: [Nombre]
**Fecha**: [fecha]
**Verificador**: @qa

---

## Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| Componentes verificados | 15 |
| Fidelidad promedio | 87% |
| Desviaciones críticas | 2 |
| Desviaciones menores | 5 |
| Estado | ⚠️ Requiere correcciones |

---

## Detalle por Componente

### Header ✅
- **Fidelidad**: 100%
- **Estado**: Correcto
- **Propiedades verificadas**: color, tamaño, fuentes, espaciado

### Button ✅
- **Fidelidad**: 95%
- **Estado**: Casi correcto
- **Desviaciones**: Border-radius 2px mayor

### Card ⚠️
- **Fidelidad**: 85%
- **Estado**: Requiere ajustes
- **Desviaciones**: 
  - Color de fondo: #F3F4F6 vs #F9FAFB
  - Sombra: 0 1px 3px vs 0 2px 4px

### Modal ❌
- **Fidelidad**: 70%
- **Estado**: Requiere correcciones críticas
- **Desviaciones**:
  - Ancho: 400px vs 500px
  - Posición: centered vs top-aligned
  - Overlay: opacity 0.5 vs 0.7

---

## Desviaciones Críticas

### 1. Modal - Posición incorrecta
- **Diseño**: Top-aligned con 80px margin-top
- **Código**: Centered verticalmente
- **Impacto**: UX diferente al diseñado
- **Corrección**: Ajustar posición del modal

### 2. Card - Color de fondo
- **Diseño**: #F9FAFB
- **Código**: #F3F4F6
- **Impacto**: Visual diferente
- **Corrección**: Actualizar color de fondo

---

## Recomendaciones

1. **Corregir desviaciones críticas** antes de producción
2. **Revisar desviaciones menores** para mejorar fidelidad
3. **Considerar sugerencias** para mejora de UX
4. **Re-verificar** después de correcciones
```

## Integración con OpenDesign

### Comandos Disponibles
```bash
# Obtener diseño de componente
opendesign:get-component [nombre]

# Exportar especificaciones
opendesign:export-specs [proyecto]

# Comparar con código
opendesign:compare [componente] [código]

# Generar reporte
opendesign:report [proyecto] --type=fidelity
```

### Sincronización
```bash
# Sincronizar diseños con código
opendesign:sync [proyecto]

# Detectar desviaciones
opendesign:drift [proyecto]

# Actualizar desde código
opendesign:update-from-code [proyecto]
```

## Configuración

```json
{
  "design-fidelity": {
    "enabled": true,
    "auto_verify": true,
    "strict_mode": false,
    "tolerance": 5,
    "report_format": "detailed"
  }
}
```

## Convenciones

1. **Siempre verificar** después de implementar UI
2. **Clasificar desviaciones** por severidad
3. **Documentar desviaciones** aceptadas
4. **Re-verificar** después de correcciones
5. **Mantener reportes** actualizados
6. **Integrar con OpenDesign** para fuentes de verdad
