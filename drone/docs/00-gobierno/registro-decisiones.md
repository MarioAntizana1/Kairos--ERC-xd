# Registro de decisiones

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Visión

## 1. ADRs

| ADR | Título | Estado | Fecha | Reemplaza |
|---|---|---|---|---|
| [ADR-0001](../03-arquitectura/adr/0001-pi5-computo.md) | Raspberry Pi 5 8 GB como computadora de visión | Aceptada | 2026-11-21 | — |
| [ADR-0002](../03-arquitectura/adr/0002-stereo-cm3.md) | Par estéreo con 2 × Camera Module 3 Standard | Aceptada | 2026-11-21 | — |
| [ADR-0003](../03-arquitectura/adr/0003-tof-vl53l5cx.md) | ToF de piso: TFmini Plus 12 m para 6 m | Aceptada | 2026-11-21 | — |
| [ADR-0004](../03-arquitectura/adr/0004-pipeline-stereo.md) | Pipeline Picamera2 + OpenCV + ROS 2 | Propuesta | 2026-11-21 | — |
| [ADR-0005](../03-arquitectura/adr/0005-evidencia-reproducible.md) | Evidencia reproducible con hash | Aceptada | 2026-11-21 | — |

> Los ADR se numeran secuencialmente y nunca se borran. Si uno se reemplaza, se
> marca `Reemplazado por ADR-XXXX` y se conserva.

## 2. Decisiones abiertas

| ID | Pregunta | Propuesta | Impacto | Responsable | Estado |
|---|---|---|---|---|---|
| OQ-01 | ¿Camera Module 3 Standard o Wide? | Standard para profundidad; Wide si se prioriza cobertura | Óptica, calibración, BOM | Visión | Abierta |
| OQ-02 | ¿Qué ToF de piso y para qué altura? | **Cerrada:** TFmini Plus 12 m para 6 m; VL53L1X/8×8 solo ≤4 m | BOM, plazo, calibración | Hardware / Visión | Cerrada |
| OQ-03 | ¿HAT+ M.2 disponible? | Confirmar antes de comprar SSD 2242 | Almacenamiento | Hardware | Abierta |
| OQ-04 | ¿Modelo de controladora de vuelo y MAVLink? | Necesario para pose y `OBSTACLE_DISTANCE` | Integración | Software | Abierta |
| OQ-05 | ¿Baseline 150 mm o 200 mm? | 150 mm para 1–10 m; 200 mm si se prioriza lejos | Mecánica, precisión | Visión | Abierta |
| OQ-06 | ¿ROS 2 Jazzy o Python puro? | ROS 2 si se reutiliza el stack del rover; Python puro si el overhead es alto | Software | Visión | Abierta |
| OQ-07 | ¿UBEC dedicado o BEC del dron? | Dedicado si el BEC no garantiza 5 A | Energía, seguridad | Hardware | Abierta |
| OQ-08 | ¿WiFi/BT deshabilitados en vuelo? | Sí, salvo prueba de no interferencia | Seguridad | Seguridad | Abierta |
| OQ-09 | ¿Georreferencia con GPS o solo pose local? | Pose local para la primera fase; GPS si la FC lo entrega | Nube 3D | Visión | Abierta |
| OQ-10 | ¿Cámaras global shutter como plan B? | Evaluar si el rolling shutter arruina el estéreo | BOM, calidad | Visión | Abierta |
| OQ-11 | ¿Cámaras mirando al piso o al frente? | Mapeo del suelo: abajo; inspección: al frente. El ToF de piso solo es referencia directa si el piso es visible | Montaje, calibración, misión | Visión | Abierta |
| OQ-12 | ¿Habrá posición local en la jaula? | Optical flow/mocap/FC; si no, la nube queda en frame local | Georreferencia, mapa 3D | Software | Abierta |

## 3. Bitácora de decisiones

| Fecha | ID | Decisión | Motivo | Evidencia |
|---|---|---|---|---|
| 2026-11-21 | ADR-0001 | Pi 5 8 GB | Doble CSI, ISP, PCIe, precio y stock local | F-01, F-06 |
| 2026-11-21 | ADR-0002 | 2 × CM3 Standard | 12 MP, autofoco, 66° H, precio; GS como alternativa | F-02, F-07 |
| 2026-11-21 | ADR-0003 | ToF de piso: TFmini Plus 12 m para 6 m; VL53L1X/8×8 solo ≤4 m | Altura de competencia 6 m y entorno cerrado; alcance con margen | F-13, F-14, F-15, F-17, F-18 |
| 2026-11-21 | ADR-0004 | Picamera2 + OpenCV + ROS 2 | Reutiliza el stack del rover y permite integración | F-04, F-23, F-25 |
| 2026-11-21 | ADR-0005 | Evidencia con hash | Trazabilidad y reproducibilidad | F-26 |

## 4. Cómo se toma una decisión

1. Escribir el contexto y el problema.
2. Comparar al menos dos alternativas con criterios explícitos.
3. Registrar la decisión y sus consecuencias.
4. Actualizar interfaces, BOM, requisitos y pruebas afectadas.
5. Aprobación del responsable; si es irreversible, consultar al PO.
