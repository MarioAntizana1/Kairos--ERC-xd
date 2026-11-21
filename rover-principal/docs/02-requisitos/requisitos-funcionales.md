# Requisitos funcionales

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto
> Prioridad MoSCoW: **M**ust, **S**hould, **C**ould, **W**on't.

## 1. Resumen

| ID | Requisito | Prioridad | Verificación |
|---|---|---|---|
| RF-01 | Cargar la misión desde un archivo YAML validado | M | Prueba |
| RF-02 | Navegar de forma autónoma por una secuencia de waypoints | M | Prueba |
| RF-03 | Evitar obstáculos estáticos con LiDAR 2D | M | Prueba |
| RF-04 | Localizarse en el mapa de la arena | M | Prueba |
| RF-05 | Publicar telemetría de estado y progreso | M | Prueba |
| RF-06 | Abortar la misión de forma segura y permitir reanudar | M | Prueba |
| RF-07 | Registrar bag, logs y resumen de misión | M | Prueba |
| RF-08 | Ejecutar la misma pila en simulación y hardware | M | Prueba |
| RF-09 | Ofrecer una interfaz de operador simple | S | Demostración |
| RF-10 | Ejecutar un preflight automatizado | S | Prueba |
| RF-11 | Reintentar un waypoint fallido según configuración | S | Prueba |
| RF-12 | Regresar a la base al terminar o abortar | C | Prueba |
| RF-13 | Monitorizar la batería y detenerse bajo umbral | S | Prueba |

## 2. Detalle

### RF-01 — Carga de misión desde YAML

El sistema **debe** cargar una lista de waypoints desde un archivo YAML con esquema conocido (`frame_id`, `loop`, `waypoints[]`), validarla y rechazar misiones inválidas antes de mover el rover.

**Criterio de aceptación**

- Dado un YAML con 5 waypoints válidos, cuando se inicia el nodo, entonces la misión queda cargada con 5 waypoints y estado `IDLE`.
- Dado un YAML con IDs duplicados, coordenadas no finitas o lista vacía, cuando se inicia el nodo, entonces falla con un error claro y no envía ningún objetivo.

**Verificación:** TC-01, TC-05, TC-10.

### RF-02 — Navegación autónoma por waypoints

El sistema **debe** enviar cada waypoint a Nav2 mediante la acción `NavigateToPose`, esperar el resultado y continuar con el siguiente solo si el anterior se alcanzó.

**Criterio de aceptación**

- Dada una misión de 5 waypoints y un mapa válido, cuando se ejecuta, entonces el rover visita los 5 en orden y termina en estado `COMPLETED`.
- El operador no envía comandos de velocidad durante la ejecución.

**Verificación:** TC-09, TC-10, TC-15.

### RF-03 — Evitación de obstáculos

El sistema **debe** detectar obstáculos estáticos dentro del alcance del LiDAR y planificar una ruta que los evite, sin colisiones.

**Criterio de aceptación**

- Dado un obstáculo en la ruta directa entre dos waypoints, cuando el rover navega, entonces lo rodea y llega al waypoint sin contacto.
- La distancia mínima al obstáculo es mayor que el radio del robot.

**Verificación:** TC-11.

### RF-04 — Localización

El sistema **debe** estimar la pose del rover en el frame `map` usando AMCL, el mapa de la arena y el LiDAR, y publicar la transformada `map → odom`.

**Criterio de aceptación**

- Dada una pose inicial conocida, cuando el rover se mueve, entonces `map → odom → base_footprint` está disponible y la pose converge.
- El error de posición final es ≤ 0.30 m.

**Verificación:** TC-07, TC-09, TC-16.

### RF-05 — Telemetría

El sistema **debe** publicar el estado de la misión y el progreso en topics ROS 2, con un formato estable y documentado.

**Criterio de aceptación**

- Durante la misión se publica `/rover/mission/status` (JSON) al menos a 1 Hz.
- Se publica `/rover/mission/progress` como `Float32` entre 0.0 y 1.0.
- La latencia de actualización es ≤ 1 s.

**Verificación:** TC-08, TC-10.

### RF-06 — Abortado seguro y reanudación

El sistema **debe** permitir abortar la misión mediante un servicio o la parada de emergencia, detener el rover y registrar el motivo. Si el aborto es por software, **debe** poder reanudarse desde el waypoint actual.

**Criterio de aceptación**

- Dado un comando de aborto, cuando se recibe, entonces se cancela el objetivo de Nav2, se publica `ABORTED` y el rover se detiene.
- Tras un aborto por software, un comando de reanudación continúa desde el waypoint no alcanzado.

**Verificación:** TC-13.

### RF-07 — Registro de datos

El sistema **debe** permitir grabar un rosbag2 con los topics de navegación y guardar logs y un resumen de misión en la carpeta de evidencia.

**Criterio de aceptación**

- Al finalizar una misión, existe un bag con `/scan`, `/odom`, `/cmd_vel`, `/tf`, `/tf_static`, `/rover/mission/status` y `/rover/mission/progress`.
- Existe un `summary.json` con estado, waypoints alcanzados, tiempo y errores.

**Verificación:** TC-10, TC-19.

### RF-08 — Simulación y hardware con la misma pila

El sistema **debe** usar los mismos paquetes y la misma configuración de Nav2 en simulación y en el rover, cambiando solo el launch y los drivers.

**Criterio de aceptación**

- La misión de 5 waypoints se ejecuta en Gazebo y en hardware sin cambios en `rover_mission`.
- El launch de simulación y el de hardware comparten `nav2_params.yaml`.

**Verificación:** TC-06, TC-10, TC-19.

### RF-09 — Interfaz de operador

El sistema **debe** ofrecer una forma simple de iniciar, pausar, abortar y visualizar la misión, sin exigir conocimientos de ROS 2.

**Criterio de aceptación**

- El runbook permite a una persona no desarrolladora ejecutar la demo en ≤ 15 min de preparación.
- RViz2 muestra mapa, robot, LiDAR, ruta y estado.
- Existe un comando de una línea para iniciar y otro para abortar.

**Verificación:** TC-14, TC-19.

### RF-10 — Preflight automatizado

El sistema **debe** comprobar el estado del sistema antes de cada misión: nodos, TF, topics, batería, disco y e-stop.

**Criterio de aceptación**

- El script devuelve código 0 si todo está listo y ≠ 0 si falta algo crítico.
- El informe de preflight se guarda en la evidencia.

**Verificación:** TC-14.

### RF-11 — Reintento de waypoint

El sistema **debe** reintentar un waypoint fallido hasta `max_retries` veces antes de declarar la misión fallida.

**Criterio de aceptación**

- Con `max_retries: 1`, un fallo se reintenta una vez.
- Si el reintento falla, la misión termina en `FAILED` y se registra el motivo.

**Verificación:** TC-03, TC-12.

### RF-12 — Retorno a base

El sistema **debe** poder enviar el rover a un waypoint de base al terminar la misión o tras un aborto por software, si está configurado.

**Criterio de aceptación**

- Con `return_to_base: true`, `BASE` debe ser el último waypoint de la lista y se navega a él al completar la secuencia.
- Si el retorno falla, el estado es `COMPLETED_WITH_WARNING` y se registra.

**Verificación:** TC-10 (opcional).

### RF-13 — Monitorización de batería

El sistema **debe** leer el voltaje de la batería y detener la misión si cae por debajo del umbral configurado.

**Criterio de aceptación**

- Con un voltaje simulado por debajo del umbral, la misión se aborta y se publica `BATTERY_LOW`.
- El umbral es configurable y está documentado.

**Verificación:** TC-18 (pendiente de hardware).

## 3. Requisitos descartados (Won't)

| ID | Requisito | Motivo |
|---|---|---|
| W-01 | Brazo manipulador | Fase rover grande |
| W-02 | Perforación | Fase rover grande |
| W-03 | Dron | Fase rover grande |
| W-04 | SLAM visual | Complejidad y CPU |
| W-05 | Navegación GPS | No necesaria para el demo indoor |

## 4. Historial

| Fecha | Cambio | Autor |
|---|---|---|
| 2026-11-21 | Versión inicial | Producto |
