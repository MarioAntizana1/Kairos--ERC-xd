# Guion de demo y FAQ

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Comunicación

## 1. Demo de 5 minutos

| Min | Qué se muestra | Qué se dice |
|---:|---|---|
| 0:00 | Título y problema | “Un dron vuela a 6 m en una jaula y necesita profundidad y obstáculos con poco peso y coste.” |
| 0:30 | Payload | “Pi 5, dos CM3 y un TFmini Plus de piso; baseline 150 mm.” |
| 1:00 | Cotización | “Núcleo de visión S/ 1.403; kit completo S/ 2.341.” |
| 1:30 | Arquitectura | “Estéreo para densidad y color; ToF de piso para altura y referencia de escala.” |
| 2:00 | Aclaración | “El ToF de piso da la referencia métrica; el par estéreo calibrado hace la geometría epipolar.” |
| 2:30 | Calibración | “ChArUco, RMS <0,5 px, baseline ±1 mm.” |
| 3:00 | Demo en vivo | Captura, profundidad, nube, obstáculo. |
| 4:00 | Métricas | “Error ≤10 cm a 5 m y ~7 cm a 6 m; latencia ≤200 ms; 20 min sin throttling.” |
| 4:30 | Seguridad | “Visión advisory; failsafe y piloto conservan la autoridad.” |
| 5:00 | Cierre | “Evidencia reproducible y siguiente paso: vuelo cautivo.” |

## 2. Demo de 10 minutos

Añadir:

- Comparación Standard vs Wide vs global shutter.
- ToF de piso: 1 punto vs 8×8; 4 m vs 12 m.
- Nube de una maqueta con cotas.
- Curva error vs distancia.
- Curva FPS vs resolución.
- Lecciones y riesgos.

## 3. Guion de demo en vivo

1. Encender Pi y payload; mostrar `rpicam-hello --list-cameras`.
2. Mostrar `vcgencmd measure_temp` y `get_throttled`.
3. Abrir la estación; mostrar preview y estado.
4. Iniciar `CAPTURE`; mostrar frames y timestamps.
5. Iniciar `SCAN`; mostrar profundidad y nube.
6. Mostrar la altura del ToF de piso y compararla con cinta.
7. Acercar un obstáculo; mostrar la distancia del estéreo y la latencia.
8. Detener y apagar de forma ordenada.
9. Mostrar la carpeta de evidencia y el hash.

## 4. Contingencias

| Falla | Plan B |
|---|---|
| Cámara no detectada | Reiniciar; revisar cable; usar video grabado |
| ToF de piso no lee | Mostrar cinta/altitud; explicar el fallback |
| Nube no se ve | Mostrar PCD/PLY grabado |
| Pi lenta | Bajar resolución; explicar el trade-off |
| Red cae | Seguir con demo local y logs |
| Público pregunta algo delicado | “No tenemos ese dato medido; está en el plan.” |

## 5. FAQ

**¿Por qué Pi 5 y no Jetson?**
Doble CSI, ISP, PCIe, precio y stock local. Jetson es mejor para IA, pero más
caro, pesado y consume más. La decisión está en ADR-0001.

**¿Por qué Camera Module 3 y no una cámara global shutter?**
12 MP, color, autofoco y precio. La GS es el plan B para movimiento; es
monocroma y de 1 MP. Ver ADR-0002.

**¿Para qué el ToF de piso?**
Para medir la distancia cámara–suelo y usarla como referencia métrica: escala,
plano del suelo, comparación con \(Z_{stereo}\) y extrínseca ToF–cámara. La
competencia vuela a 6 m, así que se usa **TFmini Plus 12 m**; el VL53L1X y el
VL53L5CX son de 4 m y no alcanzan.

**¿El ToF hace la visión epipolar?**
No. La geometría epipolar sale del par estéreo calibrado. El ToF de piso da una
referencia de altura/escala; no calcula líneas epipolares. Ver
[`../04-diseno/diseno-vision.md`](../04-diseno/diseno-vision.md) §6.4.

**¿Qué precisión tienen?**
Objetivo ≤10 cm a 5 m y ≤25 cm a 10 m con baseline 150 mm y σ_d 0,5 px. Es un
cálculo de diseño; se mide en TC-06. No prometemos precisión LiDAR.

**¿Cómo sincronizan las cámaras?**
La Pi 5 captura de las dos CSI, pero la CM3 no tiene genlock. Es casi
simultáneo por software; el rolling shutter puede producir skew en giros. Se
mitiga con vuelo lento y exposición corta.

**¿Qué pasa si falla la visión?**
La FC sigue volando; la visión es advisory. El payload se apaga o reinicia sin
tocar los motores. Ver [`../03-arquitectura/seguridad.md`](../03-arquitectura/seguridad.md).

**¿Y sin GPS en la jaula?**
La FC debe usar posicionamiento local/optical flow o el sistema de la
organización. Si no hay posición, la nube queda en un frame local y se registra
la limitación (OQ-12). El ToF de piso da la altura.

**¿Cuánto cuesta?**
Núcleo de visión S/ 1.403; kit de banco S/ 1.497,80; kit completo S/ 1.805,36
con 5 % de contingencia. Precios del 2026-11-21; no autoriza compra.

**¿Es legal volar?**
Depende de la zona, permiso, seguro y normativa local. El proyecto no sustituye
la autorización aeronáutica. Ver
[`../01-investigacion/normativa-y-seguridad.md`](../01-investigacion/normativa-y-seguridad.md).

**¿Qué falta?**
Hardware, captura, calibración, métricas y vuelo. La documentación está en G0/G1;
no hay resultados de hardware.

## 6. Checklist de presentación

- [ ] Demo ensayada 3 veces.
- [ ] Hardware cargado y con repuestos.
- [ ] Video de respaldo.
- [ ] Evidencia y hashes a mano.
- [ ] Preguntas difíciles preparadas.
- [ ] Tiempo medido.
- [ ] Licencia/permiso de imágenes.
