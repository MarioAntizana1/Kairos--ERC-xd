# Lista de materiales y presupuesto (Perú, PEN)

> Estado: Estimado · Versión: 0.2 · Revisión: 2026-11-21 · Responsable: rol de Hardware
>
> **Precios en soles peruanos (PEN) con IGV**, consultados el 2026-11-21 en
> catálogos públicos. No incluyen envío; se añade **5 % de imprevistos**.
> El stock no está reservado y debe cotizarse antes de comprar.
>
> **Base de cómputo (ADR-0010):** Raspberry Pi 4 Model B de 8 GB + Argon ONE,
> SSD USB 3.0 y fuente de 5 V. La Pi 4 y la carcasa se reutilizan del inventario
> de facultad; si se compran, hay que cotizarlas aparte.
>
> **Proveedores y enlaces:** el detalle está en
> [`bom-peru.md`](bom-peru.md) y [`bom-peru.csv`](bom-peru.csv). La ruta vigente
> se resume en la sección 5.3 de `bom-peru.md`.
>
> **Propuesta de interfaz (ADR-0008):** el ESP32-S3 para PWM, encoders, IMU,
> batería y expansión I²C **no está incluido** en esta BOM. Su add-on y costes
> están en [`bom-peru.md`](bom-peru.md), sección 4.6.
>
> **Variante 6×6 (estudio paralelo):** tiene BOM separada en
> [`energia/bom-6x6.md`](energia/bom-6x6.md), todavía en EUR y pendiente de
> OQ-09. **No mezclar ambas BOM ni comprar hardware de la variante.**
>
> **Spike de percepción 3D (ADR-0009, obsoleto):** el montaje de 2 × Camera
> Module 3 no es ejecutable en la Pi 4 (un solo CSI). La alternativa con Camera
> V2.1 + USB se evalúa en
> [`../03-arquitectura/adr/0011-estereo-csi-usb.md`](../03-arquitectura/adr/0011-estereo-csi-usb.md).
>
> **Inventario de facultad:** la Pi 4 y la carcasa Argon se declaran a coste 0
> por reutilización. El resto del material (TB6612, IMU, ToF, cámara, LiPo y
> paneles) **no se descuenta** hasta que se apruebe su uso concreto; el análisis
> está en [`inventario-facultad.md`](inventario-facultad.md).

## 1. Escenario recomendado (PEN)

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. (S/) | Total (S/) | Proveedor / nota |
|---|---|---|---|---|---:|---:|---|
| 1 | Cómputo | Raspberry Pi 4 Model B 8 GB | — | 1 | 0,00 | 0,00 | Inventario de facultad; si se compra, cotizar |
| 2 | Cómputo | SSD SATA 2.5" 256 GB + caja USB 3.0 | ADATA SU650 + caja | 1 | 210,70 | 210,70 | Falabella; **sin HAT M.2** (la Pi 4 no tiene PCIe). Alternativa: SSD M.2 + caja USB compatible |
| 3 | Cómputo | Carcasa Argon ONE V2 con ventilador | — | 1 | 0,00 | 0,00 | Inventario; si se compra, cotizar. Verificar CSI |
| 4 | Cómputo | microSD 64 GB A2 | SanDisk Extreme Pro | 1 | 64,90 | 64,90 | Falabella; respaldo |
| 5 | Cómputo | Fuente 27 W USB-C (5,1 V 5 A) | Oficial Raspberry Pi | 1 | 67,00 | 67,00 | The Pi Box; banco. Alternativa 5 V/3 A |
| 6 | Sensor | LiDAR 2D 360° | RPLIDAR A1M8-R6 12 m | 1 | 600,00 | 600,00 | Electromanía; 12 m, 10 Hz |
| 7 | Sensor | IMU 9-DOF | BNO085 | 1 | 100,00 | 100,00 | Electronics Peru (Ica) |
| 8 | Sensor | Monitor de batería | INA219 I²C | 1 | 12,50 | 12,50 | Electromanía |
| 9 | Tracción | Motorreductor 12 V con encoder | FIT0185 83 rpm 45 kg·cm | 2 | 145,00 | 290,00 | Electromanía; sustituto del 50 rpm; 7 A de bloqueo |
| 10 | Tracción | Driver puente H | BTS7960 43 A | 2 | 45,00 | 90,00 | Naylamp; 2 módulos sustituyen al MDD10A |
| 11 | Tracción | Ruedas 90 mm | Buje PETG + banda TPU | 4 | 25,00 | 100,00 | Print3D/taller; estimado |
| 12 | Chasis | Perfil V-Slot 2040, 3,2 m | — | 1 | 160,00 | 160,00 | Naylamp; el 2020 está agotado |
| 13 | Chasis | Placas PETG/aluminio | Corte o impresión 3D | 1 | 80,00 | 80,00 | Print3D/taller; estimado |
| 14 | Energía | Batería LiFePO4 12 V 10 Ah | Goldenmate BMS IP67 | 1 | 239,00 | 239,00 | Falabella; importada; BMS 10 A |
| 15 | Energía | Cargador LiFePO4 14,6 V | LVYUAN o equivalente | 1 | 200,00 | 200,00 | Estimado; el de 20 A cuesta S/ 359 |
| 16 | Energía | DC-DC 5 V 5 A | XL4005 5 A | 1 | 6,59 | 6,59 | Electromanía; derratear y medir rizado |
| 17 | Energía | DC-DC 5 V 3 A | XL4005 5 A | 1 | 6,59 | 6,59 | Electromanía; segundo módulo |
| 18 | Energía | Portafusibles | Línea mini cuchilla 12 A | 1 | 15,90 | 15,90 | Falabella |
| 19 | Energía | Fusibles | Surtido 250 V | 1 | 12,00 | 12,00 | Electromanía; para banco |
| 20 | Energía | E-stop seta NC | 660 V 10 A | 1 | 8,00 | 8,00 | Electromanía |
| 21 | Energía | Interruptor general | Desconectador 12–48 V | 1 | 46,90 | 46,90 | Falabella |
| 22 | Cableado | Cable y conectores | XT60/XT30 14–18 AWG | 1 | 80,00 | 80,00 | Naylamp/Electromanía; estimado |
| 23 | Tornillería | Tornillos y tuercas | M3/M4 y tuercas en T | 1 | 50,00 | 50,00 | Naylamp/ferretería; estimado |
| 24 | Varios | Ventilador, rejilla, espuma | Accesorios de caja | 1 | 30,00 | 30,00 | The Pi Box/ferretería; estimado |
| 25 | Repuestos | Fusibles, cable, conectores | Reposición | 1 | 50,00 | 50,00 | Varios; crítico para la demo |
| | | | | | **Subtotal** | **2.520,08** | |
| | | | | | **Imprevistos / envío local (5 %)** | **126,00** | |
| | | | | | **Total estimado** | **2.646,08** | |

> **Revisión 2026-11-21 (ADR-0010 + precios Perú):** el total vigente es
> **S/ 2.646,08** (subtotal S/ 2.520,08 + 5 %). Incluye cargador de batería, que
> la BOM anterior no listaba. La Pi 4 y la Argon están a S/ 0 porque se
> reutilizan; si se compran, sumar su precio de mercado. El total queda
> **pendiente de aprobación formal del PO y del responsable de Hardware**; no se
> autoriza compra.

## 2. Escenario mínimo (PEN)

Recortes posibles, no aprobados:

| Cambio | Ahorro estimado | Riesgo |
|---|---:|---|
| Pi 4 4 GB en lugar de 8 GB | S/ 0 (si está disponible) | RAM justa para Nav2; no recomendado |
| microSD en lugar de SSD USB | −S/ 210,70 | Corrupción y lentitud; solo banco |
| LiDAR LD19 en lugar de A1M8 | −S/ 200,00 | Menos soporte y validación |
| Chasis impreso 100 % PETG | −S/ 100,00 | Menos rigidez |
| Sin IMU BNO085 | −S/ 100,00 | Odometría menos robusta; se puede usar el MPU-6050 del inventario |
| **Total mínimo aproximado** | **~S/ 1.900–2.100 + 5 %** | Mayor riesgo; no aprobado |

> Estimación indicativa sobre la ruta Perú. No sustituye una cotización ni una
> decisión de compra.

## 3. Escenario ampliado (PEN)

| Añadido | Coste estimado | Beneficio |
|---|---:|---|
| Cámara RGB-D | S/ 650–1.300 | Percepción 3D |
| GNSS RTK | S/ 650–1.700 | Navegación exterior |
| Segundo LiDAR | S/ 600 | Redundancia |
| Jetson Orin Nano | S/ 1.100 | Visión/IA |
| **Total ampliado** | **+S/ 3.000–4.700** | Futuro |

> Precios de referencia; cotizar en Perú antes de cualquier compra.

## 4. Herramientas (PEN)

Si el equipo no las tiene, añadir:

| Herramienta | Coste estimado |
|---|---:|
| Multímetro | S/ 100 |
| Soldador + estaño | S/ 130 |
| Crimpadora | S/ 100 |
| Destornilladores y llaves | S/ 130 |
| Fuente de laboratorio | S/ 260 |
| **Total** | **S/ 720** |

> Muchas universidades tienen taller; comprobar antes de comprar.

## 5. Licencias y software

| Elemento | Coste | Nota |
|---|---:|---|
| Ubuntu 24.04 | 0 | Open source |
| ROS 2 Jazzy | 0 | Apache-2.0 |
| Nav2 | 0 | Apache-2.0 |
| Gazebo Harmonic | 0 | Apache-2.0 |
| FreeCAD / KiCad | 0 | Open source |
| SOLIDWORKS | 0 (licencia ERC) | Solo finalistas |

## 6. Plan de compra

| Prioridad | Componentes | Cuándo |
|---|---|---|
| 1 | Pi 4 8 GB y Argon (reutilizadas), SSD USB, fuente | Semana 1 |
| 2 | LiDAR, IMU, drivers, motores | Semana 2–3 |
| 3 | Batería, cargador, DC-DC, fusibles, e-stop | Semana 3–4 |
| 4 | Chasis, ruedas, cableado | Semana 4–5 |
| 5 | Repuestos y herramientas | Semana 5 |

## 7. Riesgos de suministro

- LiDAR y motores: pedir con 4–6 semanas de margen; el stock cambia.
- Batería LiFePO4: restricciones de envío; comprar proveedor local o importar con plazo.
- Perfil V-Slot 2020: agotado; se usa 2040 (verificar cotas).
- Drivers BTS7960: confirmar stock y lógica 3.3 V.
- Aduanas: presupuestar 10–20 % adicional si se importa.
- Precios: el tipo de cambio y el IGV pueden cambiar; esta BOM es una fotografía a 2026-11-21.

## 8. Control de cambios

Cualquier cambio de BOM debe:

1. Registrarse en este documento.
2. Actualizar el presupuesto en PEN.
3. Revisar el impacto en el diseño eléctrico/mecánico.
4. Aprobarse por el PO y el HW.

## 9. Spike de percepción 3D (obsoleto)

El [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md) preveía
2 × Camera Module 3 + ToF sobre una Pi 5. La Pi 4 tiene **un solo CSI**, así que
ese montaje **no es ejecutable** y no se compra. La alternativa con la Camera
V2.1 + USB se evalúa en
[ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md); no sustituye al
LiDAR ni al ToF y no se usa para seguridad. La tabla histórica de esa BOM está
en el ADR-0009 y no se incluye en el total.

## 10. Revisión por ADR-0010 y precios Perú

| Concepto | Ruta Pi 5 (histórica) | Ruta Pi 4 (vigente) | Delta |
|---|---:|---:|---:|
| Subtotal | S/ 3.317,98 | S/ 2.520,08 | −S/ 797,90 |
| Imprevistos / envío (5 %) | S/ 165,90 | S/ 126,00 | −S/ 39,90 |
| **Total** | **S/ 3.483,88** | **S/ 2.646,08** | **−S/ 837,80** |

> La ruta histórica incluía Pi 5 8 GB (S/ 768) y Active Cooler (S/ 29,90). La
> ruta vigente usa la Pi 4 y la Argon del inventario a S/ 0, mantiene el SSD USB
> y añade cargador de batería. Si la Pi 4 o la Argon se compran, el total sube.
> La BOM en EUR anterior se conserva en el historial del proyecto; **la
> referencia de compra es esta tabla en PEN**.

## 11. Enlaces

- Cotización detallada en Perú: [`bom-peru.md`](bom-peru.md).
- Datos de la cotización: [`bom-peru.csv`](bom-peru.csv).
- Inventario de facultad: [`inventario-facultad.md`](inventario-facultad.md).
- ADR-0010 (Pi 4): [`../03-arquitectura/adr/0010-raspberry-pi-4.md`](../03-arquitectura/adr/0010-raspberry-pi-4.md).
- ADR-0011 (cámara CSI + USB): [`../03-arquitectura/adr/0011-estereo-csi-usb.md`](../03-arquitectura/adr/0011-estereo-csi-usb.md).
- ADR-0012 (LTE/GNSS): [`../03-arquitectura/adr/0012-lilygo-lte-gnss.md`](../03-arquitectura/adr/0012-lilygo-lte-gnss.md).
- Variante 6×6: [`energia/bom-6x6.md`](energia/bom-6x6.md).
