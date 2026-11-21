# ADR-0011 — Percepción con cámara CSI + USB en Raspberry Pi 4 (spike)

> Estado: Propuesta · Fecha: 2026-11-21 · Responsable: Navegación · Reemplaza a: [ADR-0009](0009-spike-percepcion-3d.md) (obsoleta por el cambio a Pi 4)

## Contexto

El [ADR-0010](0010-raspberry-pi-4.md) cambia la computadora de a bordo a una
**Raspberry Pi 4 Model B**, que tiene **un solo puerto CSI de 15 pines** (F-54).
El [ADR-0009](0009-spike-percepcion-3d.md) asumía dos puertos CSI de 22 pines en
una Pi 5 para conectar **dos Camera Module 3**; esa premisa ya no se cumple.

El inventario de facultad (F-52) incluye una **Raspberry Camera Module V2.1**
(IMX219, CSI de 15 pines, F-56). El responsable del proyecto propone añadir una
**cámara USB** para tener «algo de estéreo». La idea es atractiva por coste y
disponibilidad, pero hay que separar una prueba de laboratorio de un sensor de
navegación:

- Una cámara CSI y una USB usan **pipelines distintos** (`libcamera`/`camera_ros`
  frente a V4L2/UVC); no comparten reloj de exposición ni disparo hardware.
- Para estéreo métrico se necesitan dos cámaras **sincronizadas**, con la misma
  resolución, óptica y orientación, y una calibración estéreo común.
- La cámara V2.1 es de obturador de rodillo y enfoque fijo (F-56); la USB puede
  tener otra lente, otro campo de visión y otro tiempo de exposición.
- La Pi 4 tiene menos CPU que la Pi 5; el *block matching* compite con Nav2.
- La seguridad y la evitación de obstáculos deben seguir apoyadas en el **LiDAR
  2D** y el **ToF**, no en un estéreo aproximado.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste | Madurez |
|---|---|---|---|---|
| **CSI V2.1 + USB (spike)** | Usa la cámara disponible y una USB barata; prueba de concepto | Sin sincronía hardware; sensores/ópticas distintas; calibración difícil; CPU | Bajo (USB por confirmar) | Baja para métrica |
| CSI V2.1 + ToF (recomendada para el demo) | Un solo pipeline; ToF da distancia directa; poca CPU | No hay nube de puntos densa; cobertura limitada | 0 (ToF en inventario) | Alta |
| Dos cámaras USB idénticas | Mismo driver; más fácil calibrar | Siguen sin sincronía hardware; ancho de banda USB; dos puertos | Medio | Media-baja |
| OAK-D Lite | Estéreo sincronizado y profundidad a bordo; USB | Coste ~269 USD; otro stack | Alto | Alta |
| Dos CM3 + multiplexor CSI | Reutiliza la idea original | La Pi 4 no tiene dos CSI; multiplexor y soporte inciertos | Medio | Baja |
| Cámara global shutter + trigger | Sincronía hardware | Coste, lentes, montura; no es plug-and-play | Alto | Media |

## Decisión propuesta

Ejecutar un **spike de 2 semanas efectivas (máximo 20 h de trabajo)** con la
**Camera Module V2.1 en CSI** y **una cámara USB UVC** de campo de visión
similar, para medir si el par produce una profundidad aproximada útil a corta
distancia y baja velocidad.

El spike **no sustituye** al LiDAR ni al ToF y **no se usa para seguridad,
evitación de obstáculos ni localización**. La percepción primaria del demo sigue
siendo LiDAR 2D + ToF; la cámara se usa para teleoperación, registro y, como
mucho, para un experimento de profundidad.

Si el spike no cumple los criterios, se vuelve a **CSI V2.1 + ToF** y se cierra
la línea estéreo con la evidencia del intento.

## Plan de validación

| Paso | Medición | Criterio de éxito |
|---|---|---|
| 1 | Detección de ambas cámaras en ROS 2 | `image_raw` y `camera_info` de las dos a la vez |
| 2 | Sincronía de timestamps | Desfase mediano ≤ 33 ms (un frame a 30 fps) |
| 3 | Calibración individual y estéreo | Error de reproyección < 1 px por cámara; calibración estéreo estable |
| 4 | Profundidad a 0,5 / 1 / 2 m | Error ≤ 30 % a 1 m; no se exige precisión métrica |
| 5 | Frecuencia y CPU | ≥ 5 Hz a 640 × 480; CPU < 60% y T < 80 °C en Pi 4 |
| 6 | Movimiento | Sin artefactos graves a ≤ 0.3 m/s y exposición corta |

> Los umbrales son una propuesta para el spike; se confirman antes de empezar.
> No se presentan como resultados.

## Consecuencias

### Positivas

- Se aprovecha la cámara CSI disponible y una USB de bajo coste.
- Permite aprender calibración, sincronía y `stereo_image_proc` en la Pi 4.
- Da una vía de percepción barata para teleoperación y experimentos.
- No bloquea el demo: el LiDAR y el ToF siguen siendo la base.

### Negativas / deuda asumida

- **No es un estéreo sincronizado**: la profundidad será aproximada y sensible
  a movimiento, exposición y desalineación.
- Sensores y lentes distintos complican la rectificación y la calibración.
- La CPU de la Pi 4 puede limitar la resolución/frecuencia.
- La cámara USB añade cable, consumo y un punto de fallo; su modelo y montaje
  están por definir.
- No sirve para seguridad ni para evitar obstáculos; no se debe presentar como
  equivalente a un estéreo industrial.

### Neutrales

- Si el spike falla, la cámara CSI sigue siendo útil para teleoperación.
- La cámara USB puede reutilizarse para el operador o para el registro de demo.
- El ADR-0009 se conserva como referencia histórica.

## Impacto documental

| Documento | Cambio |
|---|---|
| `03-arquitectura/adr/0009-spike-percepcion-3d.md` | Marcar obsoleta por el cambio a Pi 4 |
| `04-diseno/bom.md` | Sección 9 (2 CM3) no ejecutable; añadir USB camera al spike |
| `04-diseno/inventario-facultad.md` | Camera V2.1 disponible; USB camera por confirmar |
| `01-investigacion/percepcion-3d.md` | Nota Pi 4 y sección CSI + USB |
| `06-pruebas/casos-prueba.md` | Nuevo caso si el spike se acepta (pendiente) |
| `02-requisitos/` | Sin cambios: el estéreo no es requisito Must |

## Criterios de revisión

- El desfase de timestamps o el error de profundidad no permiten ni siquiera un
  experimento docente.
- La CPU de la Pi 4 no sostiene Nav2 + estéreo a 5 Hz.
- Se aprueba presupuesto para una cámara estéreo sincronizada (OAK-D Lite u
  otra) o se renuncia a la línea estéreo.
- El demo exige percepción 3D como requisito Must, lo que obliga a reabrir
  requisitos y presupuesto.

## Referencias

- F-40, F-42, F-44, F-47: cámaras, `libcamera`, multicámara y calibración.
- F-52: inventario de facultad.
- F-54: Raspberry Pi 4 (un CSI, USB 3.0).
- F-56: Raspberry Pi Camera Module V2.
- [ADR-0009](0009-spike-percepcion-3d.md) — spike original con 2 CM3 en Pi 5.
- [ADR-0010](0010-raspberry-pi-4.md) — plataforma Pi 4.
