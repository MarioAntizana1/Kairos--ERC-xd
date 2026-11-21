# Inventario de materiales disponible en facultad

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware

> **Alcance:** este documento registra el material declarado por el responsable
> del proyecto el 2026-11-21 y lo contrasta con la BOM vigente y la variante
> 6×6. Sirve de entrada a los ADR-0010 (Pi 4), ADR-0011 (cámara CSI + USB) y
> ADR-0012 (LTE/GNSS). **No autoriza compras ni descuenta partidas del
> presupuesto.** El material no se ha inspeccionado físicamente.

## 1. Fuente y método

- Archivo original: `inventario actual.txt`, en la raíz del repositorio.
- Contraste: [`bom.md`](bom.md), [`bom-peru.md`](bom-peru.md),
  [`energia/bom-6x6.md`](energia/bom-6x6.md),
  [`diseno-electrico.md`](diseno-electrico.md),
  [`energia/calculo-energetico.md`](energia/calculo-energetico.md),
  [`../02-requisitos/requisitos-no-funcionales.md`](../02-requisitos/requisitos-no-funcionales.md),
  [ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md),
  [ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md) y
  [ADR-0012](../03-arquitectura/adr/0012-lilygo-lte-gnss.md).
- Fuente registrada: F-52 en [`fuentes.md`](../01-investigacion/fuentes.md).
- Confianza: media. Es una declaración del usuario; faltan modelos exactos,
  cantidades, hojas de datos y estado físico.

> **Supuestos:** (1) el Pi 4 es de 8 GB, funciona y tiene una fuente adecuada;
> (2) el LilyGO es el T-SIM7600X; (3) el LM2596 es el módulo HW-411 de 3 A
> nominales; (4) la LiPo no incluye BMS ni cargador. Si algún supuesto es falso,
> la fila correspondiente se revisa.

## 2. Inventario declarado

| # | Material declarado | Cant. | Tipo | Nota |
|---|---|---|---|---|
| 1 | Argon ONE V2 para Pi 4 (confirmar modelo) | 1 (implícito) | Cómputo/mecánica | Carcasa de aluminio con ventilador y botón; verificar acceso al CSI (F-55). |
| 2 | Raspberry Pi 4 Model B 8 GB | 1 (implícito) | Cómputo | 8 GB confirmados por el usuario; Ubuntu 24.04 (F-18); base del ADR-0010. |
| 3 | Arduino «XD» | 1 | Control | Modelo por confirmar; no está en la arquitectura (ADR-0008 usa ESP32-S3). |
| 4 | TB6612FNG | 3 | Tracción | 6 canales en total; 1 A continuo y 3 A de pico por canal, 4,5–13,5 V (F-006). |
| 5 | PCA9685 | 1 (implícito) | Control | 16 PWM por I²C; útil para servos y pan-tilt. |
| 6 | GY-271 | 1 (implícito) | Sensor | Magnetómetro; chip y calibración por confirmar. |
| 7 | VL53L0/1XV2 | s/i | Sensor | ToF de un punto; modelo y cantidad por confirmar; no es un LiDAR 360°. |
| 8 | MPU-6050 | s/i | Sensor | IMU de 6 ejes (acelerómetro + giroscopio); no incluye magnetómetro. |
| 9 | LM2596 / HW-411 | s/i | Energía | Buck ajustable; supuesto de 3 A nominales, menos sin disipador; verificar. |
| 10 | Raspberry Camera V2.1 | 1 (implícito) | Sensor | CSI de 15 pines; la Pi 4 tiene un solo puerto. Una USB para estéreo aproximado se evalúa en ADR-0011, pero no está declarada. |
| 11 | SG90 | 4 | Actuador | Microservo de 9 g; para pan-tilt o pruebas ligeras, no para dirección. |
| 12 | MG90S | 6 | Actuador | 2,2 kg·cm a 6,6 V (F-003); insuficiente para dirección 6×6 (≥10 kg·cm). |
| 13 | Motorreductor de metal 10F125 sin encoder | 6 | Tracción | Sin encoder; faltan tensión, RPM, par y corriente. |
| 14 | LilyGO ESP32 7600X | 1 (implícito) | Control/telemetría | Si es T-SIM7600X: ESP32-WROVER-B + SIM7600 LTE/GNSS; módem por UART, un USB-C; no es ESP32-S3 (F-53). Propuesto como gateway LTE/GNSS (ADR-0012). |
| 15 | Celdas solares HFK 6 V 720 mA, 165×165 mm | 4 | Energía | 17,3 Wp; 2S2P = 12 V nominales, distinto de los 14,4 V de F-008. |
| 16 | Encendedor | 1 (implícito) | Herramienta | No es un componente del rover. |
| 17 | LiPo DUPU 11,1 V 2200 mAh 25C | 1 (implícito) | Energía | 24,4 Wh; sin BMS ni cargador declarados; 55 A de cortocircuito teórico. |

## 3. Mapeo a la BOM base (2 motores)

| Necesidad de la BOM base | Disponible | Veredicto | Comentario |
|---|---|---|---|
| Pi 4 8 GB + Argon | Pi 4 B 8 GB + Argon ONE | Cubre | Base del ADR-0010; sin NVMe, usar SSD USB 3.0 o SD A2; verificar acceso al CSI. |
| LiDAR A1M8 / LD19 | — | No cubre | Bloquea RF-03 y la localización de RF-04/AMCL. |
| BNO085 | MPU-6050 + GY-271 | Parcial | Más calibración y fusión; el magnetómetro sufre cerca de motores. |
| INA219 | — | No cubre | RF-13 se queda sin medición de batería. |
| 2 motores 12 V con encoder | 6 motores sin encoder | No cubre | Sin odometría de ruedas; además faltan datos del motor. |
| Cytron MDD10A | 3 TB6612FNG | Parcial | 1 A continuo y 3 A de pico por canal (F-006); depende del motor. |
| Ruedas y chasis | — | No cubre | No hay plataforma mecánica declarada. |
| LiFePO4 12,8 V 6 Ah | LiPo 3S 2200 mAh | Parcial | 24,4 Wh frente a 76,8 Wh; autonomía y seguridad justas. |
| DC-DC 5 V 3 A / 5 A | LM2596 (3 A nominales) | Parcial | Para Pi 4 + sensores puede; medir rizado y temperatura. Preferir una fuente dedicada de 5 V/3 A. |
| Fusibles, e-stop e interruptor | — | No cubre | RNF-10 exige fusible, e-stop y BMS. |
| Cámara (no incluida en la base) | Camera V2.1 | Extra | Útil para teleoperación y visión; un solo CSI. La USB para estéreo aproximado se evalúa en ADR-0011. |
| Cámara USB para estéreo aproximado | No declarada | Pendiente | ADR-0011: modelo, FOV y sincronía por confirmar; no apta para seguridad. |
| ESP32-S3 (ADR-0008) | LilyGO 7600X | No cubre para tiempo real; propuesto para LTE/GNSS (ADR-0012) | Es ESP32-WROVER-B; el SIM7600 va por UART; no usarlo como controlador de motores. |

## 4. Mapeo a la variante 6×6

| Necesidad de la variante | Disponible | Veredicto | Comentario |
|---|---|---|---|
| 6 motores con encoder | 6 motores sin encoder | No cubre | Bloqueante para la odometría. |
| 3 drivers dobles | 3 TB6612FNG | Parcial | Corriente por confirmar; 1 A continuo y 3 A de pico por canal (F-006). |
| PCA9685 | 1 | Cubre | 16 canales; sobran para 6 servos. |
| 6 servos ≥10 kg·cm | 6 MG90S | No cubre | 2,2 kg·cm (F-003) frente a ≥10 kg·cm; el cálculo ya los descarta. |
| Pack 2S4P 100,8 Wh + BMS | LiPo 3S 2200 mAh | No cubre | 24,4 Wh; química y tensión distintas; requiere rediseño energético. |
| MPPT 2S | — | No cubre | Sin MPPT no hay carga solar controlada. |
| 4 paneles 7,2 V / 600 mA | 4 paneles 6 V / 720 mA | Parcial | Misma potencia (17,3 Wp), otra tensión; revisar el MPPT. |
| Pi 5 | Pi 4 8 GB | Parcial | ADR-0010; recalcular consumo y BOM de la variante; CPU por medir. |
| LiDAR | — | No cubre | Igual que en la base. |
| Camera Module 3 | Camera V2.1 | Parcial | Sirve para visión; no es el spike estéreo de ADR-0009. |
| INA226 | — | No cubre | Telemetría del pack pendiente. |
| Chasis, ruedas y servo savers | — | No cubre | Diseño mecánico pendiente. |
| MCU Teensy / RP2040 | Arduino / LilyGO | Por confirmar | ADR-0008 prefiere ESP32-S3; el LilyGO no es S3 y se reserva para LTE/GNSS (ADR-0012). |

## 5. Brechas críticas

| Brecha | Impacto | Requisito / ADR | Acción mínima |
|---|---|---|---|
| LiDAR 2D 360° | Sin `scan` no hay evitación ni AMCL | RF-03, RF-04; ADR-0005 | Comprar o prestar un A1M8/LD19; registrar fuente y prueba. |
| Encoders | Sin `odom` fiable no se cumplen RF-02/RF-04 | RF-02, RF-04; RNF-02 | Añadir encoders o cambiar motores; medir CPR. |
| Protecciones | RNF-10 no se cumple; riesgo de incendio | RNF-10; H-03, RSK-13 | Fusible, e-stop NC y BMS/alarma; carga supervisada. |
| DC-DC 5 V / 3 A | El LM2596 de 3 A es marginal para Pi 4 + USB | RNF-07; F-54 | Fuente de 5 V/3 A o 5 V/5 A; medir rizado y temperatura. |
| Chasis y ruedas | No hay rover físico | RF-08 | Diseñar o imprimir; validar masa y cotas. |
| Cargador LiPo | No se puede recargar con seguridad | RNF-06, RNF-10 | Cargador balanceador 3S y bolsa ignífuga. |
| Almacenamiento sin NVMe | La Pi 4 no expone PCIe; solo USB/SD | ADR-0010 | SSD USB 3.0 128 GB o microSD A2; asegurar cable y apagado. |
| Estéreo CSI + USB | Sin sincronía hardware; solo aproximado | ADR-0011 | Spike de 2 semanas; si falla, CSI + ToF. No usar para seguridad. |
| LTE/GNSS | Variante, bandas, SIM, antena y consumo por validar | ADR-0012 | Spike; fuera del lazo de control. |
| INA219 / INA226 | RF-13 sin medición de batería | RF-13 | Comprar y calibrar. |
| Datos del motor | No se dimensionan drivers, fusibles ni autonomía | RNF-06 | Hoja de datos o medir tensión, corriente, RPM y par. |

## 6. Qué se puede hacer ya

> Nada de esto está ejecutado todavía; son candidatos a *spike*. No cuentan como
> G4 ni como evidencia de runtime.

- Banco de tracción con Pi 4, TB6612 y 2–6 motores; primero medir consumo y par.
- Teleoperación y lectura de IMU, ToF y cámara.
- ROS 2 Jazzy en Pi 4 (F-18), con la misma pila; medir CPU, RAM y temperatura.
- Evitación reactiva con ToF; no sustituye a RF-03.
- Spike de cámara CSI + USB (ADR-0011) para medir sincronía y profundidad;
  no sustituye al LiDAR/ToF.
- Spike de LTE/GNSS con el LilyGO (ADR-0012), fuera del lazo de control.
- Caracterización de los paneles (Vmp, Imp) con multímetro.
- Revisión física, inventario fotografiado y comprobación de cantidades.

## 7. Decisiones que este documento no cambia

- **ADR-0010 (Pi 4 8 GB):** aceptado; reemplaza a ADR-0002. RNF-07 se mide en
  Pi 4 y la BOM se revisa en consecuencia.
- **OQ-09 (2 motores/LiFePO4 frente a 6×6/Li-ion/solar):** sigue abierta; no se
  mezclan las BOM y el estudio 6×6 debe recalcularse si se adopta.
- **ADR-0008 (ESP32-S3):** el LilyGO no es un S3; se propone para LTE/GNSS
  (ADR-0012), no como controlador de motores.
- **ADR-0011 (CSI + USB):** propuesta de spike; no cambia requisitos ni la
  percepción primaria (LiDAR + ToF).
- **BOM y presupuesto:** el total revisado es 671 EUR, pendiente de aprobación;
  disponibilidad no es compra.
- **Química de la batería:** la LiPo 3S no reemplaza a la LiFePO4 sin un
  análisis de energía y seguridad.

## 8. Datos pendientes de confirmar

- Pi 4: estado, fuente, tarjeta SD, acceso al CSI con la carcasa Argon y
  arranque desde USB.
- Motores 10F125: tensión, RPM, par, corriente, eje y masa.
- LiPo: estado, ciclos, resistencia interna, conector, cargador y BMS.
- LilyGO: modelo, variante (E/G/SA-H), bandas del operador, SIM y antena.
- Paneles: Vmp, Imp, Voc, Isc y estado.
- Arduino: modelo exacto.
- Cámara USB: modelo, FOV, resolución, UVC y montaje (si se usa en ADR-0011).
- ToF, MPU-6050 y LM2596: cantidades y variantes.
- Fotos y verificación física del material.

## 9. Seguridad

- La LiPo 3S de 2200 mAh y 25C almacena 24,4 Wh y puede entregar hasta 55 A en
  cortocircuito teórico. No conectarla al rover sin fusible, alarma de baja
  tensión y BMS o protección equivalente; cargarla con cargador balanceador,
  bolsa ignífuga y supervisión. Aplican RNF-10, H-03 y RSK-13.
- No usar los MG90S para la dirección de un 6×6: 2,2 kg·cm (F-003) frente a
  ≥10 kg·cm del cálculo.
- Medir el Voc de los paneles antes de conectar; no cortocircuitarlos.
- No mover el rover sin e-stop accesible y zona despejada.
- El encendedor es una herramienta; no dejarlo dentro del rover.

## 10. Enlaces

- BOM base: [`bom.md`](bom.md).
- BOM Perú: [`bom-peru.md`](bom-peru.md).
- Variante 6×6: [`energia/bom-6x6.md`](energia/bom-6x6.md).
- Diseño eléctrico: [`diseno-electrico.md`](diseno-electrico.md).
- Cálculo energético: [`energia/calculo-energetico.md`](energia/calculo-energetico.md).
- Requisitos no funcionales: [`../02-requisitos/requisitos-no-funcionales.md`](../02-requisitos/requisitos-no-funcionales.md).
- ADR-0002 (histórico): [`../03-arquitectura/adr/0002-raspberry-pi-5.md`](../03-arquitectura/adr/0002-raspberry-pi-5.md).
- ADR-0008: [`../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md`](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md).
- ADR-0010: [`../03-arquitectura/adr/0010-raspberry-pi-4.md`](../03-arquitectura/adr/0010-raspberry-pi-4.md).
- ADR-0011: [`../03-arquitectura/adr/0011-estereo-csi-usb.md`](../03-arquitectura/adr/0011-estereo-csi-usb.md).
- ADR-0012: [`../03-arquitectura/adr/0012-lilygo-lte-gnss.md`](../03-arquitectura/adr/0012-lilygo-lte-gnss.md).
- OQ-09: [`../00-gobierno/registro-decisiones.md`](../00-gobierno/registro-decisiones.md).
- Fuentes: [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Seguridad: [`../03-arquitectura/seguridad.md`](../03-arquitectura/seguridad.md).
