# BOM de la variante 6×6 (estudio)

> Estado: Estudio · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Diseño electrónico
> **No comprar esta BOM.** Es una variante que requiere resolver OQ-09 y aprobar un ADR de energía. La BOM vigente del mini demo es [`../bom.md`](../bom.md).
>
> **Nota ADR-0010 (2026-11-21):** la línea de Pi 5 8 GB queda sustituida por la
> Pi 4 8 GB disponible en facultad. Si se adopta la variante 6×6, recalcular
> consumo, BOM y compatibilidad; OQ-09 sigue abierta. La BOM se mantiene en EUR
> como estudio; si se adopta, se cotiza en PEN con proveedores peruanos.
>
> **Inventario de facultad:** hay 6 motoreductores **sin encoder**, 3 × TB6612,
> PCA9685 y 6 × MG90S. Los MG90S no bastan para la dirección (F-003) y los
> motores no tienen encoder; los paneles declarados son de 6 V/720 mA, no de
> 7,2 V/600 mA. Análisis completo en
> [`../inventario-facultad.md`](../inventario-facultad.md). **No se descuenta del
> total ni se autoriza compra.**

## 1. Relación con los otros documentos

Esta lista materializa la variante descrita en:

- [`calculo-energetico.md`](calculo-energetico.md) — consumo, batería, solar y par de dirección.
- [`diseno-electrico-6x6.md`](diseno-electrico-6x6.md) — arquitectura eléctrica, protecciones y buses.

No mezclar con la BOM base. Algunos componentes (Raspberry Pi, LiDAR, cámara,
NVMe) son compartibles si se reutilizan, pero la arquitectura de potencia,
tracción y dirección es distinta.

## 2. BOM

> Precios orientativos en EUR a 2026-11-21, sin IVA, envío ni aduanas. Cotizar
> con al menos dos proveedores antes de comprar.

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. | Total | Nota |
|---|---|---|---|---:|---:|---:|---|
| 1 | Cómputo | Raspberry Pi 5 8 GB | — | 1 | 90 | 90 | Compartible con la base |
| 2 | Cómputo | HAT NVMe | — | 1 | 35 | 35 | Compartible |
| 3 | Cómputo | SSD NVMe 128 GB | — | 1 | 25 | 25 | Compartible |
| 4 | Cómputo | Refrigeración activa | Oficial o equivalente | 1 | 10 | 10 | — |
| 5 | Cómputo | Cámara | Camera Module 3 | 1 | 30 | 30 | Opcional |
| 6 | Percepción | LiDAR 2D | RPLIDAR A1M8 / LD19 | 1 | 100 | 100 | Compartible |
| 7 | Cómputo | microSD 64 GB A2 | — | 1 | 12 | 12 | Respaldo |
| 8 | Energía | Celdas 18650 3,6 V 3500 mAh | Descarga ≥10 A | 8 | 6 | 48 | 2S4P |
| 9 | Energía | BMS 2S 30 A | Pico ≥40 A, carga ≥5 A, puerto común | 1 | 25 | 25 | Con temperatura |
| 10 | Energía | MPPT 2S | 8,4 V / ≥2 A | 1 | 30 | 30 | Para 4 paneles |
| 11 | Energía | DC-DC 5,1 V 5 A | — | 1 | 15 | 15 | Pi 5 |
| 12 | Energía | BEC 6 V 20 A | — | 1 | 25 | 25 | Servos |
| 13 | Energía | INA226 | Shunt 0,002 Ω | 1 | 8 | 8 | I²C 0x40 |
| 14 | Energía | Fusible 30 A + portafusible | Curva lenta | 1 | 10 | 10 | Principal |
| 15 | Energía | Fusibles 5 A / 20 A | Surtido | 1 | 10 | 10 | Pi y servos |
| 16 | Energía | Interruptor general | 30 A, bipolar | 1 | 10 | 10 | — |
| 17 | Energía | E-stop NC 2 polos | Enclavado | 1 | 15 | 15 | Corta actuadores |
| 18 | Energía | Resistencia de precarga | 100 Ω / 5 W | 1 | 5 | 5 | Condensadores |
| 19 | Cableado | Cable 14/16/18 AWG, XT60/XT30, terminales | — | 1 | 40 | 40 | — |
| 20 | Tracción | Motorreductor 25D LP 6 V 99:1 | Pololu 4827 u homólogo | 6 | 30 | 180 | Con encoder |
| 21 | Tracción | Driver doble TB6612FNG | Opción A | 3 | 8 | 24 | 18 GPIO |
| 22 | Tracción | Driver DRV8871 | Opción B (alternativa a #21) | 6 | 8 | 48 | Menos GPIO |
| 23 | Tracción | Ruedas 120 mm | Goma/TPU | 6 | 8 | 48 | Radio 60 mm |
| 24 | Dirección | Servo MG996R o 20 kg·cm | Clase ≥10 kg·cm | 6 | 15 | 90 | MG90S no basta |
| 25 | Dirección | Servo saver | — | 6 | 5 | 30 | Protección |
| 26 | Dirección | PCA9685 | 16 canales, I²C | 1 | 8 | 8 | Dirección 0x41 |
| 27 | Control | MCU de tracción | Teensy 4.1 o RP2040 | 1 | 30 | 30 | 6 PWM + encoders |
| 28 | Chasis | Chasis 6 ruedas | Aluminio o impresión reforzada | 1 | 100 | 100 | Diseño propio |
| 29 | Chasis | Rodamientos y tornillería | — | 1 | 30 | 30 | — |
| 30 | Montaje | Soporte de cámara/LiDAR | Impresión 3D | 1 | 5 | 5 | — |
| 31 | Repuestos | Fusibles, cable, conectores | — | 1 | 40 | 40 | Crítico |
| | | | | | **Subtotal** | **1.128** | |
| | | | | | **Envío estimado (10%)** | **113** | |
| | | | | | **Total estimado** | **1.241** | |

> Si se elige la opción B de drivers (#22) en lugar de #21, el total sube ~24 EUR.
> Si se reutilizan Pi, NVMe, LiDAR y cámara de la base, se descuentan ~290 EUR.
>
> **Celdas:** esta BOM usa 8 celdas (2S4P, 100,8 Wh). Si se baja a 2S2P,
> restar 24 EUR y recalcular autonomía y masa. Para 2S8P (16 celdas) el
> cargador de 2 A no es suficiente; haría falta uno de 5–10 A. Nada de esto
> está incluido en el total.

## 3. Comparación con la base

| Elemento | Base mini demo | Variante 6×6 |
|---|---|---|
| Tracción | 2 motores | 6 motores |
| Dirección | Diferencial | 6 servos independientes |
| Batería | LiFePO4 12,8 V 6 Ah | Li-ion 2S4P 7,2 V 14 Ah |
| Solar | No | 4 paneles + MPPT |
| Drivers | 1 doble | 3 dobles o 6 simples |
| Control | Pi + driver | Pi + MCU de tiempo real |
| BOM estimada | ~775 EUR | ~1.241 EUR |

## 4. Componentes que no incluye

- Herramientas (multímetro, soldador, crimpadora, fuente).
- Paneles solares (se asumen 4 × 7,2 V / 600 mA ya disponibles según F-008).
- Cargador externo 8,4 V / 5 A.
- Extintor, arena y elementos de seguridad de pista.
- Piezas de repuesto específicas de chasis.

## 5. Decisiones pendientes

1. **OQ-09:** elegir arquitectura antes de comprar.
2. **ADR de energía** si se adopta la variante.
3. Motor definitivo y curva I-V.
4. Servo definitivo y corriente de bloqueo real.
5. Driver: TB6612 (más GPIO) vs DRV8871 (menos GPIO, más unidades).
6. MCU: Teensy 4.1 vs RP2040.
7. Masa, radio de rueda y `scrub radius` reales.

## 6. Enlaces

- Cálculo energético: [`calculo-energetico.md`](calculo-energetico.md).
- Diseño eléctrico: [`diseno-electrico-6x6.md`](diseno-electrico-6x6.md).
- BOM base: [`../bom.md`](../bom.md).
- OQ-09: [`../../00-gobierno/registro-decisiones.md`](../../00-gobierno/registro-decisiones.md).
- Fuentes: [`../../01-investigacion/fuentes.md`](../../01-investigacion/fuentes.md).
