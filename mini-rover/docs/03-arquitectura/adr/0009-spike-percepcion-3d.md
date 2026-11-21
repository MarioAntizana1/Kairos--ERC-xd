# ADR-0009 — Spike de percepción 3D con dos Camera Module 3 y un ToF

> Estado: Obsoleta por [ADR-0010](0010-raspberry-pi-4.md) (Pi 4); ver [ADR-0011](0011-estereo-csi-usb.md) · Alcance: spike · Fecha: 2026-11-21 · Responsable: Navegación / Hardware · Reemplaza a: —

> **Decisión obsoleta desde el 2026-11-21.** El cambio a Raspberry Pi 4
> ([ADR-0010](0010-raspberry-pi-4.md)) elimina el segundo puerto CSI y hace
> inviable el montaje de 2 × Camera Module 3. La alternativa con la cámara CSI
> disponible + USB se evalúa en [ADR-0011](0011-estereo-csi-usb.md). **No
> comprar el hardware de esta BOM para el demo.**

## Contexto

El mini demo navega con un LiDAR 2D y un mapa estático. Esa pila cumple los
requisitos Must, pero el LiDAR no ve obstáculos bajos, voladizos ni obstáculos
negativos (huecos, escalones, bordillos). El ERC 2027 tampoco tiene reglamento
publicado; cualquier sensor nuevo debe poder justificarse y probarse sin poner
en riesgo la demo.

El responsable del proyecto propone dos **Raspberry Pi Camera Module 3** (una
en cada puerto CSI de la Pi 5) y un **ToF multizona** delante, cerca de las
cámaras, para obtener profundidad 3D en tiempo real sin gastar toda la
energía. La investigación previa está en
[`../../01-investigacion/percepcion-3d.md`](../../01-investigacion/percepcion-3d.md).

Restricciones y hechos relevantes:

- La Pi 5 tiene dos transceptores MIPI de 4 carriles y 1,5 Gbps; admite dos
  cámaras simultáneas (F-39, F-42).
- La CM3 usa 2 carriles, obturación progresiva y autofocus por VCM; necesita
  cable de 15 a 22 pines (F-40, F-41).
- `libcamera` no tiene estéreo nativo: dos procesos, 3A manual y sincronía
  software de decenas de microsegundos; la CM3 no tiene disparo externo XTR
  (F-42, F-43).
- En Ubuntu 24.04 + Jazzy, la CM3 exige el fork de `libcamera` de Raspberry Pi
  y `camera_ros` compilado; el paquete upstream no la detecta (F-44).
- El VL53L8CX da 8 × 8 zonas, 65° diagonal, 4 m en oscuridad, ~2,8 m a
  5 000 lx, 60 Hz y 100 mA típicos (F-45).
- La alternativa con profundidad a bordo es el OAK-D Lite: 7,5 cm de base,
  obturación global, 2,5–3 W y 269 USD (F-46).

El proyecto dispone de ~10 meses de calendario hasta el ERC 2027 (fecha por
confirmar). El riesgo no es llegar tarde, sino que el spike consuma el tiempo
del demo base; por eso se mantiene acotado y en paralelo.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste de lista | Madurez |
|---|---|---|---|---|
| **A. 1 CM3 + ToF** | Bajo riesgo; +1,75 W; ToF robusto de corto alcance; una sola cámara | Sin 3D denso; una CM3 solo da color/evidencia | ~50 USD | Alta |
| **B. 2 CM3 + ToF** | 3D denso barato; aprende estéreo; usa los dos puertos CSI | Sincronía software; 3A manual; calibración; CPU; rolling shutter; +4,75 W | ~105 USD (≈130 USD con importación) | Media |
| **C. OAK-D Lite** | Profundidad a bordo; global shutter; poca CPU; 30 fps | 269 USD + importación; SDK DepthAI; otra dependencia | ~283 USD | Alta |
| **D. 2 Global Shutter + sincronía** | Global shutter; disparo hardware; buena base para estéreo | Mono; montura C/CS y lentes; voluminoso; más caro que B | ~150–200 USD | Media |

La comparación detallada, el error de profundidad y el presupuesto energético
están en [`percepcion-3d.md`](../../01-investigacion/percepcion-3d.md).

## Decisión

**Aprobar un spike acotado con la opción B: dos Camera Module 3 estándar y un
VL53L8CX, con A (1 CM3 + ToF) como fallback.** El proyecto tiene ~10 meses de
calendario hasta el ERC 2027, así que el spike no necesita una fecha de entrega
del demo. Se plantea como una línea de trabajo de **hasta 10 semanas efectivas
(2,5 meses), con hitos de 2 semanas**, en paralelo al demo base. La compra
tiene un plazo estimado de **10 días laborables**; ese plazo es de suministro,
**no** de desarrollo.

La decisión tiene tres límites explícitos:

1. **No cambia los requisitos Must ni la arquitectura aceptada.** El LiDAR
   sigue siendo el sensor primario de navegación. No se crea un RF nuevo hasta
   que el spike pase.
2. **No autoriza por sí sola la compra.** El PO debe confirmar presupuesto y
   proveedor. El coste estimado es ~105 USD en materiales y ~130 USD con
   envío/importación; la BOM de spike está en
   [`../../04-diseno/bom.md`](../../04-diseno/bom.md), sección 9.
3. **No entra en el camino crítico del demo.** Si el spike no cumple los
   criterios, se vuelve a A y se documenta el resultado negativo.

### Objetivo del spike

Demostrar, con evidencia reproducible, si la Pi 5 puede generar profundidad
3D útil para navegación a **640 × 480 y ≥ 5 Hz**, con error ≤ 10 % a 1 m y
≤ 20 % a 3 m, CPU < 60 %, temperatura < 80 °C y menos de 6 W adicionales.

### Montaje

- 2 × CM3 **estándar** (no wide): 66° H, 4,74 mm, mejor para profundidad.
- Base rígida de 70 mm (aluminio 2020 o placa de aluminio; no una pieza
  impresa flexible).
- VL53L8CX inclinado 20–30° hacia el suelo, con parasol y separado del
  chasis para no verse a sí mismo.
- Cable de I²C corto (< 8 cm) hasta el adaptador; el resto por USB o por el
  bus de la Pi.
- Alimentación desde el riel de 5 V existente; no se añade DC-DC.

### Software

- Ubuntu 24.04 + ROS 2 Jazzy.
- Fork de `libcamera` de Raspberry Pi compilado en el workspace y
  `camera_ros`, o un nodo propio si se necesita la sincronía servidor/cliente.
- `stereo_image_proc` para rectificación, disparidad y nube de puntos.
- Driver del ToF: `tof_imager_ros` si se usa L5CX/L7CX, o un nodo propio con
  la ULD de ST para el L8CX.
- Los topics y frames del spike son **tentativos** y no se añaden a
  [`interfaces.md`](../../03-arquitectura/interfaces.md) hasta que el spike
  pase. Se documentarán en el README de la evidencia.

### Calibración

- Checkerboard rígido, 20–30 pares, misma resolución de trabajo.
- Error de reproyección < 0,5 px.
- Bloquear enfoque, exposición y ganancia antes de calibrar.
- Repetir la calibración si cambia la base, el enfoque o la resolución.

### Medidas y criterio de paso

| Métrica | Criterio |
|---|---|
| Frecuencia de profundidad | ≥ 5 Hz a 640 × 480 |
| Error a 1 m | ≤ 10 % |
| Error a 3 m | ≤ 20 % |
| CPU media con Nav2 | < 60 % |
| Temperatura máxima | < 80 °C |
| Potencia añadida | < 6 W |
| Frames válidos | ≥ 90 % en laboratorio |
| Prueba exterior | Se registra, pero no bloquea el paso si el alcance baja |

Se hacen 30 repeticiones por distancia (0,5, 1, 2 y 3 m), con luz de
laboratorio (300–1 000 lx) y una prueba a la intemperie. La evidencia va en
`docs/08-evidencia/artefactos/<fecha>-spike-percepcion-3d/` con bag, CSV,
logs, fotos y `MANIFEST.sha256`.

## Consecuencias

### Positivas

- Se aprende estéreo real sobre la Pi 5 con material asequible.
- Si pasa, el demo gana profundidad densa y detección de obstáculos bajos.
- El ToF aporta una medida absoluta y robusta de corto alcance, útil incluso
  si el estéreo falla.
- La Pi 5 ya está dimensionada; no hace falta cambiar de computadora.
- El resultado, pase o falle, deja evidencia y una decisión documentada.

### Negativas / deuda asumida

- El estéreo de dos CM3 no es plug-and-play: sincronía software, 3A manual,
  calibración y montaje rígido.
- `camera_ros` en Ubuntu 24.04 exige el fork de `libcamera`; una actualización
  puede romper la captura.
- El estéreo compite por CPU con Nav2, AMCL y el LiDAR; si no se limita la
  resolución, H3 (CPU < 80 %) puede incumplirse.
- La Pi 5 pasa de ~4 W a ~7 W; la caja necesita ventilación y hay que medir la
  temperatura.
- El coste y el plazo de compra (~10 días) pueden retrasar el inicio del spike.
- La obturación progresiva y el autofocus añaden fragilidad a la calibración.

### Neutrales

- El LiDAR sigue siendo el sensor primario; el ToF y el estéreo son
  complementos.
- La BOM base no incluye cámara; la BOM del spike es aditiva y no se suma al
  total publicado hasta que el PO la apruebe.
- El ERC 2027 no tiene reglamento publicado; si cambia la normativa, se revisa.

## Criterios de revisión

Reabrir este ADR si:

1. El spike no alcanza 5 Hz o los errores de profundidad superan los umbrales.
2. La CPU media supera el 60 % o la temperatura supera 80 °C con Nav2.
3. La compra tarda más de 10 días laborables o el presupuesto no se aprueba.
4. `camera_ros`/`libcamera` deja de funcionar tras una actualización.
5. El PO decide que el 3D denso no es un objetivo de esta fase.
6. Aparece una OAK-D Lite o una GS a un precio/plazo mejor y se prefiere
   cambiar de alternativa.

Si el spike pasa, se crea un **ADR-0010** con la arquitectura de percepción
definitiva, se añade el requisito «Could» correspondiente, se
actualizan `interfaces.md`, la trazabilidad y la BOM base.

## Referencias

- [`../../01-investigacion/percepcion-3d.md`](../../01-investigacion/percepcion-3d.md)
  — análisis, números y alternativas.
- [`../../01-investigacion/fuentes.md`](../../01-investigacion/fuentes.md)
  — F-39 a F-51.
- [`../../01-investigacion/hipotesis-y-experimentos.md`](../../01-investigacion/hipotesis-y-experimentos.md)
  — H6/E5.
- [`../../04-diseno/bom.md`](../../04-diseno/bom.md) — sección 9, BOM del spike.
- [`../../00-gobierno/registro-decisiones.md`](../../00-gobierno/registro-decisiones.md)
  — OQ-11 resuelta; OQ-12 a OQ-15 abiertas.
- F-39: Raspberry Pi 5 Product Brief.
- F-40: Raspberry Pi Camera Module 3 Product Brief.
- F-41: Arducam — IMX708 / Camera Module 3.
- F-42: Raspberry Pi — `rpicam-apps` multiple cameras.
- F-43: Raspberry Pi — Global Shutter Camera.
- F-44: `camera_ros`.
- F-45: Pololu — VL53L8CX.
- F-46: Luxonis — OAK-D Lite.
- F-47: Vadzo — guía de estéreo en Pi 5.
- F-48: Raspberry Pi — AI Camera.
- F-49: ROS 2 `stereo_image_proc`.
- F-50: `tof_imager_ros`.
- F-51: ST — VL53L8CX datasheet / ULD API.
