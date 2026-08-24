---
name: Desktop Project
description: Proyectos de aplicación de escritorio
location: C:\Users\juani\.config\opencode\skills\project-type-desktop\SKILL.md
---

# Desktop Project

Guía para desarrollo de aplicaciones de escritorio multiplataforma.

## Uso

Activar cuando el usuario trabaje en un proyecto de aplicación de escritorio (Windows, macOS, Linux).

## Stacks

### Electron
- **Framework**: Electron + React/Vue/Angular
- **State**: Igual que web (Zustand, Redux, etc)
- **IPC**: electron.ipcMain, ipcRenderer
- **Storage**: electron-store, leveldb
- **Auto-update**: electron-updater

### Tauri
- **Framework**: Tauri + React/Vue/Svelte
- **Backend**: Rust
- **State**: Frontend framework state
- **Storage**: tauri-plugin-store
- **Security**: Better than Electron

### .NET (WPF/WinForms)
- **Framework**: .NET 6+
- **UI**: WPF (XAML), WinForms
- **State**: MVVM (CommunityToolkit.Mvvm)
- **Storage**: SQLite, JSON files
- **Cross-platform**: .NET MAUI

## Consideraciones

### Seguridad
- Sandboxing de procesos
- Permisos de sistema
- Actualizaciones seguras
- Storage encriptado

### Performance
- Startup time < 2 segundos
- Memory usage < 200MB idle
- Responsive UI (no bloquear main thread)
- Lazy loading de módulos

### Distribución
- Installers (MSI, DMG, DEB)
- Auto-update mechanism
- Code signing
- Notarización (macOS)

### Integración OS
- System tray
- Global shortcuts
- Native menus
- File associations
- Notifications nativas

## Pasos

1. **Evaluar stack** - Electron vs Tauri vs .NET según necesidades
2. **Configurar proyecto** - Estructura base y dependencias
3. **Diseñar UI** - Nativa o web-based según framework
4. **Implementar IPC** - Comunicación frontend-backend
5. **Testing** - Unit + Integration + E2E
6. **Empaquetar** - Build, sign, distribuir

## Ejemplos

- "Crea una app de escritorio con Tauri y React"
- "Implementa system tray con Electron"
- "Configura auto-update para la aplicación"
- "Integra notificaciones nativas del sistema"

## Referencias

- Tauri preferido sobre Electron para nuevos proyectos
- Minimizar tamaño del bundle
- Probar en todas las plataformas objetivo
- Considerar distribución offline
