# Lista de materiales y presupuesto (Perú, PEN)

> Estado: Estimado · Versión: 0.3 · Revisión: 2026-11-23 · Responsable: rol de Hardware
>
> **Precios en soles peruanos (PEN) con IGV**, consultados el 2026-11-21 y
> revisados el 2026-11-23 en catálogos públicos. No incluyen envío; se añade
> **5 % de imprevistos**. El stock no está reservado y debe cotizarse antes de
> comprar.
>
> **Base de cómputo (ADR-0010):** Raspberry Pi 4 Model B de 8 GB + Argon ONE,
> arranque por **microSD A2** y pack Li-ion **2S4P** de 8 celdas. La Pi 4 y la
> carcasa se reutilizan del inventario de facultad; si se compran, hay que
> cotizarlas aparte.
>
> **Cambios del 2026-11-23:** salen la LiFePO4 Goldenmate y su cargador de red,
> el SSD USB, el perfil V-Slot 2040 y las ruedas/placas encargadas; entran el
> pack 2S4P, el cargador solar TP5100-84, el boost de 400 W, el ToF TFmini Plus
> y la webcam Brio 4K. El detalle está en el bloque “Cambios del 2026-11-23” de
> [`bom-peru.md`](bom-peru.md).
>
> **Proveedores y enlaces:** el detalle está en [`bom-peru.md`](bom-peru.md) y
> [`bom-peru.csv`](bom-peru.csv), que es la fuente única de verdad de las filas.
> La ruta vigente se resume en la sección 5.1 de [`bom-peru.md`](bom-peru.md).
>
> **Propuesta de interfaz (ADR-0008):** el ESP32-S3 para PWM, encoders, IMU,
> batería y expansión I²C **no está incluido** en esta BOM y queda como
> **opcional**. Su add-on y costes están en [`bom-peru.md`](bom-peru.md),
> sección 4.6.
>
> **Pack 3S2P/3S3P (opcional):** alternativas al pack 2S4P, no la ruta base; se
> comparan en [`bom-peru.md`](bom-peru.md), sección 4.7.
>
> **Variante 6×6 (estudio paralelo):** tiene BOM separada en
> [`energia/bom-6x6.md`](energia/bom-6x6.md), todavía en EUR y pendiente de
> OQ-09. **No mezclar ambas BOM ni comprar hardware de la variante.**
>
> **Spike de percepción 3D (histórico, ADR-0009 obsoleto):** el montaje de
> 2 × Camera Module 3 no es ejecutable en la Pi 4 (un solo CSI). La BOM base
> lleva una **webcam USB Brio 4K**; la alternativa con Camera V2.1 + USB se
> evalúa en
> [`../03-arquitectura/adr/0011-estereo-csi-usb.md`](../03-arquitectura/adr/0011-estereo-csi-usb.md).
>
> **Inventario de facultad:** la Pi 4 y la carcasa Argon se declaran a coste 0
> por reutilización, igual que el perfil V-Slot 2040 y los paneles solares. El
> resto del material (TB6612, IMU, ToF, cámara, LiPo) **no se descuenta** hasta
> que se apruebe su uso concreto; el análisis está en
> [`inventario-facultad.md`](inventario-facultad.md).

## 1. Escenario recomendado (PEN)

### 1.1 Tabla de las 28 filas

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. (S/) | Total (S/) | Proveedor / nota |
|---|---|---|---|---:|---:|---|
| 1 | Cómputo | Raspberry Pi 4 Model B 8 GB | Placa oficial | 1 | 0,00 | 0,00 | Inventario de facultad; si se compra, cotizar |
| 2 | Cómputo | Carcasa Argon ONE V2 | Con ventilador | 1 | 0,00 | 0,00 | Inventario; verificar acceso al CSI |
| 3 | Almacenamiento | microSD 64 GB A2 | SanDisk Extreme Pro | 1 | 64,90 | 64,90 | Falabella; arranque del sistema (sin HAT M.2) |
| 4 | Percepción | LiDAR 2D 360° | RPLIDAR A1M8-R6 12 m | 1 | 600,00 | 600,00 | Electromanía; 12 m, 10 Hz |
| 5 | Percepción | ToF de piso | TFmini Plus 12 m, UART/I²C, IP65 | 1 | 330,00 | 330,00 | Electromanía; quedaban 8 |
| 6 | Percepción | Webcam USB 4K | Logitech Brio 4K Ultra HD Pro | 1 | 487,00 | 487,00 | Memory Kings; la Pi 4 tiene un solo CSI |
| 7 | Percepción | IMU 9-DOF | BNO085 | 1 | 100,00 | 100,00 | Electronics Peru (Ica) |
| 8 | Percepción | Monitor de batería | INA219 I²C | 1 | 12,50 | 12,50 | Electromanía |
| 9 | Tracción | Motorreductor 12 V con encoder | FIT0185 83 rpm 45 kg·cm | 2 | 145,00 | 290,00 | Electromanía; 7 A de bloqueo por motor |
| 10 | Tracción | Driver | BTS7960 43 A | 2 | 45,00 | 90,00 | Naylamp; un módulo por motor |
| 11 | Energía | Celda Li-ion 18650 | EVE INR18650/35V 3500 mAh | 8 | 19,00 | 152,00 | Bracsan; pack 2S4P |
| 12 | Energía | BMS 2S | 25 A, 7,4/8,4 V | 1 | 18,00 (ref.) | 18,00 | Bracsan; confirmar SKU 2S |
| 13 | Energía | Plaquita de níquel | Tira de 1 m | 1 | 5,00 | 5,00 | Bracsan |
| 14 | Energía | Espaciadores | 3×1 para 18650 | 4 | 0,60 | 2,40 | Bracsan; arreglo 2×4 |
| 15 | Energía | Conector | XT60 macho/hembra | 1 | 4,50 | 4,50 | Bracsan |
| 16 | Energía | Arnés del pack | Cable, termorretráctil, fusible 20–25 A | 1 | 20,00 (est.) | 20,00 | Bracsan / varios; fusible a recalcular |
| 17 | Energía | Cargador solar | TP5100-84, 4,2/8,4 V, 2 A | 1 | 5,60 | 5,60 | Hifisac; desde 2 paneles de 6 V en serie |
| 18 | Energía | Boost de tracción | Step-up 400 W, 15 A, 7,4 → 12 V | 1 | 55,00 (est.) | 55,00 | MTLAB; solo riel de motores |
| 19 | Energía | DC-DC 5 V 5 A | XL4005 5 A | 1 | 6,59 | 6,59 | Electromanía; derratear y medir rizado |
| 20 | Energía | DC-DC 5 V 3 A | XL4005 5 A | 1 | 6,59 | 6,59 | Electromanía; segundo módulo |
| 21 | Energía | Portafusibles | Línea mini cuchilla 12 A | 1 | 15,90 (ref.) | 15,90 | Bracsan; precio de referencia de Falabella |
| 22 | Energía | Fusibles | Surtido de vidrio 250 V | 1 | 12,00 | 12,00 | Electromanía; para banco |
| 23 | Energía | Parada de emergencia | Seta enclavada 660 V 10 A | 1 | 8,00 | 8,00 | Electromanía; 10 A, ver riesgo |
| 24 | Energía | Interruptor general | Desconectador 12–48 V | 1 | 46,90 | 46,90 | Falabella; corte de potencia del pack |
| 25 | Cableado | Cable y conectores | XT60/XT30 14–18 AWG | 1 | 80,00 (est.) | 80,00 | Naylamp / Electromanía; incluye termorretráctil |
| 26 | Tornillería | Tornillos y tuercas | M3/M4 + tuercas en T | 1 | 50,00 (est.) | 50,00 | Naylamp / ferretería |
| 27 | Varios | Accesorios de caja | Ventilador, rejilla, espuma | 1 | 30,00 (est.) | 30,00 | The Pi Box / ferretería |
| 28 | Repuestos | Fusibles, cable, conectores | Reposición | 1 | 50,00 (est.) | 50,00 | Varios; crítico para la demo |
| | | | | | **Subtotal** | **2.542,88** | |
| | | | | | **Imprevistos / envío local (5 %)** | **127,14** | |
| | | | | | **Total estimado** | **2.670,02** | |

### 1.2 Resumen por categoría

| Categoría | Subtotal (S/) |
|---|---:|
| Cómputo (inventario) | 0,00 |
| Almacenamiento | 64,90 |
| Percepción | 1.529,50 |
| Tracción | 380,00 |
| Energía y protección | 358,48 |
| Cableado | 80,00 |
| Tornillería | 50,00 |
| Varios | 30,00 |
| Repuestos | 50,00 |
| **Subtotal** | **2.542,88** |
| Imprevistos / envío local (5 %) | **127,14** |
| **Total estimado** | **2.670,02** |

> **Revisión 2026-11-23 (pack 2S4P + microSD + precios Perú):** el total vigente
> es **S/ 2.670,02** (subtotal S/ 2.542,88 + 5 %). La Pi 4 y la Argon están a
> S/ 0 porque se reutilizan; el perfil V-Slot 2040 también se reutiliza y las
> ruedas y placas se imprimen en local, así que no suman. El total queda
> **pendiente de aprobación formal del PO y del responsable de Hardware**; no se
> autoriza compra.

### 1.3 Escenario “compra todo” (sin reutilizar el cómputo)

Si en lugar de reutilizar la Pi 4 y la Argon se compra el cómputo, se sustituyen
por **Pi 5 8 GB (S/ 768) + Active Cooler (S/ 29,90)**:

| Concepto | Importe (S/) |
|---|---:|
| Subtotal de la tabla 1.1 | 2.542,88 |
| Pi 5 8 GB | +768,00 |
| Active Cooler | +29,90 |
| **Subtotal compra todo** | **3.340,78** |
| Imprevistos (5 %) | **167,04** |
| **Total compra todo** | **3.507,82** |

> Este escenario no incluye HAT M.2 ni SSD: aunque se compre la Pi 5, la BOM
> mantiene el arranque por microSD. No está aprobado; sirve para presupuestar la
> reposición completa del cómputo.

## 2. Escenario mínimo (PEN)

Recortes posibles, no aprobados. Todos son sustituciones por material del
inventario o menos unidades, nunca recortes de seguridad (e-stop, fusible, BMS
ni carcasa del pack):

| Cambio | Ahorro estimado | Riesgo |
|---|---:|---|
| Sin webcam Brio 4K (usar la Camera V2.1 del inventario) | −487,00 | Visión de 8 MP y sin 4K; un solo CSI; sirve para teleoperación, no para estéreo |
| Sin ToF TFmini Plus (usar el VL53L0/1XV2 del inventario) | −330,00 | Alcance de 2–4 m según la variante del inventario; no detecta desniveles lejanos |
| Sin IMU BNO085 (usar el MPU-6050 del inventario) | −100,00 | Odometría menos robusta; más calibración |
| Sin boost de tracción | −55,00 | El rover baja a ~51 rpm y ~0,24 m/s |
| Pack 2S3P (6 celdas) en lugar de 2S4P | −38,00 | Menos autonomía; el BMS 2S y el TP5100-84 sirven igual |
| Sin línea de repuestos | −50,00 | Sin repuesto de fusibles ni cable; riesgo alto en demo |
| **Subtotal mínimo** | **1.482,88** | |
| Imprevistos (5 %) | **74,14** | |
| **Total mínimo aproximado** | **1.557,02** | Mayor riesgo; no aprobado |

> Estimación indicativa sobre la ruta Perú. No sustituye una cotización ni una
> decisión de compra. El pack 2S3P se arma con las mismas 6 celdas del 3S2P,
> pero con BMS 2S y el TP5100-84.

## 3. Escenario ampliado (PEN)

| Añadido | Coste estimado | Beneficio |
|---|---:|---|
| Cámara RGB-D | S/ 650–1.300 | Percepción 3D |
| GNSS RTK | S/ 650–1.700 | Navegación exterior |
| Segundo LiDAR | S/ 600 | Redundancia |
| Jetson Orin Nano | S/ 1.100 | Visión/IA |
| **Total ampliado** | **+S/ 3.000–4.700** | Futuro |

> Precios de referencia; cotizar en Perú antes de cualquier compra. La webcam
> Brio 4K ya está en el escenario recomendado, así que el “añadido” de cámara
> es solo para profundidad o visión estéreo aproximada.

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
>
> **Soldador de punto (opcional):** el pack 2S4P se arma con nickel soldado por
> puntos. El portátil de Bracsan cuesta S/ 390 y **no está incluido** en los
> S/ 720; si no se tiene, conviene pagar el armado a un taller. **No soldar
> celdas 18650 con cautín.**

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
| 1 | Electromanía: LiDAR A1M8, ToF TFmini Plus, 2 × FIT0185, INA219, 2 × XL4005, fusibles y e-stop | Semana 1–2 |
| 2 | Bracsan: 8 celdas, BMS 2S, níquel, espaciadores, XT60, arnés y portafusibles | Semana 2 |
| 3 | Naylamp: 2 × BTS7960, cable/conectores y tornillería | Semana 2–3 |
| 4 | Falabella: microSD A2 y desconectador; Memory Kings: webcam Brio 4K | Semana 3 |
| 5 | Electronics Peru (BNO085), Hifisac (TP5100-84) y MTLAB (boost) | Semana 3–4 |
| 6 | Impresión local de chasis, ruedas y placas; repuestos y microSD clonada | Semana 4–5 |

> El cómputo (Pi 4 + Argon) y el perfil V-Slot 2040 ya están en el inventario:
> no se compran. Confirmar stock y precio final antes de cada pedido.

## 7. Riesgos de suministro

- LiDAR y motores: pedir con 4–6 semanas de margen; el stock cambia (quedaban 12
  LiDAR y 30 motores a la fecha de la consulta).
- ToF TFmini Plus: quedaban 8 unidades; es el sensor que puede agotarse primero.
- Webcam Brio 4K: Memory Kings la lista en un listado de categoría, no en una
  ficha; confirmar SKU y oferta antes de pagar.
- Celdas 18650 y pack armado: restricciones de transporte de litio; el pack
  armado no hereda automáticamente la certificación de la celda. Carga
  supervisada y fuera del rover.
- BMS 2S: Bracsan publica el módulo de 3S; confirmar SKU 2S de 25 A y balanceo.
- Cargador TP5100-84: Hifisac vende por WhatsApp y sus fichas marcan “sin
  existencias”; confirmar stock.
- Boost de 400 W: solo Lima/Callao por MTLAB y con precio a cotizar.
- Portafusibles: el precio es de referencia (Falabella) y el calibre declarado
  (12 A) es menor que el fusible recalculado (20–25 A); comprar uno adecuado.
- microSD: es el único medio de arranque; comprar una segunda tarjeta clonada.
- Drivers BTS7960: confirmar stock y lógica 3,3 V.
- Aduanas: presupuestar 10–20 % adicional si se importa.
- Precios: el tipo de cambio y el IGV pueden cambiar; esta BOM es una fotografía
  al 2026-11-23.

## 8. Control de cambios

Cualquier cambio de BOM debe:

1. Registrarse en este documento.
2. Actualizar el presupuesto en PEN y la fila correspondiente en
   [`bom-peru.csv`](bom-peru.csv), que es la fuente única de verdad.
3. Revisar el impacto en el diseño eléctrico/mecánico y, si cambia la energía,
   en [`diseno-electrico.md`](diseno-electrico.md).
4. Aprobarse por el PO y el HW.

## 9. Spike de percepción 3D (histórico, ADR-0009 obsoleto)

El [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md) preveía
2 × Camera Module 3 + ToF sobre una Pi 5. La Pi 4 tiene **un solo CSI**, así que
ese montaje **no es ejecutable** y no se compra. Desde el 2026-11-23 la BOM base
lleva una **webcam USB Logitech Brio 4K** (fila 6), que resuelve la visión de
color y la teleoperación, no la profundidad estéreo. La alternativa con Camera
V2.1 + USB sigue evaluándose en
[ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md); no sustituye al
LiDAR ni al ToF y no se usa para seguridad. La tabla histórica de esa BOM está
en el ADR-0009 y no se incluye en el total.

## 10. Historial de rutas y precios

> Sección **histórica** de control. La ruta vigente es la de la sección 1; las
> cifras anteriores se conservan solo para comparar y **no deben citarse como
> presupuesto actual**.

| Concepto | Pi 5 — histórica (2026-11-21) | Pi 4 + SSD + LiFePO4 — histórica (2026-11-21) | Pi 4 + microSD + 2S4P — vigente (2026-11-23) |
|---|---:|---:|---:|
| Subtotal | 3.317,98 | 2.520,08 | 2.542,88 |
| Imprevistos / envío (5 %) | 165,90 | 126,00 | 127,14 |
| **Total** | **3.483,88** | **2.646,08** | **2.670,02** |

| Versión | Fecha | Ruta | Subtotal (S/) | Total (S/) | Nota |
|---|---|---|---:|---:|---|
| 0.1 | 2026-11-21 | BOM en EUR (671 EUR) | — | — | Primera estimación, moneda distinta; histórica |
| 0.2 | 2026-11-21 | Pi 4 + SSD USB + LiFePO4 10 Ah | 2.520,08 | 2.646,08 | Revisión de ADR-0010; hoy histórica |
| 0.3 | 2026-11-23 | Pi 4 + microSD + pack 2S4P | 2.542,88 | 2.670,02 | **Vigente**, sincronizada con `bom-peru.csv` |

> **El importe vigente es S/ 2.670,02.** Los importes S/ 2.646,08 y
> S/ 3.483,88 son históricos: el primero correspondía a la BOM con LiFePO4 y SSD
> USB, y el segundo a la ruta con Pi 5. El alza de S/ 22,80 frente a S/ 2.646,08
> se explica por el ToF, la webcam, el boost y el pack 2S4P, compensada por la
> salida de la batería LiFePO4, su cargador de red, el SSD, el perfil V-Slot, las
> ruedas, las placas y la fuente de 27 W.
>
> Si la Pi 4 o la Argon se compran, el total sube: el escenario “compra todo”
> con Pi 5 está en [`bom-peru.md`](bom-peru.md), sección 5.2 (S/ 3.507,82).

## 11. Enlaces

- Cotización detallada en Perú: [`bom-peru.md`](bom-peru.md).
- Datos de la cotización (fuente única de verdad): [`bom-peru.csv`](bom-peru.csv).
- Add-ons opcionales (ESP32 y pack 3S): [`bom-peru-addons.csv`](bom-peru-addons.csv).
- Inventario de facultad: [`inventario-facultad.md`](inventario-facultad.md).
- Diseño eléctrico: [`diseno-electrico.md`](diseno-electrico.md).
- ADR-0010 (Pi 4): [`../03-arquitectura/adr/0010-raspberry-pi-4.md`](../03-arquitectura/adr/0010-raspberry-pi-4.md).
- ADR-0011 (cámara CSI + USB): [`../03-arquitectura/adr/0011-estereo-csi-usb.md`](../03-arquitectura/adr/0011-estereo-csi-usb.md).
- ADR-0012 (LTE/GNSS): [`../03-arquitectura/adr/0012-lilygo-lte-gnss.md`](../03-arquitectura/adr/0012-lilygo-lte-gnss.md).
- Variante 6×6: [`energia/bom-6x6.md`](energia/bom-6x6.md).
