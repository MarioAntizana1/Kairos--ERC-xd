# Estado del arte y benchmarking

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Visión

## 1. Métodos de percepción 3D

| Método | Principio | Ventajas | Limitaciones | Uso en este proyecto |
|---|---|---|---|---|
| **Estéreo pasivo** | Dos cámaras, disparidad | Denso, color, pasivo, barato | Depende de textura; baseline; rolling shutter | **Sí, fuente principal** |
| **ToF de piso** | Tiempo de vuelo de luz | Activo, mide altura, rápido | 1 punto u 8×8; 4 m (12 m TFmini); sol/IR | **Sí, altitud/referencia** |
| **Estéreo activo** | Proyector + cámaras | Denso en paredes lisas | Proyector, consumo, alcance | No en esta fase |
| **LiDAR 3D** | Barrido láser | Preciso, largo alcance | Peso, coste, sin color | Fuera de alcance |
| **Monocular IA** | Red aprende profundidad | Una cámara | Escala ambigua, entrenamiento | No en esta fase |
| **RGB-D comercial** | Cámara de profundidad | Fácil | Coste, alcance, sol | Alternativa |

La elección **estéreo + ToF de piso** equilibra coste, peso y robustez. El
estéreo da densidad y color; el ToF de piso da altitud y una referencia métrica
para escalar/validar la calibración. No se promete precisión LiDAR.

## 2. Cámaras

| Cámara | Sensor | Resolución | Shutter | FoV | Autofoco | Precio local | Rol |
|---|---|---|---:|---|---|---|---|
| Camera Module 3 Standard | IMX708 | 11,9 MP | Rolling | 66° H | Sí | S/ 140 | **Base** |
| Camera Module 3 Wide | IMX708 | 11,9 MP | Rolling | 102° H | Sí | S/ 195 | Cobertura |
| Camera Module 3 NoIR | IMX708 | 11,9 MP | Rolling | 66° H | Sí | — | IR |
| Global Shutter OV9281 | OV9281 | 1 MP | Global | 79° | No | S/ 200 | Movimiento |
| HQ Camera | IMX477 | 12,3 MP | Rolling | Lente C/CS | Manual | S/ 310 | Lente intercambiable |
| AI Camera | IMX500 | 12,3 MP | Rolling | 66° H | No | S/ 390 | IA en sensor |

**Decisión:** CM3 Standard por resolución, autofoco, 66° H y precio. La Wide se
reserva para interiores; la GS para escenas dinámicas (monocroma, 1 MP).

> **Rolling shutter:** la CM3 no tiene obturador global. En un dron, un giro
> rápido produce skew. Mitigación: vuelo lento, exposición corta, evitar giros
> bruscos. La GS elimina el skew pero pierde color y resolución.

## 3. ToF de piso

| Sensor | Zonas | Alcance | FoV | Frecuencia | Interfaz | Precio | Rol |
|---|---|---|---:|---|---|---|---|
| **TFmini Plus** | 1 | **12 m** | ~2° | 100 Hz | UART/I²C | S/ 330 | **Base para 6 m** |
| VL53L1X | 1 | 4 m | 27° | 50 Hz | I²C | S/ 75 | Alternativa ≤4 m |
| VL53L5CX | 8×8 | 4 m | 63° | 60 Hz | I²C | US$ 19,95 | Plano 8×8 ≤4 m |
| VL53L4CX | 1 | 6 m | 18° | — | I²C | US$ 14,95 | Justo a 6 m; sin margen |
| DFRobot 4 m IP67 | 1 | 4 m | — | 19–38 ms | I²C | S/ 115 | Robustez ≤4 m |

**Decisión:** **TFmini Plus 12 m** para la competencia a 6 m; VL53L1X o
VL53L5CX 8×8 solo para banco o vuelo ≤4 m. El haz del VL53L1X es de 27° y
promedia una zona grande; el TFmini Plus es estrecho (~2°) y mide un spot más
preciso (~21 cm a 6 m). Para calibrar, usar una superficie plana y mate. La jaula
no tiene GPS: la altitud del ToF es la referencia vertical; la horizontal depende
de la FC/posicionamiento local.

## 4. Cómputo

| Plataforma | CPU/GPU | CSI | PCIe | Potencia | Precio | Rol |
|---|---|---|---|---|---|---|
| **Raspberry Pi 5 8 GB** | 4×A76 2,4 GHz, VideoCore VII | 2 | 1×PCIe 2.0 | 5–12 W | S/ 768 | **Base** |
| Raspberry Pi 4B 8 GB | 4×A72 1,5 GHz | 1 | — | 5–10 W | ~S/ 600 | Alternativa limitada |
| Jetson Orin Nano | 6×A78 + GPU | 2 | 1×PCIe | 7–25 W | US$ 249+ | IA/denso |
| x86 NUC | x86 | USB | 1×M.2 | 15–35 W | US$ 300+ | Laboratorio |

**Decisión:** Pi 5 8 GB por doble CSI, ISP, PCIe, precio y stock local. La GPU
no está disponible para OpenCV; el estéreo corre en CPU. Jetson queda como
upgrade si se necesita IA o profundidad densa.

## 5. Software

| Componente | Opción | Nota |
|---|---|---|
| Captura | Picamera2 / rpicam-apps | Soporte oficial de CM3 |
| Calibración | OpenCV `calibrateCamera` / `stereoCalibrate` | Estándar |
| Estéreo | SGBM / BM / WLS | CPU; SGBM mejor calidad |
| Nube | OpenCV `reprojectImageTo3D`, PCL/Open3D | PCD/PLY |
| Middleware | ROS 2 Jazzy / Python puro | Reutiliza stack del rover |
| Vuelo | MAVLink / MAVROS | Pose y telemetría |
| Registro | rosbag2 / HDF5 / JPEG+PNG | NVMe |

## 6. Brecha y contribución

No se encontró una receta local “Pi 5 + 2 × CM3 + ToF de piso” con calibración,
métricas y evidencia reproducible para un dron. La contribución del proyecto es:

1. Un **método de calibración y validación** de bajo coste.
2. Una **arquitectura de referencia estéreo + ToF de piso** con límites
   explícitos.
3. **Evidencia reproducible** de precisión, FPS, latencia y térmica.
4. Una **BOM local** con alternativas y riesgos.

## 7. Fuentes

`F-01`–`F-05`, `F-14`–`F-18`, `F-23`–`F-26`.
