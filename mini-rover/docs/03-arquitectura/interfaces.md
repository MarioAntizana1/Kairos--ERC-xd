# Interfaces del sistema

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Navegación

## 1. Convenciones

- Frames en `snake_case`, según REP 105.
- Topics en minúsculas, con prefijo `/rover/` para los propios.
- Mensajes estándar siempre que sea posible.
- Los cambios de interfaz son versionados y se registran en el CHANGELOG.

## 2. Árbol TF

```text
map
└── odom                (AMCL)
    └── base_footprint  (odometría / base)
        └── base_link
            ├── laser_link
            ├── imu_link
            ├── camera_link (opcional)
            ├── wheel_front_left_link
            ├── wheel_front_right_link
            ├── wheel_rear_left_link
            └── wheel_rear_right_link
```

| Transformada | Publica | Tipo | Nota |
|---|---|---|---|
| `map → odom` | AMCL | Dinámica | Corrige deriva |
| `odom → base_footprint` | Driver / Gazebo + broadcaster | Dinámica | Odometría |
| `base_footprint → base_link` | `robot_state_publisher` | Estática | Altura del chasis |
| `base_link → laser_link` | `robot_state_publisher` | Estática | Montaje del LiDAR |
| `base_link → imu_link` | `robot_state_publisher` | Estática | Montaje de IMU |
| `base_link → wheel_*` | `robot_state_publisher` | Dinámica (joint states) | Ruedas |

> En simulación, el plugin `DiffDrive` publica odometría; un nodo `odom_tf_broadcaster.py` convierte `/odom` en `odom → base_footprint`. En hardware, el driver de base debe publicar ambas cosas.

## 3. Topics

| Topic | Tipo | Dirección | Frecuencia | QoS | Descripción |
|---|---|---|---|---|---|
| `/scan` | `sensor_msgs/msg/LaserScan` | Sensor → sistema | 10 Hz | Sensor data | LiDAR 2D |
| `/imu` | `sensor_msgs/msg/Imu` | Sensor → sistema | 50 Hz | Sensor data | IMU |
| `/odom` | `nav_msgs/msg/Odometry` | Base → sistema | 20–50 Hz | Reliable | Odometría |
| `/cmd_vel` | `geometry_msgs/msg/Twist` | Nav2 → base | 20 Hz | Reliable | Velocidad |
| `/cmd_vel_smoothed` | `geometry_msgs/msg/Twist` | Suavizado → control | 20 Hz | Reliable | Velocidad suavizada |
| `/tf` | `tf2_msgs/msg/TFMessage` | Varios | 20–50 Hz | Reliable | Transformadas |
| `/tf_static` | `tf2_msgs/msg/TFMessage` | Varios | Al cambiar | Transient local | Transformadas estáticas |
| `/clock` | `rosgraph_msgs/msg/Clock` | Gazebo → sistema | 100 Hz | Reliable | Reloj de simulación |
| `/rover/mission/status` | `std_msgs/msg/String` | Misión → operador | 2 Hz | Reliable | JSON de estado |
| `/rover/mission/progress` | `std_msgs/msg/Float32` | Misión → operador | 2 Hz | Reliable | 0.0–1.0 |
| `/rover/mission/summary` | `std_msgs/msg/String` | Misión → evidencia | Al terminar | Transient local | JSON de resumen |

### 3.1 Direccionalidad en `ros_gz_bridge`

| Topic | Bridge | Dirección |
|---|---|---|
| `/clock` | `rosgraph_msgs/msg/Clock` ↔ `gz.msgs.Clock` | GZ → ROS |
| `/scan` | `sensor_msgs/msg/LaserScan` ↔ `gz.msgs.LaserScan` | GZ → ROS |
| `/imu` | `sensor_msgs/msg/Imu` ↔ `gz.msgs.IMU` | GZ → ROS |
| `/odom` | `nav_msgs/msg/Odometry` ↔ `gz.msgs.Odometry` | GZ → ROS |
| `/cmd_vel` | `geometry_msgs/msg/Twist` ↔ `gz.msgs.Twist` | ROS → GZ |

## 4. Acciones

### `navigate_to_pose` (Nav2)

- **Tipo:** `nav2_msgs/action/NavigateToPose`
- **Cliente:** `rover_mission`
- **Servidor:** Nav2 `bt_navigator`
- **Objetivo:**

```yaml
pose:
  header:
    frame_id: map
  pose:
    position: {x: 4.0, y: 2.5, z: 0.0}
    orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
behavior_tree: ""
```

- **Feedback:** `current_pose`, `navigation_time`, `estimated_time_remaining`, `number_of_recoveries`, `distance_remaining`.
- **Resultado:** `nav2_msgs/action/NavigateToPose_Result`.

## 5. Servicios

| Servicio | Tipo | Descripción | Seguridad |
|---|---|---|---|
| `/rover/mission/start` | `std_srvs/srv/Trigger` | Inicia la misión cargada | Requiere rover en `IDLE` |
| `/rover/mission/abort` | `std_srvs/srv/Trigger` | Aborta y cancela el objetivo | Siempre permitido |
| `/rover/mission/pause` | `std_srvs/srv/Trigger` | Pausa tras el waypoint actual | Opcional |
| `/rover/mission/resume` | `std_srvs/srv/Trigger` | Reanuda desde el waypoint actual | Solo tras pausa/aborto software |

## 6. Formato de misión (YAML)

```yaml
frame_id: map
loop: false
return_to_base: true
max_retries: 1
goal_timeout_s: 120.0
waypoints:
  - id: WP-01
    x: 4.0
    y: 2.5
    yaw: 0.0
    tolerance: 0.25
    timeout_s: 90.0
  - id: WP-02
    x: -4.0
    y: 2.5
    yaw: 1.57
    tolerance: 0.25
    timeout_s: 90.0
```

### Reglas de validación

- `frame_id` no vacío.
- Al menos un waypoint.
- IDs únicos y no vacíos.
- `x`, `y`, `yaw`, `tolerance`, `timeout_s` finitos.
- `tolerance > 0` y `timeout_s > 0`.
- `max_retries ≥ 0`.
- Si `return_to_base: true`, debe existir un waypoint con `id: BASE` y debe ser el **último** de la lista.

## 7. Estado de misión (JSON)

```json
{
  "state": "RUNNING",
  "mission_id": "demo-2026-11-21T12-00-00",
  "frame_id": "map",
  "current_waypoint": "WP-02",
  "index": 1,
  "total": 5,
  "progress": 0.2,
  "attempts": 0,
  "message": "navigating to WP-02",
  "timestamp": "2026-11-21T12:00:00.000Z"
}
```

### Estados

| Estado | Significado |
|---|---|
| `IDLE` | Cargado, sin empezar |
| `RUNNING` | Navegando |
| `PAUSED` | Pausado tras el waypoint actual |
| `COMPLETED` | Todos los waypoints alcanzados |
| `COMPLETED_WITH_WARNING` | Completado, con fallo en el retorno |
| `FAILED` | Waypoint fallido sin reintentos |
| `ABORTED` | Cancelado por el operador |
| `BATTERY_LOW` | Abortado por batería |

## 8. Resumen de misión (JSON)

```json
{
  "mission_id": "demo-2026-11-21T12-00-00",
  "state": "COMPLETED",
  "started_at": "2026-11-21T12:00:00.000Z",
  "finished_at": "2026-11-21T12:04:32.000Z",
  "duration_s": 272.0,
  "total_waypoints": 5,
  "reached": ["WP-01", "WP-02", "WP-03", "WP-04", "WP-05"],
  "failed": [],
  "attempts": 5,
  "aborted_reason": null
}
```

## 9. Parámetros de Nav2

| Parámetro | Valor | Justificación |
|---|---|---|
| `robot_radius` | 0.33 m | Radio del chasis con margen |
| `max_vel_x` | 0.45 m/s | RNF-03 |
| `max_vel_theta` | 1.2 rad/s | Giro seguro |
| `xy_goal_tolerance` | 0.25 m | Tolerancia de waypoint |
| `yaw_goal_tolerance` | 0.25 rad | Orientación |
| `inflation_radius` | 0.55 m | Evitar roces |
| `controller_frequency` | 10 Hz | CPU del Pi |
| `planner_frequency` | 1 Hz | Suficiente para mapa estático |
| `use_sim_time` | `true` en sim | Reloj de Gazebo |

El archivo completo está en `ros_ws/src/rover_bringup/config/nav2_params.yaml`.

## 10. Versionado de interfaces

| Versión | Cambio | Compatibilidad |
|---|---|---|
| 0.1 | Versión inicial | — |
| 0.2 (propuesta) | Interfaz Pi 4 ↔ ESP32; `/battery_state`, `/estop`, `/mcu/heartbeat`, `/diagnostics` | Aditiva; no rompe los topics existentes |
| 0.3 (propuesta) | Nodo LTE/GNSS LilyGO; telemetría remota fuera de DDS | Aditiva; no entra en el lazo de control |

Un cambio incompatible en topics, acciones o YAML requiere:

1. Nuevo campo o topic versionado (`/rover/v2/...`).
2. Actualización de este documento.
3. Actualización de pruebas y del nodo.
4. Registro en el CHANGELOG.

## 11. Interfaz Pi 4 ↔ ESP32 (propuesta ADR-0008)

> **Estado:** propuesta en revisión. No cambia los topics aceptados hasta que se
> apruebe el [ADR-0008](adr/0008-esp32-interfaz-tiempo-real.md). La Pi 4 sigue
> siendo el cerebro; el ESP32 es la interfaz de tiempo real.

### 11.1 Enlace físico

| Elemento | Propuesta |
|---|---|
| Bus | USB CDC (puerto nativo del ESP32-S3) |
| Middleware | micro-ROS sobre USB; `micro_ros_agent` en la Pi |
| Dispositivo | `/dev/rover_mcu` por regla udev; no depender de `/dev/ttyACM0` |
| Alimentación | 5 V 3 A separado; masa común en estrella |
| Velocidad | USB full-speed; el baudrate no aplica al CDC nativo |
| Cable | Corto, con ferrita y alivio de tensión |

### 11.2 Topics propuestos

| Topic | Tipo | Dirección | Frecuencia | QoS | Descripción |
|---|---|---|---|---|---|
| `/cmd_vel` | `geometry_msgs/msg/Twist` | Pi → MCU | 20–50 Hz | Reliable, depth 1 | Velocidad deseada |
| `/odom` | `nav_msgs/msg/Odometry` | MCU → Pi | 50 Hz | Sensor data | Odometría diferencial |
| `/imu` | `sensor_msgs/msg/Imu` | MCU → Pi | 50–100 Hz | Sensor data | BNO085 |
| `/battery_state` | `sensor_msgs/msg/BatteryState` | MCU → Pi | 1–5 Hz | Reliable | INA219/INA226 |
| `/estop` | `std_msgs/msg/Bool` | MCU → Pi | Al cambiar | Reliable, transient local | Estado de la seta |
| `/mcu/heartbeat` | `std_msgs/msg/UInt32` | Pi → MCU | 10 Hz | Reliable | Latido para watchdog |
| `/joint_states` | `sensor_msgs/msg/JointState` | MCU → Pi | 50 Hz | Sensor data | Ruedas, opcional |
| `/diagnostics` | `diagnostic_msgs/msg/DiagnosticArray` | MCU → Pi | 1 Hz | Reliable | Temperatura, corriente, estado |

### 11.3 Reglas de seguridad

- Si no llega `/cmd_vel` en **500 ms**, el MCU rampa a cero y deshabilita los
  drivers.
- Si no llega `/mcu/heartbeat` en **1 s**, el MCU también se detiene.
- La e-stop **corta la potencia del driver en hardware**; `/estop` es solo
  informativo y de diagnóstico.
- El MCU arranca siempre en estado `IDLE` con motores deshabilitados.
- El MCU no publica `odom → base_footprint`; la transformada la publica la Pi
  con `robot_localization` o un broadcaster dedicado.

### 11.4 Frontera con la Pi

| Se queda en la Pi | Se va al MCU |
|---|---|
| LiDAR `/scan` | PWM y dirección de motores |
| Cámara | Lectura de encoders |
| Nav2, AMCL, SLAM | IMU BNO085 |
| Misión y rosbag2 | INA219/INA226 |
| EKF y TF | E-stop, watchdog, LEDs |
| Registro y telemetría pesada | Sensores I²C de baja tasa |

> El LiDAR y la cámara **no** pasan por el MCU: son de alta tasa y ya tienen
> USB/CSI en la Pi. El MCU no reemplaza al LiDAR ni al driver de la Pi.

## 12. Interfaz LTE/GNSS (propuesta ADR-0012)

> **Estado:** propuesta. El enlace LTE es opcional y **no** forma parte de la
> cadena de seguridad ni del lazo de control. Ver
> [ADR-0012](adr/0012-lilygo-lte-gnss.md).

| Elemento | Propuesta |
|---|---|
| Enlace Pi 4 ↔ LilyGO | USB serie (puente USB-UART) o UART; el SIM7600 va por UART al ESP32 |
| Red | LTE Cat-4; variante SA-H/G compatible con el operador |
| Datos | MQTT/TLS o VPN; **no** exponer DDS/ROS a Internet |
| GNSS | `sensor_msgs/msg/NavSatFix` si se integra en ROS 2 |
| Telemetría | `/rover/remote/status` y logs; frecuencia ≤ 1 Hz |
| Seguridad | Sin `cmd_vel`, e-stop ni watchdog por LTE |
| Fallo | El rover sigue la misión local; solo se pierde telemetría remota |

Topics propuestos (si se acepta el spike):

| Topic | Tipo | Dirección | Frecuencia | QoS |
|---|---|---|---|---|
| `/rover/remote/status` | `std_msgs/msg/String` (JSON) | Pi → enlace | 0.2–1 Hz | Best effort |
| `/rover/remote/gnss` | `sensor_msgs/msg/NavSatFix` | LilyGO → Pi | 1 Hz | Sensor data |

> El detalle de firmware (PPP/RNDIS, MQTT o AT) se decide en el spike. No se
> asume que el puente exista.
