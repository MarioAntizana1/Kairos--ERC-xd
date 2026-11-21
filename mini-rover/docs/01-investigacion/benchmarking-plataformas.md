# Benchmarking de plataformas de cómputo

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
> **Aviso:** precios orientativos a 2026-11-21, sin IVA ni envío. Cotizar antes de comprar.
>
> **Revisión ADR-0010 (2026-11-21):** este estudio se redactó cuando la
> decisión era Pi 5. La base vigente es **Raspberry Pi 4 8 GB + Argon ONE**
> ([ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md)). La comparación se
> conserva como histórico; las referencias a Pi 5 no son la decisión actual.

## 1. Criterios

| Criterio | Peso | Justificación |
|---|---|---|
| Soporte ROS 2 Jazzy | 25% | Evita compilaciones y sorpresas |
| Rendimiento suficiente | 20% | Nav2 + LiDAR + logs a 10–20 Hz |
| Consumo y calor | 15% | Alimentación por batería, caja cerrada |
| Precio | 15% | Presupuesto universitario |
| Disponibilidad | 10% | Plazos de entrega |
| Ecosistema y documentación | 10% | Curva de aprendizaje |
| Tamaño y peso | 5% | Chasis pequeño |

## 2. Matriz comparativa

| Plataforma | CPU/GPU | RAM | ROS 2 Jazzy | Consumo típico | Precio est. | Disponibilidad | Puntuación |
|---|---|---|---|---|---|---|---|
| **Raspberry Pi 5 8 GB** | 4× Cortex-A76 2.4 GHz | 8 GB | Binarios arm64 en Ubuntu 24.04 | 5–12 W | ~90 EUR | Alta | **8.6/10** |
| Raspberry Pi 4B 8 GB | 4× Cortex-A72 1.8 GHz | 8 GB | Binarios arm64 en Ubuntu 24.04 | 4–8 W | ~85 EUR | Alta | 7.4/10 |
| Jetson Orin Nano Super 8 GB | 6× A78AE + GPU Ampere | 8 GB | JetPack 6 (Ubuntu 22.04); Jazzy vía contenedor | 7–25 W | ~250 EUR | Media | 7.8/10 |
| Mini PC x86 N100 | 4× Alder Lake-N | 16 GB | Ubuntu 24.04 nativo | 6–20 W | ~180 EUR | Alta | 8.2/10 |
| Laptop x86 existente | Variable | 16 GB | Ubuntu 24.04 nativo | 15–45 W | 0 EUR (si se tiene) | Alta | 8.0/10 (solo desarrollo) |

## 3. Análisis

### Raspberry Pi 5 8 GB — evaluación original (no vigente)

**Ventajas**

- Binarios oficiales de ROS 2 Jazzy para arm64 sobre Ubuntu 24.04.
- Relación precio/rendimiento excelente.
- GPIO, I2C, SPI y UART para sensores y drivers.
- Comunidad enorme, tutoriales y sombreros (HATs) abundantes.
- Bajo consumo y tamaño reducido.
- NVMe por PCIe (con HAT) para evitar corrupción de SD.

**Desventajas**

- No tiene GPU CUDA; visión pesada limitada.
- Necesita refrigeración activa en caja cerrada.
- La SD se corrompe con cortes de energía; usar NVMe y apagado seguro.
- El WiFi integrado puede ser irregular; para operación crítica, Ethernet o dongle externo.

**Mitigaciones**

- Disipador + ventilador.
- NVMe 128 GB.
- Alimentación con DC-DC regulado y fusible.
- Watchdog de hardware y apagado controlado.

### Raspberry Pi 4B 8 GB — plataforma elegida (ADR-0010)

Suficiente para Nav2 a baja velocidad, con menos margen de CPU y sin PCIe/NVMe.
Es la plataforma disponible en facultad y la base vigente. El mismo software
funciona; hay que medir CPU y temperatura y usar SSD USB 3.0 o microSD A2.

### Jetson Orin Nano Super — descartada para esta fase

Potente para visión e IA, pero:

- JetPack 6 se basa en Ubuntu 22.04; ROS 2 Jazzy no es la combinación oficial (se puede usar contenedor).
- Consumo y precio mayores.
- No aporta ventaja si el demo es navegación 2D con LiDAR.

Queda como opción futura si se añade visión estereoscópica o SLAM visual.

### Mini PC x86 — alternativa de laboratorio

Muy cómodo para desarrollo y simulación, pero más pesado y con mayor consumo. Útil como estación de desarrollo y como *fallback* de demo si el Pi falla.

## 4. Rendimiento esperado en Pi 4 8 GB

| Carga | Estimación | Nota |
|---|---|---|
| Nav2 completo (AMCL + Navfn + RPP + costmaps) | 25–50% CPU | A 10–20 Hz, mapa 12×8 m |
| LiDAR 10 Hz | 5–10% CPU | Driver USB |
| Rosbag2 (6 topics) | 5–15% CPU | SSD USB 3.0 recomendado |
| Mission node | < 2% CPU | Python |
| RViz2 | **No ejecutar en el Pi** | Usar estación remota |
| Total esperado | 40–70% CPU | Margen para picos |

> Estas cifras son estimaciones de diseño, no mediciones. Se validan en E2 (hardware) y se registran en la evidencia.

## 5. Decisión

La decisión vigente es **Raspberry Pi 4 Model B de 8 GB + Argon ONE**, con SSD
USB 3.0 y fuente de 5 V/3 A. Ver
[ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md). El análisis original
elegía Pi 5; se conserva como histórico.

### Criterios de revisión

- Si el CPU medio supera el 80% o la temperatura supera 80 °C en pruebas de 30 min.
- Si se necesita NVMe, dos CSI o más de 8 GB para una función aprobada.
- Si se añade visión pesada o SLAM 3D.
- Si el presupuesto permite una Pi 5 y la Pi 4 no cumple RNF-01/RNF-02.

## 6. Fuentes

[F-06] ROS 2 Jazzy installation, [F-11] Ubuntu for Raspberry Pi, [F-13] guía comunitaria Pi 5 + Jazzy, [F-12] REP 2000. Detalle en [`fuentes.md`](fuentes.md).
