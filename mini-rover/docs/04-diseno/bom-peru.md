# BOM de electrónica cotizada en Perú (mini demo)

> Estado: Estudio de abastecimiento · Versión: 0.2 · Revisión: 2026-11-23 · Responsable: rol de Hardware
>
> **No autoriza compra.** Precios en soles peruanos (PEN) con IGV cuando la tienda
> lo indica, consultados el 2026-11-21 y revisados el 2026-11-23. No incluyen
> envío, embalaje, aduanas ni fluctuaciones. El stock es el que declaraba la
> tienda en línea en ese momento; no se reservó ningún artículo.
>
> **Fuente única de verdad:** [`bom-peru.csv`](bom-peru.csv), sincronizado el
> 2026-11-23. Si este documento y el CSV divergen, manda el CSV.
>
> Esta cotización cubre la **BOM base del mini demo** (2 motores, pack Li-ion
> **2S4P** de 8 celdas, 8,4 V de carga) de [`bom.md`](bom.md). **No** cotiza la
> variante 6×6 de [`energia/bom-6x6.md`](energia/bom-6x6.md), que sigue pendiente
> de OQ-09 y no debe comprarse.
>
> **Ruta vigente (ADR-0010):** Pi 4 8 GB + Argon ONE del inventario a coste 0 y
> arranque por **microSD**. La ruta vigente está resumida en 5.1 (**S/ 2.670,02**
> con 5 % de imprevistos). Las tablas históricas con Pi 5, SSD USB y LiFePO4 se
> conservan solo para comparar; **no comprar Pi 5, HAT M.2 ni SSD** por esta BOM.

## Cambios del 2026-11-23

1. **Fuera la LiFePO4 Goldenmate (S/ 239) y su cargador de red (S/ 200).** La
   energía pasa a un **pack Li-ion 2S4P** de 8 celdas: 4 en paralelo por rama,
   7,4 V nominales, 8,4 V de carga, 14 Ah, 103,6 Wh y BMS 2S de 25 A.
2. **Fuera el SSD SATA, la caja USB 3.0 y cualquier NVMe:** la Pi 4 no tiene HAT
   M.2. El arranque va por **microSD 64 GB A2**, que queda como único medio de
   almacenamiento de la BOM.
3. **Fuera el perfil V-Slot 2040** (ya se tenía) y las **ruedas y placas
   impresas**: se imprimen en local y no tienen costo de proveedor.
4. **Nuevos:** **ToF TFmini Plus** de 12 m, **webcam Logitech Brio 4K** (la Pi 4
   tiene una sola CSI, así que no hay par estéreo), **cargador TP5100-84** desde
   2 paneles de 6 V en serie y **boost step-up de 400 W** solo en el riel de
   tracción.
5. **Portafusibles a Bracsan** con precio de referencia de Falabella y **fusible
   recalculado a 20–25 A** por la corriente del pack de 2S.
6. Los add-ons **ESP32-S3** y **pack 3S2P/3S3P** quedan como **propuesta u
   opcional** y no entran en el subtotal. Subtotal **S/ 2.542,88**; total con
   5 % de imprevistos **S/ 2.670,02**.

## 1. Resumen ejecutivo

**Sí se puede comprar casi toda la electrónica en Perú.** Las brechas de esta
revisión son tres:

1. **Motorreductor de 50 rpm con encoder exacto:** no está en stock. Se usa el
   FIT0185 de 83 rpm con encoder y el boost de 12 V en el riel de tracción.
2. **Driver Cytron MDD10A:** no se encontró en tiendas peruanas. Se sustituye
   por dos BTS7960 de 43 A.
3. **BMS 2S de 25 A:** Bracsan publica el módulo de 3S; hay que confirmar el SKU
   de **2S** antes de pagar. El TP5100-84 de Hifisac y el step-up de MTLAB están
   en catálogo, con stock y precio a confirmar.

Ya no hay que buscar LiFePO4, cargador de red, SSD USB ni HAT M.2: salieron de
la BOM el 2026-11-23. Tampoco se necesita el perfil V-Slot 2040, las ruedas ni
las placas: están en el inventario o se imprimen en local.

La ruta vigente **100 % Perú con Pi 4** cuesta **S/ 2.670,02** (subtotal
S/ 2.542,88 + 5 % de imprevistos) e incluye el pack de energía, el cargador
solar, el boost de tracción, el ToF y la webcam. Si se compra todo el cómputo en
lugar de reutilizar (Pi 5 8 GB + Active Cooler), el total sube a **S/ 3.507,82**
(subtotal S/ 3.340,78). Los **add-ons propuestos** —ESP32-S3 como interfaz de
tiempo real y pack Li-ion 3S2P/3S3P— van aparte: ~S/ 195 y ~S/ 218/306,
respectivamente. El detalle verificable está en la sección 4 y en
[`bom-peru.csv`](bom-peru.csv).

**Recomendación:** el cómputo ya está disponible (Pi 4 8 GB + Argon ONE); no
comprar Pi 5. Comprar primero en Electromanía (LiDAR, ToF, motores, sensores,
e-stop), Bracsan (celdas, BMS, materiales del pack) y Naylamp (drivers,
conectores). Dejar para una segunda orden la webcam, el cargador solar y el
boost.

## 2. Método y alcance

- Búsqueda en tiendas peruanas con envío nacional, marketplaces y tiendas de
  provincia, además de canales de importación.
- Se contrastó precio, moneda, IVA declarado, disponibilidad y, cuando estaba
  publicado, ciudad de despacho.
- Se priorizó el **componente exacto o funcionalmente equivalente**, no el más
  barato a cualquier costo.
- No se hicieron compras, reservas ni consultas por WhatsApp. Los precios son
  los del catálogo web.
- Las filas de la BOM y su estado (`Verificado`, `Referencia`, `Estimado`,
  `Inventario`) se mantienen en [`bom-peru.csv`](bom-peru.csv); este documento
  es su versión narrativa y la numeración 1–28 coincide con el CSV.
- Seis filas son **estimaciones de planificación** (arnés del pack, boost,
  cableado, tornillería, accesorios de caja y repuestos) y dos son **precios de
  referencia** de otra tienda (BMS 2S y portafusibles); están marcadas como
  tales en la tabla.
- Los enlaces y las fechas de acceso de los proveedores originales están en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md), fuentes
  `F-19` a `F-38`. Las cuatro filas nuevas (TFmini Plus, Brio 4K, TP5100-84 y
  step-up de 400 W) llevan su URL en el CSV; **falta registrarlas como `F-xx`**
  en `fuentes.md`, que no se tocó en esta revisión.

> **Sobre el stock:** “En stock” significa que el catálogo lo declaraba así. En
> Memory Kings y Falabella, “sin stock en tienda” puede convivir con “despacho a
> domicilio” porque el vendedor es un marketplace. Confirmar antes de pagar.

## 3. Proveedores encontrados

| Proveedor | Ubicación | Cobertura | Especialidad | Envío | Enlace |
|---|---|---|---|---|---|
| **The Pi Box** | Lima (Chacarilla) | Todo el Perú | Raspberry Pi, HAT, accesorios, cajas | Olva Courier; tarifa en checkout; express solo Lima | <https://thepibox.pe/> |
| **Electromanía** | Lima | Todo el Perú | DFRobot, LiDAR, ToF, motores, sensores, drivers | Desde S/ 10; agencia o domicilio | <https://www.electromania.pe/> |
| **Naylamp Mechatronics** | Perú | Todo el Perú | Robótica, V-Slot, drivers, conectores, Raspberry Pi | Gratis desde S/ 200 | <https://naylampmechatronics.com/> |
| **Electronics Peru** | **Ica** | Nacional, a coordinar | Componentes, módulos, IMU | A coordinar con la tienda | <https://www.electronicsperu.com/> |
| **Bracsan** | Lima (Jr. Paruro 1353) | Recojo / envío a coordinar | Celdas 18650, BMS, cargadores, fusibles, conectores, cable | A coordinar | <https://bracsan.pe/> |
| **Memory Kings** | Lima | Todo el Perú | Cámaras web, periféricos, cómputo | A coordinar | <https://www.memorykings.pe/listados/176/camaras-webcam> |
| **Tesla Electronic** | **Trujillo** | Nacional | ESP32-S3, módulos, sensores | Envío al interior en 24 h hábiles | <https://www.teslaelectronic.com.pe/> |
| **MTLAB** | Lima (San Martín de Porres) | Lima y Callao | ESP32-C6, shields, módulos step-up | Olva; S/ 10; solo Lima/Callao | <https://mtlab.pe/> |
| **Hifisac** | Lima (venta por WhatsApp) | Nacional, a coordinar | Catálogo amplio: cargadores, BMS, ESP32, INA219, pasivos | WhatsApp/email; web sin stock online | <https://hifisac.com/shop> |
| **Falabella** | Lima / marketplace | Todo el Perú | microSD, fusibles, interruptores | Domicilio; algunos productos se envían desde EE. UU. | <https://www.falabella.com.pe/> |
| **Autosolar** | Lima | Todo el Perú | Solar, LiFePO4, cargadores | A coordinar | <https://autosolar.pe/> |
| **Print3D.pe** | **Trujillo** | Servicio nacional | Impresión 3D, TPU, piezas técnicas | A coordinar | <https://print3d.pe/> |
| **Adafruit** | EE. UU. | Importación | HAT M.2, BNO085, RPLIDAR | Internacional | <https://www.adafruit.com/> |
| **Pololu** | EE. UU. | Importación | Motores 37D, drivers, ruedas | Internacional | <https://www.pololu.com/> |

> No se encontró una tienda de robótica “todo en uno” fuera de Lima. Lo que sí
> existe es electrónica en **Ica** (Electronics Peru) y servicio de impresión 3D
> en **Trujillo** (Print3D.pe). Las tiendas de Lima despachan a provincia.
>
> **Hifisac (revisión 2026-11-21):** el catálogo muestra precios, pero las fichas
> probadas —ESP32-S3, BMS, INA219, level shifter, e-stop, fusibles— aparecían
> **“Sin existencias”** y el carrito deshabilitado. La venta es por
> WhatsApp/email; usa sus precios como referencia y confirma stock. El
> **TP5100-84** de esta BOM es de Hifisac: confirmar antes de pagar.

## 4. BOM cotizada: ruta recomendada 100 % Perú

### 4.1 Cómputo y almacenamiento

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 1 | Raspberry Pi 4 Model B 8 GB | Placa oficial | 1 | Inventario de facultad | S/ 0,00 | S/ 0,00 | Reutilizada (ADR-0010) | — |
| 2 | Carcasa y refrigeración | Argon ONE V2 con ventilador | 1 | Inventario de facultad | S/ 0,00 | S/ 0,00 | Reutilizada; verificar CSI | — |
| 3 | Almacenamiento y arranque | microSD 64 GB A2 (SanDisk Extreme Pro) | 1 | Falabella | S/ 64,90 | S/ 64,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador> |
| | | | | | **Subtotal 4.1** | **S/ 64,90** | | |

> **Nota:** la Pi 4 y la Argon se reutilizan del inventario a S/ 0 (ADR-0010).
> Si se compran, el escenario “compra todo” está en 5.2: Pi 5 8 GB (S/ 768) +
> Active Cooler (S/ 29,90).
>
> **Por qué no HAT M.2:** la Raspberry Pi 4 **no expone PCIe**, así que el
> HAT+ M.2 oficial (diseñado para la Pi 5) **no aplica**. El arranque va por
> **microSD A2**, que es el único medio de almacenamiento de la BOM. Un SSD USB
> 3.0 sigue siendo posible, pero ya no está en la lista ni en el total.
>
> **Fuente de 5 V:** la Pi 4 necesita 5 V / 3 A. La BOM no incluye fuente porque
> se asume que el inventario tiene una; si no aparece, hay que cotizarla aparte.
>
> **microSD:** la A2 de Falabella es la mejor para el sistema operativo; la
> Kingston A1 de 64 GB de Naylamp (S/ 60) sirve como respaldo. Conviene una
> segunda tarjeta ya clonada: sin SSD, la SD es el único medio de arranque.

### 4.2 Percepción

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 4 | LiDAR 2D 360° | RPLIDAR A1M8-R6 (12 m) | 1 | Electromanía | S/ 600,00 | S/ 600,00 | En stock; quedaban 12 | <https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/> |
| 5 | ToF de piso | TFmini Plus 12 m, UART/I²C, IP65 | 1 | Electromanía | S/ 330,00 | S/ 330,00 | Solo quedan 8 | <https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/> |
| 6 | Webcam USB 4K | Logitech Brio 4K Ultra HD Pro | 1 | Memory Kings | S/ 487,00 | S/ 487,00 | Más de 10; confirmar SKU | <https://www.memorykings.pe/listados/176/camaras-webcam> |
| 7 | IMU 9-DOF | Módulo BNO085 | 1 | Electronics Peru (Ica) | S/ 100,00 | S/ 100,00 | En stock | <https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/> |
| 8 | Monitor de batería | INA219 I²C | 1 | Electromanía | S/ 12,50 | S/ 12,50 | En stock | <https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/> |
| | | | | | **Subtotal 4.2** | **S/ 1.529,50** | | |

> **Por qué webcam USB en lugar de estéreo CSI:** la Pi 4 tiene **un solo CSI**
> (F-54), así que no admite el par de Camera Module 3 de ADR-0009. La Brio 4K
> entrega UVC por USB 3.0 y permite visión de color y teleoperación, no
> profundidad estéreo. Confirmar SKU, firmware y que la oferta esté vigente en
> Memory Kings; el listado no es una ficha de producto.
>
> **ToF de piso:** el TFmini Plus mide un punto con 12 m de alcance, IP65 y
> UART/I²C; se monta en la parte delantera baja para detectar escalones y
> desniveles. **No sustituye al LiDAR**: sin barrido 360° no hay SLAM.
>
> **Alternativas de LiDAR:** el RPLIDAR C1 (DTOF, 12 m, IP54, ROS/ROS2) está a
> S/ 450 en Electromanía y es más moderno, pero conviene validar el driver antes
> de adoptarlo. El A1M8 es la opción con más soporte y la que usa la BOM.
> Naylamp tiene el A1M8 a S/ 840, pero **agotado**.
>
> **Alternativas de IMU:** si no se quiere depender de una sola tienda, Naylamp
> tiene MPU9250 (S/ 85) y MPU6050 (S/ 18). El BNO085 es superior por su fusión
> interna; el MPU9250 es un reemplazo razonable si se acepta más trabajo de
> calibración. Adafruit vende el BNO085 a US$ 29,50, pero la opción de Ica es
> más barata y evita importar.

### 4.3 Tracción

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 9 | Motorreductor 12 V con encoder | DFRobot FIT0185, 83 rpm, 45 kg·cm, encoder Hall | 2 | Electromanía | S/ 145,00 | S/ 290,00 | En stock; quedaban 30 | <https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/> |
| 10 | Driver | BTS7960 43 A (un módulo por motor) | 2 | Naylamp | S/ 45,00 | S/ 90,00 | En stock | <https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html> |
| | | | | | **Subtotal 4.3** | **S/ 380,00** | | |

> **El motor exacto no está:** la BOM pedía 50 rpm con encoder. El FIT0185 da
> 83 rpm y 45 kg·cm (4,4 N·m) con encoder de 2096 pulsos/vuelta. Con el boost
> de 12 V de la sección 4.4 recupera sus 83 rpm y el rover queda en ~0,39 m/s;
> sin boost, a 7,4 V, gira a ~51 rpm y el rover cae a ~0,24 m/s. Si se prefiere
> el eje de 50 rpm, el DFRobot FIT0492-A (sin encoder) está a S/ 69,90, pero
> habría que añadir encoder y acoplarlo.
>
> **El driver exacto tampoco:** el Cytron MDD10A no aparece en las tiendas
> peruanas consultadas. Dos BTS7960 cuestan S/ 90 y sobran para 7 A de bloqueo
> por motor, pero requieren más cableado y lógica de enable.
>
> **Advertencia de corriente:** el FIT0185 declara unos **7 A de bloqueo por
> motor**; dos motores pueden pedir 14 A. El boost de 400 W declara 15 A, así
> que el bloqueo simultáneo queda justo en el límite: limitar corriente en
> firmware y no arrancar en rampa contra un obstáculo. Ver la sección 7.
>
> **Ruedas y placas:** se imprimen en local (Print3D.pe o taller de facultad) y
> **no tienen costo de proveedor**, por eso no están en la tabla. El diseño está
> en [`diseno-mecanico.md`](diseno-mecanico.md). La rueda de 90 mm es la que
> asume el cálculo: 83 rpm con 90 mm de diámetro dan ~0,39 m/s.

### 4.4 Energía y protección

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 11 | Celda Li-ion 18650 | EVE INR18650/35V, 3,6 V, 3500 mAh | 8 | Bracsan | S/ 19,00 | S/ 152,00 | En stock | <https://bracsan.pe/producto/bateria-de-litio-li-ion-recargable-3-7v-3500mah-eve-inr18650-35v/> |
| 12 | BMS 2S | 25 A, 7,4/8,4 V | 1 | Bracsan | ref. S/ 18,00 | S/ 18,00 | Precio de referencia del 3S; confirmar SKU 2S | <https://bracsan.pe/producto/modulo-para-carga-de-baterias-de-li-ion-bms-3s-25a-11-1v-12v-12-6v-18650-bc-3s25a/> |
| 13 | Plaquita de níquel | Tira de 1 m | 1 | Bracsan | S/ 5,00 | S/ 5,00 | En stock | <https://bracsan.pe/producto/platina-niquel-para-conexion-de-baterias-18650-x-metro-1mt/> |
| 14 | Espaciadores | 3×1 para 18650 | 4 | Bracsan | S/ 0,60 | S/ 2,40 | En stock; arreglo 2×4 | <https://bracsan.pe/producto/espaciadores-3x1-para-bateria-de-li-ion-3-celda-18650/> |
| 15 | Conector | XT60 macho/hembra | 1 | Bracsan | S/ 4,50 | S/ 4,50 | En stock | <https://bracsan.pe/producto/conector-xt60-macho-hembra-bala-para-bateria-lipo-amass-xt60/> |
| 16 | Arnés del pack | Cable, termorretráctil y fusible de 20–25 A | 1 | Bracsan / varios | est. S/ 20,00 | S/ 20,00 | Estimado; fusible a recalcular | <https://bracsan.pe/> |
| 17 | Cargador solar | Módulo TP5100-84, 4,2/8,4 V, 2 A | 1 | Hifisac | S/ 5,60 | S/ 5,60 | Disponible; confirmar stock | <https://hifisac.com/shop/category/baterias-240?search=cargador> |
| 18 | Boost de tracción | Step-up 400 W, 15 A, 7,4 → 12 V | 1 | MTLAB | est. S/ 55,00 | S/ 55,00 | Cotizar | <https://mtlab.pe/producto/modulo-step-up-dc-dc-elevador-de-voltaje-150w-200w-400w/> |
| 19 | DC-DC 5 V 5 A | XL4005 5 A | 1 | Electromanía | S/ 6,59 | S/ 6,59 | En stock; derratear | <https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> |
| 20 | DC-DC 5 V 3 A | XL4005 5 A (segundo módulo, regulado a 5 V) | 1 | Electromanía | S/ 6,59 | S/ 6,59 | En stock | <https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> |
| 21 | Portafusibles | Línea mini cuchilla, 12 A | 1 | Bracsan | ref. S/ 15,90 | S/ 15,90 | Precio de referencia de Falabella; confirmar en Bracsan | <https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a> |
| 22 | Fusibles | Surtido de vidrio 250 V (banco) | 1 | Electromanía | S/ 12,00 | S/ 12,00 | En stock | <https://www.electromania.pe/producto/100x-fusibles-de-vidrio-250v/> |
| 23 | Parada de emergencia | Seta roja enclavada, contactos NC/NO, 660 V 10 A | 1 | Electromanía | S/ 8,00 | S/ 8,00 | En stock; 10 A; ver riesgo 2 | <https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/> |
| 24 | Interruptor general | Desconectador de batería 12–48 V | 1 | Falabella | S/ 46,90 | S/ 46,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco> |
| | | | | | **Subtotal 4.4** | **S/ 358,48** | | |

> **El pack: 2S4P de 8 celdas.** Cuatro celdas en paralelo por cada rama en
> serie: **7,4 V nominales, 8,4 V de carga, 14 Ah y 103,6 Wh**, con BMS de 2S
> y 25 A. Sustituye a la LiFePO4 Goldenmate de 10 Ah y a su cargador de red, que
> salieron de la BOM el 2026-11-23. Las celdas se emparejan por capacidad y
> resistencia interna antes de armar el pack; no se sueldan con cautín.
>
> **Carga:** el **TP5100-84** acepta 5–18 V de entrada y carga 2S a 8,4 V con
> 2 A. Se alimenta con **2 paneles de 6 V en serie (12 V)** del inventario
> (F-52); **nunca 3 en serie**, porque su Voc supera los 18 V del módulo. Con
> 2 A sobre 14 Ah, la carga completa ronda las 7 h sin pérdidas (estimación):
> el solar es de mantenimiento, no de recarga rápida. La carga siempre
> supervisada, sobre superficie no inflamable y fuera del rover.
>
> **Boost de tracción:** el step-up de 400 W (15 A) alimenta **solo** el riel de
> los BTS7960 → motores, de 7,4 a 12 V. Devuelve las 83 rpm y ~0,39 m/s. Sin
> boost el rover queda a ~51 rpm y ~0,24 m/s. No usar el boost para la Pi ni
> para los DC-DC: el cómputo va directo al pack a través de los XL4005. Ojo con
> la corriente de entrada: 12 V × 15 A son ~180 W, que a 7,4 V piden ~25 A,
> justo el límite del BMS y del fusible de 20–25 A.
>
> **Portafusibles y fusible:** el fusible principal se recalcula a **20–25 A**
> por la corriente del pack de 2S. Ojo: el portafusibles mini cuchilla listado
> está declarado para 12 A, así que hay que conseguir uno del calibre adecuado
> (o usar un desconectador con fusible) antes de montar el fusible definitivo.
> Confirmar precio y stock en Bracsan; el de Falabella es solo referencia.
>
> **DC-DC:** los dos XL4005 son de 5 A nominales; derratear a ~3 A, medir rizado
> y temperatura, y no alimentar motores desde ellos. Uno va a la Pi 4 (5 V/3 A)
> y el otro a sensores y webcam (5 V/5 A).

### 4.5 Cableado, tornillería, varios y repuestos

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 25 | Cable y conectores | XT60/XT30, cable 14–18 AWG, termorretráctil | 1 | Naylamp / Electromanía | est. S/ 80,00 | S/ 80,00 | Parcialmente verificado | <https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html> · <https://www.electromania.pe/producto/conector-amass-xt60-con-cable-siliconado-macho-14awg-10cm/> |
| 26 | Tornillos y tuercas | M3/M4 y tuercas en T | 1 | Naylamp / ferretería | est. S/ 50,00 | S/ 50,00 | Estimado | <https://naylampmechatronics.com/72-tornillos-y-tuercas> |
| 27 | Accesorios de caja | Ventilador, rejilla, espuma | 1 | The Pi Box / ferretería | est. S/ 30,00 | S/ 30,00 | Estimado; no va en el pedido de cómputo | <https://thepibox.pe/> |
| 28 | Repuestos críticos | Fusibles, cable, conectores | 1 | Varios | est. S/ 50,00 | S/ 50,00 | Estimado | — |
| | | | | | **Subtotal 4.5** | **S/ 210,00** | | |

> **Chasis:** el perfil V-Slot 2040 de 3,2 m **ya se tenía** y sale de la BOM
> (antes S/ 160). Las placas y las ruedas se imprimen en local y tampoco tienen
> costo de proveedor. Si hiciera falta un perfil adicional, el 2040 de Naylamp
> está a S/ 160; el 2020 sigue agotado.
>
> **Repuestos:** con un pack Li-ion armado a mano y un arranque por microSD, los
> repuestos críticos son fusibles, cable, terminales y una microSD clonada. No
> recortar esta línea para la demo.

### 4.6 Interfaz ESP32 (propuesta ADR-0008, opcional)

> **No incluido en el total base.** Es una propuesta en revisión
> ([ADR-0008](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md)) y desde
> el 2026-11-23 queda como **opcional**: la BOM base usa la Pi 4 directamente
> para PWM, encoders, IMU, batería y e-stop. Si se aprueba, el ESP32 ejecuta
> esas funciones y añade ~S/ 195 al total.

| # | Componente | Modelo | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| E1 | MCU de interfaz | ESP32-S3-DevKitC-1 N16R8 | 1 | Tesla Electronic (Trujillo) | S/ 110,00 | S/ 110,00 | En stock; 4 unidades | <https://www.teslaelectronic.com.pe/producto/nodemcu-esp32-s3-devkitc-1-n16r8-tipo-usb-c/> |
| E2 | Alternativa C6 | ESP32-C6-DevKitC-1 N8 | 1 | MTLAB (Lima) | S/ 100,00 | S/ 100,00 | Últimas unidades; solo Lima/Callao | <https://mtlab.pe/producto/esp32-c6-devkitc-1-n8-placa-de-desarrollo-espressif/> |
| E3 | Alternativa compacta | Seeed XIAO ESP32-C6 | 1 | Electromanía | S/ 39,00 | S/ 39,00 | En stock; solo 11 GPIO | <https://www.electromania.pe/producto/seeed-studio-xiao-esp32-c6-tape-reel/> |
| E4 | Expansor I²C | TCA9548A, 8 canales | 1 | Electromanía | S/ 5,00 | S/ 5,00 | En stock | <https://www.electromania.pe/producto/modulo-i2c-8-canales-tca9548a/> |
| E5 | Adaptador de nivel | 3,3–5 V, 4 líneas | 1 | Electromanía | S/ 3,00 | S/ 3,00 | En stock | <https://www.electromania.pe/producto/convertidor-de-nivel-logico-3-3-5v-de-4-lineas/> |
| E6 | Optoacoplador | PC817, para sentido de e-stop | 1 | Tesla Electronic | S/ 2,00 | S/ 2,00 | En stock | <https://www.teslaelectronic.com.pe/producto/pc817-optocoplador-fototransistor/> |
| E7 | Protoboard, headers, terminales | Shield/arnés | 1 | Bracsan / Electromanía | ~S/ 40,00 | ~S/ 40,00 | Estimado | <https://bracsan.pe/> |
| E8 | Cable USB con ferrita | USB-C, corto | 1 | Varios | ~S/ 15,00 | ~S/ 15,00 | Estimado | — |
| E9 | Caja / soporte | Impresión 3D o acrílico | 1 | Print3D.pe / taller | ~S/ 20,00 | ~S/ 20,00 | Estimado | <https://print3d.pe/> |

**Subtotal con S3:** ~S/ 195,00. **Con C6:** ~S/ 185,00. **Con XIAO C6:**
~S/ 124,00, pero sus 11 GPIO no alcanzan para BTS7960 + 2 encoders + I²C +
e-stop + LED; solo tiene sentido con MDD10A y aceptando cero margen.

> **Pines:** el S3 tiene 45 GPIO, 8 LEDC, 2 MCPWM, 4 PCNT, 20 ADC y 2 I²C. El C6
> tiene 30/22 GPIO, 6 LEDC, 1 MCPWM, 4 PCNT, 7 ADC y 2 I²C. Para 2 motores con
> MDD10A (1 PWM + 1 DIR cada uno) y 2 encoders, ambos alcanzan; para 6×6, el S3
> tiene más margen.
>
> **Nivel lógico:** los encoders FIT0185 son de 5 V y los GPIO del ESP32 son de
> 3,3 V. El adaptador de 4 líneas cubre A/B de los dos motores. No conectar 5 V
> directo.
>
> **E-stop:** la seta corta la potencia del driver en hardware; el PC817 solo
> lleva el estado al MCU. El MCU no sustituye la cadena de seguridad.
>
> **Alimentación:** usar el riel de 5 V 3 A, no el USB de la Pi, para evitar
> reinicios por ruido de motores. Masa común en estrella.
>
> **Hifisac (cotizar):** ESP32-S3 N16R8 S/ 49; INA219 S/ 8,20; level shifter
> S/ 2,70; BMS 3S 25A S/ 9,90. Si confirman stock, el add-on baja ~S/ 60; pero
> la web marca “Sin existencias” en todos esos productos. No está contabilizado
> en el subtotal.

### 4.7 Pack 3S2P / 3S3P (opcional, no es la ruta base)

> **No incluido en el total base.** Desde el 2026-11-23 la ruta base es el pack
> **2S4P** de la sección 4.4, que se carga con el TP5100-84 desde 12 V solares.
> Las opciones 3S solo tienen sentido si se decide subir la tensión de tracción
> y cambiar el cargador por uno de 12,6 V; entonces hay que revisar también el
> boost y el riel de 5 V. Requieren armado del pack, BMS con balanceo y carga
> supervisada; el reglamento del ERC debe revisarse antes de adoptarlas.

**Opción 3S2P (6 celdas, ~7 Ah, ~75,6 Wh):**

| # | Componente | Modelo | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| B1 | Celda Li-ion 18650 | EVE INR18650/35V, 3,6 V, 3500 mAh | 6 | Bracsan | S/ 19,00 | S/ 114,00 | En stock | <https://bracsan.pe/producto/bateria-de-litio-li-ion-recargable-3-7v-3500mah-eve-inr18650-35v/> |
| B2 | BMS 3S | 25 A, 11,1/12,6 V | 1 | Bracsan | S/ 18,00 | S/ 18,00 | En stock | <https://bracsan.pe/producto/modulo-para-carga-de-baterias-de-li-ion-bms-3s-25a-11-1v-12v-12-6v-18650-bc-3s25a/> |
| B3 | Nickel | Tira para 18650, 1 m | 1 | Bracsan | S/ 5,00 | S/ 5,00 | En stock | <https://bracsan.pe/producto/platina-niquel-para-conexion-de-baterias-18650-x-metro-1mt/> |
| B4 | Espaciadores | 3×1 para 18650 | 2 | Bracsan | S/ 0,60 | S/ 1,20 | En stock | <https://bracsan.pe/producto/espaciadores-3x1-para-bateria-de-li-ion-3-celda-18650/> |
| B5 | Conector | XT60 macho/hembra | 1 | Bracsan | S/ 4,50 | S/ 4,50 | En stock | <https://bracsan.pe/producto/conector-xt60-macho-hembra-bala-para-bateria-lipo-amass-xt60/> |
| B6 | Cargador | 12,6 V, 3 A | 1 | Bracsan | S/ 48,00 | S/ 48,00 | En stock | <https://bracsan.pe/producto/cargador-para-bateria-de-litio-li-ion-12-6v-3a-jx-12630/> |
| B7 | Cable, termorretráctil, fusible | Arnés del pack | 1 | Bracsan / varios | ~S/ 20,00 | ~S/ 20,00 | Estimado | <https://bracsan.pe/> |
| B8 | Relé de potencia | 12 V 30 A + porta relay | 1 | Bracsan | S/ 7,50 | S/ 7,50 | En stock | <https://bracsan.pe/producto/relay-12vdc-5-pines-250vac-30a-songle-sla-12vdc-sl-a/> · <https://bracsan.pe/producto/porta-relay-de-ceramica-para-relay-automotriz-de-5-pines-kavto-kv-s008-23/> |

**Subtotal 3S2P:** ~S/ 218,20, sin soldador de punto. El soldador de punto
portátil de Bracsan cuesta S/ 390; si no se tiene, conviene pagar el armado a un
taller o pedir prestado el equipo. **No soldar celdas 18650 con cautín.**

**Opción 3S3P (9 celdas, ~10,5 Ah, ~113,4 Wh):** 9 celdas (S/ 171) + BMS
(S/ 18) + nickel 10 m (S/ 35) + 3 espaciadores (S/ 1,80) + XT60 (S/ 4,50) +
cargador (S/ 48) + varios (S/ 20) + relé (S/ 7,50) = **~S/ 305,80**.

| Comparación | 2S4P — base (8 celdas) | 3S2P — opcional | 3S3P — opcional |
|---|---:|---:|---:|
| Materiales del pack + su carga | S/ 207,50 (S/ 201,90 + TP5100-84) | ~S/ 218,20 | ~S/ 305,80 |
| Energía | 103,6 Wh | ~75,6 Wh | ~113,4 Wh |
| Tensión | 7,4 V nominal; 8,4 V de carga | 11,1 V nominal; 12,6 V de carga | 11,1 V nominal; 12,6 V de carga |
| Corriente máxima | BMS 25 A; 4P admite hasta ~32 A teóricos | BMS 25 A; 2P admite ~16 A | BMS 25 A; 3P admite ~24 A |
| Masa de celdas | ~0,40 kg | ~0,30 kg | ~0,45 kg |
| Riesgo | Li-ion 2S, BMS y carga supervisada | Li-ion 3S, ídem | Li-ion 3S, ídem |
| Estado | **En la BOM vigente** | Propuesta | Propuesta |

> **Por qué 2S4P es la base:** con el boost en el riel de tracción se recuperan
> los 12 V de los motores, y el pack de 7,4 V se carga desde 12 V solares con un
> TP5100-84 de S/ 5,60. Un pack 3S necesitaría un cargador de 12,6 V y revisar
> el resto del riel, y además el 3S2P tiene **menos** energía que el 2S4P
> (75,6 Wh frente a 103,6 Wh); el 3S3P apenas la supera (113,4 Wh) a cambio de
> otro cargador y otro BMS. No justifica el cambio.
>
> **Corriente:** la celda EVE 35V declara 10,2 A máximos “not for cycle life”.
> Para vida útil, tratar 8 A por celda como techo continuo. Con 4P el pack puede
> dar mucho más de los 25 A del BMS, así que el límite práctico lo fija el BMS y
> el fusible de 20–25 A.
>
> **Protección y e-stop:** la seta de S/ 8 está rated 10 A; no debe cortar 20–25
> A. Usar el desconectador de la fila 24 para la potencia y dejar que la seta
> corte la lógica de enable de los BTS7960 y del boost. Si se quiere corte de
> potencia por seta, añadir el relé de 30 A (B8, opcional) y que la seta corte
> solo la bobina.
>
> **Armado:** medir capacidad y resistencia interna de cada celda antes de
> armar; agrupar las más parecidas. Usar portaceldas/espaciadores, nickel y
> soldador de punto. Aislar el pack con termorretráctil y carcasa ignífuga;
> fijarlo al chasis con soporte, no con velcro.
>
> **Hifisac (cotizar):** BMS 3S 25A S/ 9,90 y portaceldas 18650 S/ 1,90; sus
> celdas de 3000 mAh cuestan S/ 24,50, peor relación precio/capacidad que la EVE
> 35V de Bracsan (S/ 19). La web marca “Sin existencias”; confirmar por
> WhatsApp.
>
> **Pack completo:** la lista de estos add-ons está en
> [`bom-peru-addons.csv`](bom-peru-addons.csv), que no se modificó el
> 2026-11-23.

## 5. Totales

### 5.1 Ruta recomendada (100 % Perú, vigente al 2026-11-23)

| Bloque | Subtotal |
|---|---:|
| Cómputo (Pi 4 + Argon, inventario) | S/ 0,00 |
| Almacenamiento (microSD A2) | S/ 64,90 |
| Percepción (LiDAR, ToF, webcam, IMU, INA219) | S/ 1.529,50 |
| Tracción (2 motores + 2 drivers) | S/ 380,00 |
| Energía y protección (pack 2S4P, carga, boost, DC-DC) | S/ 358,48 |
| Cableado y conectores | S/ 80,00 |
| Tornillería | S/ 50,00 |
| Varios (accesorios de caja) | S/ 30,00 |
| Repuestos | S/ 50,00 |
| **Subtotal** | **S/ 2.542,88** |
| Imprevistos / envío local (5 %) | S/ 127,14 |
| **Total estimado** | **S/ 2.670,02** |

> Las ruedas, las placas y el perfil V-Slot 2040 **no** suman: los dos primeros
> se imprimen en local y el perfil ya estaba en el inventario. La Pi 4 y la
> Argon se declaran a S/ 0 por reutilización (ADR-0010).
>
> **Add-ons no incluidos:** la interfaz ESP32 suma ~S/ 195 (sección 4.6); el
> pack 3S2P cuesta ~S/ 218 y el 3S3P ~S/ 306 (sección 4.7). Ninguna de estas
> variantes está aprobada.

### 5.2 Comparación de rutas en PEN

| Concepto | Pi 4 — vigente | Pi 5 — compra todo (2026-11-23) | Pi 5 — histórica (2026-11-21) |
|---|---:|---:|---:|
| Cómputo y almacenamiento | 64,90 | 862,80 | 1.140,50 |
| Percepción | 1.529,50 | 1.529,50 | 712,50 |
| Tracción (motores + drivers) | 380,00 | 380,00 | 480,00 |
| Energía y protección | 358,48 | 358,48 | 534,98 |
| Chasis, cableado y montaje | 210,00 | 210,00 | 450,00 |
| **Subtotal** | **2.542,88** | **3.340,78** | **3.317,98** |
| Imprevistos / envío (5 %) | 127,14 | 167,04 | 165,90 |
| **Total** | **2.670,02** | **3.507,82** | **3.483,88** |

> **Escenario “compra todo”:** si en lugar de reutilizar se compra el cómputo,
> se sustituyen la Pi 4 y la Argon por **Pi 5 8 GB (S/ 768) + Active Cooler
> (S/ 29,90)**: subtotal **S/ 3.340,78** y total con 5 % **S/ 3.507,82**. No
> incluye HAT M.2 ni SSD: la Pi 5 no cambia la ruta de almacenamiento elegida.
>
> **Ruta histórica (2026-11-21):** S/ 3.483,88, con Pi 5 + Active Cooler, SSD
> USB de 256 GB, LiFePO4 de 10 Ah, cargador de red, perfil 2040, ruedas y placas
> encargadas. Se conserva solo como comparación; **no es la ruta de compra**.
>
> La BOM en EUR anterior se conserva en el historial del proyecto; **la
> referencia de compra es [`bom.md`](bom.md) en PEN**.

## 6. Disponibilidad: exacto vs. sustituto vs. importación

> **Nota de vigencia:** tabla revisada el 2026-11-23. La ruta vigente no compra
> Pi 5, HAT M.2, SSD ni LiFePO4; el cómputo y el chasis se reutilizan o se
> imprimen en local.

| Componente | ¿Exacto en Perú? | Sustituto local | Importación | Impacto / decisión |
|---|---|---|---|---|
| Raspberry Pi 4 8 GB | **No hace falta** (inventario) | Pi 5 8 GB (S/ 768) si se compra | Adafruit / tiendas Pi | La ruta base reutiliza la Pi 4; el escenario “compra todo” está en 5.2 |
| Almacenamiento | **Sí** (microSD A2) | microSD A1 de 64 GB (S/ 60, Naylamp) | — | Sin HAT M.2 ni SSD en la BOM: la Pi 4 arranca por microSD |
| LiDAR A1M8 | **Sí** (Electromanía) | RPLIDAR C1 (S/ 450) | Adafruit US$ 99,95 / LD19 | A1M8 tiene más soporte; C1 es más moderno |
| ToF de piso TFmini Plus | **Sí** (Electromanía) | — | Benewake directo | Quedaban 8 unidades; IP65 y 12 m |
| Webcam Brio 4K | **Listada, no verificada** (Memory Kings) | Otra webcam UVC 1080p | Logitech / importación | Confirmar SKU y oferta; sustituye al estéreo CSI imposible en la Pi 4 |
| BNO085 | **Sí** (Ica) | MPU9250 (S/ 85) / MPU6050 (S/ 18) | Adafruit US$ 29,50 / Mouser | BNO085 ahorra calibración; el MPU exige más trabajo |
| INA219 | **Sí** | INA226 (S/ 29) | — | Suficiente para el bus del pack de 2S |
| Motor 50 rpm con encoder | **No con stock** | FIT0185 83 rpm con encoder (S/ 145) | Pololu 4753 US$ 60,95 | Con el boost a 12 V recupera 83 rpm y ~0,39 m/s |
| Cytron MDD10A | **No** | 2 × BTS7960 (S/ 90) | Cytron / RobotShop | BTS7960 exige más cableado; MDD10A es más compacto |
| Celdas 18650 | **Sí** (Bracsan) | Hifisac 3000 mAh (S/ 24,50) | Tiendas de litio | EVE 35V es la mejor relación precio/capacidad |
| BMS 2S 25 A | **A confirmar** | BMS 3S (S/ 18) solo para pack 3S | — | Confirmar SKU 2S en Bracsan antes de pagar |
| Cargador 2S | **Sí** (Hifisac) | Cargador 12,6 V 3 A (S/ 48) solo para 3S | — | TP5100-84 desde 12 V; nunca 3 paneles en serie |
| Boost 12 V | **A cotizar** (MTLAB) | Otro step-up ≥15 A | AliExpress / Pololu | Solo riel de motores; verificar rizado y temperatura |
| DC-DC 5 V 5 A | **Sí** | XL4005 5 A (S/ 6,59) | Pololu / Mouser | Verificar ripple y temperatura; derratear |
| E-stop | **Sí** | Seta 22 mm de Naylamp (S/ 15, agotada) | Schneider / Eaton | La de Electromanía es lenta de liberar girando y de 10 A |
| Interruptor general | **Sí** | Desconectador de batería 12–48 V | — | Verificar corriente continua, no solo pico |
| Perfil 2040 | **No hace falta** | 2040 de Naylamp (S/ 160) si se requiere más | AliExpress / OpenBuilds | El perfil está en el inventario |
| Ruedas y placas | **Impresión local** | Print3D.pe o taller de facultad | — | Sin costo de proveedor; el diseño está en [`diseno-mecanico.md`](diseno-mecanico.md) |
| Fusibles / cable / conectores | **Sí** | Bracsan, Naylamp, Electromanía | — | Comprar surtido y repuestos |
| MCU de interfaz (opcional) | **Sí** | ESP32-S3 S/ 110 (Trujillo); C6 S/ 100 (Lima); XIAO C6 S/ 39 | Adafruit / Mouser | Add-on opcional, no entra en el total |
| Pack 3S2P/3S3P (opcional) | **Sí, a medida** | Celdas EVE 35V + BMS 3S en Bracsan | — | ~S/ 218 / ~S/ 306; requiere armado y cargador 12,6 V |

## 7. Riesgos y verificaciones antes de comprar

1. **Fusible y portafusibles.** El fusible principal se recalcula a **20–25 A**
   por el pack de 2S, pero el portafusibles mini cuchilla del listado está
   declarado para 12 A. Comprar un portafusibles del calibre adecuado o usar un
   desconectador con fusible; si no, el propio portafusibles es el eslabón débil.
2. **E-stop de 10 A.** La seta de Electromanía está rated 10 A y el pack puede
   entregar 25 A. No usarla para cortar la potencia principal: que corte la
   lógica de enable de los BTS7960 y del boost, y que el desconectador (fila 24)
   corte la potencia. Si se quiere corte de potencia por seta, añadir un relé de
   30 A.
3. **BMS 2S.** Bracsan publica el módulo de 3S; confirmar el SKU de **2S de
   25 A** y que balancee. Un BMS sin balanceo exige cargador balanceador o
   revisión manual de las ramas.
4. **Cargador TP5100-84.** Entrada máxima 18 V: usar **2 paneles de 6 V en
   serie (12 V)** y **nunca 3**, porque el Voc de tres paneles supera el límite
   y el módulo se destruye. La carga solar de 2 A sobre 14 Ah es de
   mantenimiento (≈7 h); para recargas rápidas hace falta una fuente de banco.
5. **Boost de 400 W.** Declara 15 A y dos FIT0185 pueden pedir 14 A en bloqueo
   simultáneo. Limitar corriente en firmware, arrancar en rampa y verificar
   rizado y temperatura del step-up antes de exigirlo.
6. **Almacenamiento en microSD.** Sin SSD, la tarjeta es el único medio de
   arranque: riesgo de corrupción por apagones y desgaste. Clonar una tarjeta de
   respaldo y apagar con el comando correcto.
7. **Webcam USB.** Un solo CSI en la Pi 4; la Brio consume ancho de banda USB y
   corriente. Conectarla al puerto USB 3.0, confirmar SKU y UVC, y no esperar
   profundidad estéreo.
8. **ToF de piso.** Quedaban 8 unidades; montarlo protegido en la parte baja
   delantera y no usarlo como único sensor de seguridad. El TFmini no sustituye
   al LiDAR.
9. **PWM en Raspberry Pi 4.** Dos BTS7960 necesitan PWM y enable; la Pi 4 no
   tiene tantos canales PWM hardware. Validar `lgpio`/ROS 2 o añadir un RP2040
   o el ESP32 de la sección 4.6 como controlador de tracción.
10. **Stock de marketplace.** “Sin stock en tienda” no significa “sin stock para
    despacho”. Confirmar vendedor, precio final y fecha de entrega en Memory
    Kings y Falabella.
11. **Precios volátiles.** Todos los precios son del 2026-11-21, con la revisión
    del 2026-11-23. Volver a cotizar antes de emitir la orden de compra.
12. **Aduanas.** Los envíos internacionales pueden sumar flete, IGV, derechos y
    gastos del courier. Confirmar el régimen aplicable con SUNAT y el courier;
    este documento no incluye esos costos.
13. **No hay compra aprobada.** Esta lista es un estudio de abastecimiento. La
    compra requiere aprobación del PO y del responsable de Hardware.

## 8. Plan de compra sugerido

| Orden | Qué comprar | Dónde | Por qué primero |
|---|---|---|---|
| 1 | RPLIDAR A1M8, TFmini Plus, 2 × FIT0185, INA219, 2 × XL4005, fusibles, e-stop | Electromanía | Sensores y tracción; un solo envío |
| 2 | 8 celdas, BMS 2S, níquel, espaciadores, XT60, arnés, portafusibles | Bracsan | El pack es la base de la energía; confirmar BMS 2S y portafusibles |
| 3 | 2 × BTS7960, cable/conectores, tornillería | Naylamp | Drivers y cableado; envío gratis > S/ 200 |
| 4 | microSD 64 GB A2, desconectador 12–48 V | Falabella | Arranque y corte general; marketplace |
| 5 | Webcam Brio 4K | Memory Kings | Confirmar SKU y oferta antes de pagar |
| 6 | BNO085 | Electronics Peru (Ica) | Única tienda con stock claro del módulo |
| 7 | TP5100-84 | Hifisac (WhatsApp) | Necesario para cargar el pack; confirmar stock |
| 8 | Step-up de 400 W | MTLAB (Lima/Callao) | Recupera los 12 V de tracción; cotizar |
| 9 | Accesorios de caja, repuestos y microSD clonada | The Pi Box / ferretería | Al final, con el remanente |

> **Antes de pagar:** pedir por WhatsApp/correo la confirmación de stock, el
> precio final con envío y el plazo a la ciudad del equipo. Guardar la
> cotización como evidencia de la compra.

## 9. Alternativas si no se consigue algo

### 9.1 Si no hay Pi 4 8 GB

- **Pi 4B 4 GB** (S/ 471,50 en The Pi Box): compatible con Ubuntu 24.04, pero
  con RAM justa para Nav2; estaba **agotada** al momento de la consulta. No
  recomendado.
- **Pi 5 8 GB** (S/ 768 en The Pi Box): más CPU, pero no es la base y requeriría
  revisar ADR-0010, RNF-07 y la BOM. Es el escenario “compra todo” de 5.2.
- **Importar** una Pi 4 8 GB; sumar flete e impuestos.

### 9.2 Si no hay LiDAR A1M8

- **RPLIDAR C1** (S/ 450, Electromanía): 12 m, DTOF, IP54, ROS/ROS2. Validar
  driver y parámetros de Nav2.
- **LD19 / DTOF** importado: más barato que el A1M8, pero con menos soporte
  documentado en el repo.
- **LiDAR de un solo punto** (TFmini) no sirve para SLAM 2D; no es sustituto.

### 9.3 Si no hay motor con encoder

- **FIT0185 83 rpm** (S/ 145): la opción recomendada.
- **FIT0492-A 50 rpm sin encoder** (S/ 69,90) + encoder externo: más barato,
  pero más trabajo mecánico y de calibración.
- **Pololu 4753 50:1 12 V con encoder** (US$ 60,95): el exacto funcional, pero
  importado y más caro.
- **Naylamp 37D 35 rpm con encoder** (S/ 70): agotado; consultar reposición.

### 9.4 Si no hay driver MDD10A

- **2 × BTS7960** (S/ 90): disponible, sobrado de corriente, más cableado.
- **Pololu Dual G2 18v18 for Raspberry Pi** (US$ 74,95): compacto y montable
  sobre la Pi, pero importado.
- **MDD10A importado**: la solución más limpia si se acepta el plazo.

### 9.5 Si no hay celdas 18650 o BMS 2S

- **Pack 3S2P / 3S3P** (opcional, sección 4.7): requiere BMS 3S, cargador de
  12,6 V y revisar el boost y el riel de 5 V. No es un cambio de conector: es
  otro diseño energético.
- **Armado a medida** en un taller de baterías o en Litio Energy
  (<https://litioperu.com/>): se piden las 8 celdas en 2S4P con BMS de 25 A y
  se paga el armado; cotizar.
- **Paquete 2S listo para usar** de otra tienda de litio: aceptar que el BMS y
  el conector no los eliges tú; verificar 25 A y 8,4 V.
- **LiFePO4 12,8 V 10 Ah** (S/ 239, Falabella): alternativa **histórica**, fuera
  de la ruta base. Exigiría un cargador de red de 14,6 V que ya no está en la
  BOM y no es compatible con el TP5100-84 ni con el riel de 7,4 V.
- **No usar celdas 18650 sin BMS, sin fusible y sin carcasa ignífuga.**

### 9.6 Si no hay perfil o chasis

- El **2040 de 3,2 m ya está en el inventario**; esta BOM no lo compra. Si hace
  falta más longitud, Naylamp lo tiene a S/ 160.
- **Chasis impreso en PETG reforzado**: válido para el mini demo, no para
  cargas altas.
- **Importar 2020** de AliExpress/OpenBuilds: largo plazo, pero mantiene el
  diseño original. No se encontró V-Slot 2020 con stock en Perú.

### 9.7 Almacenamiento: la ruta es microSD

- **microSD 64 GB A2** (S/ 64,90, Falabella): es la ruta base y el único medio
  de arranque de la BOM. Comprar una segunda tarjeta ya clonada.
- **microSD A1 64 GB** (S/ 60, Naylamp): respaldo aceptable; algo más lenta.
- **SSD USB 3.0 + caja** (S/ 210,70 en la versión 0.2): opcional si la SD se
  queda corta o se corrompe; **no está en el total vigente** y no requiere HAT.
- **No hay HAT M.2 posible:** la Pi 4 **no expone PCIe**; el HAT oficial es
  para la Pi 5. No comprar HAT para esta placa.

### 9.8 Si no hay ESP32-S3 (add-on opcional)

- **ESP32-C6-DevKitC-1 N8** (S/ 100, MTLAB): suficiente para 2 motores; menos
  margen para 6×6.
- **XIAO ESP32-C6** (S/ 39): compacto, pero 11 GPIO; solo con MDD10A y sin
  margen para LEDs o sensores extra.
- **ESP32 DevKit V1 clásico** (S/ 32–35): interino, más disponible; sin Wi-Fi 6
  ni Thread.
- **RP2040 / Teensy 4.1**: si no se necesita Wi-Fi y se prioriza determinismo.

### 9.9 Si no se quiere armar el pack

- **Pack 2S4P armado por un taller** (Litio Energy o taller de baterías de
  Lima): pedir 7,4 V, 14 Ah, BMS de 25 A con balanceo, XT60 y fusible; cotizar.
- **2S4P con portaceldas y cable** en lugar de nickel soldado: más simple y sin
  soldador de punto, a costa de más volumen y contactos menos robustos.
- **3S2P con cargador 12,6 V** (opcional, sección 4.7): sigue exigiendo armado.
- **LiFePO4 12,8 V 10 Ah + cargador 14,6 V**: alternativa **histórica**; más
  pesada, con otro cargador y fuera de la ruta base.
- **No usar celdas 18650 sin BMS, sin fusible y sin carcasa ignífuga.**

## 10. Fuentes y trazabilidad

- Fuente única de verdad de la BOM: [`bom-peru.csv`](bom-peru.csv), sincronizado
  el 2026-11-23.
- Fuentes de precios y stock de los proveedores originales: `F-19` a `F-38` en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Inventario de facultad (Pi 4, Argon, paneles de 6 V y celdas solares): `F-52`
  y [`inventario-facultad.md`](inventario-facultad.md).
- Fuentes de la propuesta ESP32/Li-ion y Hifisac: `F-30` a `F-38`.
- BOM base: [`bom.md`](bom.md).
- Diseño eléctrico base: [`diseno-electrico.md`](diseno-electrico.md).
- Variante 6×6 (no comprar): [`energia/bom-6x6.md`](energia/bom-6x6.md).
- Add-ons de ESP32 y pack 3S:
  [`bom-peru-addons.csv`](bom-peru-addons.csv).

> **Pendiente de registro:** las filas nuevas del 2026-11-23 (TFmini Plus y Brio
> 4K de Electromanía y Memory Kings, TP5100-84 de Hifisac, step-up de MTLAB y
> el portafusibles en Bracsan) llevan URL y fecha en el CSV, pero todavía no
> tienen `F-xx` propio en `fuentes.md`. Ese registro queda pendiente para no
> tocar archivos fuera de esta revisión.

> **Evidencia:** consulta web del 2026-11-21, revisada el 2026-11-23. No se
> ejecutaron pruebas de hardware ni se realizaron compras. Los precios deben
> revalidarse antes de la orden de compra.
