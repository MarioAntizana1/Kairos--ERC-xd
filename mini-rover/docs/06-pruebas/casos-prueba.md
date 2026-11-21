# Casos de prueba

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
> Los resultados se registran en [`matriz-trazabilidad-pruebas.md`](matriz-trazabilidad-pruebas.md) y en la evidencia.

## 1. Resumen

| ID | Nombre | Nivel | Requisito | Estado |
|---|---|---|---|---|
| TC-01 | Validación de waypoints | Unitario | RF-01 | Pendiente |
| TC-02 | Transiciones de estado | Unitario | RF-02, RF-06 | Pendiente |
| TC-03 | Reintentos y fallo | Unitario | RF-11 | Pendiente |
| TC-04 | Progreso y resumen | Unitario | RF-05 | Pendiente |
| TC-05 | Carga del YAML de ejemplo | Unitario | RF-01 | Pendiente |
| TC-06 | Build y launch de simulación | Integración | RF-08, RNF-08 | Pendiente |
| TC-07 | Árbol TF completo | Integración | RF-04 | Pendiente |
| TC-08 | Topics y frecuencias | Integración | RF-05, RNF-03, RNF-13 | Pendiente |
| TC-09 | Goal simple con Nav2 | Integración | RF-02, RF-04 | Pendiente |
| TC-10 | Misión nominal de 5 waypoints | Sistema | RF-02, RF-07 | Pendiente |
| TC-11 | Evitación de obstáculo | Sistema | RF-03 | Pendiente |
| TC-12 | Fallo inducido y reintento | Sistema | RF-11 | Pendiente |
| TC-13 | Aborto seguro | Sistema | RF-06 | Pendiente |
| TC-14 | Preflight y arranque | Sistema | RF-09, RF-10, RNF-05, RNF-08 | Pendiente |
| TC-15 | 10 repeticiones de fiabilidad | Sistema | RNF-01 | Pendiente |
| TC-16 | Precisión final | Sistema | RNF-02 | Pendiente |
| TC-17 | Parada de emergencia | Hardware | RNF-04, RNF-10 | Pendiente |
| TC-18 | Batería baja y autonomía | Hardware | RF-13, RNF-06 | Pendiente |
| TC-19 | Demo completa de aceptación | Aceptación | RF-09, RNF-12 | Pendiente |
| TC-20 | Rendimiento en Pi 4 8 GB | Análisis | RNF-07 | Pendiente |
| TC-21 | Validación documental y trazabilidad | Documentación | RNF-11 | Pendiente |

## 2. Casos unitarios

### TC-01 — Validación de waypoints

- **Objetivo:** rechazar misiones inválidas antes de mover el rover.
- **Precondiciones:** Python 3.10+; sin ROS.
- **Procedimiento:**
  1. Crear una lista vacía → `MissionPlanner` debe lanzar `ValueError`.
  2. Crear dos waypoints con el mismo ID → `ValueError`.
  3. Crear un waypoint con `x = NaN` → `ValueError`.
  4. Crear un waypoint con `tolerance = 0` → `ValueError`.
  5. Crear un waypoint con `timeout_s = -1` → `ValueError`.
- **Esperado:** todos los casos inválidos fallan con un mensaje claro; el caso válido se acepta.
- **Comando:** `python3 -m unittest discover -s ros_ws/src/rover_mission/test -v`.
- **Evidencia:** salida de tests en `logs/`.

### TC-02 — Transiciones de estado

- **Objetivo:** verificar la máquina de estados.
- **Procedimiento:**
  1. `IDLE → start() → RUNNING`.
  2. `RUNNING → mark_reached()` avanza.
  3. `RUNNING → pause() → PAUSED`; `resume() → RUNNING`.
  4. `RUNNING → abort() → ABORTED`.
  5. Intentar `mark_reached()` en `IDLE` → error.
- **Esperado:** cada transición es válida y las inválidas lanzan excepción.
- **Requisitos:** RF-02, RF-06.

### TC-03 — Reintentos y fallo

- **Objetivo:** comprobar la política de reintentos.
- **Procedimiento:**
  1. `max_retries=1`; `mark_failed("timeout")` → devuelve `True` y sigue `RUNNING`.
  2. Segundo `mark_failed("timeout")` → devuelve `False`, estado `FAILED`.
  3. `max_retries=0`; primer fallo → `FAILED`.
- **Esperado:** se reintenta exactamente `max_retries` veces y luego falla.
- **Requisitos:** RF-11.

### TC-04 — Progreso y resumen

- **Objetivo:** validar el cálculo de progreso y el resumen.
- **Procedimiento:**
  1. Misión de 4 waypoints; alcanzar 1 → progreso 0.25.
  2. Alcanzar 4 → progreso 1.0 y estado `COMPLETED`.
  3. Generar `summary()` y comprobar conteos y listas.
- **Esperado:** progreso correcto; resumen con reached/failed/attempts.
- **Requisitos:** RF-05.

### TC-05 — Carga del YAML de ejemplo

- **Objetivo:** validar el archivo `waypoints_demo.yaml` real.
- **Procedimiento:**
  1. Cargar el YAML con `yaml.safe_load`.
  2. Construir `MissionPlanner`.
  3. Comprobar 5 waypoints y IDs únicos.
  4. Verificar que existe `BASE` si `return_to_base: true`.
- **Esperado:** carga sin errores y misión válida.
- **Requisitos:** RF-01.

## 3. Casos de integración

### TC-06 — Build y launch de simulación

- **Objetivo:** comprobar que el workspace compila y la simulación arranca.
- **Precondiciones:** Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic.
- **Procedimiento:**
  1. `rosdep install --from-paths src --ignore-src -r -y`.
  2. `colcon build --symlink-install`.
  3. `ros2 launch rover_bringup sim.launch.py`.
  4. Esperar 30 s.
- **Esperado:** build sin errores; Gazebo, RViz, Nav2 y el nodo de misión arrancan sin excepciones.
- **Evidencia:** log de build + captura + `ros2 node list`.
- **Requisitos:** RF-08, RNF-08.

### TC-07 — Árbol TF completo

- **Objetivo:** verificar las transformadas.
- **Procedimiento:**
  1. `ros2 run tf2_ros tf2_echo map base_footprint`.
  2. `ros2 run tf2_ros tf2_echo base_footprint laser_link`.
  3. `ros2 run tf2_tools view_frames`.
- **Esperado:** `map → odom → base_footprint → base_link → laser_link` sin huecos.
- **Requisitos:** RF-04.

### TC-08 — Topics y frecuencias

- **Objetivo:** verificar sensores, comandos y telemetría.
- **Procedimiento:**
  1. `ros2 topic hz /scan` (≈ 10 Hz).
  2. `ros2 topic hz /odom` (≥ 20 Hz).
  3. `ros2 topic echo /cmd_vel --once` durante la misión.
  4. `ros2 topic hz /rover/mission/status` (≈ 2 Hz).
  5. Comprobar que `linear.x ≤ 0.45`.
- **Esperado:** frecuencias y límites correctos.
- **Requisitos:** RF-05, RNF-03, RNF-13.

### TC-09 — Goal simple con Nav2

- **Objetivo:** validar la interfaz `NavigateToPose` antes de la misión.
- **Procedimiento:**
  1. Enviar un goal a `(2, 0)` con `ros2 action send_goal`.
  2. Observar el resultado.
- **Esperado:** el rover llega y el resultado es `SUCCEEDED`.
- **Requisitos:** RF-02, RF-04.

## 4. Casos de sistema

### TC-10 — Misión nominal de 5 waypoints

- **Objetivo:** completar la misión de referencia.
- **Procedimiento:**
  1. Lanzar simulación y misión.
  2. Ejecutar `start`.
  3. Observar los 5 waypoints.
  4. Al terminar, revisar estado y resumen.
- **Esperado:** `COMPLETED`, 5/5, sin colisiones ni intervenciones, ≤ 10 min.
- **Evidencia:** bag + summary + vídeo.
- **Requisitos:** RF-02, RF-07.

### TC-11 — Evitación de obstáculo

- **Objetivo:** demostrar evitación.
- **Procedimiento:**
  1. Colocar un obstáculo en la línea entre WP-01 y WP-02 (sim: insertar modelo; hw: caja).
  2. Ejecutar la misión.
  3. Medir la distancia mínima al obstáculo.
- **Esperado:** rodea el obstáculo y llega; distancia > radio del robot.
- **Requisitos:** RF-03.

### TC-12 — Fallo inducido y reintento

- **Objetivo:** comprobar la recuperación.
- **Procedimiento:**
  1. Hacer inalcanzable un waypoint (bloquearlo con un obstáculo).
  2. Ejecutar con `max_retries=1`.
  3. Revisar logs y estado.
- **Esperado:** un reintento y luego `FAILED`; sin acelerar ni colisionar.
- **Requisitos:** RF-11.

### TC-13 — Aborto seguro

- **Objetivo:** verificar el aborto por software.
- **Procedimiento:**
  1. Durante la misión, llamar `/rover/mission/abort`.
  2. Medir el tiempo hasta `/cmd_vel = 0`.
  3. Revisar el estado y el motivo.
- **Esperado:** estado `ABORTED`, velocidad cero en ≤ 0.5 s, rover detenido.
- **Requisitos:** RF-06.

### TC-14 — Preflight y arranque

- **Objetivo:** verificar el chequeo previo y el tiempo de arranque.
- **Procedimiento:**
  1. Ejecutar `scripts/demo/preflight.sh`.
  2. Medir el tiempo desde el encendido hasta `IDLE` + Nav2 activo.
  3. Forzar un fallo (desconectar LiDAR) y repetir.
- **Esperado:** preflight 0 con todo correcto; ≠ 0 con fallo; arranque ≤ 60 s.
- **Requisitos:** RF-09, RF-10, RNF-05, RNF-08.

### TC-15 — 10 repeticiones de fiabilidad

- **Objetivo:** medir RNF-01.
- **Procedimiento:** ejecutar 10 veces la misión nominal, registrar éxito/fallo y calcular la tasa.
- **Esperado:** ≥ 8/10.
- **Requisitos:** RNF-01.

### TC-16 — Precisión final

- **Objetivo:** medir RNF-02.
- **Procedimiento:** en cada ensayo, medir la distancia final al waypoint (Gazebo o cinta métrica).
- **Esperado:** media ≤ 0.30 m; p95 ≤ 0.50 m.
- **Requisitos:** RNF-02.

## 5. Casos de hardware y seguridad

### TC-17 — Parada de emergencia

- **Objetivo:** verificar la e-stop.
- **Procedimiento:**
  1. Rover a 0.3 m/s en línea recta.
  2. Accionar la e-stop.
  3. Medir la distancia recorrida hasta el reposo.
  4. Rearmar y comprobar que no se mueve solo.
- **Esperado:** detención ≤ 0.30 m; sin movimiento al rearmar; motores sin potencia.
- **Requisitos:** RNF-04, RNF-10.
- **Nota:** prueba con observador y zona despejada.

### TC-18 — Batería baja y autonomía

- **Objetivo:** verificar RF-13 y RNF-06.
- **Procedimiento:**
  1. Simular voltaje bajo (o descargar batería de forma controlada).
  2. Comprobar aborto y estado `BATTERY_LOW`.
  3. Medir autonomía con carga completa hasta el umbral.
- **Esperado:** aborto al cruzar el umbral; autonomía ≥ 30 min.
- **Requisitos:** RF-13, RNF-06.
- **Referencia de diseño:** [`calculo-energetico.md`](../04-diseno/energia/calculo-energetico.md).
- **Estado:** pendiente de hardware.

### TC-20 — Rendimiento en Raspberry Pi 4 8 GB

- **Objetivo:** medir RNF-07.
- **Procedimiento:**
  1. Ejecutar la misión durante 30 min.
  2. Registrar CPU, RAM y temperatura cada 5 s.
  3. Revisar throttling.
- **Esperado:** CPU media < 80%, pico < 95%, RAM < 6 GB, T < 80 °C.
- **Requisitos:** RNF-07.

## 6. Aceptación y documentación

### TC-19 — Demo completa de aceptación

- **Objetivo:** validar el guion de demo de 10 minutos.
- **Procedimiento:**
  1. Seguir el runbook.
  2. Ejecutar la misión.
  3. Mostrar evidencia y FAQ.
  4. Medir el tiempo.
- **Esperado:** demo completa en ≤ 10 min, sin intervención no prevista.
- **Requisitos:** RF-09, RNF-12.

### TC-21 — Validación documental y trazabilidad

- **Objetivo:** comprobar que la documentación es coherente.
- **Procedimiento:**
  1. `make docs`.
  2. `make assets-check`.
  3. Revisar que todos los RF/RNF tienen caso y evidencia.
- **Esperado:** 0 errores; 100% de trazabilidad.
- **Requisitos:** RNF-11.

## 7. Historial

| Fecha | Cambio | Autor |
|---|---|---|
| 2026-11-21 | Versión inicial con 21 casos | QA |
