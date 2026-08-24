import { defineConfig, devices } from '@playwright/test';

/**
 * Configuración de Playwright para testing E2E
 * Docs: https://playwright.dev/docs/test-configuration
 */
export default defineConfig({
  testDir: './tests/e2e',
  
  /* Ejecutar tests en paralelo */
  fullyParallel: true,
  
  /* Fallar si hay test pendiente (solo en CI) */
  forbidOnly: !!process.env.CI,
  
  /* Reintentos en CI */
  retries: process.env.CI ? 2 : 0,
  
  /* Workers paralelos */
  workers: process.env.CI ? 1 : undefined,
  
  /* Reporteros */
  reporter: [
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['json', { outputFile: 'playwright-results.json' }],
    ['list']
  ],
  
  /* Configuración global de tests */
  use: {
    /* URL base de la aplicación */
    baseURL: 'http://localhost:3000',
    
    /* Trace en primer retry (para debugging) */
    trace: 'on-first-retry',
    
    /* Screenshots solo en fallas */
    screenshot: 'only-on-failure',
    
    /* Video solo en fallas */
    video: 'retain-on-failure',
    
    /* Timeouts */
    actionTimeout: 10000,
    navigationTimeout: 30000,
    
    /* Viewport por defecto */
    viewport: { width: 1280, height: 720 },
    
    /* Locale y timezone */
    locale: 'es-AR',
    timezoneId: 'America/Argentina/Buenos_Aires',
    
    /* Permissions */
    permissions: ['geolocation'],
    geolocation: { latitude: -34.6037, longitude: -58.3816 },
    
    /* Color scheme */
    colorScheme: 'light',
  },

  /* Proyectos para diferentes browsers y dispositivos */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
    {
      name: 'Tablet',
      use: { ...devices['iPad (gen 7)'] },
    },
  ],

  /* Servidor web para ejecutar tests */
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120000,
    cwd: process.env.FRONTEND_DIR || './apps/frontend',
  },

  /* Configuración de proyectos de testing */
  expect: {
    toHaveScreenshot: {
      maxDiffPixelRatio: 0.01,
    },
    toMatchSnapshot: {
      maxDiffPixelRatio: 0.01,
    },
  },
});
