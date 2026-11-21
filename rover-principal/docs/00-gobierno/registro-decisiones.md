# Registro de decisiones (ADR index) — Visión

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Tech Lead

Una decisión arquitectónica se documenta en un **ADR** (Architecture Decision Record). Los ADRs no se borran: si una decisión cambia, se crea uno nuevo y se marca el anterior como reemplazado.

> **Numeración:** esta sección usa `ADR-1xxx` para no colisionar con los `ADR-0001`–`ADR-0009` del mini demo. El LiDAR, la metodología y ROS 2 Jazzy se heredan como decisiones ya tomadas; no se reabren aquí.

## Decisiones aceptadas

| ADR | Título | Decisión | Estado | Fecha |
|---|---|---|---|---|
| — | — | Aún no hay ADRs propios de la sección | — | — |

## Decisiones propuestas

| ADR | Título | Decisión | Estado | Fecha |
|---|---|---|---|---|
| — | — | Aún no hay propuestas formales | — | — |

## Decisiones heredadas (solo referencia)

| ADR | Título | Qué se hereda | Estado |
|---|---|---|---|
| [ADR-0001](../03-arquitectura/adr/0001-ros2-jazzy.md) | ROS 2 Jazzy Jalisco | Middleware base | Aceptada en el mini demo |
| [ADR-0002](../03-arquitectura/adr/0002-raspberry-pi-5.md) | Raspberry Pi 5 8 GB | Cómputo del mini demo; **no obliga al rover grande** | Aceptada en el mini demo |
| [ADR-0003](../03-arquitectura/adr/0003-nav2.md) | Nav2 | Pila de navegación | Aceptada en el mini demo |
| [ADR-0004](../03-arquitectura/adr/0004-gazebo-harmonic.md) | Gazebo Harmonic | Simulación | Aceptada en el mini demo |
| [ADR-0005](../03-arquitectura/adr/0005-mapa-estatico-amcl.md) | Mapa estático + AMCL | Localización del demo | Aceptada en el mini demo |
| [ADR-0006](../03-arquitectura/adr/0006-python-mision.md) | Nodo de misión en Python | Orquestación | Aceptada en el mini demo |
| [ADR-0007](../03-arquitectura/adr/0007-evidencia-reproducible.md) | Evidencia reproducible | Metadatos y hash | Aceptada en el mini demo |
| [ADR-0008](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md) | ESP32-S3 como interfaz | Propuesta, no aceptada | Propuesta en el mini demo |
| [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md) | Spike de percepción 3D | Lecciones de estéreo y ToF; no obliga al rover grande | Aceptada en el mini demo |
| — | LiDAR en la lista del rover grande | Sensor primario de navegación | Decisión del proyecto principal |

## Decisiones abiertas

| ID | Pregunta | Opciones | Responsable | Necesaria antes de |
|---|---|---|---|---|
| OQ-V01 | ¿Qué plataforma de cómputo tendrá el rover grande? | Jetson Orin Nano/NX, x86 embebido, Raspberry Pi 5 + acelerador | PO / TL | Arquitectura y compra |
| OQ-V02 | ¿El 3D denso es requisito o línea de aprendizaje? | Requisito «Must/Should» vs. spike vs. descartado | PO | Requisitos |
| OQ-V03 | ¿Se aprueba el presupuesto para dos cámaras + ToF? | Sí / no / por fases | PO | Compra |
| OQ-V04 | ¿La operación será exterior con sol directo? | Sí / no / por confirmar; afecta al ToF y al estéreo | PO / Investigación | Diseño y pruebas |
| OQ-V05 | ¿Se compran dos Elgato Facecam 4K o se importa un estéreo global shutter / OAK-D? | Elgato local vs. importar | HW / PO | Compra |
| OQ-V06 | ¿Qué ToF: TFmini Plus, TFmini-S, LIDAR-Lite v3HP o VL53L8CX importado? | Single-point local vs. multizona importado | HW | Compra |
| OQ-V07 | ¿Quién calibra y mantiene el estéreo? | Equipo / externo | Equipo | G4 |
| OQ-V08 | ¿Dónde se monta la cámara: mástil, brazo o ambos? | Mástil, brazo, carcasa frontal | HW / NAV | Diseño mecánico |
| OQ-V09 | ¿Se necesita sincronía hardware entre cámaras? | Sí (global shutter) / no (software) | TL | Arquitectura |
| OQ-V10 | ¿Se usa ROS 2 Jazzy también en el rover grande? | Jazzy / distro más reciente | TL | G2 |

## Convención de numeración

- `ADR-1001` a `ADR-1999`, secuencial y sin reutilizar.
- El título del archivo es `1xxx-titulo-corto.md`.
- Estado posible: `Propuesta`, `Aceptada`, `Rechazada`, `Reemplazada por ADR-XXXX`, `Obsoleta`.

## Plantilla

Usar [`plantillas/adr.md`](plantillas/adr.md).
