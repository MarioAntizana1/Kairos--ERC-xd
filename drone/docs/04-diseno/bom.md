# Lista de materiales y presupuesto de referencia (USD)

> Estado: Estimado · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
>
> **Aviso:** precios orientativos en USD a 2026-11-21, sin IGV, envío ni aduanas.
> No autoriza compra. La cotización local en soles, con stock y alternativas, está
> en [`bom-peru.md`](bom-peru.md).

## 1. Escenario recomendado

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. (USD) | Total (USD) | Nota |
|---|---|---|---|---:|---:|---:|---|
| 1 | Cómputo | Raspberry Pi 5 8 GB | Placa oficial | 1 | 80 | 80 | Doble CSI, PCIe |
| 2 | Cómputo | HAT+ M.2 | Oficial | 1 | 12–17 | 15 | NVMe 2242 |
| 3 | Cómputo | SSD NVMe 128 GB | M.2 2242 | 1 | 30 | 30 | Arranque/registro |
| 4 | Cómputo | Refrigeración | Active Cooler | 1 | 5 | 5 | Necesario en caja |
| 5 | Cómputo | microSD 64 GB A2 | Respaldo | 1 | 10 | 10 | Arranque de emergencia |
| 6 | Cómputo | Fuente de banco | 27 W USB-C | 1 | 12 | 12 | Solo banco |
| 7 | Sensor | Cámara estéreo | Camera Module 3 Standard | 2 | 25 | 50 | IMX708, 12 MP |
| 8 | Sensor | Cables FPC 22→15 | 300 mm | 2 | 4 | 8 | Repuesto |
| 9 | Sensor | ToF de piso | TFmini Plus 12 m | 1 | 45 | 45 | Base para 6 m |
| 10 | Sensor | Cable Qwiic | 100 mm | 1 | 3 | 3 | I²C |
| 11 | Energía | UBEC 5 V/5 A | Matek BEC12S-PRO | 1 | 27 | 27 | 2–12S |
| 12 | Energía | Conectores/fusible | XT60/XT30, 5 A | 1 | 15 | 15 | Protección |
| 13 | Mecánica | Montaje/baseline | Impresión 3D + tornillería | 1 | 40 | 40 | 150 mm |
| 14 | Mecánica | Aisladores | Silicona M3 | 1 | 8 | 8 | 4–8 puntos |
| 15 | Cableado | Varios | USB-C, Dupont, termorretráctil | 1 | 20 | 20 | — |
| | | | | | | **~368** | Sin envío |

> El total es una **referencia internacional**, no una cotización. La ruta Perú
> con IGV, envío local y contingency está en [`bom-peru.md`](bom-peru.md):
> **S/ 2.341,08** para el kit completo con TFmini Plus (6 m); **S/ 2.073,33** si
> se baja a un ToF de 4 m (solo banco).

## 2. Escenario mínimo

| Cambio | Ahorro aprox. (USD) | Riesgo |
|---|---:|---|
| Sin HAT/SSD; arranque por microSD A2 | ~45 | Corrupción y lentitud |
| ToF VL53L1X en lugar de TFmini Plus | ~30 | Solo mide hasta 4 m; no ve el piso a 6 m |
| Cámaras Wide en lugar de Standard | +20 | Más cobertura, menos resolución angular |
| Sin UBEC; usar BEC del dron | ~27 | Verificar 5 A y ripple |
| Montaje impreso simple | ~20 | Menos rigidez; calibración frágil |
| **Total mínimo aproximado** | **~280** | Mayor riesgo |

## 3. Escenario ampliado

| Añadido | Coste aprox. (USD) | Beneficio |
|---|---|---|
| 2 × cámara global shutter | +100 | Sin rolling shutter; monocroma |
| TF-Luna 8 m (import.) | +0 | Alternativa más liviana al TFmini Plus |
| SSD 512 GB | +30 | Más registro |
| IMU rígida a la cámara (BNO085) | +30 | VIO si la FC no da pose |
| Jetson Orin Nano | +250 | IA/profundidad densa |
| **Total ampliado** | **+450–500** | Futuro |

## 4. Herramientas

Si el equipo no las tiene, añadir:

| Herramienta | Coste est. (USD) |
|---|---:|
| Multímetro | 25 |
| Soldador + estaño | 30 |
| Crimpadora | 25 |
| Destornilladores y llaves | 30 |
| Fuente de laboratorio | 60 |
| **Total** | **170** |

> Muchas universidades tienen taller; comprobar antes de comprar.

## 5. Licencias y software

| Elemento | Coste | Nota |
|---|---|---|
| Raspberry Pi OS / Ubuntu 24.04 | 0 | Open source |
| libcamera / Picamera2 | 0 | Open source |
| OpenCV | 0 | Apache-2.0 |
| ROS 2 Jazzy | 0 | Apache-2.0 |
| MAVLink / MAVROS | 0 | LGPL / BSD |
| FreeCAD / KiCad | 0 | Open source |

## 6. Plan de compra

| Prioridad | Componentes | Cuándo |
|---|---|---|
| 1 | Pi 5, 2 × CM3, cables, cooler, fuente | Semana 1 |
| 2 | microSD, HAT/SSD | Semana 1–2 |
| 3 | ToF de piso, aisladores, tornillería | Semana 2 |
| 4 | UBEC, conectores, fusibles | Semana 2–3 |
| 5 | Montaje impreso | Semana 3–4 |
| 6 | Repuestos y herramientas | Semana 4 |

## 7. Riesgos de suministro

- **HAT+ M.2:** stock irregular; confirmar antes de comprar el SSD 2242.
- **ToF de piso:** el VL53L1X es local pero de 4 m; el TFmini Plus/8×8 se importan
  o cotizan; plazo y aduana.
- **UBEC:** no verificado localmente; cotizar landed.
- **Cámaras:** stock declarado en The Pi Box; comprar las dos juntas para que sean
  del mismo lote y tengan características similares.
- **Aduanas:** presupuestar 10–20 % adicional si se importa.

## 8. Control de cambios

Cualquier cambio de BOM debe:

1. Registrarse en este documento y en [`bom-peru.md`](bom-peru.md).
2. Actualizar el presupuesto y el CSV.
3. Revisar el impacto en el diseño de visión y en el peso.
4. Aprobarse por el PO y el responsable de Hardware.
