# Percepción 3D: dos Camera Module 3 y un ToF

> Estado: Investigación · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Navegación / Hardware
>
> Este documento **no cambia** requisitos ni arquitectura. Alimenta OQ-11 y el
> ADR-0009. Decisión del 2026-11-21: se aprueba la opción **B (2 CM3 + ToF)
> como spike**, con A como fallback; la arquitectura definitiva no se acepta
> hasta que el spike pase. Los cálculos de consumo y de error de profundidad son
> estimaciones de prediseño; los que dependen del runtime están marcados como
> **pendiente de medir**.
>
> **Revisión ADR-0010/0011 (2026-11-21):** este estudio asume una Pi 5 con dos
> puertos CSI. La base vigente es una **Raspberry Pi 4 8 GB con un solo CSI**
> ([ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md)); el montaje de
> 2 × Camera Module 3 **no es ejecutable**. Se conserva como referencia. La
> alternativa con la Camera Module V2.1 + una cámara USB se evalúa en
> [ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md). **No comprar 2 CM3
> para el demo.**

## 1. Pregunta

¿Conviene montar **dos Raspberry Pi Camera Module 3** y un **ToF pequeño** en
el mini demo para obtener profundidad 3D en tiempo real sin gastar toda la
energía?

La propuesta inicial es:

- 2 × Camera Module 3 (IMX708) en los dos puertos CSI de la Pi 5.
- 1 × sensor ToF multizona delante, cerca de las cámaras.
- Fusión o uso alternativo: ToF para distancia robusta de corto alcance,
  estéreo para densidad 3D.

## 2. Veredicto

1. **La Pi 5 sí puede con dos Camera Module 3.** Tiene dos transceptores MIPI
   de 4 carriles y 1,5 Gbps, y admite dos cámaras simultáneas. La CM3 usa dos
   carriles y necesita cable adaptador de 15 a 22 pines.
2. **El ToF es una buena adición**, especialmente para obstáculos bajos,
   negativos (huecos, bordillos) y superficies sin textura, donde el LiDAR 2D
   y el estéreo fallan. Es barato y consume poco.
3. **Pero «2 CM3 + ToF» no es 3D denso enchufar y listo.** `libcamera` no
   ofrece estéreo nativo; la sincronía es por software, hay que bloquear
   exposición, ganancia y enfoque, calibrar y montar las cámaras en una base
   rígida. Además, el estéreo consume CPU de la Pi 5, que ya ejecuta Nav2,
   AMCL y el LiDAR.
4. **El límite no es la batería.** Añadir la segunda cámara, el ToF y el
   cómputo estéreo suma del orden de **+4,8 W en el riel de 5 V** (estimación).
   Con la LiFePO4 de 12,8 V / 6 Ah (76,8 Wh) siguen quedando más de 2,5 h
   teóricas; el requisito de 30 min tiene margen de sobra. El coste real es
   **tiempo de integración, CPU y calor**, no energía.
5. **Para esta fase:** dejar el LiDAR como sensor primario de navegación.
   Se aprueba un **spike de 2 CM3 + ToF** (ADR-0009) con **A (1 CM3 + ToF)**
   como fallback. El estéreo no entra en el camino crítico del demo hasta que
   el spike pase los criterios de la sección 7.
6. **Si el 3D denso es un entregable**, la opción de ingeniería es una cámara
   con profundidad a bordo (OAK-D Lite) o dos cámaras global shutter
   sincronizadas por hardware, no dos CM3 de obturación progresiva.

## 3. Hechos verificados

### 3.1 Raspberry Pi 5 y los dos puertos CSI

| Hecho | Dato | Fuente |
|---|---|---|
| Puertos MIPI | 2 × 4 carriles, 1,5 Gbps por carril; cualquier combinación de hasta dos cámaras o pantallas | F-39 |
| Uso simultáneo | La documentación de `rpicam-apps` confirma dos cámaras a la vez en Pi 5 | F-42 |
| Cable | La CM3 usa FPC de 15 pines; la Pi 5, conector de 22 pines; hace falta adaptador | F-40, F-44 |

### 3.2 Camera Module 3

| Hecho | Dato | Fuente |
|---|---|---|
| Sensor | Sony IMX708, 11,9 MP, 4608 × 2592, píxel de 1,4 µm, diagonal 7,4 mm | F-40 |
| Vídeo | 1080p50, 720p100, 480p120; RAW10 | F-40 |
| Variantes | Estándar 4,74 mm f/1,8, 66° H (75° diagonal); wide 2,75 mm f/2,2, 102° H (120° diagonal) | F-40 |
| Enfoque | Automático por VCM con PDAF; se puede fijar la posición de lente | F-40 |
| Obturación | **Rolling shutter** (progresiva) | F-41 |
| Enlace | 2 carriles MIPI CSI-2 por defecto; configurable a 4 en el sensor | F-41 |
| Consumo | 250 mA a 5 V según la documentación de la Pi; máximo 1,16 W según Arducam | F-001, F-41 |
| Precio de lista | 25 USD la estándar; 35 USD la wide (sin impuestos ni envío) | F-41 |

Matiz importante: la CM3 es una cámara **con autofocus**. Para estéreo hay que
bloquear el enfoque (`LensPosition`) y la exposición/ganancia; si el enfoque se
mueve, cambian los intrínsecos y la calibración deja de valer.

### 3.3 `libcamera` y sincronía

| Hecho | Dato | Fuente |
|---|---|---|
| Estéreo nativo | `libcamera` **no** ofrece soporte estereoscópico; dos cámaras se abren en procesos separados | F-42 |
| Sincronía 3A | No hay forma de sincronizar la exposición/ganancia/balance entre las dos cámaras; hay que pasar a modo manual | F-42 |
| Sincronía software | Sí existe: un servidor difunde tiempos y los clientes ajustan la duración de frame; se espera coincidencia de inicio de frame en «varias decenas de microsegundos» | F-42 |
| Sincronía hardware | Solo la cámara Global Shutter (IMX296) tiene entrada de disparo externo XTR; la CM3 no | F-43 |
| Integración ROS 2 | En Ubuntu 24.04 + Jazzy, la CM3 necesita el fork de `libcamera` de Raspberry Pi y `camera_ros` compilado; el paquete upstream no la detecta | F-44 |

La sincronía software es útil, pero **no está expuesta por `camera_ros`**: es
una función de `rpicam-apps`/`libcamera`. Para usarla desde ROS 2 haría falta
un nodo propio, o emparejar frames por `SensorTimestamp` y descartar los que
estén lejos. A 30 fps, un par con 10 ms de diferencia sigue siendo válido para
un rover a 0,3 m/s, pero no para objetos rápidos.

### 3.4 ToF multizona

| Hecho | Dato | Fuente |
|---|---|---|
| Modelo de referencia | ST VL53L8CX, 8 × 8 zonas (o 4 × 4) | F-45 |
| Campo de visión | 65° diagonal (45° horizontal/vertical) | F-45 |
| Alcance | 20 mm a 4 m; 4 m en oscuridad; ~2,8 m con 5 000 lx y blanco muy reflectante | F-45 |
| Frecuencia | Hasta 60 Hz | F-45 |
| Resolución | 1 mm de profundidad, 64 zonas | F-45 |
| Interfaz | I²C hasta 1 MHz o SPI hasta 3 MHz; alimentación 3,2–5,5 V | F-45 |
| Consumo | 100 mA típicos en ranging activo; 150 mA de pico; el modo de bajo consumo es mucho menor, pero no es el modo de operación normal | F-45 |
| Potencia | ~0,5 W a 5 V típicos; ~0,75 W de pico | Cálculo propio con F-45 |
| Naturaleza | Es un «LiDAR 3D básico» de 64 zonas, no una cámara de profundidad densa | F-45 |
| ROS 2 | Hay driver para VL53L5CX/L7CX (`tof_imager_ros`); para L8CX habría que portar la API o usar la ULD de ST | F-50 |

Dos detalles prácticos:

- El carrier de Pololu pide cables de I²C **cortos** (idealmente < 8 cm) por la
  sensibilidad del level shifter.
- El sol directo reduce el alcance. El ERC no tiene reglamento 2027 publicado
  y la sede puede ser exterior; hay que medir en condiciones reales, no asumir
  los 4 m de laboratorio.

## 4. Análisis de la propuesta

### 4.1 ¿Se pueden sincronizar dos CM3?

Sí, pero con condiciones:

1. **Sincronía de frames:** usar el modo servidor/cliente de `libcamera` o
   emparejar por timestamp. La primera opción no está en `camera_ros`; la
   segunda es más simple pero puede descartar frames.
2. **3A manual:** fijar exposición, ganancia y balance de blancos en ambas
   cámaras. Si no, una imagen sale más clara que la otra y el *matching* falla.
3. **Enfoque fijo:** fijar `LensPosition` en ambas. La CM3 no tiene anillo de
   enfoque manual, pero el VCM se puede bloquear por software.
4. **Montaje rígido:** base de aluminio o placa gruesa; una base impresa en
   PLA/PETG flexible se deforma con la vibración y la calibración se pierde.
5. **Calibración a la resolución de trabajo:** si se calibra a 1280 × 720 y se
   ejecuta a 640 × 480, hay que recalibrar o escalar los intrínsecos.

Para un rover lento (0,3 m/s) la obturación progresiva no es crítica: en 10 ms
se desplaza 3 mm. El problema aparece con giros rápidos o terreno muy irregular.

### 4.2 Calidad de profundidad alcanzable

La profundidad estéreo sigue:

```text
Z = f · B / d
```

donde `f` es la focal en píxeles, `B` la línea base y `d` la disparidad en
píxeles. El error por píxel de disparidad es:

```text
ΔZ = Z² / (f · B)
```

Para la CM3 estándar (4,74 mm) a 1280 × 720, con píxel efectivo de 2,8 µm
(2 × 2 binning), `f ≈ 940 px`. Con `B = 70 mm`:

| Distancia | Disparidad | Error por 1 px | Error con 2 px |
|---:|---:|---:|---:|
| 1 m | 66 px | 1,5 cm | 3,0 cm |
| 2 m | 33 px | 6,1 cm | 12,2 cm |
| 3 m | 22 px | 13,7 cm | 27,4 cm |
| 4 m | 16 px | 24,4 cm | 48,8 cm |
| 5 m | 13 px | 38,0 cm | 76,0 cm |

A 2304 × 1296 (sin escalar), `f ≈ 1 693 px`, el error se reduce a la mitad:
7,6 cm/px a 3 m y 13,5 cm/px a 4 m. Pero el coste de cómputo se multiplica.

Conclusiones:

- El estéreo con 70 mm de base es útil para **obstáculos de 0,3 a 3 m**, no
  para geometría fina a 5–10 m.
- A 640 × 480 el error se duplica otra vez: a 3 m, ~27 cm/px. Solo sirve para
  el corto alcance.
- El ToF de 64 zonas tiene una resolución angular mucho menor (cada zona cubre
  ~20 cm a 2 m y ~40 cm a 4 m), pero es **absoluto, robusto y barato**. No
  sustituye al estéreo; lo complementa.
- Superficies sin textura, paredes lisas, repeticiones y luz solar directa
  degradan el estéreo. Objetos negros, transparentes o muy inclinados degradan
  el ToF. La combinación tiene sentido.

### 4.3 Cómputo

La Pi 5 no tiene acelerador de estéreo. El *block matching* corre en CPU:

- `StereoBM` es el más rápido; `StereoSGBM` da mejores mapas pero es varias
  veces más caro.
- A 640 × 480 y 64 disparidades, es razonable esperar **decenas de fps con
  BM** y **unos pocos fps con SGBM**; a 1280 × 720, bastante menos. Es una
  estimación: **hay que medirla** con `stereo_image_proc` en C++ y con la pila
  Nav2 corriendo, no en un banco aislado.
- La hipótesis H3 del proyecto exige CPU media < 80 % y temperatura < 80 °C.
  El estéreo compite con Nav2, AMCL, el LiDAR y el registro; si se añade, hay
  que bajar resolución o frecuencia, o aceptar que H3 se incumpla.

Para navegación, **5–10 Hz de profundidad a 640 × 480** es suficiente. No hace
falta 30 fps; el costmap de Nav2 corre a 5 Hz. Perseguir 30 fps a 720p es la
forma más rápida de comerse la CPU y el presupuesto térmico.

### 4.4 Energía

Presupuesto actual del riel de 5 V en el cálculo energético: **8,35 W**,
incluida una CM3 (F-001). Añadir:

| Carga | Potencia | Nota |
|---|---:|---|
| Segunda CM3 | +1,25 W | 250 mA a 5 V, F-001 |
| VL53L8CX | +0,50 W | 100 mA a 5 V, F-45 |
| Cómputo estéreo en la Pi | +3,00 W | **Estimación**; la Pi pasa de ~4 W a ~7 W |
| **Total en 5 V** | **+4,75 W** | 13,1 W, 2,6 A; dentro del DC-DC de 5 A |
| **Visto por la batería** | **+5,3 W** | con 90 % de rendimiento |

Con la LiFePO4 12,8 V / 6 Ah (76,8 Wh) y un 80 % de descarga útil (61,4 Wh),
una misión de 24 W duraría ~2,5 h teóricas. El requisito de 30 min (RNF-06)
sigue teniendo un factor > 5. **La energía no es el argumento en contra.**

Lo que sí empeora:

- La Pi 5 a 7 W en una caja cerrada necesita el *active cooler* y ventilación.
  El BOM ya incluye refrigeración; hay que verificar la temperatura en caja.
- El convertidor de 5 V de 5 A aguanta, pero el pico de arranque de dos cámaras
  y el SSD conviene medirlo.
- El ToF de 0,5 W no es despreciable, pero es 10 veces menos que la Pi.

Si el objetivo es **mínimo consumo**, la combinación correcta es **1 CM3 + ToF**
(+1,75 W) y no el estéreo. Si el objetivo es **3D denso**, el consumo extra de
la Pi es el precio, no las cámaras.

### 4.5 Integración ROS 2

| Pieza | Estado | Trabajo |
|---|---|---|
| CM3 en Pi 5 + Ubuntu 24.04 + Jazzy | Con fricción conocida | Compilar el fork de `libcamera` de Raspberry Pi y `camera_ros`; el paquete upstream no basta (F-44) |
| Dos CM3 | Dos nodos `camera_ros` (índices 0 y 1) | La sincronía no viene incluida; hace falta nodo propio o emparejar timestamps |
| Estéreo | `stereo_image_proc` de `image_pipeline` | Calibración `camera_info` izquierda/derecha; publica disparidad y `PointCloud2` |
| ToF | Driver propio o `tof_imager_ros` | L8CX no está listado; portar la API ULD o usar L5CX/L7CX |
| Nav2 | `voxel_layer`/`obstacle_layer` con `PointCloud2`, o `range_sensor_layer` para 3 zonas | No meter una nube densa a 30 Hz en el costmap; bajar a 5–10 Hz y limitar la ventana |
| Simulación | Gazebo tiene cámara RGB-D; el ToF de 64 zonas no es nativo | Modelar como cámara de profundidad de baja resolución o publicar una nube sintética; documentar la brecha sim-real |

Esto no es un fin de semana. La parte óptica y de calibración suele ser la que
más tiempo consume; la parte ROS 2 es la más predecible.

## 5. Alternativas

| Opción | Hardware | Coste de lista | Potencia añadida | Profundidad | CPU | Sincronía | Riesgo | Veredicto |
|---|---|---|---:|---|---|---|---|---|
| **A. 1 CM3 + ToF** | CM3 estándar + VL53L8CX | ~50 USD | +1,75 W | 64 zonas, 0,2–4 m | Bajo | N/A | Bajo | **Recomendada para el demo** |
| **B. 2 CM3 + ToF** | 2 × CM3 + VL53L8CX | ~105 USD | +4,75 W | Densidad 0,3–3 m | Alto | Software | Medio-alto | **Spike aprobado (ADR-0009)** |
| **C. OAK-D Lite** | Cámara estéreo con RVC2 | ~283 USD | +3,0–3,5 W | 0,8–12 m, 30 fps | Bajo (a bordo) | Hardware | Medio | **Mejor 3D si hay presupuesto** |
| **D. 2 GS + sincronía** | 2 × IMX296 + lentes + disparo | ~150–200 USD | +2,5 W + CPU | 0,3–5 m, mono | Alto | Hardware | Medio | Alternativa si se quiere estéreo “de verdad” |
| **E. 1 CM3 sola** | CM3 | ~28 USD | +1,25 W | Ninguna | Bajo | N/A | Bajo | Solo color/evidencia |

Notas:

- **B** incluye 2 CM3, cables, ToF, base rígida y tablero de calibración;
  ~130 USD con envío/importación estimados. El plazo de compra es ~10 días
  laborables; la ejecución es aparte (10 semanas efectivas, con hitos de 2
  semanas).
- **C (OAK-D Lite):** 7,5 cm de base, obturación global en los sensores mono,
  4 TOPS, profundidad a bordo y 2,5–3 W de consumo base (F-46). Es la opción
  que menos CPU de la Pi consume y la que mejor resuelve la sincronía. El
  precio de lista es 269 USD más cable; con importación, más.
- **D (Global Shutter):** la cámara GS de Raspberry Pi cuesta 50 USD, es mono,
  1,6 MP, con montura C/CS y entrada XTR (F-43). Dos cámaras + dos lentes +
  cableado de disparo son más voluminosas y caras que dos CM3, pero eliminan
  el problema de la obturación progresiva y permiten sincronía hardware.
- **AI Camera (70 USD):** tiene inferencia en el sensor (IMX500), pero no es
  estéreo; la profundidad dependería de un modelo monocular, no de geometría
  (F-48). No resuelve el problema de esta investigación.

## 6. Recomendación

### 6.1 Para el mini demo (fase actual)

1. **LiDAR 2D como sensor primario** de obstáculos y localización. No cambiar
   RF-03 ni RF-04.
2. Añadir **1 CM3 estándar** delante para color, teleoperación, evidencia y
   futuras funciones de visión. Es barata y ya está prevista en el cálculo
   energético.
3. Añadir **1 VL53L8CX** inclinado hacia el suelo (por ejemplo, 20–30° hacia
   abajo) para:
   - obstáculos bajos que el LiDAR no ve;
   - obstáculos negativos (huecos, escalones, bordillos);
   - distancia de seguridad de corto alcance;
   - texto/QR o referencia métrica para la cámara, si se necesita.
4. Publicar el ToF como `PointCloud2` o `LaserScan` en `base_link`, a 10–15 Hz,
   y usarlo en una capa de coste límica o en un nodo de seguridad. No hace
   falta un costmap 3D completo para el demo.
5. **No** meter el estéreo de dos CM3 en el camino crítico. Se ejecutará el
   spike aprobado de la sección 7 (ADR-0009), con A como fallback.

### 6.2 Si el 3D denso es un requisito

Elegir **C (OAK-D Lite)** si el presupuesto lo permite, o **D (dos GS)** si se
prefiere componente nacional/compacto y no importar. **B (dos CM3)** solo tiene
sentido si se acepta el trabajo de sincronía, calibración y CPU y se dispone de
tiempo para medirlo.

### 6.3 Lo que no haría

- Comprar dos CM3 y un ToF y asumir que saldrá 3D denso a 30 fps “porque la Pi
  tiene dos puertos”.
- Poner el estéreo a 1280 × 720 y 30 fps con Nav2 corriendo en la misma Pi.
- Usar el ToF como único sensor de obstáculos: su campo de visión es de 65° y
  no cubre los 360° del LiDAR.
- Montar las cámaras en una pieza impresa flexible y calibrar una sola vez.

## 7. Spike aprobado (B) — histórico, suspendido por ADR-0010

> **Suspendido:** la Pi 4 tiene un solo CSI; no se pueden conectar 2 CM3. El
> protocolo se conserva como referencia. La alternativa CSI + USB está en el
> [ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md).

**Pregunta:** ¿puede la Pi 5 generar un mapa de profundidad de 640 × 480 a
≥ 5 Hz, con error ≤ 10 % a 1 m y ≤ 20 % a 3 m, CPU < 60 % y temperatura
< 80 °C, añadiendo menos de 6 W?

El plazo de compra y el de ejecución son independientes: **10 días
laborables de suministro no son 10 días de desarrollo**. El proyecto tiene
~10 meses de calendario hasta el ERC 2027, así que el spike se acota a **10
semanas efectivas con hitos de 2 semanas** para que no se coma el tiempo del
demo base.

| Campo | Valor |
|---|---|
| Horizonte del proyecto | ~10 meses hasta el ERC 2027 (fecha por confirmar) |
| Compra | 10 días laborables de plazo de suministro; no es tiempo de desarrollo |
| Ejecución | 10 semanas (2,5 meses) de trabajo efectivo, con hitos de 2 semanas |
| Hardware | Pi 5 8 GB, 2 × CM3 estándar, base rígida de 70 mm, VL53L8CX |
| Software | Ubuntu 24.04, Jazzy, fork de `libcamera`, `camera_ros` o nodo propio, `stereo_image_proc` |
| Calibración | Checkerboard, 20–30 pares, error de reproyección < 0,5 px, misma resolución de trabajo |
| Iluminación | 300–1 000 lx de laboratorio y una prueba a la intemperie |
| Métricas | fps, CPU, RAM, temperatura, potencia, error de profundidad a 0,5/1/2/3 m, tasa de frames válidos |
| Repeticiones | 30 por distancia |
| Evidencia | Bag, CSV, logs, fotos del montaje y del mapa de disparidad |
| Criterio de paso | 5 Hz, error ≤ 10 % a 1 m, ≤ 20 % a 3 m, CPU < 60 %, T < 80 °C, +6 W |
| Si falla | Se vuelve a A (1 CM3 + ToF) y se documenta el resultado |

El spike se registra como H6/E5 en
[`hipotesis-y-experimentos.md`](hipotesis-y-experimentos.md). La compra de los
componentes requiere confirmación de presupuesto; el ADR-0009 no autoriza la
compra por sí solo.

### 7.1 Revisión Pi 4: Camera V2.1 + USB (ADR-0011)

La Pi 4 tiene un solo CSI de 15 pines (F-54) y el inventario incluye una Camera
Module V2.1 (IMX219, F-56). La idea de añadir una cámara USB produce un par
**no sincronizado**:

| Aspecto | CSI V2.1 + USB | CSI V2.1 + ToF |
|---|---|---|
| Sincronía | Dos pipelines (`libcamera` + V4L2); sin disparo común | No aplica; el ToF mide directo |
| Óptica | Sensores y lentes posiblemente distintos | Una sola cámara |
| Calibración | Individual + estéreo; más trabajo | Solo intrínseca de la cámara |
| Profundidad | Aproximada, sensible a movimiento y exposición | Distancia directa en el campo del ToF |
| CPU | `stereo_image_proc` en Pi 4; compite con Nav2 | Baja |
| Uso seguro | **No** para evitación ni e-stop | Sí, como redundancia del LiDAR |
| Coste | Bajo si la USB está disponible | 0 (ToF en inventario) |
| Madurez | Baja para métrica | Alta |

**Conclusión:** el par CSI + USB puede servir para un spike docente o una
demonstración de profundidad aproximada, pero no es un estéreo métrico ni un
sensor de seguridad. Para el demo, la opción robusta es **CSI + ToF**; el
LiDAR sigue siendo el sensor primario de navegación. El spike CSI + USB se
acota a 2 semanas y 20 h, con criterios en el ADR-0011.

## 8. Preguntas abiertas

OQ-11 quedó **resuelta** por el
[ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md), pero esa
decisión está **obsoleta** por el cambio a Pi 4
([ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md)). La pregunta vuelve
a estar abierta como **OQ-18**, con la alternativa CSI + USB del
[ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md).

| ID | Pregunta | Responsable | Necesaria antes de |
|---|---|---|---|
| OQ-12 | ¿El 3D denso es un requisito de demo o una línea de aprendizaje? | PO | Requisitos y presupuesto |
| OQ-13 | ¿Hay presupuesto para una cámara de 269 USD o se prioriza el bajo coste? | PO | Compra |
| OQ-14 | ¿La arena del ERC 2027 es exterior? ¿Hay sol directo? | PO / Investigación | Diseño del ToF y pruebas |
| OQ-15 | ¿Quién calibra y mantiene el estéreo? | Equipo | G4 |
| OQ-18 | ¿Estéreo CSI + USB, CSI + ToF o cámara estéreo sincronizada? | NAV | Compra y pruebas |

## 9. Fuentes

- F-001: Raspberry Pi Documentation — Power supply.
- F-39: Raspberry Pi 5 Product Brief — 2 × 4-lane MIPI, 1,5 Gbps.
- F-40: Raspberry Pi Camera Module 3 Product Brief — IMX708, FoV, enfoque.
- F-41: Arducam — IMX708 / Camera Module 3 — rolling shutter, 2-lane, precio.
- F-42: Raspberry Pi Documentation — `rpicam-apps` multiple cameras — estéreo
  no nativo, sincronía software, 3A manual.
- F-43: Raspberry Pi Documentation — Global Shutter Camera — XTR.
- F-44: `camera_ros` — fork de libcamera necesario para CM3 en Ubuntu.
- F-45: Pololu — VL53L8CX — 8 × 8, 4 m, 65°, 100 mA, 5 klx.
- F-46: Luxonis — OAK-D Lite — 7,5 cm, 0,8–12 m, 2,5–3 W, 4 TOPS.
- F-47: Vadzo — guía práctica de estéreo en Pi 5 — calibración, timestamps,
  error de 1 px.
- F-48: Raspberry Pi AI Camera — 70 USD, IMX500.
- F-49: `stereo_image_proc` — pipeline de estéreo de ROS 2.
- F-50: `tof_imager_ros` — driver ROS 2 para VL53L5CX/L7CX.
- F-51: ST — VL53L8CX datasheet / ULD API (referenciado a través de F-45).
