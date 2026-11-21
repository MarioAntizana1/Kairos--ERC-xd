# Interfaces de datos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Software
>
> Interfaces propuestas. Si se implementa ROS 2, los nombres y tipos se respetan;
> si se usa Python puro, se mantiene el mismo contrato lógico.

## 1. Topics ROS 2

| Topic | Tipo | Frecuencia | Frame | QoS | Nota |
|---|---|---|---:|---|---|
| `/vision/left/image_raw` | `sensor_msgs/Image` | 10–15 Hz | `camera_left_optical` | Best effort | 2304 × 1296, bayer/rgb8 |
| `/vision/right/image_raw` | `sensor_msgs/Image` | 10–15 Hz | `camera_right_optical` | Best effort | Igual que izquierda |
| `/vision/left/camera_info` | `sensor_msgs/CameraInfo` | 1 Hz | `camera_left_optical` | Reliable | K, D, R, P |
| `/vision/right/camera_info` | `sensor_msgs/CameraInfo` | 1 Hz | `camera_right_optical` | Reliable | K, D, R, P |
| `/vision/disparity` | `stereo_msgs/DisparityImage` | 5–15 Hz | `camera_left_optical` | Best effort | 1152 × 648 |
| `/vision/depth` | `sensor_msgs/Image` (32FC1) | 5–15 Hz | `camera_left_optical` | Best effort | Metros; NaN inválido |
| `/vision/points` | `sensor_msgs/PointCloud2` | 2–5 Hz | `camera_left_optical` o `map` | Best effort | XYZRGB; voxel 5 cm |
| `/vision/tof` | `std_msgs/Float32MultiArray` | 10–50 Hz | `tof_link` | Best effort | Distancia al piso: 1 o 64 zonas + estado |
| `/vision/altitude` | `sensor_msgs/Range` | 10–50 Hz | `tof_link` | Best effort | Altitud bajo la cámara; `radiation_type=INFRARED` |
| `/vision/obstacle` | `sensor_msgs/PointCloud2` o `vision_msgs/Detection3DArray` | 10 Hz | `base_link` | Best effort | Rejilla de distancia libre del estéreo |
| `/vision/status` | `diagnostic_msgs/DiagnosticStatus` | 1 Hz | — | Reliable | Salud, FPS, temperatura |
| `/vision/scan` | Acción `vision/Scan` (propuesta) | — | — | Reliable | Inicio/fin de escaneo |

## 2. Topics de la FC

| Topic | Tipo | Frecuencia | Uso |
|---|---|---:|---|
| `/mavros/imu/data` | `sensor_msgs/Imu` | 50 Hz | Actitud |
| `/mavros/local_position/pose` | `geometry_msgs/PoseStamped` | 10–50 Hz | Posición local |
| `/mavros/global_position/global` | `sensor_msgs/NavSatFix` | 1–10 Hz | Georreferencia |
| `/mavros/state` | `mavros_msgs/State` | 1 Hz | Estado de vuelo |

> Si no se usa MAVROS, el nodo `pose_node` puede leer MAVLink directamente y
> publicar los mismos tipos. No se envían comandos de motor desde la visión.

## 3. MAVLink

| Mensaje | Dirección | Uso |
|---|---|---|
| `ATTITUDE` | FC → Pi | Cuaternión y velocidades angulares |
| `LOCAL_POSITION_NED` | FC → Pi | Posición local |
| `GPS_RAW_INT` | FC → Pi | Posición global |
| `TIMESYNC` | bidireccional | Offset de reloj |
| `DISTANCE_SENSOR` | Pi → FC (si se soporta) | Altitud del ToF de piso; orientación DOWN |
| `OBSTACLE_DISTANCE` | Pi → FC (si se soporta) | Distancia libre del estéreo, opcional |
| `STATUSTEXT` | Pi → FC | Estado/errores |
| `HEARTBEAT` | ambos | Salud del enlace |

- Baud rate: 57600 o 921600 (confirmar con la FC).
- No usar `SET_POSITION_TARGET_*`, `COMMAND_LONG` de motores ni `RC_CHANNELS_OVERRIDE`.
- Si la FC no soporta `OBSTACLE_DISTANCE`, publicar solo en ROS 2 y en la
  estación de tierra.

## 4. Frames y convenciones

- REP-103/REP-105 para `map`, `base_link`, `odom`.
- Frames ópticos: `camera_left_optical`, `camera_right_optical`, `tof_link`.
  - \(x\) derecha, \(y\) abajo, \(z\) adelante (convención óptica).
  - `tof_link` apunta al piso en la configuración de mapeo; su extrínseca a la
    cámara se publica en `/tf_static` y en el YAML.
- `camera_left_optical` es el frame de referencia de la profundidad y la nube.
- La extrínseca cámara → cuerpo se publica en `/tf_static`.
- La baseline se documenta en el YAML y en el URDF/descripción.

## 5. Calibración (YAML)

```yaml
schema_version: 1
calibration_id: "2026-11-21T150000Z-b150"
date: "2026-11-21T15:00:00Z"
image_size: [2304, 1296]
baseline_mm: 150.0
focus_position_m: 3.0
temperature_c: 22.5
rms_intrinsic_left_px: 0.31
rms_intrinsic_right_px: 0.33
rms_stereo_px: 0.42
epipolar_error_px: 0.21
camera_matrix_left: [[1693.0, 0.0, 1152.0],
                     [0.0, 1693.0, 648.0],
                     [0.0, 0.0, 1.0]]
dist_coeffs_left: [0.0, 0.0, 0.0, 0.0, 0.0]
camera_matrix_right: [[1693.0, 0.0, 1152.0],
                      [0.0, 1693.0, 648.0],
                      [0.0, 0.0, 1.0]]
dist_coeffs_right: [0.0, 0.0, 0.0, 0.0, 0.0]
R: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
T: [-150.0, 0.0, 0.0]
R1: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
R2: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
P1: [[1693.0, 0.0, 1152.0, 0.0],
     [0.0, 1693.0, 648.0, 0.0],
     [0.0, 0.0, 1.0, 0.0]]
P2: [[1693.0, 0.0, 1152.0, -253950.0],
     [0.0, 1693.0, 648.0, 0.0],
     [0.0, 0.0, 1.0, 0.0]]
Q: [[1.0, 0.0, 0.0, -1152.0],
    [0.0, 1.0, 0.0, -648.0],
    [0.0, 0.0, 0.0, 1693.0],
    [0.0, 0.0, 1.0/150.0, 0.0]]

tof:
  model: tfmini_plus           # vl53l1x/vl53l5cx solo para ≤4 m
  mount: downward
  range_m: 12.0
  interface: uart
  extrinsic_to_camera_left:
    translation_m: [0.0, 0.0, 0.0]
    rotation_rpy_deg: [0.0, 0.0, 0.0]

ground_plane:
  normal: [0.0, 0.0, 1.0]
  distance_m: 2.0
  rms_m: 0.02
```

> Los valores son ilustrativos; se reemplazan por la calibración real. El archivo
> se guarda con hash y no se edita después de volar.

## 6. Registro de sesión

```text
sessions/2026-11-21T150000Z_scan-01/
├── metadata.json          # versión, commit, operador, lugar, clima
├── calibration.yaml       # copia de la calibración usada
├── left/000001.jpg        # frames izquierdos
├── right/000001.jpg       # frames derechos
├── depth/000001.png       # 16-bit; escala en metadata
├── tof_floor.csv          # timestamp, zona, distancia al piso, estado
├── ground_plane.yaml      # normal, altura, RMS, fecha
├── pose.csv               # timestamp, qx, qy, qz, qw, x, y, z
├── obstacles.csv          # timestamp, celda, distancia (estéreo)
└── logs/                  # stdout/stderr
```

- `metadata.json`: `session_id`, `start`, `end`, `software_version`,
  `calibration_id`, `operator`, `location`, `weather`, `notes`.
- Hash SHA-256 de la sesión al cerrar.
- No incluir rostros ni datos personales sin consentimiento.

## 7. Red

| Servicio | Puerto | Uso |
|---|---:|---|
| SSH | 22 | Administración |
| ROS 2 DDS | 7400–7500 (UDP) | Topics (si se usa ROS 2) |
| HTTP preview | 8080 | Monitorización |
| MAVLink | UART/USB | FC |

- Preferir 5 GHz; probar interferencia con la radio.
- Deshabilitar WiFi/BT en vuelo si no se usa el enlace de red.
- No exponer SSH a Internet; usar clave y firewall.

## 8. Versionado

- `schema_version` en YAML y `metadata.json`.
- `software_version` = tag/commit.
- Cambios incompatibles de topics → nueva versión y ADR.
- La calibración y el software se referencian por ID/hash en la evidencia.

## 9. Referencias

- ROS 2 Jazzy: `F-26`.
- MAVLink: `F-24`.
- Picamera2: `F-25`.
- OpenCV: `F-23`.
