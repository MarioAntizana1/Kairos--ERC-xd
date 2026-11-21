# Estado del arte

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Navegación

## 1. Resumen ejecutivo

Para un rover de bajo coste que debe navegar de forma autónoma entre waypoints, la combinación con mejor relación madurez/esfuerzo en 2026 es:

- **ROS 2 Jazzy** sobre Ubuntu 24.04.
- **Nav2** como pila de navegación.
- **AMCL** con mapa estático para el demo; **SLAM Toolbox** para cartografiar previamente.
- **Navfn** como planificador global y **Regulated Pure Pursuit (RPP)** como controlador local por su bajo coste computacional.
- **Gazebo Harmonic** + `ros_gz` como simulador.
- **Raspberry Pi 5** como computadora de a bordo, con LiDAR 2D.

Esta sección justifica la elección y documenta alternativas descartadas.

## 2. ROS 2

ROS 2 es la evolución de ROS 1 con DDS como capa de comunicación, soporte multi-plataforma, ciclo de vida de nodos y mejor seguridad (SROS2). La distribución **Jazzy Jalisco** es LTS, se publicó en mayo de 2024 y es la versión objetivo de Ubuntu 24.04 Noble. Su fin de soporte está previsto para mayo de 2029, suficiente para el ERC 2027 y más allá.

| Característica | ROS 1 | ROS 2 Jazzy |
|---|---|---|
| Comunicación | TCPROS | DDS (CycloneDDS, FastDDS) |
| Tiempo real | Limitado | Mejor soporte |
| Multi-robot | Difícil | Namespaces, DDS |
| Seguridad | No | SROS2 |
| Soporte actual | EOL | LTS hasta 2029 |
| Ecosistema Nav2 | No | Sí |

**Decisión:** ROS 2 Jazzy. Ver [ADR-0001](../03-arquitectura/adr/0001-ros2-jazzy.md).

> Nota: en 2026 ya existe ROS 2 Lyrical Luth (LTS, Ubuntu 26.04) y la documentación de Gazebo lo recomienda para instalaciones nuevas. Se mantiene Jazzy por compatibilidad con Raspberry Pi 5 + Ubuntu 24.04, madurez de Nav2 y abundancia de ejemplos. La migración se evalúa en OQ-05.

## 3. Nav2

Nav2 es la pila de navegación de referencia para ROS 2. Proporciona:

- **Map server** y **AMCL** para localización probabilística.
- **Planner server** con Navfn, Smac 2D/Planner, entre otros.
- **Controller server** con DWB, MPPI, RPP, Rotation Shim.
- **Behavior server** con recuperación (spin, backup, wait).
- **BT Navigator** con árboles de comportamiento configurables.
- **Waypoint follower** y **route server**.
- **Costmaps** por capas (estática, obstáculos, inflación, voxel).

### 3.1 Comparativa de pilas

| Criterio | Nav2 | Stack propio | ArduPilot/MAVROS | ROS 1 move_base |
|---|---|---|---|---|
| Madurez | Alta | Baja | Alta en aerial/UGV |Legacy |
| ROS 2 nativo | Sí | Depende | Vía MAVROS | No |
| Coste de desarrollo | Medio | Alto | Medio | Alto (migración) |
| Flexibilidad | Alta | Total | Media | Media |
| Documentación | Excelente | Nula | Buena | Obsoleta |
| Soporte Pi 5 | Sí | Depende | Sí | No oficial |
| Recomendado | **Sí** | No | Solo si hay MAVLink | No |

**Decisión:** Nav2. Ver [ADR-0003](../03-arquitectura/adr/0003-nav2.md).

### 3.2 Planificadores

| Planificador | Tipo | Ventajas | Desventajas | Uso |
|---|---|---|---|---|
| Navfn | Grid, Dijkstra/A* | Simple, rápido, probado | Rutas poco suaves | **Global del demo** |
| Smac 2D | Grid, A* | Mejores rutas, suave | Más parámetros | Alternativa |
| Smac Hybrid-A* | Kinemático | Considera cinemática | Más CPU | Futuro Ackermann |
| Theta* | Grid any-angle | Rutas más cortas | Menos usado | Evaluar |

### 3.3 Controladores

| Controlador | Ventajas | Desventajas | CPU | Uso |
|---|---|---|---|---|
| DWB | Maduro, muchos críticos | Sensible a tuning | Media | Alternativa |
| MPPI | Muy bueno en obstáculos | Pesado para Pi | Alta | Descartado para Pi |
| RPP | Ligero, estable, fácil | Menos óptimo en pasillos | Baja | **Elegido** |
| Rotation Shim | Mejora giros | Requiere RPP/DWB | Baja | Opcional |

**Decisión:** RPP para el demo por su bajo coste computacional y comportamiento predecible en un rover diferencial. Se documenta la comparación con DWB en el protocolo de experimentos (opcional).

## 4. Localización y cartografía

| Enfoque | Cuándo usarlo | Ventajas | Limitaciones |
|---|---|---|---|
| **AMCL + mapa estático** | Entorno conocido y repetible | Determinista, ligero, fácil de evaluar | Requiere mapa previo y pose inicial |
| **SLAM Toolbox (online)** | Entorno desconocido o cambiante | No requiere mapa previo | Deriva, más CPU, mapa no determinista |
| **Cartographer** | Grandes entornos, 2D/3D | Robusto, loop closure | Complejo, más recursos |
| **VIO (ORB-SLAM3, etc.)** | Sin LiDAR o con cámara | Riqueza visual | Sensible a luz, más CPU |
| **GNSS + IMU** | Exterior, ERC permite GNSS | Global | No disponible indoor; precisión métrica |

**Decisión:** mapa estático + AMCL para el demo; SLAM Toolbox se usa fuera de línea para generar el mapa si la arena cambia. Ver [ADR-0005](../03-arquitectura/adr/0005-mapa-estatico-amcl.md).

### 4.1 Odometría

La odometría de ruedas es barata pero deriva. Opciones:

1. **Solo encoders** + modelo diferencial: suficiente para trayectos cortos.
2. **EKF (`robot_localization`)** fusionando encoders + IMU: mejor robustez.
3. **Visual odometry / LiDAR odometry**: más preciso, más complejo.

Para el demo se empieza con encoders y se evalúa EKF como mejora (OQ-08). El paquete `rover_localization` no se implementa en esta fase.

## 5. Simulación

| Simulador | ROS 2 | Físicas | Sensores | Curva de aprendizaje | Uso |
|---|---|---|---|---|---|
| **Gazebo Harmonic** | `ros_gz` | Buenas | LiDAR, IMU, cámara | Media | **Elegido** |
| Gazebo Classic | `gazebo_ros` | Buenas | Buenos | Media | EOL |
| Webots | `webots_ros2` | Muy buenas | Excelentes | Media | Alternativa |
| Isaac Sim | `isaac_ros` | Excelentes | RTX | Alta | Futuro |
| MuJoCo | Vía puentes | Excelentes | Limitados | Media | Investigación |

**Decisión:** Gazebo Harmonic + `ros_gz`, la combinación soportada con Jazzy. Ver [ADR-0004](../03-arquitectura/adr/0004-gazebo-harmonic.md).

## 6. Sensores

| Sensor | Coste | Ventajas | Limitaciones | Uso |
|---|---|---|---|---|
| LiDAR 2D (RPLIDAR A1M8, LD19) | 80–120 EUR | 360°, barato, bien soportado | Un plano, no detecta negativos | **Elegido** |
| LiDAR 3D | 400–1.000 EUR | Nube 3D | Precio, CPU | Futuro |
| Cámara RGB-D | 150–300 EUR | Color + profundidad | Luz, calibración | Futuro |
| ToF multizona (VL53L8CX) | 25–35 EUR | 64 zonas, 4 m, bajo consumo, robusto sin textura | 65° de FoV; el sol reduce el alcance | Complemento near-field (OQ-11) |
| Estéreo 2 × Camera Module 3 | 50–70 EUR | 3D denso y barato | Sincronía software, CPU, calibración, rolling shutter | Spike (ADR-0009) |
| IMU 9-DOF | 15–40 EUR | Orientación, vibración | Deriva | **Elegido** |
| Encoders | 10–30 EUR | Odometría barata | Deriva | **Elegido** |
| GNSS RTK | 150–400 EUR | Posición global | Interior, coste | Futuro ERC |

## 7. Brechas y oportunidades

| Brecha | Oportunidad |
|---|---|
| Simulación simplificada vs Marsyard real | Añadir terreno irregular y polvo en una fase posterior |
| LiDAR 2D no ve obstáculos bajos o voladizos | Complementar con ToF multizona y cámara; ver [`percepcion-3d.md`](percepcion-3d.md) |
| AMCL requiere mapa y pose inicial | Añadir localización global o GNSS en exterior |
| RPP no es óptimo en pasillos estrechos | Evaluar MPPI/DWB si la CPU lo permite |
| Sin tracción 4×4 real en simulación | Modelar skid-steer o usar un plugin de 4 ruedas |
| Sin brazo ni ciencia | Fase rover grande |

## 8. Conclusión

La pila elegida no es la más avanzada, pero es la **más adecuada para el objetivo**: bajo coste, documentación abundante, comunidad activa, ejecución en Raspberry Pi 5 y una ruta clara de escalado al rover completo. Las alternativas se revisan si aparece una limitación medida, no por preferencia.

## 9. Fuentes

[F-06] ROS 2 Jazzy — Installation, [F-07] Nav2 Quickstart, [F-08] Nav2 Jazzy params, [F-09] Gazebo + ROS installation, [F-10] ros_gz README, [F-12] REP 2000, [F-15] Nav2 first-time setup. Detalle en [`fuentes.md`](fuentes.md).
