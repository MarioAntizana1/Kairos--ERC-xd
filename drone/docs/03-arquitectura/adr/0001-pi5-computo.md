# ADR-0001 — Raspberry Pi 5 8 GB como computadora de visión

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: rol de Visión

## Contexto

El payload necesita:

- Dos puertos CSI para el par estéreo.
- Un ISP que entregue frames a 2304 × 1296 sin saturar la CPU.
- PCIe o USB 3.0 para almacenamiento.
- Consumo y peso compatibles con un dron pequeño.
- Disponibilidad y precio en Perú.
- Soporte de libcamera/Picamera2 y OpenCV.

## Alternativas

| Alternativa | Ventajas | Desventajas | Coste local |
|---|---|---|---|
| **Raspberry Pi 5 8 GB** | Doble CSI, ISP, PCIe, 8 GB, stock, precio | CPU sin CUDA; 5 V/5 A; térmica | S/ 768 |
| Raspberry Pi 4B 8 GB | Maduro, barato | **Un solo CSI**; menos CPU; sin PCIe | ~S/ 600 |
| Raspberry Pi 5 4 GB | Más barato | Menos margen para ROS 2 y buffers | S/ 488 |
| Raspberry Pi 5 16 GB | Más RAM | No resuelve CPU; +S/ 931 | S/ 1.699 |
| Jetson Orin Nano | GPU, IA, profundidad densa | Precio, consumo, peso, disponibilidad | US$ 249+ |
| x86 NUC | CPU potente | Consumo, peso, precio, CSI limitado | US$ 300+ |

## Decisión

**Raspberry Pi 5 8 GB** como computadora de visión.

Motivos:

1. Es la única opción local con **dos CSI** y ISP integrado.
2. 8 GB permiten ROS 2, buffers de imagen y OpenCV sin swapping.
3. PCIe permite NVMe compacto.
4. Precio y stock local; ecosistema y documentación.
5. Reutiliza la experiencia del proyecto rover (Ubuntu/ROS 2).

## Consecuencias

- **Positivas:** doble cámara, NVMe, comunidad, coste.
- **Negativas:** el estéreo corre en CPU; no hay CUDA; 5 V/5 A; térmica.
- **Riesgos:** throttling, brownout, HAT/SSD sin stock.
- **Mitigaciones:** Active Cooler, UBEC 5 A, resolución reducida para tiempo real,
  BM como fallback de SGBM.
- **Requisitos afectados:** RF-01, RF-02, RNF-02, RNF-05, RNF-07.

## Evidencia

- F-01, F-06, F-27.
- Cotización: [`../04-diseno/bom-peru.md`](../../04-diseno/bom-peru.md).
- Cálculo de geometría: [`../04-diseno/diseno-vision.md`](../../04-diseno/diseno-vision.md).

## Revisión

| Fecha | Revisor | Resultado |
|---|---|---|
| 2026-11-21 | Visión | Aceptada para G0/G1; revisar tras medir FPS y temperatura |
