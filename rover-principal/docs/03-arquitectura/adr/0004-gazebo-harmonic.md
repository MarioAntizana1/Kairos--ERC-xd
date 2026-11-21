# ADR-0004 — Simular con Gazebo Harmonic y ros_gz

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Software · Reemplaza a: —

## Contexto

Necesitamos validar la navegación, los sensores y la integración ROS 2 antes de comprar y montar el hardware. La simulación debe ser compatible con ROS 2 Jazzy, tener LiDAR e IMU, y permitir generar evidencia reproducible.

## Alternativas consideradas

| Alternativa | ROS 2 Jazzy | Físicas | Sensores | Curva | Veredicto |
|---|---|---|---|---|---|
| **Gazebo Harmonic + ros_gz** | Soporte oficial | Buenas | LiDAR, IMU, cámara | Media | **Elegida** |
| Gazebo Classic | EOL | Buenas | Buenos | Media | Descartada |
| Webots | `webots_ros2` | Muy buenas | Excelentes | Media | Alternativa |
| NVIDIA Isaac Sim | `isaac_ros` | Excelentes | RTX | Alta | Futuro |
| MuJoCo | Puentes | Excelentes | Limitados | Media | Investigación |

## Decisión

Usar **Gazebo Harmonic** con **`ros_gz`** (paquetes `ros-jazzy-ros-gz`), mundo SDF generado desde `arena.json`, y bridges para `/clock`, `/scan`, `/imu`, `/odom` y `/cmd_vel`.

## Consecuencias

### Positivas

- Combinación soportada por ROS 2 Jazzy y con binarios en `packages.ros.org`.
- Sensores y plugins suficientes para el demo.
- Integración directa con Nav2 y RViz.
- Mundo y mapa generados de forma determinista.

### Negativas

- El modelo URDF necesita plugins específicos de Gazebo.
- La física no reproduce fielmente el terreno real.
- El sensor `gpu_lidar` requiere renderizado (puede fallar en headless sin GPU).
- La sintaxis SDF/URDF cambia entre versiones.

### Neutrales

- El paquete de misión no depende del simulador; solo el launch.

## Mitigaciones

- Probar el launch en un host con GPU o con renderizado por software.
- Documentar la versión exacta de Gazebo y `ros_gz`.
- Validar el mundo con `gz sdf -k` antes de lanzar.
- Registrar la brecha sim-real en el protocolo de experimentos.

## Criterios de revisión

- Si el LiDAR simulado no es fiable o el rendimiento es insuficiente.
- Si se necesita terreno deformable, polvo o iluminación realista.
- Si se añade visión estéreo o IA que requiera Isaac Sim.
- Si Gazebo Harmonic deja de recibir soporte.

## Referencias

- [F-09] Gazebo + ROS installation.
- [F-10] `ros_gz` README.
- [F-07] Nav2 Quickstart (Gazebo moderno).
- [`../../01-investigacion/estado-del-arte.md`](../../01-investigacion/estado-del-arte.md).
