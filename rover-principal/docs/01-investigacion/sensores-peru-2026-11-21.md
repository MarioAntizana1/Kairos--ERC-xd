# Sensores de visión en Perú: Elgato Facecam 4K y ToF

> Estado: Investigación · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Visión / Hardware
>
> Investigación de campo del **2026-11-21**. Los precios y el stock son una
> fotografía de ese día y cambian sin aviso. Este documento **no autoriza
> compras**: alimenta las preguntas `OQ-V03`, `OQ-V05` y `OQ-V06` y el futuro
> `ADR-1xxx` de selección de sensores.

## 1. Pregunta y método

¿Qué cámaras y qué sensor ToF se pueden comprar **hoy en Perú** para la visión
del rover grande, a qué precio, con qué stock y con qué límites técnicos?

Método:

1. Se abrieron las fichas de tienda y se copió precio, stock y código de parte.
2. Se contrastaron las especificaciones con la ficha del fabricante cuando
   existía (Elgato, Benewake, ST, Garmin, DFRobot).
3. Se separó **precio de lista**, **precio internet** y **marketplace**.
4. Se marcó como `Supuesto` o `No verificado` todo lo que no se pudo confirmar.
5. Cada fuente quedó registrada en [`fuentes.md`](fuentes.md) con ID `F-xx`.

Tiendas consultadas: Memory Kings, Electromanía, Ripley, Promart, Naylamp
Mechatronics y Mouser Perú (referencia de importación).

---

## 2. Veredicto en una página

1. **En Memory Kings hay un solo modelo de cámara Elgato: la Facecam 4K
   (S/ 828, stock > 10).** No hay dos modelos distintos de cámara Elgato. El
   otro producto Elgato relacionado es el **Cam Link 4K** (S/ 375,50), que es
   una capturadora HDMI, no una cámara. Si la idea es un par estéreo, son **dos
   unidades de Facecam 4K**: S/ 1 656.
2. **La Facecam 4K es una buena cámara RGB, pero no es un sensor de
   profundidad.** Tiene un sensor Sony STARVIS 2 de 1/1.8", lente fija de 21 mm
   (nominal), 90° de FoV y UVC 1.5. No declara sincronía hardware ni
   obturación global. Sirve para un prototipo estéreo lento si se usa a
   1080p, se bloquean exposición/balance y se calibra; a 4K el enfoque fijo
   solo cubre **30–120 cm**, lo que la inutiliza para distancias de rover.
3. **El ToF potente que viste en Electromanía es casi seguro el TFmini Plus
   (S/ 330, stock 8).** Es un ToF de punto único de 0,1–12 m, 3,6° de haz,
   hasta 1 kHz por UART, IP65 y 70 klx de resistencia a la luz. Su hermano
   **TFmini-S (S/ 299, stock 3)** es más barato y liviano, pero con 2° de haz
   y 100 Hz según DFRobot.
4. **También hay un telémetro láser de largo alcance: el LIDAR-Lite v3HP
   (S/ 850, stock 11).** Mide 5 cm–40 m con 1 cm de resolución y > 1 kHz, pero
   no es una cámara ToF: es un solo punto. Si el objetivo es "un ToF potente"
   para mirar lejos, este es el candidato; si es "un ToF pequeño y barato para
   obstáculos", el TFmini Plus.
5. **No hay ToF multizona (VL53L8CX / VL53L5CX) en las tiendas peruanas
   consultadas.** El VL53L8CX (8×8 zonas, 4 m, 65°) hay que importarlo
   (Pololu/Mouser/RobotShop). El sustituto local es el VL53L1X (S/ 75,
   Naylamp) o el DFRobot de 4 m (S/ 115, Electromanía), ambos de un solo punto.
6. **Recomendación de prototipo con compra local:** 2 × Facecam 4K +
   1 × TFmini Plus = **S/ 1 986** (sin montaje, cables ni envío). Es una base
   válida para aprender estéreo y near-field, no la arquitectura definitiva de
   un rover de competición.
7. **Recomendación de ingeniería para el rover grande:** si el 3D denso es un
   requisito, no compres dos webcams y esperes profundidad de competición.
   Importa un estéreo con sincronía hardware (OAK-D o par global shutter) y un
   ToF multizona. Usa la compra local como puente y evidencia de aprendizaje.
8. **El LiDAR sigue siendo el sensor primario de navegación.** El ToF cubre
   obstáculos bajos, negativos y superficies sin textura; las cámaras aportan
   color, semántica y profundidad de corto alcance. Ninguno sustituye al LiDAR.

---

## 3. Cámaras Elgato en Memory Kings

### 3.1 Qué vende exactamente

| Dato | Valor |
|---|---|
| Producto | `CAMARA WEBCAM ELGATO FACECAM 4K UHD @60fps` |
| Código interno | `040866` |
| Número de parte | `10WAF9901` |
| Precio | `$ 238.00 ó S/ 828.00` |
| Stock | `> 10` |
| IGV | Incluido, según la ficha |
| Flete | No incluido |
| URL | <https://www.memorykings.pe/producto/354472/camara-webcam-elgato-facecam-4k-uhd-60fps> |

En el filtro de marca `elgato` hay 12 productos, pero **solo un modelo de
cámara**: la Facecam 4K. Los demás son micrófonos, luces, Stream Deck, una
base y el capturador **Cam Link 4K** (S/ 375,50). El Cam Link no es una cámara:
captura HDMI por USB. Para un par estéreo se compran **dos Facecam 4K**.
(Fuente del filtro: F-71.)

> **Aclaración:** si viste "dos Elgato", probablemente eran dos unidades de la
> misma Facecam 4K, o la Facecam 4K y el Cam Link 4K. No hay una segunda cámara
> Elgato en el catálogo consultado. Elgato sí tiene otros modelos (Facecam
> MK.2, Facecam Neo y Facecam Pro), pero Memory Kings no los lista en la fecha
> de la consulta (F-53).

### 3.2 Ficha técnica (fabricante)

| Parámetro | Valor | Fuente |
|---|---|---|
| Sensor | Sony STARVIS 2 CMOS 1/1.8" | F-53 |
| Óptica | Elgato Prime Lens, f/4.0 | F-53 |
| Distancia focal | 21 mm (dato nominal de la ficha; ver nota) | F-53 |
| Enfoque | **Fijo** | F-53 |
| Rango de enfoque | **30–120 cm a 4K**; **25 cm–infinito a 1080p** | F-53 |
| Campo de visión | 90° | F-53 |
| Vídeo | 2160p60 solo MJPG; 2160p30 NV12/MJPG; 1440p60; 1080p60; 720p60; etc. | F-53 |
| Codificación | YUY2, NV12, MJPG (MJPG si USB 2.0) | F-53 |
| Interfaz | USB-C, UVC 1.5, USB 3.0 recomendado | F-53 |
| Montaje | Rosca 1/4" | F-53 |
| Filtros | 49 mm | F-53 |
| Dimensiones / peso | 104 × 54 × 52 mm / 112 g | F-53 |
| Obturación | **No declarada**; CMOS de webcam, presumiblemente rolling shutter | Supuesto |
| Sincronía | **No declarada**; UVC, sin entrada de disparo | F-53 |
| Precio Perú | S/ 828 (Memory Kings) | F-52 |

> **Nota sobre la focal:** la ficha de Elgato dice "21 mm" sin aclarar si es
> física o equivalente. Con un sensor de 1/1.8" y 90° de FoV, lo probable es
> que sea **equivalente en formato 35 mm**; una focal física de 21 mm daría un
> campo mucho más estrecho. Para el cálculo de profundidad se usa el FoV, no
> la focal nominal. Confirmar con una calibración real antes de fijar la
> baseline.

### 3.3 ¿Sirve para estéreo?

**Sí, como prototipo; no como estéreo de competición.** Análisis:

| Factor | Efecto | Comentario |
|---|---|---|
| Sensor grande 1/1.8" | Buen rendimiento con poca luz | Ventaja frente a webcams pequeñas |
| Enfoque fijo | No hay *focus hunting* | Bueno para calibrar; pero a 4K solo enfoca 30–120 cm |
| 90° de FoV | Mucho campo, mucha distorsión | Hay que calibrar y rectificar; los bordes pierden precisión |
| Rolling shutter (supuesto) | *Skew* en vibración o giros | A 0,3–0,5 m/s es tolerable; confirmar con prueba |
| Sin sincronía hardware | Pares con *timestamp* distinto | A 30 fps y rover lento, aceptable; no para objetos rápidos |
| UVC 1.5 | Dos cámaras en un host | Ancho de banda y control de exposición por software |
| USB 3.0 | 4K60 MJPG; 1080p60 YUY2/NV12 | Dos 1080p60 YUY2 no caben en un solo bus; usar MJPG o controladores separados |

#### Error de profundidad estimado

Con `Z = f · B / d` y `ΔZ = Z² / (f · B)`, suponiendo 1080p, FoV horizontal
≈ 82° (90° diagonal) y `f ≈ 1 100 px`:

| Distancia | B = 10 cm | B = 15 cm | B = 20 cm |
|---:|---:|---:|---:|
| 1 m | 0,9 cm/px | 0,6 cm/px | 0,5 cm/px |
| 2 m | 3,6 cm/px | 2,4 cm/px | 1,8 cm/px |
| 3 m | 8,2 cm/px | 5,5 cm/px | 4,1 cm/px |
| 4 m | 14,5 cm/px | 9,7 cm/px | 7,3 cm/px |
| 5 m | 22,7 cm/px | 15,2 cm/px | 11,4 cm/px |

> **Supuesto:** `f` se estima a partir del FoV; no se midió con calibración
> real. El error se duplica con 2 px de disparidad. La tabla sirve para
> decidir, no para certificar precisión.

Conclusiones:

- A 1080p y base de 10–20 cm, el par puede dar profundidad útil de **1 a 3 m**
  para un rover lento. A 4–5 m el error ya es grande.
- A 4K el error se reduce a la mitad, pero **el enfoque fijo a 30–120 cm
  elimina la ventaja**: no se puede enfocar un obstáculo a 3 m en 4K.
- El modo de trabajo realista es **1080p, 30–60 fps, MJPG**, exposición y
  balance manuales, base rígida de 10–20 cm y calibración a esa resolución.
- Para 3D denso de competición, un par global shutter con sincronía hardware
  (o una OAK-D) es técnicamente superior.

### 3.4 Comparativa de precios en Perú

| Tienda | Precio | Stock / condición | Vendedor | Fuente |
|---|---:|---|---|---|
| **Memory Kings** | **S/ 828,00** | `> 10`; IGV incluido; flete no incluido | Memory Kings | F-52 |
| Ripley | S/ 1 069,00 (internet, −34% de S/ 1 609) | `InStock`; despacho a domicilio disponible | Marketplace: Prosmart Retail | F-54 |
| Promart | S/ 1 199,00 (−20% de S/ 1 499) | **Agotado online**; 0 unidades; solo tiendas | Marketplace: Vasil Technology's | F-55 |

Memory Kings es la opción más barata y con stock online verificable: ~23% menos
que Ripley y ~31% menos que Promart (si hubiera stock). Ripley es la segunda;
Promart no tiene stock online al momento de la consulta.

### 3.5 Alternativas de cámara en Memory Kings

Si no se compra la Elgato, el mismo catálogo tiene opciones 4K más baratas,
aunque también son webcams UVC (mismos límites de sincronía y obturación):

| Cámara | Precio | Stock | Nota | Fuente |
|---|---:|---|---|---|
| Creative Live! Cam Sync 4K UHD | S/ 261,00 | > 10 | 4K, la más barata | F-68 |
| Logitech Brio 4K Ultra HD Pro | S/ 487,00 (oferta; lista S/ 612) | > 10 | 4K, ecosistema Logitech | F-68 |
| Logitech MX Brio Ultra HD 4K | S/ 619,00 | > 10 | 4K, pensada para oficina | F-68 |
| Razer Kiyo V2 4K | S/ 657,50 | 2 | 4K, con IA | F-68 |
| Elgato Facecam 4K | S/ 828,00 | > 10 | Sensor más grande/mejor especificado de la lista (STARVIS 2 1/1.8"); no probado | F-52 |

La Elgato es la más cara de las webcams 4K, pero también la de mejor sensor y
la única con rosca 1/4" y filtros de 49 mm. Para estéreo, la cámara más barata
puede ser suficiente si se acepta la misma limitación de sincronía; la Elgato
aporta rango dinámico y baja luz.

---

## 4. ToF en Electromanía

### 4.1 Qué hay en la categoría "Distancia y proximidad"

Electromanía tiene 41 productos en la categoría. Los relevantes para el rover
(no se incluyen los LiDAR 360° como RPLIDAR A1M8/C1 porque ya están en la lista
del rover grande):

| Producto | Precio | Stock | Tipo | Fuente |
|---|---:|---|---|---|
| **TFmini Plus** | **S/ 330,00** | `Solo quedan 8` | ToF de punto único, 12 m, IP65 | F-56 |
| **TFmini-S** | **S/ 299,00** (lista S/ 310) | `Solo quedan 3` | ToF de punto único, 12 m | F-57 |
| **LIDAR-Lite v3HP** | **S/ 850,00** | `Solo quedan 11` | Telémetro láser de punto único, 40 m, IPX7 | F-58 |
| DFRobot 4 m I2C IP67 | S/ 115,00 | `Solo quedan 3` | Láser de punto único, 4 m, 19° | F-59 |
| VL53L0X | S/ 16,00 | No indicado | ToF de punto único, 2 m | F-60 |
| Sensor ultrasónico ToF de materiales | S/ 75,00 | No indicado | Detección de materiales, no distancia | — |

> **El "ToF potente" que viste es el TFmini Plus** si el módulo era pequeño,
> con dos ventanas ópticas y cable de 4 hilos. Es el único ToF de largo alcance
> de la tienda. Si el módulo era más grande, metálico y con carcasa, era el
> **LIDAR-Lite v3HP** (telémetro láser, no cámara ToF).

### 4.2 TFmini Plus — el candidato principal

| Parámetro | Valor | Fuente |
|---|---|---|
| Principio | ToF de punto único | F-63 |
| Rango | 0,1–12 m a 90% reflectividad; 0,1–4 m a 10% | F-63 |
| Precisión | ±5 cm (0,1–5 m); ±1% (5–12 m) | F-63 |
| Resolución | 1 cm | F-63 |
| Frecuencia | 1–1000 Hz por UART; 1–100 Hz por I²C | F-63 |
| FoV | 3,6° | F-63 |
| Luz ambiente | 70 klx | F-63 |
| Interfaz | UART, I²C, I/O; nivel 3,3 V | F-63 |
| Alimentación | 5 V ± 0,5 V; 110 mA media; 550 mW; pico 140 mA | F-63 |
| Protección | IP65 | F-63 |
| Peso / tamaño | 12 g; 35 × 18,5 × 21 mm | F-63 |
| Precio / stock | S/ 330; quedan 8 | F-56 |

**Uso previsto:** obstáculos frontales, distancia de seguridad, obstáculos
bajos que el LiDAR 2D no ve, y medición de altura sobre el suelo. Su haz de
3,6° es estrecho: **no cubre un campo amplio**, hay que apuntarlo o usar varios.

**Ventaja local:** es el único ToF de 12 m con IP65 y 1 kHz que encontramos en
las tiendas peruanas consultadas, sin importar. **Riesgo:** el precio local
suele ser mayor que el de importación; se paga la disponibilidad y la garantía.
No se comparó contra una cotización de importación cerrada.

### 4.3 TFmini-S — el hermano barato

| Parámetro | Valor (DFRobot) | Valor (Benewake) | Fuente |
|---|---|---|---|
| Rango | 0,1–12 m | 0,1–12 m | F-57 / F-64 |
| Precisión | ±6 cm (0,1–6 m); ±1% (6–12 m) | ±6 cm (0,1–6 m) | F-57 / F-64 |
| Frecuencia | 100 Hz | 1–1000 Hz | F-57 / F-64 |
| FoV | 2° | — | F-57 |
| Protección | No declarada | IP65 | F-57 / F-64 |
| Peso | 4,7 g | 5 g | F-57 / F-64 |
| Alimentación | 5 V; 0,6 W | 5 V; 0,7 W | F-57 / F-64 |
| Precio / stock | S/ 299; quedan 3 | — | F-57 |

> **Discrepancia:** la ficha de Electromanía (basada en DFRobot) dice 100 Hz,
> 2° y sin IP; la ficha de Benewake dice 1–1000 Hz, IP65 y 5 g. Antes de
> comprar, pide al vendedor el **datasheet del lote** y confirma el modelo
> exacto. No uses la frecuencia de 1 kHz si el driver es I²C: el propio
> TFmini Plus limita I²C a 100 Hz.

**Veredicto:** por S/ 31 menos que el Plus, el TFmini-S es más pequeño y
liviano, pero el Plus tiene mejor respaldo de ficha, IP65 confirmado y más
frecuencia. Para un rover, los 12 g del Plus no son un problema; la
documentación sí importa.

### 4.4 LIDAR-Lite v3HP — el largo alcance

| Parámetro | Valor | Fuente |
|---|---|---|
| Rango | ~5 cm–40 m (buena reflectividad) | F-58 |
| Resolución | 1 cm | F-58 |
| Precisión | ±2,5 cm típica > 2 m | F-58 |
| Frecuencia | > 1 kHz | F-58 |
| Interfaz | I²C 400 kHz y PWM; disparo externo | F-58 |
| Alimentación | 4,75–5,5 V; 65 mA reposo, 85 mA midiendo | F-58 |
| Protección | IPX7 | F-58 |
| Peso / tamaño | 34 g; 24,5 × 53,5 × 33,5 mm | F-58 |
| Precio / stock | S/ 850; quedan 11 | F-58 |

**Cuándo tiene sentido:** si el rover necesita medir distancias de 10–40 m
(aproximación a paredes, desniveles, topografía básica) y el LiDAR 2D no
alcanza. **Cuándo no:** para obstáculos cercanos y campo amplio, el TFmini
Plus es más barato y pequeño; el LIDAR-Lite sigue siendo un solo punto.

### 4.5 DFRobot 4 m y VL53L0X — near-field barato

| Producto | Rango | FoV | Frecuencia | Interfaz | Precio | Uso |
|---|---|---|---:|---|---:|---|
| DFRobot 4 m IP67 (SEN0590) | 2–400 cm | 19° | 19–38 ms (~26–52 Hz) | I²C | S/ 115 | Obstáculos bajos, huecos, distancia de seguridad |
| VL53L0X | ~2 m | 25° | ~50 Hz | I²C | S/ 16 | Prototipo, no industrial |
| VL53L1X (Naylamp) | 4 cm–4 m | 27° | ~50 Hz | I²C | S/ 75 | Similar al anterior, con más alcance |

> **Aviso sobre la ficha del DFRobot 4 m:** la página de Electromanía muestra
> imágenes de un sensor de vibración (SEN0590) que no corresponden al producto.
> El texto y las especificaciones sí describen un láser de 4 m. Pide foto real
> del lote antes de comprar. Fuente: F-59.

### 4.6 Lo que no hay: ToF multizona

No se encontró **VL53L8CX** ni **VL53L5CX** en Memory Kings, Electromanía,
Naylamp, MTLAB, Tesla Electronic ni Hifisac en la fecha de la consulta. El
VL53L8CX es el ToF 8×8 que el mini demo evaluó: 4 m, 65° diagonal, 60 Hz,
100 mA, I²C/SPI. Para el rover grande sería el complemento natural del LiDAR,
pero **hay que importarlo**.

| Opción de importación | Referencia | Precio de lista | Nota | Fuente |
|---|---|---:|---|---|
| Pololu VL53L8CX carrier | 4 m, 8×8, 65° | USD 24,95 | Carrier con regulador; envío e impuestos aparte | F-45 / F-66 |
| Mouser Perú — TFmini Plus I2C | 12 m, IP65 | No capturado | Mouser tiene sitio Perú; verificar envío/impuestos | F-67 |
| RobotShop — TF-Luna | 0,2–8 m, 250 Hz, 0,35 W | Variable | Alternativa más barata que el TFmini; no es local | F-70 |

> **Conclusión:** si el requisito es "ToF multizona para 3D", el presupuesto
> debe incluir importación y aduana. Si el requisito es "un ToF potente para
> mirar al frente", el TFmini Plus local alcanza.

### 4.7 Otras tiendas peruanas

| Tienda | Producto | Precio | Stock | Nota | Fuente |
|---|---|---:|---|---|---|
| Naylamp Mechatronics | VL53L1X | S/ 75,00 | En stock | 4 m, I²C, ±20 mm | F-61 |
| Naylamp Mechatronics | VL53L0X | S/ 69,00 | En stock | 1,2 m; más caro que Electromanía | F-62 |
| Electromanía | VL53L0X | S/ 16,00 | No indicado | La opción más barata | F-60 |

Naylamp tiene envío gratis a todo el Perú por compras mayores a S/ 200
(condiciones de la tienda). Es una alternativa si Electromanía no tiene stock.

---

## 5. Comparativa y presupuesto

### 5.1 Matriz técnica

| Criterio | Elgato Facecam 4K | TFmini Plus | TFmini-S | LIDAR-Lite v3HP | VL53L8CX (import) |
|---|---|---|---|---|---|
| Tipo | Cámara RGB UVC | ToF punto | ToF punto | ToF/láser punto | ToF 8×8 |
| Alcance | 0,3–∞ (1080p) | 0,1–12 m | 0,1–12 m | 0,05–40 m | 0,02–4 m |
| FoV | 90° | 3,6° | 2° | ~8 mrad | 65° diagonal |
| Frecuencia | 60 fps | 1 kHz UART / 100 Hz I²C | 100 Hz | > 1 kHz | 60 Hz |
| Precisión | N/A (RGB) | ±5 cm / ±1% | ±6 cm / ±1% | ±2,5 cm | ~1 cm |
| Sincronía HW | No | N/A | N/A | N/A | N/A |
| Protección | Ninguna | IP65 | IP65 (Benewake) / no declarada (DFRobot) | IPX7 | Sin carcasa |
| Interfaz | USB-C UVC | UART/I²C | UART/I²C | I²C/PWM | I²C/SPI |
| Consumo | ~2,5 W (USB) | 0,55 W | 0,6–0,7 W | 0,4 W | 0,5 W |
| Precio local | S/ 828 | S/ 330 | S/ 299 | S/ 850 | Importar |
| Stock local | > 10 | 8 | 3 | 11 | No |

### 5.2 Combinaciones con precio

| Combinación | Hardware | Coste | Comentario |
|---|---|---:|---|
| **V-A (prototipo recomendado)** | 2 × Elgato Facecam 4K + 1 × TFmini Plus | **S/ 1 986** | Estéreo 1080p + ToF frontal; compra local |
| V-B (económica) | 2 × Elgato + 1 × TFmini-S | S/ 1 955 | Ahorra S/ 31; ficha menos clara |
| V-C (near-field extra) | 2 × Elgato + 1 × TFmini Plus + 1 × VL53L1X | S/ 2 061 | ToF frontal + near-field lateral |
| V-D (largo alcance) | 2 × Elgato + 1 × LIDAR-Lite v3HP | S/ 2 506 | 40 m, pero un solo punto |
| V-E (dos ToF frontales) | 2 × Elgato + 2 × TFmini Plus | S/ 2 316 | Cubre izquierda/derecha; más cableado |
| V-F (3D multizona) | 2 × Elgato + 1 × TFmini Plus + VL53L8CX importado | S/ 1 986 + importación | La opción técnicamente más completa |

No incluye:

- Montaje rígido (barra de aluminio, soportes, tornillería): estimado
  **S/ 100–250** según taller y material.
- Cables USB 3.0 certificados, hub alimentado o tarjeta USB: estimado
  **S/ 80–200**.
- Envío: Memory Kings no incluye flete; Electromanía y Naylamp cobran según
  destino (Naylamp tiene envío gratis > S/ 200).
- Importación del VL53L8CX: envío + aduana + IGV, variable.

> **Supuesto:** los montajes y cables se fabrican o compran localmente. No se
> cotizaron; son un orden de magnitud, no un precio comprometido.

### 5.3 Coste total realista

| Escenario | Hardware | Montaje/cables | Total estimado |
|---|---|---:|---:|
| Mínimo local | S/ 1 955 | S/ 180 | **~S/ 2 135** |
| Recomendado local | S/ 1 986 | S/ 250 | **~S/ 2 236** |
| Con LIDAR-Lite | S/ 2 506 | S/ 250 | **~S/ 2 756** |
| Con VL53L8CX importado | S/ 1 986 + importación | S/ 250 | **~S/ 2 500–2 900** |

Los totales son estimaciones de planificación; no sustituyen una cotización
formal. La BOM editable está en
[`../04-diseno/bom-vision.md`](../04-diseno/bom-vision.md) y
[`../04-diseno/bom-vision.csv`](../04-diseno/bom-vision.csv).

---

## 6. Recomendación

### 6.1 Para el prototipo de esta sección

1. **Compra 2 × Elgato Facecam 4K en Memory Kings** (S/ 1 656). Es el mejor
   precio local verificado y hay stock.
2. **Compra 1 × TFmini Plus en Electromanía** (S/ 330). Es el ToF potente,
   documentado y con IP65.
3. **No compres el segundo ToF todavía.** Primero mide el campo de cobertura
   real y decide si necesitas un segundo punto o un multizona.
4. **Usa 1080p, no 4K.** A 4K el enfoque fijo solo cubre 30–120 cm. A 1080p
   llega a infinito y el error de profundidad es aceptable a 1–3 m.
5. **Monta las cámaras en una base rígida de 10–20 cm** (aluminio, no PLA
   flexible). Calibra a la resolución de trabajo.
6. **Bloquea exposición, ganancia y balance de blancos** en ambas cámaras.
   Si el software no lo permite, usa `v4l2-ctl` o un nodo propio.
7. **Mide la sincronía real** con un evento común (p. ej. un LED que parpadea)
   y registra el delta de `SensorTimestamp`. Si el delta es > 10 ms a 30 fps,
   descarta pares y documenta.
8. **No metas el estéreo en el camino crítico** hasta que el experimento V-E1
   pase los criterios.

### 6.2 Si el 3D denso es requisito

- **Cámara:** OAK-D Lite (importada) o un par global shutter con sincronía
  hardware. La Facecam 4K no es la respuesta definitiva.
- **ToF:** VL53L8CX (8×8, 4 m, 65°) importado; el TFmini Plus queda como
  complemento de largo alcance.
- **Cómputo:** define OQ-V01 antes de comprar. Un pipeline de estéreo denso
  en una Pi 5 compite con Nav2; una Jetson o x86 lo hace con margen.

### 6.3 Lo que no haría

- Comprar dos Facecam 4K y asumir que el estéreo 4K funcionará a 5 m: el
  enfoque fijo a 4K no llega.
- Usar dos cámaras en el mismo hub USB 3.0 sin medir ancho de banda.
- Usar un solo TFmini Plus como único sensor de obstáculos: su haz es de 3,6°.
- Comprar el VL53L8CX sin cotizar importación e impuestos.
- Poner el ToF apuntando al sol directo sin capucha y esperar los 12 m.
- Comprar hardware antes de cerrar OQ-V01 y OQ-V02.

---

## 7. Experimentos propuestos

| ID | Pregunta | Hardware | Métricas | Criterio de paso |
|---|---|---|---|---|
| **E-V1** | ¿Qué error de profundidad da el par Facecam a 1080p? | 2 × Facecam + base 10/15/20 cm | Error a 1/2/3/4 m, 30 reps | ≤ 10% a 1 m; ≤ 20% a 3 m |
| **E-V2** | ¿Cuánto se desincronizan dos Facecam en el mismo host? | 2 × Facecam + LED | Delta de timestamp, frames válidos | Delta < 10 ms a 30 fps |
| **E-V3** | ¿Cómo afecta el sol al TFmini Plus? | TFmini Plus | Alcance a 70 klx vs sombra | ≥ 4 m a 70 klx con blanco 90% |
| **E-V4** | ¿Qué cobertura real tiene el haz de 3,6°? | TFmini Plus + plataforma giratoria | Ángulo de detección, diámetro de spot | Mapa de cobertura documentado |
| **E-V5** | ¿Aguanta el pipeline con Nav2? | Cómputo del rover | CPU, RAM, temperatura, fps | CPU < 70%, T < 80 °C |

El protocolo detallado está en
[`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md).
Las hipótesis se registran en
[`vision-rover-grande.md`](vision-rover-grande.md).

---

## 8. Preguntas abiertas

| ID | Pregunta | Responsable | Necesaria antes de |
|---|---|---|---|
| OQ-V01 | ¿Qué plataforma de cómputo tendrá el rover grande? | PO/TL | Arquitectura y compra |
| OQ-V02 | ¿El 3D denso es requisito o línea de aprendizaje? | PO | Requisitos |
| OQ-V03 | ¿Se aprueba el presupuesto de ~S/ 2 000–2 800? | PO | Compra |
| OQ-V04 | ¿La operación es exterior con sol directo? | PO/Investigación | Diseño del ToF |
| OQ-V05 | ¿Dos Facecam 4K o importar estéreo global shutter/OAK-D? | HW/PO | Compra |
| OQ-V06 | ¿TFmini Plus, TFmini-S, LIDAR-Lite v3HP o VL53L8CX? | HW | Compra |
| OQ-V07 | ¿Quién calibra y mantiene el estéreo? | Equipo | G4 |
| OQ-V08 | ¿Dónde se monta la cámara? | HW/NAV | Diseño mecánico |
| OQ-V09 | ¿Se necesita sincronía hardware? | TL | Arquitectura |
| OQ-V10 | ¿Se usa ROS 2 Jazzy en el rover grande? | TL | G2 |

---

## 9. Fuentes

Las fuentes `F-01`–`F-51` están en [`fuentes.md`](fuentes.md) (base heredada).
Esta tabla lista las fuentes nuevas `F-52`–`F-71` de la investigación de campo.

| ID | Fuente | URL | Fecha | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-52 | Memory Kings — Elgato Facecam 4K | <https://www.memorykings.pe/producto/354472/camara-webcam-elgato-facecam-4k-uhd-60fps> | 2026-11-21 | S/ 828, stock > 10, código 040866, parte 10WAF9901, IGV incluido, flete no incluido | Alta (tienda) |
| F-53 | Elgato — Facecam 4K specs | <https://www.elgato.com/ww/en/p/facecam-4k> | 2026-11-21 | Sensor STARVIS 2 1/1.8", f/4.0, 21 mm, enfoque fijo 30–120 cm a 4K y 25 cm–∞ a 1080p, 90°, UVC 1.5, USB 3.0 | Alta (fabricante) |
| F-54 | Ripley — Elgato Facecam 4K | <https://simple.ripley.com.pe/camara-web-elgato-facecam-4k-resolucion-4k-pmp20001315623> | 2026-11-21 | S/ 1 069 internet (−34% de S/ 1 609), marketplace Prosmart Retail, InStock | Alta (tienda) |
| F-55 | Promart — Elgato Facecam 4K | <https://www.promart.pe/camara-web-elg-to-facecam-4k-de-estudio-4k60-1001297476/p> | 2026-11-21 | S/ 1 199 (−20% de S/ 1 499), marketplace Vasil, agotado online, 0 unidades, solo tiendas | Alta (tienda) |
| F-56 | Electromanía — TFmini Plus | <https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/> | 2026-11-21 | S/ 330, quedan 8, 0,1–12 m, ±5 cm, 1000 Hz, 3,6°, IP65, 110 mA | Alta (tienda) |
| F-57 | Electromanía — TFmini-S | <https://www.electromania.pe/producto/sensor-lidar-de-estado-solido-de-rango-de-un-solo-punto-tfmini-s-tof-12-m-uart-i2c/> | 2026-11-21 | S/ 299 (lista S/ 310), quedan 3, 0,1–12 m, ±6 cm, 100 Hz, 2°, 0,6 W | Alta en precio; media en specs (discrepancia con F-64) |
| F-58 | Electromanía — LIDAR-Lite v3HP | <https://www.electromania.pe/producto/sensor-lidar-lite-v3hp/> | 2026-11-21 | S/ 850, quedan 11, 5 cm–40 m, 1 cm, > 1 kHz, I²C/PWM, IPX7, 85 mA | Alta (tienda) |
| F-59 | Electromanía — DFRobot 4 m | <https://www.electromania.pe/producto/sensor-de-distancia-laser-mini-4-m-i2c-ip67/> | 2026-11-21 | S/ 115, quedan 3, 2–400 cm, ±4%, I²C, 19–38 ms, 19°, IP67; imágenes inconsistentes | Alta en precio; media en ficha |
| F-60 | Electromanía — VL53L0X | <https://www.electromania.pe/producto/sensor-de-distancia-tof-vl53l0x/> | 2026-11-21 | S/ 16, ToF de punto único, ~2 m | Alta (tienda) |
| F-61 | Naylamp — VL53L1X | <https://naylampmechatronics.com/sensores-proximidad/715-sensor-de-distancia-tof-vl53l1x.html> | 2026-11-21 | S/ 75, en stock, 4 cm–4 m, ±20 mm, I²C | Alta (tienda) |
| F-62 | Naylamp — VL53L0X | <https://naylampmechatronics.com/sensores-proximidad/325-sensor-vl53l0x-de-tof.html> | 2026-11-21 | S/ 69, en stock, ~1,2 m | Alta (tienda) |
| F-63 | Benewake — TFmini Plus | <https://ai.benewake.com/en/products/tfmini-plus/> | 2026-11-21 | 0,1–12 m @90%, 0,1–4 m @10%, ±5 cm/±1%, 1–1000 Hz UART, 1–100 Hz I²C, 3,6°, IP65, 550 mW, 70 klx | Alta (fabricante) |
| F-64 | Benewake — TFmini-S | <https://en.benewake.com/TFminiS/index.html> | 2026-11-21 | 0,1–12 m, 1–1000 Hz, IP65, 42×15×16 mm, 5 g, 0,7 W; DFRobot lista 100 Hz, 2°, 0,6 W | Media (discrepancia) |
| F-65 | ST — VL53L8CX | <https://www.st.com/en/imaging-and-photonics-solutions/vl53l8cx.html> | 2026-11-21 | 8×8 zonas, 4 m, 65° diagonal, bajo consumo | Alta (fabricante) |
| F-66 | Pololu — VL53L8CX carrier | <https://www.pololu.com/product/3419> | 2026-11-21 | Carrier 8×8, 4 m, 65°, USD 24,95; importación | Alta (distribuidor) |
| F-67 | Mouser Perú — TFmini Plus I2C | <https://www.mouser.pe/ProductDetail/Benewake/TFmini-Plus-I2C> | 2026-11-21 | Referencia de importación; precio no capturado | Media |
| F-68 | Memory Kings — webcams relacionadas | <https://www.memorykings.pe/listados/176/camaras-webcam> | 2026-11-21 | Creative 4K S/ 261; Brio 4K S/ 487; MX Brio S/ 619; Razer Kiyo V2 4K S/ 657,50 | Alta (tienda) |
| F-69 | Electromanía — HUSKYLENS 2 / visión | <https://www.electromania.pe/productos/modulos-y-sensores/sensores/camara-vision-ia/> | 2026-11-21 | HUSKYLENS 2 6 TOPS S/ 550; Arducam 16 MP S/ 220; Arducam 64 MP S/ 530; no son estéreo | Alta (tienda) |
| F-70 | Benewake — TF-Luna | <https://en.benewake.com/TFLuna/index.html> | 2026-11-21 | 0,2–8 m, 250 Hz, 0,35 W, < 5 g; alternativa de importación | Alta (fabricante) |
| F-71 | Memory Kings — filtro de marca Elgato | <https://www.memorykings.pe/filtros/280/elgato> | 2026-11-21 | 12 productos Elgato; un solo modelo de cámara (Facecam 4K); Cam Link 4K S/ 375,50 con stock > 10 | Alta (tienda) |

### Historial de consultas

| Fecha | Fuentes | Resultado |
|---|---|---|
| 2026-11-21 | F-52, F-53, F-54, F-55 | Facecam 4K: S/ 828 en Memory Kings; S/ 1 069 en Ripley; S/ 1 199 sin stock en Promart; enfoque 4K limitado a 30–120 cm |
| 2026-11-21 | F-56, F-57, F-58, F-59, F-60 | ToF locales: TFmini Plus, TFmini-S, LIDAR-Lite, DFRobot 4 m y VL53L0X |
| 2026-11-21 | F-61, F-62 | Naylamp: VL53L1X S/ 75 y VL53L0X S/ 69, en stock |
| 2026-11-21 | F-63, F-64, F-65, F-66, F-70 | Fichas de fabricante y opciones de importación |
| 2026-11-21 | F-67, F-68, F-69 | Mouser, alternativas de cámara y HUSKYLENS 2 |
| 2026-11-21 | F-71 | Elgato en Memory Kings: 12 productos, una sola cámara (Facecam 4K), Cam Link 4K S/ 375,50 |
