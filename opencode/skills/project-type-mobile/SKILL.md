---
name: Mobile Project
description: Proyectos de aplicación móvil
location: C:\Users\juani\.config\opencode\skills\project-type-mobile\SKILL.md
---

# Mobile Project

Guía para desarrollo de aplicaciones móviles multiplataforma y nativas.

## Uso

Activar cuando el usuario trabaje en un proyecto de aplicación móvil (iOS, Android, cross-platform).

## Stacks

### React Native
- **Framework**: Expo (recomendado), CLI
- **Navigation**: React Navigation, Expo Router
- **State**: Zustand, Redux Toolkit
- **UI**: React Native Paper, NativeBase
- **Storage**: AsyncStorage, MMKV

### Flutter
- **Framework**: Flutter SDK
- **State**: Riverpod, Bloc, GetX
- **UI**: Material Design, Cupertino widgets
- **Storage**: Hive, SharedPreferences
- **HTTP**: Dio, http package

### Swift (iOS)
- **Framework**: SwiftUI, UIKit
- **State**: Combine, SwiftUI state
- **Storage**: CoreData, UserDefaults
- **Networking**: URLSession, Alamofire

### Kotlin (Android)
- **Framework**: Jetpack Compose, XML views
- **State**: ViewModel, StateFlow
- **Storage**: Room, DataStore
- **Networking**: Retrofit, Ktor

## Consideraciones

### Performance
- 60fps minimum
- Memory management
- Battery optimization
- App size optimization

### UX Nativa
- Platform-specific patterns (iOS/Android)
- Haptic feedback
- Gestures nativos
- Animaciones fluidas

### Offline
- Sync strategy
- Local storage
- Conflict resolution
- Queue de operaciones

### Distribución
- App Store (iOS)
- Play Store (Android)
- Internal testing (TestFlight, Play Console)
- OTA updates (EAS Update, CodePush)

## Pasos

1. **Evaluar stack** - Cross-platform vs nativo según necesidades
2. **Configurar entorno** - SDKs, emuladores, dispositivos
3. **Diseñar UI/UX** - Seguir guías de plataforma
4. **Implementar features** - Componentes reutilizables
5. **Testing** - Unit + Integration + Device testing
6. **Distribuir** - Build, sign, submit a stores

## Ejemplos

- "Crea una app React Native con Expo"
- "Implementa navegación con React Navigation"
- "Configura push notifications para iOS y Android"
- "Prepara el build para App Store y Play Store"

## Referencias

- Seguir guías de Material Design (Android) y HIG (iOS)
- Probar en dispositivos reales, no solo emuladores
- Manejar permisos correctamente
- Considerar diferentes tamaños de pantalla
