# Visión del rover grande: problema, casos de uso y arquitecturas

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Visión
>
> Este documento enmarca la sección. No elige hardware: define qué tiene que
> resolver la visión, qué alternativas existen y cómo se evaluarán. La
> investigación de campo está en
> [`sensores-peru-2026-11-21.md`](sensores-peru-2026-11-21.md).

## 1. Problema

El rover grande debe operar en un entorno tipo Marte, con polvo, iluminación
variable, obstáculos de formas y reflectividades distintas, y una misión con
tiempo limitado. El LiDAR 2D resuelve la navegación global y los obstáculos a
su altura, pero no ve:

- obstáculos **bajos** (piedras, bordillos, herramientas);
- obstáculos **negativos** (huecos, zanjas, escalones);
- superficies **sin textura** o muy reflectantes;
- objetos que requieren **semántica** (muestras, paneles, marcadores, personas);
- el punto de agarre del brazo o el estado de un instrumento.

La visión debe cubrir esas brechas sin comprometer energía, cómputo ni
seguridad. El LiDAR sigue siendo el sensor primario de navegación; la visión
es complementaria y, en algunas tareas, la única fuente posible.

## 2. Casos de uso

| ID | Caso de uso | Sensores candidatos | Éxito |
|---|---|---|---|
| CU-V1 | Detectar obstáculos bajos y negativos delante del rover | ToF inclinado, estéreo, RGB-D | Detección a 0,5–2 m con < 10% de falsos negativos |
| CU-V2 | Estimar profundidad de corto alcance para el costmap | Estéreo, RGB-D, ToF multizona | Nube o capa de coste a ≥ 5 Hz |
| CU-V3 | Reconocer marcadores, paneles o muestras | RGB + modelo de visión | Precisión ≥ 90% en el set de validación |
| CU-V4 | Guiar el brazo hasta un objeto | Cámara en muñeca + RGB frontal | Error de centrado < 2 cm a 30 cm |
| CU-V5 | Dar imagen al operador en teleoperación | RGB frontal, cámara trasera | Latencia < 200 ms; vídeo estable |
| CU-V6 | Registrar evidencia visual de la misión | RGB, vídeo, fotos | Artefacto con fecha, hash y metadatos |
| CU-V7 | Fusionar LiDAR + visión en una representación común | LiDAR, estéreo, ToF, TF | Nube/occupancy coherente en `base_link` |

> **Prioridad inicial:** CU-V1, CU-V2 y CU-V6. CU-V3/CU-V4 dependen de la
> ciencia y el brazo, que aún no están en alcance. CU-V5 es útil desde el
> primer prototipo.

## 3. Arquitecturas candidatas

### A. Una cámara RGB + ToF de punto

- **Hardware:** 1 × cámara UVC o CSI + 1 × TFmini Plus.
- **Ventajas:** barato, simple, bajo consumo, fácil de integrar en ROS 2.
- **Límites:** sin profundidad densa; el ToF cubre un haz estrecho.
- **Uso:** teleoperación, evidencia, seguridad de corto alcance.

### B. Dos cámaras UVC + ToF (prototipo local)

- **Hardware:** 2 × Elgato Facecam 4K + 1 × TFmini Plus.
- **Ventajas:** compra local, sensor grande, 1080p, enfoque fijo, rosca 1/4".
- **Límites:** sin sincronía hardware, rolling shutter presumible, 4K limitado
  a 30–120 cm, ancho de banda USB.
- **Uso:** aprender estéreo, medir error real, generar evidencia.
- **Coste:** ~S/ 1 986 + montaje.

### C. Estéreo global shutter sincronizado

- **Hardware:** 2 × cámara global shutter (p. ej. IMX296) + base rígida +
  disparo común; o un módulo estéreo integrado.
- **Ventajas:** sin *skew*, sincronía hardware, calibración estable.
- **Límites:** importación, lentes, cableado, precio; mono salvo que se añada
  color.
- **Uso:** profundidad de competición a 0,3–5 m.

### D. Cámara de profundidad integrada (OAK-D / RGB-D)

- **Hardware:** OAK-D Lite o similar; profundidad a bordo.
- **Ventajas:** poca CPU del host, sincronía y calibración de fábrica, SDK.
- **Límites:** importación, precio (~USD 269+), ecosistema propio.
- **Uso:** 3D denso con cómputo limitado.

### E. Híbrido recomendado a futuro

- LiDAR 2D/3D primario.
- Estéreo global shutter u OAK-D para profundidad.
- 1–2 ToF para near-field y obstáculos negativos.
- Cámara RGB de evidencia/teleoperación.
- Fusión en `base_link` con `robot_localization` y capas de coste.

## 4. Criterios de evaluación

| Criterio | Peso | Cómo se mide |
|---|---:|---|
| Exactitud de profundidad | 20% | Error a 1/2/3/5 m contra tablero y cinta métrica |
| Cobertura / FoV | 15% | Mapa de detección; obstáculos bajos y negativos |
| Sincronía y obturación | 15% | Delta de timestamp; *skew* en movimiento |
| Integración ROS 2 | 10% | Driver, `camera_info`, `PointCloud2`, QoS |
| Cómputo y energía | 15% | CPU, RAM, temperatura, vatios |
| Robustez ambiental | 10% | Sol, polvo, agua, vibración |
| Disponibilidad en Perú | 10% | Stock, plazo, garantía, importación |
| Coste total | 5% | Hardware + montaje + envío + aduana |

## 5. Hipótesis

| ID | Hipótesis | Criterio de aceptación | Experimento |
|---|---|---|---|
| H-V1 | Dos Facecam 4K a 1080p y base de 10–20 cm dan profundidad útil para un rover lento a 1–3 m | Error ≤ 10% a 1 m y ≤ 20% a 3 m; ≥ 5 Hz | E-V1 |
| H-V2 | La desincronización de dos Facecam en el mismo host es < 10 ms a 30 fps | Delta p95 < 10 ms; ≥ 95% de pares válidos | E-V2 |
| H-V3 | El TFmini Plus mantiene ≥ 4 m a 70 klx sobre blanco 90% | ≥ 4 m en 9/10 mediciones | E-V3 |
| H-V4 | Un TFmini Plus de 3,6° cubre suficiente campo para la marcha frontal si se inclina 20–30° | Detecta obstáculos en el 80% del ancho de vía a 1,5 m | E-V4 |
| H-V5 | El pipeline de visión cabe en el cómputo del rover con Nav2 | CPU < 70%, T < 80 °C, ≥ 5 Hz | E-V5 |

Las hipótesis se declaran antes de ejecutar. Si los datos las contradicen, se
documenta y se revisa el diseño; no se cambia el criterio a posteriori.

## 6. Requisitos candidatos (borrador)

> No son requisitos aprobados. Alimentan la fase 02 y la futura matriz de
> trazabilidad.

| ID | Requisito candidato | Prioridad | Verificación |
|---|---|---|---|
| RFC-V01 | La visión debe publicar profundidad o nube a ≥ 5 Hz | Must | Tasa de mensajes |
| RFC-V02 | El error de profundidad debe ser ≤ 10% a 1 m y ≤ 20% a 3 m | Must | E-V1 |
| RFC-V03 | La cámara debe enfocar de 0,3 m a infinito en el modo de trabajo | Must | Ficha + prueba |
| RFC-V04 | El ToF debe detectar obstáculos bajos de 10 cm a 1,5 m | Must | E-V4 |
| RFC-V05 | El sistema debe sobrevivir polvo y salpicaduras (IP54 mínimo en exterior) | Should | Ficha + prueba |
| RFC-V06 | La latencia de vídeo para teleoperación debe ser < 200 ms | Should | Medición |
| RFC-V07 | La calibración debe ser reproducible y verificable | Must | Tablero + reproyección |
| RFC-V08 | El sistema debe registrar evidencia con fecha y hash | Must | EV-Vxx |
| RFC-V09 | El consumo de visión no debe superar el 20% del presupuesto | Should | Medición |
| RFC-V10 | La integración debe ser ROS 2 Jazzy y `tf2` | Must | Launch + topics |

## 7. Decisiones que bloquean el diseño

| ID | Pregunta | Por qué bloquea |
|---|---|---|
| OQ-V01 | Plataforma de cómputo | Define drivers, CPU, potencia y sistema operativo |
| OQ-V02 | ¿3D denso es requisito? | Define estéreo vs. RGB + ToF |
| OQ-V03 | Presupuesto | Define local vs. importado |
| OQ-V04 | Sol directo | Define alcance del ToF y filtros |
| OQ-V08 | Montaje | Define baseline, vibración y calibración |
| OQ-V09 | Sincronía hardware | Define rolling vs. global shutter |

## 8. Plan inmediato

1. Cerrar OQ-V01 y OQ-V02 con el PO.
2. Aprobar o rechazar el presupuesto de la combinación V-A (S/ 1 986).
3. Comprar 2 × Facecam 4K + 1 × TFmini Plus si se aprueba.
4. Ejecutar E-V2 (sincronía) antes de E-V1 (profundidad).
5. Documentar resultados en `08-evidencia/` y actualizar H-V1/H-V2.
6. Decidir si se importa VL53L8CX o se queda el prototipo local.

## 9. Referencias

- [`sensores-peru-2026-11-21.md`](sensores-peru-2026-11-21.md) — precios, stock y fichas.
- [`percepcion-3d.md`](percepcion-3d.md) — estéreo, calibración y CPU.
- [`../00-gobierno/registro-decisiones.md`](../00-gobierno/registro-decisiones.md) — OQ-Vxx.
- [`../02-requisitos/vision-alcance.md`](../02-requisitos/vision-alcance.md) — alcance.
- [`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md) — protocolo.
