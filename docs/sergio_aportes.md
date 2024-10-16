# Contribuciones de Sergio Pezo

## Configuración Inicial del Proyecto

### Estructura Básica del Repositorio
- Creación de plantillas para historias de usuario y flujos de trabajo de CI
- Configuración inicial de Docker y Docker Compose
- Establecimiento de la estructura básica del proyecto y dependencias

### Configuración del Backend
- Configuración inicial del backend y Prometheus
- Creación de directorios y archivos necesarios
- Actualización del archivo compose.yml para incluir el servicio backend

## Desarrollo del Backend

### Implementación de Funcionalidades de Jugador
- Desarrollo del endpoint para crear jugadores
- Implementación de la funcionalidad de inicio de sesión
- Creación del endpoint de actualización de jugadores
- Adición de opción de registro en el menú del juego

### Persistencia de Datos
- Implementación de la persistencia de datos de jugadores
- Actualización del modelo de jugador
- Finalización del endpoint de actualización

### Pruebas y Calidad de Código
- Adición de pruebas de comportamiento (Behave) y pruebas de integración
- Implementación de pruebas en el pipeline de CI
- Configuración de pre-commit hooks para mantener la calidad del código

## Monitorización y Métricas

### Configuración de Prometheus y Grafana
- Configuración inicial de Prometheus y Grafana
- Implementación de métricas para el inicio de sesión y registro de jugadores
- Adición de métricas para seguimiento de estadísticas del juego
- Configuración de un exportador de métricas para MongoDB


### Dashboards de Grafana
- Creación de dashboards en Grafana para visualización de métricas


Para grafana se configuraron 3 principales, dashboards en `grafana/dashboards` directory usando Prometheus como datasource.

- `game_stats.json`:

Dashboard para ver las métricas de juego de los jugadores.

![](https://imgur.com/BOnORIP.png)

- `server_stats.json`: 

Dashboard para conocer el estado de las solicitudes del backend.

![](https://imgur.com/YJ4fQvb.png)

- `mongo_stats.json`:
  
Dashboard para conocer el estado del contenedor de mongo.

![](https://imgur.com/DNJ6LfS.png)

Así como también se configuraron 3 alertas, que notificaran a mi correo gracias a `grafana/grafana.ini`.


![](https://imgur.com/KHaWbD3.png)

El primero es una lanzó la alerta cuando el backend registró a más de cinco personas.
![](https://imgur.com/KnQdRcM.png)


## Integración y Despliegue Continuo

### Mejoras en el Pipeline de CI
- Actualización del pipeline de CI para incluir nuevas pruebas y verificaciones
- Optimización del proceso de construcción y despliegue

## Interfaz de Usuario

### Implementación del Menú de Inicio de Sesión
- Creación de la pantalla de menú inicial para el inicio de sesión de jugadores
- Implementación de la funcionalidad de inicio de sesión en la pantalla del menú

## Finalización del Juego

### Actualización de Jugadores al Finalizar el Juego
- Implementación de la actualización de estadísticas de jugadores al finalizar una partida
- Integración de la solicitud POST de actualización en la vista del juego

## Documentación y Mantenimiento

### Mejora de la Documentación
- Adición de comentarios y documentación en el código
- Actualización de README y otros documentos del proyecto

### Resolución de Problemas y Optimización
- Identificación y corrección de errores
- Optimización del rendimiento en varias partes del sistema


## Code reviews

Helping team members with pull requests.