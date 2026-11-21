# Glosario

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Documentación

| Término | Definición |
|---|---|
| **ADR** | Architecture Decision Record. Documento que registra una decisión arquitectónica, sus alternativas y consecuencias. |
| **AMCL** | Adaptive Monte Carlo Localization. Filtro de partículas para localizar el robot en un mapa conocido. |
| **Bag (rosbag2)** | Archivo que graba mensajes de ROS 2 para su reproducción y análisis. |
| **BT** | Behavior Tree. Árbol de comportamiento usado por Nav2 para decidir acciones. |
| **colcon** | Herramienta de build para workspaces ROS 2. |
| **Costmap** | Representación en rejilla del entorno con costes de navegación. |
| **DDS** | Data Distribution Service. Capa de comunicación de ROS 2. |
| **DSR** | Design Science Research. Marco de investigación basado en construir y evaluar artefactos. |
| **E-stop** | Parada de emergencia. Pulsador que corta la potencia de los motores. |
| **FMEA** | Failure Mode and Effects Analysis. Análisis de modos de fallo y efectos. |
| **Frame** | Sistema de coordenadas en ROS (por ejemplo, `map`, `odom`, `base_link`). |
| **Gazebo Harmonic** | Simulador de robótica usado con ROS 2 Jazzy. |
| **GNSS** | Sistema global de navegación por satélite (GPS, Galileo, etc.). |
| **IMU** | Inertial Measurement Unit. Mide aceleración y velocidad angular. |
| **LiDAR** | Sensor de distancia por láser. |
| **MoSCoW** | Técnica de priorización: Must, Should, Could, Won't. |
| **Nav2** | Pila de navegación de ROS 2. |
| **Odometría** | Estimación del movimiento a partir de encoders, IMU u otros sensores. |
| **OSD** | Open Source Definition. Criterios de licencia de código abierto. |
| **PoC** | Proof of Concept. Prueba de concepto. |
| **QoS** | Quality of Service. Política de entrega de mensajes DDS. |
| **RACI** | Matriz de responsabilidades: Responsible, Accountable, Consulted, Informed. |
| **RF** | Requisito funcional. |
| **RNF** | Requisito no funcional. |
| **ROS 2** | Robot Operating System 2. Middleware y ecosistema para robótica. |
| **RPP** | Regulated Pure Pursuit. Controlador de seguimiento de trayectoria. |
| **SDLC** | Software Development Life Cycle. Ciclo de vida del desarrollo de software. |
| **SDF** | Simulation Description Format. Formato de descripción de Gazebo. |
| **SLAM** | Simultaneous Localization and Mapping. |
| **TF** | Transform Framework. Sistema de transformadas de ROS 2. |
| **URDF** | Unified Robot Description Format. |
| **Waypoint** | Punto objetivo de una misión. |
| **Wilson (intervalo)** | Intervalo de confianza para proporciones, robusto con muestras pequeñas. |
| **YAML** | Formato de serialización legible usado para configuración. |
| **Baseline (estéreo)** | Distancia entre los centros ópticos de las dos cámaras. A mayor base, mejor profundidad a distancia, pero más volumen y oclusiones. |
| **Disparidad** | Diferencia en píxeles entre un punto visto por la cámara izquierda y la derecha. La profundidad es inversamente proporcional a la disparidad. |
| **Global shutter** | Obturación global: todos los píxeles se exponen al mismo tiempo. Evita el *skew* de las cámaras rolling shutter. |
| **IP65 / IP67 / IPX7** | Grados de protección contra polvo y agua. IP65: polvo y chorro de agua; IP67: inmersión breve; IPX7: inmersión breve sin especificar polvo. |
| **Klux (klx)** | Miles de lux. Unidad de iluminancia usada para expresar la resistencia de un sensor a la luz ambiente. |
| **LiDAR-Lite v3HP** | Telémetro láser de Garmin de 5 cm–40 m, 1 cm de resolución y > 1 kHz. No es una cámara de profundidad. |
| **Rolling shutter** | Obturación progresiva: las filas se exponen secuencialmente. Produce *skew* en movimiento y vibración. |
| **SPAD** | Single-Photon Avalanche Diode. Fotodetector de un solo fotón usado en sensores ToF. |
| **Stereo rectification** | Rectificación estéreo: transforma las dos imágenes para que las líneas epipolares sean horizontales y la disparidad sea 1D. |
| **TFmini Plus / TFmini-S** | Sensores ToF de punto único de Benewake, 0,1–12 m, UART/I²C. El Plus tiene IP65, 3,6° y hasta 1 kHz; el S es más pequeño y barato. |
| **ToF (Time of Flight)** | Tiempo de vuelo. Mide distancia a partir del tiempo que tarda un pulso de luz en ir y volver. |
| **ToF camera** | Cámara ToF: matriz de zonas (por ejemplo 8×8) que entrega varias distancias a la vez, no un solo punto. |
| **UVC** | USB Video Class. Estándar plug-and-play para cámaras USB; no requiere driver propietario. |
| **VCSEL** | Vertical-Cavity Surface-Emitting Laser. Láser semiconductor usado en sensores ToF de corto alcance. |
| **VL53L8CX** | Sensor ToF multizona de ST: 8×8 zonas, 4 m, 65° diagonal. No se encontró en tiendas peruanas en 2026-11-21. |
