# BOM consolidado por proveedor — solicitud de cotizaciones

> **Estado:** Borrador de planificación · **Versión:** 0.2 · **Fecha:** 2026-11-23
> **Responsable:** equipo Kairos (ERC) · **Moneda:** soles peruanos (PEN) salvo indicación
> **Precios:** catálogo web consultado el **2026-11-21** por cada subproyecto.
> **No autoriza compra ni reserva.** No se ha contactado a ningún proveedor.
>
> **Cambios de la v0.2 (revisión del equipo, 2026-11-23):** ver §5. Se quitaron
> HAT, fuente, SSD, batería LiFePO4, cargador, perfil de aluminio e impresión 3D
> de proveedor; se reasignó el LiDAR al rover principal; el ToF pasa a 4 unidades;
> se añadió una webcam para el mini-rover; la energía pasa a un pack Li-ion de
> Bracsan con carga solar.

Este documento reúne las líneas de BOM de los tres subproyectos
(`mini-rover/`, `drone/`, `rover-principal/`), las agrupa **por proveedor** y calcula
las **cantidades totales** para enviar una sola solicitud de cotización a cada
empresa. Los BOM de origen no se modifican: siguen siendo la fuente de verdad de
cada subproyecto (ver §8 para lo que hay que actualizar allí).

---

## 1. Cómo usar este documento

1. Abre la sección del proveedor y copia su tabla en la plantilla
   [`solicitud-plantilla.md`](solicitud-plantilla.md).
2. Envía la solicitud por el canal indicado.
3. Registra la respuesta en la tabla de seguimiento de la plantilla.
4. Si una cotización cambia una cantidad o un modelo, actualiza **primero** el BOM
   del subproyecto y luego este consolidado.

Leyenda de proyecto: **MR** = Mini-rover · **DR** = Drone · **RP** = Rover-principal.
Leyenda de precio: `S/` verificado en catálogo · `~S/` **estimación de
planificación** · `ref.` precio de referencia de otra tienda.

---

## 2. Resumen por proveedor

| Proveedor | Líneas | Unidades | Verificado | Estimado | Canal | Prioridad |
|---|---:|---:|---:|---:|---|---|
| [Electromanía](#41-electromanía) | 10 | 17 | S/ 2.287,27 | ~S/ 25 | electromania.pe · WhatsApp | 1 |
| [Memory Kings](#42-memory-kings) | 2 | 3 | S/ 2.143,00 | — | memorykings.pe | 1 |
| [The Pi Box](#43-the-pi-box) | 3 | 4 | S/ 1.077,90 | — | thepibox.pe | 1 |
| [Bracsan](#44-bracsan) | 7 | 13 | S/ 158,60 | ~S/ 20 | bracsan.pe · WhatsApp 950 970 761 | 1 |
| [Falabella](#45-falabella-marketplace) | 2 | 3 | S/ 176,70 | — | falabella.com.pe | 2 |
| [Naylamp Mechatronics](#46-naylamp-mechatronics) | 4 | 5 | S/ 90,00 | ~S/ 110 | naylampmechatronics.com | 2 |
| [Electronics Peru](#47-electronics-peru) | 1 | 1 | S/ 100,00 | — | electronicsperu.com | 2 |
| [Cableado por decidir](#48-cableado-por-decidir) | 2 | 2 | — | ~S/ 140 | Naylamp o Electromanía | 2 |
| [Cargador solar 3S](#49-cargador-solar-3s-cn3722) | 1 | 1 | — | ~S/ 50 | importación / a cotizar | 3 |
| [Taller / tienda local](#410-taller--tienda-local) | 2 | 2 | — | ~S/ 400 | sin proveedor | 4 |
| [Varios / ferretería](#411-varios--ferretería) | 5 | 5 | — | ~S/ 150 | local | 4 |
| **Total** | **39** | **56** | **S/ 6.033,47** | **~S/ 895,00** | | |

> **Total consolidado: ~S/ 6.928,47** (sin envío, sin IGV adicional y sin aduanas).
> No incluye la copia de la BOM del mini demo que está en `rover-principal/`
> (ver §7.1), ni alternativas, ni add-ons, ni el estudio 6×6, ni la impresión 3D
> (se hace en local).

### 2.1 Totales por proyecto

| Escenario | Verificado | Estimado | Total |
|---|---:|---:|---:|
| Solo Mini-rover (MR) | S/ 1.613,08 | ~S/ 280 | S/ 1.893,08 |
| Solo Drone (DR) | S/ 1.504,39 | ~S/ 215 | S/ 1.719,39 |
| Solo Rover-principal, bloque visión (RP) | S/ 2.916,00 | ~S/ 400 | S/ 3.316,00 |
| Mini-rover + Drone | S/ 3.117,47 | ~S/ 495 | S/ 3.612,47 |
| **Los tres (MR + DR + RP)** | **S/ 6.033,47** | **~S/ 895** | **S/ 6.928,47** |

> El bloque RP sube respecto de la v0.1 porque ahora incluye el **LiDAR de
> S/ 600** y **2 ToF** (antes 1). El mini-rover baja porque ya no compra batería
> LiFePO4, SSD, caja USB, cargador, perfil de aluminio ni impresión 3D, y porque
> su LiDAR pasa al rover principal.

---

## 3. Qué pedir en todas las solicitudes

- **Stock real** para la cantidad total pedida (no el stock del buscador).
- **Precio unitario con IGV** y, si aplica, precio sin IGV.
- **Descuento por volumen**: es una compra única de equipo universitario.
- **Costo y plazo de envío a Lima** (y a Trujillo o Ica si el proveedor está fuera).
- **Factura o boleta con RUC** a nombre de la universidad.
- **Garantía**, política de devolución y forma de pago.
- **Vigencia de la cotización** (días) y nombre del vendedor.
- Si el modelo exacto no está: **sustituto** con especificación equivalente.

El detalle del mensaje está en [`solicitud-plantilla.md`](solicitud-plantilla.md).

---

## 4. Detalle por proveedor

### 4.1 Electromanía

- **Canal:** <https://www.electromania.pe/> · Lima · venta por WhatsApp · envío desde S/ 10.
- **Prioridad:** 1 (LiDAR, motores, ToF, sensores y e-stop).
- **Sube mucho respecto de la v0.1:** el **TFmini Plus pasa de 2 a 4 unidades**
  (1 dron + 2 rover principal + 1 mini-rover) y el **LiDAR se asigna al rover
  principal**. El stock declarado era de **8** ToF: alcanza, pero pedir reserva.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | LiDAR 2D 360° | RPLIDAR A1M8-R6 12 m (Slamtec) | RP | 1 | S/ 600,00 | S/ 600,00 | Quedaban 12 | [ver](https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/) |
| 2 | ToF de piso | TFmini Plus 12 m UART/I²C IP65 | MR + DR + RP | 4 | S/ 330,00 | S/ 1.320,00 | Solo quedan 8 | [ver](https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/) |
| 3 | Motorreductor 12 V con encoder | FIT0185 83 rpm 45 kg·cm | MR | 2 | S/ 145,00 | S/ 290,00 | En stock | [ver](https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/) |
| 4 | Cable FPC 22→15 | 300 mm para Pi 5 | DR | 2 | S/ 12,50 | S/ 25,00 | En stock | [ver](https://www.electromania.pe/producto/cable-para-camara-raspberry-pi-5-300mm/) |
| 5 | Regulador DC-DC | XL4005 5 A (4–38 V → 5 V) | MR + DR | 3 | S/ 6,59 | S/ 19,77 | En stock | [ver](https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/) |
| 6 | Monitor de batería | INA219 I²C | MR | 1 | S/ 12,50 | S/ 12,50 | En stock | [ver](https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/) |
| 7 | Fusibles de vidrio | Surtido 250 V | MR | 1 | S/ 12,00 | S/ 12,00 | En stock | [ver](https://www.electromania.pe/producto/100x-fusibles-de-vidrio-250v/) |
| 8 | Parada de emergencia | Seta enclavada 660 V 10 A | MR | 1 | S/ 8,00 | S/ 8,00 | En stock | [ver](https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/) |
| 9 | Capacitor 1000 µF low ESR | Protección del riel 5 V del dron | DR | 1 | ~S/ 5,00 | ~S/ 5,00 | Estimado | — |
| 10 | Dupont / JST / termorretráctil | Arnés del dron | DR | 1 | ~S/ 20,00 | ~S/ 20,00 | Estimado | — |
| | **Total** | | | **17** | | **S/ 2.287,27 + ~S/ 25** | | |

> **Sobre el LiDAR:** el repuesto de S/ 600 de Electromanía es el **RPLIDAR
> A1M8-R6 de Slamtec**, no un DFRobot (DFRobot es la marca del motorreductor
> FIT0185). Si el rover principal debe llevar otro modelo, hay que cambiarlo
> antes de enviar la solicitud.

### 4.2 Memory Kings

- **Canal:** <https://www.memorykings.pe/> · Lima · precio con IGV, **flete no incluido**.
- **Prioridad:** 1 (es el bloque más caro después de Electromanía).
- **Nuevo en la v0.2:** se añade la **Logitech Brio 4K para el mini-rover**, que
  no tiene doble CSI y por eso usa webcam USB en lugar del par estéreo.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Cámara web 4K | Elgato Facecam 4K · 040866 / 10WAF9901 | RP | 2 | S/ 828,00 | S/ 1.656,00 | > 10 | [ver](https://www.memorykings.pe/producto/354472/camara-webcam-elgato-facecam-4k-uhd-60fps) |
| 2 | Cámara web 4K | Logitech Brio 4K Ultra HD Pro | MR | 1 | S/ 487,00 | S/ 487,00 | > 10 | [catálogo](https://www.memorykings.pe/listados/176/camaras-webcam) |
| | **Total** | | | **3** | | **S/ 2.143,00** | | |

> La Brio salía en la lista a **S/ 487** como oferta (lista S/ 612). Pedir el SKU
> exacto y confirmar si la oferta sigue vigente; si no, la **Creative Live! Cam
> Sync 4K (S/ 261)** es la alternativa barata para el mini-rover.

### 4.3 The Pi Box

- **Canal:** <https://thepibox.pe/> · Lima (Chacarilla) · Olva Courier.
- **Prioridad:** 1 (cómputo y cámaras del dron).
- **Se quitó el HAT+ M.2 y la fuente de 27 W**: no van en ninguno de los tres
  proyectos. El dron arranca desde **microSD** (ver riesgo en §7.2).
- A lo mucho se añadiría **una microSD** para esa Pi 5; hoy está cotizada en
  Falabella y puede pedirse aquí si conviene juntar el envío.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Raspberry Pi 5 8 GB | Placa oficial | DR | 1 | S/ 768,00 | S/ 768,00 | En stock | [ver](https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444) |
| 2 | Cámara estéreo | Camera Module 3 Standard (IMX708) | DR | 2 | S/ 140,00 | S/ 280,00 | En stock | [ver](https://thepibox.pe/shop/cam-rp-006-camara-v3-estandar-raspberry-pi-3368) |
| 3 | Refrigeración | Active Cooler oficial | DR | 1 | S/ 29,90 | S/ 29,90 | En stock | [ver](https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454) |
| | **Total** | | | **4** | | **S/ 1.077,90** | | |

> Las dos cámaras deben ser **del mismo lote**: pedirlas juntas.

### 4.4 Bracsan

- **Canal:** <https://bracsan.pe/> · Jr. Paruro 1353 Int. 214, Cercado de Lima ·
  WhatsApp **950 970 761** · L–S 9:00–18:00.
- **Prioridad:** 1 (es la energía del mini-rover).
- **Nuevo en la v0.2:** se sustituye la batería LiFePO4 de Falabella por un
  **pack Li-ion 3S2P armado a mano** con celdas EVE de 3500 mAh, plaquitas de
  níquel y soldadura por punto.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Celda Li-ion 18650 | EVE INR18650/35V 3500 mAh | MR | 6 | S/ 19,00 | S/ 114,00 | En stock | [ver](https://bracsan.pe/producto/bateria-de-litio-li-ion-recargable-3-7v-3500mah-eve-inr18650-35v/) |
| 2 | BMS 3S | 25 A, 11,1/12,6 V | MR | 1 | S/ 18,00 | S/ 18,00 | En stock | [ver](https://bracsan.pe/producto/modulo-para-carga-de-baterias-de-li-ion-bms-3s-25a-11-1v-12v-12-6v-18650-bc-3s25a/) |
| 3 | Plaquita de níquel | Tira 1 m | MR | 1 | S/ 5,00 | S/ 5,00 | En stock | [ver](https://bracsan.pe/producto/platina-niquel-para-conexion-de-baterias-18650-x-metro-1mt/) |
| 4 | Espaciadores | 3×1 para 18650 | MR | 2 | S/ 0,60 | S/ 1,20 | En stock | [ver](https://bracsan.pe/producto/espaciadores-3x1-para-bateria-de-li-ion-3-celda-18650/) |
| 5 | Conector XT60 | Macho/hembra | MR | 1 | S/ 4,50 | S/ 4,50 | En stock | [ver](https://bracsan.pe/producto/conector-xt60-macho-hembra-bala-para-bateria-lipo-amass-xt60/) |
| 6 | Portafusible en línea | Mini cuchilla 12 A | MR | 1 | ref. S/ 15,90 | S/ 15,90 | **Confirmar** | [ref. Falabella](https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a) |
| 7 | Arnés del pack | Cable, termorretráctil, fusible | MR | 1 | ~S/ 20,00 | ~S/ 20,00 | Estimado | — |
| | **Total** | | | **13** | | **S/ 158,60 + ~S/ 20** | | |

> **Portafusible:** el equipo indica que Bracsan lo tiene; no se pudo confirmar
> SKU ni precio en el catálogo web (la búsqueda no devolvió el producto). Se deja
> con el precio de referencia de Falabella (S/ 15,90) y hay que confirmarlo en
> tienda al pedir el pack.
>
> **Soldadura por punto:** ver §6.2. No soldar celdas 18650 con cautín.

### 4.5 Falabella (marketplace)

- **Canal:** <https://www.falabella.com.pe/> · despacho a domicilio; algunos
  productos se envían desde EE. UU.
- **Prioridad:** 2.
- **Queda muy reducida:** sin batería, sin SSD, sin M.2, sin caja USB y sin
  cargador.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | microSD 64 GB A2 | SanDisk Extreme Pro | MR + DR | 2 | S/ 64,90 | S/ 129,80 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador) |
| 2 | Desconectador de batería | 12–48 V universal | MR | 1 | S/ 46,90 | S/ 46,90 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco) |
| | **Total** | | | **3** | | **S/ 176,70** | | |

> El desconectador también podría estar en Bracsan: preguntar. Si lo tienen, se
> mueve y Falabella queda solo con las microSD. **Ojo:** es marketplace; pedir
> cotización con el vendedor real y su RUC.

### 4.6 Naylamp Mechatronics

- **Canal:** <https://naylampmechatronics.com/> · envío gratis a todo el Perú desde S/ 200.
- **Prioridad:** 2.
- **Se quitó el perfil V-Slot 2040**: ya lo tienen.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Driver de motor | BTS7960 43 A | MR | 2 | S/ 45,00 | S/ 90,00 | En stock | [ver](https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html) |
| 2 | Aisladores de vibración | Silicona M3 (4–8 puntos) | DR | 1 | ~S/ 25,00 | ~S/ 25,00 | Estimado | [ver](https://naylampmechatronics.com/) |
| 3 | Tornillería e insertos | M2,5 / M3 | DR | 1 | ~S/ 35,00 | ~S/ 35,00 | Estimado | [ver](https://naylampmechatronics.com/72-tornillos-y-tuercas) |
| 4 | Tornillos y tuercas | M3/M4 + tuercas en T | MR | 1 | ~S/ 50,00 | ~S/ 50,00 | Estimado | [ver](https://naylampmechatronics.com/72-tornillos-y-tuercas) |
| | **Total** | | | **5** | | **S/ 90,00 + ~S/ 110** | | |

### 4.7 Electronics Peru

- **Canal:** <https://www.electronicsperu.com/> · **Ica** · envío a coordinar.
- **Prioridad:** 2 (única tienda con stock claro del BNO085).
- Es la única línea con despacho desde Ica: confirmar plazo.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | IMU 9-DOF | BNO085 (AHRS) | MR | 1 | S/ 100,00 | S/ 100,00 | En stock | [ver](https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/) |
| | **Total** | | | **1** | | **S/ 100,00** | | |

### 4.8 Cableado por decidir

Figuran en los BOM como "Naylamp **o** Electromanía". Se piden a **un solo
proveedor** para no duplicar el envío.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Enlace |
|---:|---|---|---|---:|---:|---:|---|
| 1 | Cable y conectores | XT60/XT30, 14–18 AWG + termorretráctil | MR | 1 | ~S/ 80,00 | ~S/ 80,00 | [Naylamp XT60](https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html) |
| 2 | Conectores / cable / fusible / interruptor | XT60/XT30, 18–20 AWG, fusible 5 A | DR | 1 | ~S/ 60,00 | ~S/ 60,00 | [Naylamp conectores](https://naylampmechatronics.com/216-conectores-xt) |
| | **Total** | | | **2** | | **~S/ 140,00** | |

### 4.9 Cargador solar 3S (CN3722)

- **Canal:** importación o consultar disponibilidad en Hifisac / Bracsan.
- **Prioridad:** 3.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Nota |
|---:|---|---|---|---:|---:|---:|---|
| 1 | Cargador solar MPPT 3S | CN3722, 3S 12,6 V, 3 A (entrada 7,5–28 V) | MR | 1 | ~S/ 50,00 | ~S/ 50,00 | Para 3 celdas (12,6 V); ver §6.1 |
| | **Total** | | | **1** | | **~S/ 50,00** | |

> Referencia internacional del módulo: [CN3722 3S 12,6 V MPPT](https://il.dhgate.com/product/12v-mppt-solar-charger-controller-module/997131045.html).
> **El TP5100 no sirve para este pack** (ver §6.1).

### 4.10 Taller / tienda local

Sin proveedor definido: piezas y cables a medida del bloque de visión del
rover-principal. Se cotizan en Lima.

| # | Ítem | Alcance | Proy. | Cant. | P. unit. | Subtotal |
|---:|---|---|---|---:|---:|---:|
| 1 | Montaje rígido de visión | Barra de aluminio + soportes a medida para 2 cámaras | RP | 1 | ~S/ 250,00 | ~S/ 250,00 |
| 2 | Cables USB 3.0 + hub | Cables certificados y hub alimentado | RP | 1 | ~S/ 150,00 | ~S/ 150,00 |
| | **Total** | | | **2** | | **~S/ 400,00** |

### 4.11 Varios / ferretería

Consumibles y repuestos. No se pide cotización formal.

| # | Ítem | Proy. | Cant. | P. unit. | Subtotal | Nota |
|---|---|---:|---:|---:|---:|---|
| 1 | Repuestos: fusibles, cable, conectores | MR | 1 | ~S/ 50,00 | ~S/ 50,00 | Crítico para la demo |
| 2 | Repuestos: fusibles, cable, conectores | DR | 1 | ~S/ 30,00 | ~S/ 30,00 | — |
| 3 | USB-C corto + ferrita | DR | 1 | ~S/ 25,00 | ~S/ 25,00 | Alimentación del Pi 5 |
| 4 | Térmicos / espuma / velcro | DR | 1 | ~S/ 15,00 | ~S/ 15,00 | Almohadilla y fijación |
| 5 | Accesorios de caja (ventilador, rejilla, espuma) | MR | 1 | ~S/ 30,00 | ~S/ 30,00 | No va en el pedido a The Pi Box |
| | **Total** | | **5** | | **~S/ 150,00** | |

---

## 5. Cambios de esta revisión (v0.1 → v0.2)

| # | Corrección del equipo | Efecto en el consolidado |
|---:|---|---|
| 1 | El LiDAR 360 de S/ 600 es para el **rover principal**, no para el mini-rover | RP +1 LiDAR; **MR queda sin LiDAR** (ver §6.3) |
| 2 | ToF: **1 dron, 2 rover principal, 1 mini-rover** | TFmini Plus de 2 → **4 unidades** (+S/ 660) |
| 3 | Pi Box: **el HAT no va en ninguno** | −1 HAT+ M.2 (−S/ 60) |
| 4 | Pi Box: **la fuente 27 W tampoco** | −2 fuentes (−S/ 134) |
| 5 | Pi Box: a lo mucho **una microSD** | microSD sigue en Falabella; nota en §4.3 |
| 6 | Memory Kings: **añadir Logitech para el mini-rover** | +1 Brio 4K (+S/ 487) |
| 7 | Falabella: **sin batería** → pack de celdas Bracsan soldadas por punto | −S/ 239; nuevo bloque Bracsan (+S/ 158,60) |
| 8 | Falabella: **sin SSD, sin M.2, sin caja USB** | −S/ 360,50 |
| 9 | Falabella: **sin cargador** → módulo con panel solar | −S/ 200; +CN3722 (~S/ 50) |
| 10 | Falabella: **portafusibles en Bracsan** | línea movida (precio de referencia) |
| 11 | Naylamp: **el perfil ya lo tienen** | −S/ 160 |
| 12 | **Impresión 3D en local** | −S/ 300 (Print3D.pe sale del pedido) |
| 13 | **UBEC**: ¿para qué es y hay regulador local? | −S/ 120 de importación; +1 XL4005 (−S/ 113,41 neto). Ver §6.4 |

**Balance:** de ~S/ 7.135,68 a **~S/ 6.928,47** (−S/ 207,21), pero con +S/ 1.366
en equipo nuevo (4 ToF, webcam del mini-rover, pack de batería, cargador solar y
regulador del dron) compensado por las bajas de SSD, batería, cargador, fuente,
HAT, perfil, impresión 3D y UBEC.

---

## 6. Respuestas a las consultas técnicas

### 6.1 ¿Sirve el TP5100 para cargar el pack?

**No para un pack 3S.** El TP5100-84 que vende Hifisac es un cargador **seleccionable
4,2 / 8,4 V**, es decir, para packs de **1 o 2 celdas**; [cuesta S/ 5,60](https://hifisac.com/shop/category/baterias-240?search=cargador).
El pack Li-ion del rover es **3S (12,6 V de carga)** porque los motores son de 12 V.

| Opción | Voltaje | Sirve para 3S | Estado |
|---|---|---|---|
| TP5100-84 | 4,2 / 8,4 V | **No** (solo 1S/2S) | Disponible en Hifisac, S/ 5,60 |
| **CN3722 MPPT** | 12,6 V, 3 A, entrada 7,5–28 V | **Sí** | Importación, ~S/ 50 landed |
| Cargador 12,6 V 3 A de Bracsan | 12,6 V | Sí, pero de red | S/ 48 (no solar) |

**Con los paneles del inventario** (4 × 6 V / 720 mA) la combinación correcta es
**3 paneles en serie = 18 V** y el **CN3722** como controlador MPPT (el 4.º queda
de repuesto). Rendimiento esperado: ~13 W de entrada → **~0,8 A a 12,6 V**, o sea
unas **9 h de sol** para recargar un pack 3S2P de 7 Ah. Sirve como carga de
mantenimiento, no como reemplazo del cargador de red.

**Decisión pendiente:** si el pack necesita recargarse rápido en taller, conviene
tener **también** el cargador de red de Bracsan (S/ 48) además del módulo solar.

### 6.2 Soldadura por punto del pack

No se encontró un **servicio** publicado de soldadura por punto en Lima. Rutas
concretas:

| Opción | Costo | Nota |
|---|---:|---|
| Soldador portátil de Bracsan | S/ 390 | Herramienta reutilizable; [ficha](https://bracsan.pe/producto/soldador-de-punto-portatil-recargable-10000mah-para-bateria/) |
| Pedir a Bracsan que suelde el pack | a cotizar | Están en Jr. Paruro 1353; preguntar por WhatsApp **950 970 761** |
| Soldador de 5000 W tipo Sodimac/Falabella | precio no publicado | [ficha Sodimac](https://www.sodimac.com.pe/sodimac-pe/articulo/132104688/Soldador-De-Puntos-Para-Baterias-y-pilas-18650-regulable-5000w/132104689) |

Es una **herramienta compartida**, no un consumible: si el taller de la facultad
la consigue, el pack se arma sin comprarla. **No soldar celdas 18650 con cautín**
(regla del propio proyecto): el calor daña la celda y la unión no aguanta.

### 6.3 El mini-rover queda sin LiDAR

Con el LiDAR asignado al rover principal, el mini-rover **no tiene LiDAR 360° en
esta cotización**, y su pila de navegación (Nav2 + AMCL) lo necesita. Dos salidas:

1. **Añadir una segunda unidad** del RPLIDAR A1M8 (+S/ 600) → total ~S/ 7.528,47.
2. Usar un **RPLIDAR C1 (S/ 450)** para el mini-rover, o un LiDAR del inventario
   de facultad (hoy no hay ninguno listado).

**Recomendación:** definir esto antes de enviar la solicitud a Electromanía,
porque cambia la cantidad de 1 a 2.

### 6.4 El UBEC del dron: qué es y qué usar en su lugar

El **UBEC 5 V / 5 A** es un **regulador DC-DC** que baja la tensión de la batería
del dron (2–6S, hasta 25,2 V) a los **5 V / 5 A** que pide la Raspberry Pi 5.
Matek BEC12S-PRO es una versión "de vuelo": liviana y de bajo ruido, por eso
costaba ~S/ 120 importada.

| Opción local | Precio | Entrada | Nota |
|---|---:|---|---|
| **XL4005 5 A** (Electromanía) | S/ 6,59 | 4–38 V | Ya se usa en el mini-rover; acepta 6S (25,2 V). Añadir capacitor y verificar ripple |
| XH-M249 5 A (Hifisac) | S/ 10,00 | 24/12 V nominal | Sirve para 4S; **marginal para 6S** |
| XL4015 5 A (Hifisac) | S/ 9,40 | 4–38 V | **Agotado** al consultar |

Se toma el **XL4005** como base (1 unidad extra para el dron). Si el equipo
considera crítico el ruido de conmutación o el peso, el Matek BEC vuelve como
alternativa (+~S/ 113). Para el riel del dron conviene **derratear a 3 A** y
poner el capacitor de 1000 µF que ya está en la BOM.

### 6.5 Otras notas

- **Sin HAT+ M.2 ni SSD**, el dron arranca desde **microSD**: es más lento y más
  frágil ante cortes de energía. El propio BOM del dron ya lo registra como riesgo
  (`drone/docs/04-diseno/bom.md` §2).
- **Pack 3S2P (6 celdas) ≈ 78 Wh** frente a los 128 Wh de la LiFePO4 que se
  retiró. Si se necesita más autonomía, **3S3P (9 celdas) ≈ 117 Wh** cuesta
  ~S/ 88 más (celdas + níquel + espaciadores).
- **Impresión 3D local:** ruedas, placas y soportes del dron se imprimen en casa;
  no entran en la cotización. Si falta filamento, va como consumible.

---

## 7. Exclusiones, supuestos y avisos

### 7.1 La copia de la BOM en `rover-principal/` **no se suma**

`rover-principal/docs/04-diseno/bom-peru.csv` se titula **"BOM de electrónica
cotizada en Perú (mini demo)"** y reproduce la BOM del mini-rover comprando Pi 5
y Active Cooler en lugar de reutilizar la Pi 4 y la Argon ONE del inventario. Su
total documentado es **S/ 3.317,98**.

| Variante | Qué cambia | Total | ¿Se cotiza? |
|---|---|---:|---|
| BOM del mini demo comprando todo | Bloque MR completo + Pi 5 + Active Cooler | S/ 3.317,98 | **No**, salvo decisión expresa |

> La copia además quedó **desactualizada** con esta revisión: todavía incluye
> batería LiFePO4, SSD, caja USB, cargador y perfil de aluminio.

### 7.2 No se cotiza (inventario existente)

| Ítem | Cant. | Fuente | Por qué |
|---|---:|---|---|
| Raspberry Pi 4 Model B 8 GB | 1 | Inventario de facultad (`mini-rover/inventario actual.txt`) | Se reutiliza (ADR-0010) |
| Carcasa Argon ONE V2 | 1 | Inventario de facultad | Se reutiliza; verificar acceso al CSI |
| Perfil V-Slot 2040 | 1 | Ya lo tiene el equipo | — |
| Impresión 3D (ruedas, placas, soportes) | 5 piezas | Taller local | Se imprimen en casa |
| Paneles solares 6 V / 720 mA | 4 | Inventario de facultad | Alimentan el CN3722 (3 en serie) |

### 7.3 Alternativas del dron (no incluidas)

Sustituyen líneas del bloque DR; **no** se suman.

| Alternativa | Reemplaza | Precio | Proveedor |
|---|---|---:|---|
| 2 × Camera Module 3 **Wide** | CM3 Standard | S/ 195 c/u | The Pi Box |
| ToF VL53L5CX 8×8 (4 m) | TFmini Plus | S/ 190 | Adafruit (importación) |
| ToF VL53L1X (4 m) | TFmini Plus | S/ 75 | Naylamp |
| 2 × cámara global shutter OV9281 | CM3 Standard | S/ 200 c/u | Electromanía |
| Matek BEC12S-PRO | XL4005 | ~S/ 120 landed | ZoneFPV |
| Memoria USB 3.0 128 GB | microSD | S/ 80 | The Pi Box |
| Raspberry Pi 5 16 GB | Pi 5 8 GB | S/ 1.699 | The Pi Box |

> Los ToF de 4 m **no sirven** para volar a 6 m: solo banco o vuelo ≤ 4 m.

### 7.4 Alternativas de visión del rover-principal (no incluidas)

| Alternativa | Reemplaza | Precio | Proveedor |
|---|---|---:|---|
| TFmini-S 12 m (C010A-SEN0259) | TFmini Plus | S/ 299 (quedan 3) | Electromanía |
| LIDAR-Lite v3HP | LiDAR 360 / TFmini | S/ 850 (quedan 11) | Electromanía |
| DFRobot 4 m I²C IP67 | ToF near-field | S/ 115 (quedan 3) | Electromanía |
| VL53L1X | DFRobot 4 m | S/ 75 | Naylamp |
| VL53L8CX 8×8 carrier | ToF multizona | USD 24,95 + envío | Pololu (importación) |
| Creative Live! Cam Sync 4K | Logitech Brio 4K (MR) | S/ 261 | Memory Kings |
| Logitech Brio 4K | Elgato Facecam 4K (RP) | S/ 487 | Memory Kings |

### 7.5 Add-ons y estudios (no incluidos)

| Bloque | Contenido | Monto | Estado |
|---|---|---:|---|
| Interfaz de tiempo real | ESP32-S3/C6/XIAO + TCA9548A + level shifter + PC817 + arnés | ~S/ 195 | Propuesta; depende de `OQ` de arquitectura |
| Pack 3S3P | 9 celdas + BMS + níquel 10 m + espaciadores + XT60 | ~S/ 246,80 | Alternativa si se necesita autonomía |
| Soldador de punto | Portátil 10 000 mAh | S/ 390 | Herramienta opcional (§6.2) |
| Estudio 6×6 | `mini-rover/docs/04-diseno/energia/bom-6x6.md` | — | Pendiente de `OQ-09`; **no comprar** |

### 7.6 Supuestos de este consolidado

> **Supuesto 1:** se construyen los tres bloques (MR + DR + RP-visión) y se
> reutiliza la Pi 4 8 GB y la Argon ONE del inventario de facultad.
> **Supuesto 2:** el rover-principal usa la BOM de visión V-A (2 × Elgato + 2 ×
> TFmini Plus + LiDAR 360 + montaje + cables).
> **Supuesto 3:** el pack del mini-rover es **3S2P** (6 celdas) y se carga con
> **CN3722 + 3 paneles de 6 V en serie**.
> **Supuesto 4:** los precios son los del catálogo web del 2026-11-21; no hubo
> reserva ni consulta a los vendedores. Las averiguaciones del 2026-11-23
> (TP5100, CN3722, reguladores, soldadura) son de referencia y están marcadas.
> **Supuesto 5:** no se suman envíos, aduanas, IGV no declarado ni fluctuación
> del tipo de cambio (S/ 3,75 por USD en los estudios de origen).
> **Supuesto 6:** las líneas con `~` son estimaciones de planificación y deben
> reemplazarse por la cotización real del proveedor.

---

## 8. Pendientes en los BOM de origen

Este consolidado ya no coincide con los CSV de cada subproyecto. Hay que aplicar
los mismos cambios allí para que la fuente de verdad no diverja:

| Subproyecto | Archivo | Cambios pendientes |
|---|---|---|
| Mini-rover | `docs/04-diseno/bom-peru.csv` | Quitar LiFePO4, cargador, SSD SATA, caja USB, perfil; añadir pack Bracsan, CN3722, webcam Logitech; pasar el LiDAR a RP; definir si lleva LiDAR propio |
| Mini-rover | `docs/04-diseno/bom-peru-addons.csv` | El pack 3S2P deja de ser add-on y pasa a ser la energía base |
| Drone | `docs/04-diseno/bom-peru.csv` | Quitar HAT, fuente, SSD NVMe y UBEC; añadir XL4005 y el ToF ya estaba; aclarar arranque por microSD |
| Rover-principal | `docs/04-diseno/bom-vision.csv` | Añadir LiDAR 360 y el segundo TFmini Plus |

---

## 9. Trazabilidad

| Dato | Archivo de origen |
|---|---|
| Bloque MR | `mini-rover/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../mini-rover/docs/04-diseno/bom-peru.md) |
| Bloque DR | `drone/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../drone/docs/04-diseno/bom-peru.md) |
| Bloque RP visión | `rover-principal/docs/04-diseno/bom-vision.csv` y [`bom-vision.md`](../../rover-principal/docs/04-diseno/bom-vision.md) |
| Pack de batería | `mini-rover/docs/04-diseno/bom-peru-addons.csv` (bloques 3S2P y 3S3P) |
| Variante excluida | `rover-principal/docs/04-diseno/bom-peru.csv` (copia del mini demo) |
| Fuentes `F-xx` | `docs/01-investigacion/fuentes.md` de cada subproyecto |
| Averiguaciones v0.2 | Hifisac (TP5100 S/ 5,60 · XH-M249 S/ 10 · XL4015 S/ 9,40 agotado), Bracsan (WhatsApp 950 970 761), CN3722 (importación) y soldadura por punto (Sodimac/Bracsan) — consultadas el 2026-11-23 |
| Versión tabular | [`bom-consolidado.csv`](bom-consolidado.csv) |

---

## 10. Estado y control de cambios

- **No** se ha comprado, reservado ni consultado a ningún proveedor.
- Los precios de producto son de catálogo web al **2026-11-21**; las
  averiguaciones técnicas son del **2026-11-23** y están marcadas como tales.
- Cualquier cambio de cantidad o modelo se registra antes en el BOM del
  subproyecto y luego aquí.
- Las cotizaciones recibidas se archivan como evidencia **cuando se abra la fase
  de compras**; mientras tanto este documento queda en estado `Pendiente`.
