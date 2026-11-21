# Registro de decisiones (ADR index)

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Tech Lead

Una decisión arquitectónica se documenta en un **ADR** (Architecture Decision Record). Los ADRs no se borran: si una decisión cambia, se crea uno nuevo y se marca el anterior como reemplazado.

## Decisiones aceptadas

| ADR | Título | Decisión | Estado | Fecha |
|---|---|---|---|---|
| [ADR-0001](../03-arquitectura/adr/0001-ros2-jazzy.md) | ROS 2 Jazzy Jalisco | Usar ROS 2 Jazzy + Ubuntu 24.04 | Aceptada | 2026-11-21 |
| [ADR-0003](../03-arquitectura/adr/0003-nav2.md) | Nav2 | Usar Nav2 en lugar de stack propio | Aceptada | 2026-11-21 |
| [ADR-0004](../03-arquitectura/adr/0004-gazebo-harmonic.md) | Gazebo Harmonic | Simular con Gazebo Harmonic + ros_gz | Aceptada | 2026-11-21 |
| [ADR-0005](../03-arquitectura/adr/0005-mapa-estatico-amcl.md) | Mapa estático + AMCL | Localización determinista para el demo | Aceptada | 2026-11-21 |
| [ADR-0006](../03-arquitectura/adr/0006-python-mision.md) | Nodo de misión en Python | Orquestar Nav2 con un nodo Python fino | Aceptada | 2026-11-21 |
| [ADR-0007](../03-arquitectura/adr/0007-evidencia-reproducible.md) | Evidencia reproducible | Toda ejecución deja metadatos y hash | Aceptada | 2026-11-21 |
| [ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md) | Raspberry Pi 4 8 GB + Argon ONE | Pi 4 como computadora de a bordo; USB SSD, 5 V/3 A, un CSI | Aceptada | 2026-11-21 |

## Decisiones propuestas

| ADR | Título | Decisión | Estado | Fecha |
|---|---|---|---|---|
| [ADR-0008](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md) | ESP32-S3 como interfaz de tiempo real | Pi 4 como cerebro; ESP32-S3 para PWM, encoders, IMU, batería y expansión I²C | Propuesta | 2026-11-21 |
| [ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md) | Estéreo aproximado CSI + USB | Spike de 2 semanas con Camera V2.1 + USB; no sustituye al LiDAR/ToF | Propuesta | 2026-11-21 |
| [ADR-0012](../03-arquitectura/adr/0012-lilygo-lte-gnss.md) | LilyGO T-SIM7600X LTE/GNSS | Gateway LTE/GNSS opcional, fuera del lazo de control | Propuesta | 2026-11-21 |

## Decisiones obsoletas o reemplazadas

| ADR | Título | Decisión | Estado | Fecha |
|---|---|---|---|---|
| [ADR-0002](../03-arquitectura/adr/0002-raspberry-pi-5.md) | Raspberry Pi 5 8 GB | Pi 5 como computadora de a bordo | Reemplazada por ADR-0010 | 2026-11-21 |
| [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md) | Spike de percepción 3D | 2 CM3 + ToF en Pi 5 | Obsoleta; ver ADR-0011 | 2026-11-21 |

## Decisiones abiertas

| ID | Pregunta | Opciones | Responsable | Necesaria antes de |
|---|---|---|---|---|
| OQ-01 | ¿Categoría del ERC 2027? | On-site, remote, otra | PO | Registro |
| OQ-02 | ¿Chasis comprado o fabricado? | Kit, aluminio, impresión 3D | HW | Compra |
| OQ-03 | ¿LiDAR definitivo? | RPLIDAR A1M8, LD19, otro | HW | Compra |
| OQ-04 | ¿IMU con fusión o solo odometría? | BNO085, MPU-9250, ninguno | NAV | Diseño eléctrico |
| OQ-05 | ¿ROS 2 Jazzy o Lyrical? | Jazzy (estable), Lyrical (nuevo) | TL | G2 |
| OQ-06 | ¿Licencia del proyecto? | MIT, Apache-2.0, GPL, propietaria | PO | Publicación |
| OQ-07 | ¿Operación con ROS_DOMAIN_ID y DDS específicos? | CycloneDDS, FastDDS | TL | Integración |
| OQ-08 | ¿Se usará `robot_localization`? | EKF con IMU + odom, solo odom | NAV | Calibración |
| OQ-09 | ¿Arquitectura energética: 2 motores + LiFePO4 (mini demo) o 6×6 + Li-ion + solar? | Base 2 motores/LiFePO4 vs variante 6×6: [cálculo](../04-diseno/energia/calculo-energetico.md), [diseño eléctrico](../04-diseno/energia/diseno-electrico-6x6.md), [BOM](../04-diseno/energia/bom-6x6.md) | PO/HW | Compra de hardware |
| OQ-10 | ¿MCU de interfaz: ESP32-S3, ESP32-C6, RP2040 o Teensy? | [ADR-0008 propuesto](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md): S3 recomendado; C6 para base; RP2040/Teensy si no se necesita Wi-Fi | HW/TL | Compra y diseño eléctrico |
| OQ-12 | ¿El 3D denso es un requisito de demo o una línea de aprendizaje? | Requisito «Could» vs spike vs descartado; el spike B lo evalúa | PO | Requisitos y presupuesto |
| OQ-13 | ¿Hay presupuesto para una cámara de ~269 USD o se prioriza el bajo coste? | OAK-D Lite vs 2 CM3 + ToF vs 2 GS | PO | Compra |
| OQ-14 | ¿La arena del ERC 2027 es exterior y con sol directo? | Sí / no / por confirmar; afecta al alcance del ToF | PO/Investigación | Diseño del ToF y pruebas |
| OQ-15 | ¿Quién calibra y mantiene el estéreo? | Equipo de navegación / hardware / externo | Equipo | G4 |
| OQ-16 | ¿Se usa LTE en la demo oficial o solo en el banco de pruebas? | Solo telemetría de desarrollo / enlace de respaldo / requisito de demo | PO | Arquitectura y BOM |
| OQ-17 | ¿Qué variante y operador LTE se usan? | T-SIM7600SA-H o G; operador y plan de datos por confirmar | HW | Compra de SIM |
| OQ-18 | ¿Estéreo CSI + USB o cámara única + ToF? | Spike ADR-0011 / CSI + ToF / cámara estéreo sincronizada | NAV | Compra y pruebas |

> **Inventario de facultad (2026-11-21):** el material disponible condiciona
> OQ-03 (LiDAR), OQ-04 (IMU), OQ-09 (energía), OQ-10 (MCU), OQ-16–18
> (LTE/cámara); ver [`../04-diseno/inventario-facultad.md`](../04-diseno/inventario-facultad.md).

## Convención de numeración

- `ADR-0001` a `ADR-9999`, secuencial y sin reutilizar.
- El título del archivo es `NNNN-titulo-corto.md`.
- Estado posible: `Propuesta`, `Aceptada`, `Rechazada`, `Reemplazada por ADR-XXXX`, `Obsoleta`.

## Plantilla

Usar [`plantillas/adr.md`](plantillas/adr.md).
