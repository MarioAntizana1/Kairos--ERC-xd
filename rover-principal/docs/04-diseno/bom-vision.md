# BOM de visión — prototipo local

> Estado: Estimado · Versión: 0.2 · Revisión: **2026-11-23** · Responsable: Hardware
>
> Cotización de la combinación **V-A** (2 × Elgato Facecam 4K + **2 × TFmini Plus**
> + **2 × LiDAR RPLIDAR A1M8** + montaje + cables). Precios en soles (PEN) salvo A5,
> en USD; con IGV cuando la tienda lo indica. **No autoriza compra.** La aprobación
> es OQ-V03.
>
> **Cambios del 2026-11-23:** el LiDAR 360 del rover grande pasa a **dos unidades**
> (cobertura frontal y posterior, con alternativa de tres) y el ToF de punto único
> pasa a **dos unidades**, una por unidad de visión.

## 1. BOM recomendada (V-A)

| # | Ítem | Modelo / SKU | Proveedor | Cant. | Precio unit. | Subtotal | Stock | Fuente |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Cámara web 4K | Elgato Facecam 4K · 040866 / 10WAF9901 | Memory Kings | 2 | S/ 828,00 | S/ 1.656,00 | > 10 | F-52 |
| 2 | LiDAR 2D 360° | RPLIDAR A1M8-R6 · 12 m (Slamtec) | Electromanía | 2 | S/ 600,00 | S/ 1.200,00 | Quedaban 12 | F-56 |
| 3 | ToF de punto único | Benewake TFmini Plus · J006-SEN0309 | Electromanía | 2 | S/ 330,00 | S/ 660,00 | 8 | F-56 |
| 4 | Montaje rígido (barra + soportes) | A medida, aluminio | Taller local | 1 | ~S/ 250,00 | ~S/ 250,00 | — | Supuesto |
| 5 | Cables USB 3.0 + hub alimentado | Certificados | Tienda local | 1 | ~S/ 150,00 | ~S/ 150,00 | — | Supuesto |
| | **Total estimado** | | | | | **~S/ 3.916,00** | | |

> **Nota:** incluye montaje y cables estimados. Memory Kings no incluye flete;
> Electromanía cobra envío según destino. No se incluyó seguro ni garantía
> extendida.
>
> **Dos LiDAR:** hay que definir la fusión en ROS 2 (dos `scan`, `laser_filters` o
> `ira_laser_tools`) y los frames de cada uno antes de montar.
>
> **¿Por qué dos ToF?** El ToF de punto único da la referencia métrica de altura o
> distancia al suelo por unidad de visión; con dos cámaras se pide uno por unidad.

## 2. Alternativas

| # | Ítem | Modelo / SKU | Proveedor | Precio | Stock | Fuente | Cuándo |
|---:|---|---|---|---:|---|---|---|
| A1 | ToF más barato | TFmini-S · C010A-SEN0259 | Electromanía | S/ 299,00 | 3 | F-57 | Si el presupuesto aprieta; verificar ficha |
| A2 | ToF de largo alcance | LIDAR-Lite v3HP · R004-EP-176 | Electromanía | S/ 850,00 | 11 | F-58 | Si se necesitan 10–40 m |
| A3 | ToF near-field | DFRobot 4 m · SEN0590 | Electromanía | S/ 115,00 | 3 | F-59 | Obstáculos bajos y huecos |
| A4 | ToF near-field | VL53L1X · 000715 | Naylamp | S/ 75,00 | En stock | F-61 | Alternativa al DFRobot |
| A5 | ToF multizona | VL53L8CX carrier | Pololu / importación | USD 24,95 + envío | Importar | F-66 | Si el 3D multizona es requisito |
| A6 | Cámara 4K económica | Creative Live! Cam Sync 4K | Memory Kings | S/ 261,00 | > 10 | F-68 | Si no se necesita el sensor STARVIS |
| A7 | Cámara 4K alternativa | Logitech Brio 4K | Memory Kings | S/ 487,00 | > 10 | F-68 | Ecosistema Logitech |

## 3. Comparación de escenarios

| Escenario | Composición | Total estimado |
|---|---|---:|
| Mínimo local | 2 × Elgato + TFmini-S + 1 × A1M8 + montaje/cables | ~S/ 2.955 |
| **Recomendado local** | **2 × Elgato + 2 × TFmini Plus + 2 × A1M8 + montaje/cables** | **~S/ 3.916** |
| Con LIDAR-Lite | 2 × Elgato + 2 × TFmini Plus + 1 × A1M8 + LIDAR-Lite + montaje/cables | ~S/ 4.166 |
| Alternativa 3 LiDAR | Recomendado + 1 × A1M8 (tercero) | ~S/ 4.516 |

## 4. Condiciones

- Precios consultados el **2026-11-21**; pueden cambiar. La revisión de
  cantidades (2 LiDAR, 2 ToF) es del **2026-11-23**.
- Memory Kings: precio incluye IGV; flete no incluido.
- Electromanía: stock online mostrado en la ficha; verificar el día de compra.
  El LiDAR declaraba 12 unidades y el ToF 8: la compra de 2 + 2 entra, pero hay
  que confirmar reserva.
- Naylamp: envío gratis a todo el Perú por compras > S/ 200 (condiciones de la tienda).
- Importación: no incluye envío, aduana ni IGV.
- Los montajes y cables son **estimaciones** de planificación, no cotizaciones.

## 5. Referencias

- Investigación completa:
  [`../01-investigacion/sensores-peru-2026-11-21.md`](../01-investigacion/sensores-peru-2026-11-21.md).
- Fuentes: [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Preguntas: [`../00-gobierno/registro-decisiones.md`](../00-gobierno/registro-decisiones.md).
- Consolidado de compras de los tres subproyectos:
  [`../../../cotizaciones/bom-consolidado.md`](../../../cotizaciones/bom-consolidado.md).
