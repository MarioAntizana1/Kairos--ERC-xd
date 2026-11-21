# ADR-0002 — Raspberry Pi 5 (8 GB) como computadora de a bordo

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Hardware · Reemplaza a: —

## Contexto

El rover necesita cómputo a bordo para ROS 2, Nav2, LiDAR, odometría, telemetría y logs, con bajo consumo, tamaño reducido y coste contenido. La demo debe poder alimentarse con una batería y caber en un chasis de 0.55 × 0.45 m.

## Alternativas consideradas

| Alternativa | CPU/GPU | RAM | Consumo | Precio est. | ROS 2 Jazzy | Veredicto |
|---|---|---|---|---|---|---|
| **Raspberry Pi 5 8 GB** | 4× A76 2.4 GHz | 8 GB | 5–12 W | ~90 EUR | Binarios arm64 | **Elegida** |
| Raspberry Pi 4B 8 GB | 4× A72 1.8 GHz | 8 GB | 4–8 W | ~85 EUR | Binarios arm64 | Fallback |
| Jetson Orin Nano Super | 6× A78AE + GPU | 8 GB | 7–25 W | ~250 EUR | Contenedor (JetPack 6/Ubuntu 22.04) | Descartada |
| Mini PC x86 N100 | 4× Alder Lake-N | 16 GB | 6–20 W | ~180 EUR | Nativo | Alternativa de laboratorio |
| Laptop existente | Variable | 16 GB | 15–45 W | 0 EUR | Nativo | Solo desarrollo |

## Decisión

Usar **Raspberry Pi 5 de 8 GB**, con **NVMe de 128 GB** (o SD A2 de 64 GB como mínimo) y **refrigeración activa**.

## Consecuencias

### Positivas

- Suficiente para Nav2 con RPP y LiDAR 2D a 10 Hz.
- GPIO/I2C/SPI/UART para sensores y driver.
- Bajo consumo y precio.
- Comunidad y accesorios abundantes.
- Misma arquitectura que la mayoría de tutoriales.

### Negativas

- Sin GPU CUDA: visión pesada y SLAM visual limitados.
- Necesita refrigeración y apagado seguro.
- El WiFi integrado puede ser irregular; usar Ethernet o dongle para operación crítica.
- La SD se corrompe con cortes; NVMe recomendado.

### Neutrales

- El rover grande puede migrar a Jetson o x86 si añade visión; el software es portable.

## Mitigaciones

- Disipador + ventilador; monitorizar temperatura.
- NVMe y sistema de archivos con journaling.
- DC-DC regulado y fusible.
- Watchdog de hardware y apagado controlado.
- Prueba de carga de 30 min antes de la demo.

## Criterios de revisión

- CPU media > 80% o temperatura > 80 °C en pruebas de 30 min.
- Necesidad de visión estéreo, SLAM 3D o inferencia IA a bordo.
- Falta de disponibilidad o subida de precio.
- Presupuesto insuficiente: Pi 4B 8 GB o mini PC x86.

## Referencias

- [F-11] Ubuntu for Raspberry Pi.
- [F-13] ROS 2 Jazzy en Pi 5 (secundaria).
- [F-18] Matriz de soporte de Ubuntu en Pi.
- [`../../01-investigacion/benchmarking-plataformas.md`](../../01-investigacion/benchmarking-plataformas.md).
