# BOM consolidado por proveedor — solicitud de cotizaciones

> **Estado:** Borrador de planificación · **Versión:** 0.4 · **Fecha:** 2026-11-23
> **Responsable:** equipo Kairos (ERC) · **Moneda:** soles peruanos (PEN) salvo indicación
> **Precios:** catálogo web consultado el **2026-11-21** por cada subproyecto.
> **No autoriza compra ni reserva.** No se ha contactado a ningún proveedor.
>
> **Cambios de la v0.4 (2026-11-23):** LiDAR para **3 unidades** (1 mini-rover +
> **2 rover principal**, con alternativa de 3 en el rover principal); **boost
> 7,4 → 12 V** para recuperar velocidad en la tracción del mini-rover. Las tablas
> ahora muestran la cantidad de cada proyecto en columnas separadas.

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

Leyenda: **MR** = Mini-rover · **DR** = Drone · **RP** = Rover-principal ·
**Tot.** = cantidad total a cotizar. Precio: `S/` verificado · `~S/` estimación ·
`ref.` precio de referencia.

---

## 2. Resumen por proveedor

| Proveedor | Líneas | MR | DR | RP | Unid. | Verificado | Estimado | Prior. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [Electromanía](#41-electromanía) | 10 | 9 | 6 | 4 | 19 | S/ 3.487,27 | ~S/ 25 | 1 |
| [Memory Kings](#42-memory-kings) | 2 | 1 | 0 | 2 | 3 | S/ 2.143,00 | — | 1 |
| [The Pi Box](#43-the-pi-box) | 3 | 0 | 4 | 0 | 4 | S/ 1.077,90 | — | 1 |
| [Bracsan](#44-bracsan) | 7 | 17 | 0 | 0 | 17 | S/ 197,80 | ~S/ 20 | 1 |
| [Falabella](#45-falabella-marketplace) | 2 | 2 | 1 | 0 | 3 | S/ 176,70 | — | 2 |
| [Naylamp Mechatronics](#46-naylamp-mechatronics) | 4 | 3 | 2 | 0 | 5 | S/ 90,00 | ~S/ 110 | 2 |
| [Electronics Peru](#47-electronics-peru) | 1 | 1 | 0 | 0 | 1 | S/ 100,00 | — | 2 |
| [Hifisac](#48-hifisac-cargador-tp5100) | 1 | 1 | 0 | 0 | 1 | S/ 5,60 | — | 2 |
| [MTLAB](#49-mtlab-boost-para-la-tracción) | 1 | 1 | 0 | 0 | 1 | — | ~S/ 55 | 2 |
| [Cableado por decidir](#410-cableado-por-decidir) | 2 | 1 | 1 | 0 | 2 | — | ~S/ 140 | 2 |
| [Taller / tienda local](#411-taller--tienda-local) | 2 | 0 | 0 | 2 | 2 | — | ~S/ 400 | 4 |
| [Varios / ferretería](#412-varios--ferretería) | 5 | 2 | 3 | 0 | 5 | — | ~S/ 150 | 4 |
| **Total** | **40** | **38** | **17** | **8** | **63** | **S/ 7.278,27** | **~S/ 900,00** | |

> **Total consolidado: ~S/ 8.178,27** (sin envío, sin IGV adicional y sin aduanas).
> No incluye la copia de la BOM del mini demo de `rover-principal/` (§7.1), ni
> alternativas, ni add-ons, ni el estudio 6×6, ni la impresión 3D (local).

### 2.1 Totales por proyecto

| Escenario | Verificado | Estimado | Total |
|---|---:|---:|---:|
| Solo Mini-rover (MR) | S/ 2.257,88 | ~S/ 285 | S/ 2.542,88 |
| Solo Drone (DR) | S/ 1.504,39 | ~S/ 215 | S/ 1.719,39 |
| Solo Rover-principal, bloque visión (RP) | S/ 3.516,00 | ~S/ 400 | S/ 3.916,00 |
| Mini-rover + Drone | S/ 3.762,27 | ~S/ 500 | S/ 4.262,27 |
| **Los tres (MR + DR + RP)** | **S/ 7.278,27** | **~S/ 900** | **S/ 8.178,27** |
| *Alternativa:* RP con **3 LiDAR** en vez de 2 | S/ 7.878,27 | ~S/ 900 | **~S/ 8.778,27** |

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
- **Ojo con el LiDAR:** se piden **3 unidades** (1 mini-rover + 2 rover principal).
  El stock declarado era de 12 → alcanza, pero confirmar reserva.
- **Ojo con el ToF:** el stock declarado era de **8** y se piden **4**.

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [LiDAR 2D 360° — RPLIDAR A1M8-R6 12 m](https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/) | 1 | 0 | 2 | 3 | S/ 600,00 | S/ 1.800,00 | Quedaban 12 |
| 2 | [ToF de piso — TFmini Plus 12 m](https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/) | 1 | 1 | 2 | 4 | S/ 330,00 | S/ 1.320,00 | Solo quedan 8 |
| 3 | [Motorreductor 12 V con encoder — FIT0185 83 rpm 45 kg·cm](https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/) | 2 | 0 | 0 | 2 | S/ 145,00 | S/ 290,00 | En stock |
| 4 | [Cable FPC 22→15 para Pi 5, 300 mm](https://www.electromania.pe/producto/cable-para-camara-raspberry-pi-5-300mm/) | 0 | 2 | 0 | 2 | S/ 12,50 | S/ 25,00 | En stock |
| 5 | [Regulador DC-DC XL4005 5 A (4–38 V → 5 V)](https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/) | 2 | 1 | 0 | 3 | S/ 6,59 | S/ 19,77 | En stock |
| 6 | [Monitor de batería INA219 I²C](https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/) | 1 | 0 | 0 | 1 | S/ 12,50 | S/ 12,50 | En stock |
| 7 | [Fusibles de vidrio surtido 250 V](https://www.electromania.pe/producto/100x-fusibles-de-vidrio-250v/) | 1 | 0 | 0 | 1 | S/ 12,00 | S/ 12,00 | En stock |
| 8 | [Parada de emergencia, seta enclavada 660 V 10 A](https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/) | 1 | 0 | 0 | 1 | S/ 8,00 | S/ 8,00 | En stock |
| 9 | Capacitor 1000 µF low ESR (riel 5 V del dron) | 0 | 1 | 0 | 1 | ~S/ 5,00 | ~S/ 5,00 | Estimado |
| 10 | Dupont / JST / termorretráctil (arnés del dron) | 0 | 1 | 0 | 1 | ~S/ 20,00 | ~S/ 20,00 | Estimado |
| | **Total** | **9** | **6** | **4** | **19** | | **S/ 3.487,27 + ~S/ 25** | |

> El repuesto de S/ 600 es el **RPLIDAR A1M8-R6 de Slamtec**, no un DFRobot
> (DFRobot es la marca del motorreductor FIT0185).

### 4.2 Memory Kings

- **Canal:** <https://www.memorykings.pe/> · Lima · precio con IGV, **flete no incluido**.
- **Prioridad:** 1 (el bloque más caro después de Electromanía).

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Cámara web 4K — Elgato Facecam 4K · 040866 / 10WAF9901](https://www.memorykings.pe/producto/354472/camara-webcam-elgato-facecam-4k-uhd-60fps) | 0 | 0 | 2 | 2 | S/ 828,00 | S/ 1.656,00 | > 10 |
| 2 | [Cámara web 4K — Logitech Brio 4K Ultra HD Pro](https://www.memorykings.pe/listados/176/camaras-webcam) | 1 | 0 | 0 | 1 | S/ 487,00 | S/ 487,00 | > 10 |
| | **Total** | **1** | **0** | **2** | **3** | | **S/ 2.143,00** | |

> La Brio del mini-rover va porque esa placa no tiene doble CSI. Salía a S/ 487
> como oferta (lista S/ 612): confirmar que sigue. Alternativa: Creative Live! Cam
> Sync 4K (S/ 261). La Facecam del rover principal sí es par estéreo.

### 4.3 The Pi Box

- **Canal:** <https://thepibox.pe/> · Lima (Chacarilla) · Olva Courier.
- **Prioridad:** 1 (cómputo y cámaras del dron).
- **Sin HAT+ M.2 y sin fuente de 27 W**: no van en ninguno de los tres proyectos.
  El dron arranca desde **microSD** (ver §6.5).

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Raspberry Pi 5 8 GB, placa oficial](https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444) | 0 | 1 | 0 | 1 | S/ 768,00 | S/ 768,00 | En stock |
| 2 | [Camera Module 3 Standard (IMX708)](https://thepibox.pe/shop/cam-rp-006-camara-v3-estandar-raspberry-pi-3368) | 0 | 2 | 0 | 2 | S/ 140,00 | S/ 280,00 | En stock |
| 3 | [Active Cooler oficial](https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454) | 0 | 1 | 0 | 1 | S/ 29,90 | S/ 29,90 | En stock |
| | **Total** | **0** | **4** | **0** | **4** | | **S/ 1.077,90** | |

> Las dos cámaras deben ser **del mismo lote**: pedirlas juntas. Si se quiere
> sumar la microSD del dron a este pedido, quitarla de Falabella.

### 4.4 Bracsan

- **Canal:** <https://bracsan.pe/> · Jr. Paruro 1353 Int. 214, Cercado de Lima ·
  WhatsApp **950 970 761** · L–S 9:00–18:00.
- **Prioridad:** 1 (es la energía del mini-rover).
- **Pack 2S4P:** 8 celdas, 7,4 V nominales, 8,4 V de carga, **14 Ah / 103,6 Wh**.

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Celda Li-ion 18650 — EVE INR18650/35V 3500 mAh](https://bracsan.pe/producto/bateria-de-litio-li-ion-recargable-3-7v-3500mah-eve-inr18650-35v/) | 8 | 0 | 0 | 8 | S/ 19,00 | S/ 152,00 | En stock |
| 2 | BMS **2S** 25 A, 7,4 / 8,4 V ([ref. 3S](https://bracsan.pe/producto/modulo-para-carga-de-baterias-de-li-ion-bms-3s-25a-11-1v-12v-12-6v-18650-bc-3s25a/)) | 1 | 0 | 0 | 1 | ref. S/ 18,00 | S/ 18,00 | **Confirmar 2S** |
| 3 | [Plaquita de níquel, tira 1 m](https://bracsan.pe/producto/platina-niquel-para-conexion-de-baterias-18650-x-metro-1mt/) | 1 | 0 | 0 | 1 | S/ 5,00 | S/ 5,00 | En stock |
| 4 | [Espaciadores 3×1 para 18650](https://bracsan.pe/producto/espaciadores-3x1-para-bateria-de-li-ion-3-celda-18650/) | 4 | 0 | 0 | 4 | S/ 0,60 | S/ 2,40 | En stock |
| 5 | [Conector XT60 macho/hembra](https://bracsan.pe/producto/conector-xt60-macho-hembra-bala-para-bateria-lipo-amass-xt60/) | 1 | 0 | 0 | 1 | S/ 4,50 | S/ 4,50 | En stock |
| 6 | Portafusible en línea, mini cuchilla 12 A ([ref. Falabella](https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a)) | 1 | 0 | 0 | 1 | ref. S/ 15,90 | S/ 15,90 | **Confirmar** |
| 7 | Arnés del pack: cable, termorretráctil, fusible | 1 | 0 | 0 | 1 | ~S/ 20,00 | ~S/ 20,00 | Estimado |
| | **Total** | **17** | **0** | **0** | **17** | | **S/ 197,80 + ~S/ 20** | |

> **BMS de 2 celdas:** el catálogo verificado muestra el **3S 25 A (S/ 18)**; se
> asume precio parecido para el **2S 25 A** y queda "confirmar". Alternativa
> comercial: HX-2S-D20 de 20 A (verificar los ~14 A de arranque de los motores).
>
> **Fusible:** a 7,4 V la corriente sube; usar **20–25 A** de curva lenta.
> **Emparejado:** las 8 celdas del mismo lote, medidas antes de soldar.
> **Soldadura por punto:** ver §6.2. No soldar celdas 18650 con cautín.

### 4.5 Falabella (marketplace)

- **Canal:** <https://www.falabella.com.pe/> · despacho a domicilio; algunos
  productos se envían desde EE. UU.
- **Prioridad:** 2. Sin batería, SSD, M.2, caja USB ni cargador.

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [microSD 64 GB A2 — SanDisk Extreme Pro](https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador) | 1 | 1 | 0 | 2 | S/ 64,90 | S/ 129,80 | Marketplace |
| 2 | [Desconectador de batería 12–48 V](https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco) | 1 | 0 | 0 | 1 | S/ 46,90 | S/ 46,90 | Marketplace |
| | **Total** | **2** | **1** | **0** | **3** | | **S/ 176,70** | |

> El desconectador también podría estar en Bracsan: preguntar. **Ojo:** es
> marketplace; pedir cotización con el vendedor real y su RUC.

### 4.6 Naylamp Mechatronics

- **Canal:** <https://naylampmechatronics.com/> · envío gratis desde S/ 200.
- **Prioridad:** 2. El perfil V-Slot ya lo tienen.

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Driver BTS7960, 43 A](https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html) | 2 | 0 | 0 | 2 | S/ 45,00 | S/ 90,00 | En stock |
| 2 | Aisladores de vibración, silicona M3 (4–8 puntos) | 0 | 1 | 0 | 1 | ~S/ 25,00 | ~S/ 25,00 | Estimado |
| 3 | [Tornillería e insertos M2,5 / M3](https://naylampmechatronics.com/72-tornillos-y-tuercas) | 0 | 1 | 0 | 1 | ~S/ 35,00 | ~S/ 35,00 | Estimado |
| 4 | [Tornillos y tuercas M3/M4 + tuercas en T](https://naylampmechatronics.com/72-tornillos-y-tuercas) | 1 | 0 | 0 | 1 | ~S/ 50,00 | ~S/ 50,00 | Estimado |
| | **Total** | **3** | **2** | **0** | **5** | | **S/ 90,00 + ~S/ 110** | |

### 4.7 Electronics Peru

- **Canal:** <https://www.electronicsperu.com/> · **Ica** · envío a coordinar.
- **Prioridad:** 2 (única tienda con stock claro del BNO085).

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [IMU 9-DOF — BNO085 (AHRS)](https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/) | 1 | 0 | 0 | 1 | S/ 100,00 | S/ 100,00 | En stock |
| | **Total** | **1** | **0** | **0** | **1** | | **S/ 100,00** | |

### 4.8 Hifisac (cargador TP5100)

- **Canal:** <https://hifisac.com/> · Lima · venta por **WhatsApp +51 964 104 648**.
- **Prioridad:** 2. Con el pack en **2S**, el TP5100 carga a **8,4 V** (§6.1).

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Cargador Li-ion TP5100-84, 4,2 / 8,4 V, 2 A](https://hifisac.com/shop/category/baterias-240?search=cargador) | 1 | 0 | 0 | 1 | S/ 5,60 | S/ 5,60 | Disponible |
| | **Total** | **1** | **0** | **0** | **1** | | **S/ 5,60** | |

> Confirmar por WhatsApp que es la variante **TP5100-84**. Pedir un repuesto.

### 4.9 MTLAB (boost para la tracción)

- **Canal:** <https://mtlab.pe/> · Lima (San Martín de Porres) · Olva, S/ 10.
- **Prioridad:** 2. **Decisión del equipo (2026-11-23):** subir la tracción del
  mini-rover a 12 V para recuperar velocidad (§6.6).

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal | Stock 21-11 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | [Módulo Step-Up DC-DC 400 W (15 A), 7,4 → 12 V](https://mtlab.pe/producto/modulo-step-up-dc-dc-elevador-de-voltaje-150w-200w-400w/) | 1 | 0 | 0 | 1 | ~S/ 55,00 | ~S/ 55,00 | Cotizar |
| | **Total** | **1** | **0** | **0** | **1** | | **~S/ 55,00** | |

> El rango de la tienda es **S/ 25–55** según potencia (150 / 200 / 400 W). Se
> elige el de **400 W / 15 A** porque dos motores pueden pedir ~14 A de arranque
> a 12 V. El BTS7960 se mantiene como driver.

### 4.10 Cableado por decidir

Se piden a **un solo proveedor** (Naylamp o Electromanía) para no duplicar envío.

| # | Ítem y enlace | MR | DR | RP | Tot. | P. unit. | Subtotal |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | [Cable y conectores XT60/XT30, 14–18 AWG + termorretráctil](https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html) | 1 | 0 | 0 | 1 | ~S/ 80,00 | ~S/ 80,00 |
| 2 | [Conectores / cable / fusible 5 A, XT60/XT30 18–20 AWG](https://naylampmechatronics.com/216-conectores-xt) | 0 | 1 | 0 | 1 | ~S/ 60,00 | ~S/ 60,00 |
| | **Total** | **1** | **1** | **0** | **2** | | **~S/ 140,00** |

### 4.11 Taller / tienda local

Sin proveedor definido: piezas y cables a medida del bloque de visión.

| # | Ítem | MR | DR | RP | Tot. | P. unit. | Subtotal |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Montaje rígido de visión (barra de aluminio + soportes para 2 cámaras) | 0 | 0 | 1 | 1 | ~S/ 250,00 | ~S/ 250,00 |
| 2 | Cables USB 3.0 + hub alimentado | 0 | 0 | 1 | 1 | ~S/ 150,00 | ~S/ 150,00 |
| | **Total** | **0** | **0** | **2** | **2** | | **~S/ 400,00** |

### 4.12 Varios / ferretería

Consumibles y repuestos. No se pide cotización formal.

| # | Ítem | MR | DR | RP | Tot. | P. unit. | Subtotal |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | Repuestos: fusibles, cable, conectores (crítico para la demo) | 1 | 0 | 0 | 1 | ~S/ 50,00 | ~S/ 50,00 |
| 2 | Repuestos: fusibles, cable, conectores | 0 | 1 | 0 | 1 | ~S/ 30,00 | ~S/ 30,00 |
| 3 | USB-C corto + ferrita (alimentación del Pi 5) | 0 | 1 | 0 | 1 | ~S/ 25,00 | ~S/ 25,00 |
| 4 | Térmicos / espuma / velcro | 0 | 1 | 0 | 1 | ~S/ 15,00 | ~S/ 15,00 |
| 5 | Accesorios de caja (ventilador, rejilla, espuma) | 1 | 0 | 0 | 1 | ~S/ 30,00 | ~S/ 30,00 |
| | **Total** | **2** | **3** | **0** | **5** | | **~S/ 150,00** |

---

## 5. Cambios acumulados (v0.1 → v0.4)

| # | Corrección del equipo | Efecto |
|---:|---|---|
| 1 | ToF: **1 dron, 2 rover principal, 1 mini-rover** | TFmini Plus de 2 → **4 unidades** (+S/ 660) |
| 2 | Pi Box: **sin HAT+ M.2** | −S/ 60 |
| 3 | Pi Box: **sin fuente 27 W** | −S/ 134 |
| 4 | Memory Kings: **webcam para el mini-rover** | +1 Brio 4K (+S/ 487) |
| 5 | Falabella: **sin batería** → pack Bracsan | −S/ 239; bloque Bracsan |
| 6 | Falabella: **sin SSD, M.2 ni caja USB** | −S/ 360,50 |
| 7 | Falabella: **sin cargador** → módulo solar | −S/ 200; +TP5100 (S/ 5,60) |
| 8 | **Portafusibles en Bracsan** | línea movida (precio de referencia) |
| 9 | Naylamp: **el perfil ya lo tienen** | −S/ 160 |
| 10 | **Impresión 3D en local** | −S/ 300 |
| 11 | **UBEC → regulador local** | −S/ 113,41 neto (+1 XL4005) |
| 12 | **Pack 2S4P de 8 celdas** (7,4 V / 14 Ah) | +2 celdas (+S/ 38), +2 espaciadores (+S/ 1,20), BMS 2S, TP5100 en vez de CN3722 (−S/ 44,40) |
| 13 | **LiDAR: 3 unidades** (1 MR + 2 RP) | +S/ 1.200 respecto de la v0.3 (antes 1 en RP) |
| 14 | **Boost 7,4 → 12 V para la tracción** | +~S/ 55 (MTLAB) |

**Balance:** de ~S/ 7.135,68 (v0.1) a **~S/ 8.178,27** (+S/ 1.042,59), casi todo
explicado por el LiDAR extra y los 2 ToF adicionales.

---

## 6. Respuestas a las consultas técnicas

### 6.1 El TP5100 sí sirve: el pack es 2S

**Corrección sobre la v0.2.** Se asumió un pack 3S (12,6 V) y por eso se descartó
el TP5100. Con **2S4P (7,4 V nominales, 8,4 V de carga)** el TP5100-84 es el
módulo correcto:

| Dato | TP5100 | Fuente |
|---|---|---|
| Entrada | 5–18 V | [hoja de datos](https://www.utmel.com/components/understanding-of-tp5100-2a-lithium-battery-charger-module-faq?id=1856) |
| Tipo | Buck conmutado | ídem |
| Corriente de carga | hasta **2 A**, programable | ídem |
| Batería | **4,2 V (1S) o 8,4 V (2S)** | ídem |
| Precio local | **S/ 5,60** | [Hifisac](https://hifisac.com/shop/category/baterias-240?search=cargador) |

- **Paneles:** **2 en serie = 12 V**. **No 3 en serie**: el Voc ronda 21,6 V y
  supera el máximo de 18 V del TP5100.
- **Carga solar:** ~8,6 W → **~0,8 A a 8,4 V** → unas **16 h** para 14 Ah.
- **Carga rápida:** con fuente de 12 V / 2 A → **~7 h**.
- El **CN3722 (3S)** ya no aplica.

### 6.2 Soldadura por punto del pack

No se encontró un **servicio** publicado en Lima. Rutas:

| Opción | Costo | Nota |
|---|---:|---|
| Soldador portátil de Bracsan | S/ 390 | Herramienta reutilizable; [ficha](https://bracsan.pe/producto/soldador-de-punto-portatil-recargable-10000mah-para-bateria/) |
| Pedir a Bracsan que suelde el pack | a cotizar | Jr. Paruro 1353 · WhatsApp **950 970 761** |
| Soldador de 5000 W tipo Sodimac/Falabella | precio no publicado | [ficha Sodimac](https://www.sodimac.com.pe/sodimac-pe/articulo/132104688/Soldador-De-Puntos-Para-Baterias-y-pilas-18650-regulable-5000w/132104689) |

**No soldar celdas 18650 con cautín.**

### 6.3 LiDAR: 3 unidades (decisión del 2026-11-23)

| Vehículo | Unidades | Uso |
|---|---:|---|
| Mini-rover | **1** | navegación (Nav2 + AMCL) |
| Rover-principal | **2** | cobertura frontal + posterior |
| **Total a cotizar** | **3** | S/ 1.800 |

- **Alternativa:** el rover-principal con **3 unidades** (total 4 en el pedido) →
  **+S/ 600**, total del consolidado ~S/ 8.778,27.
- El modelo es el **RPLIDAR A1M8-R6 de 12 m** (S/ 600, Electromanía). Stock
  declarado: 12 unidades → alcanza para 3, confirmar reserva.
- Verificar que el frame ROS 2 soporte **dos LiDAR** en el rover-principal
  (dos `urg_node` o dos tópicos `scan` + fusión en `laser_filters`/`ira_laser_tools`).

### 6.4 El UBEC del dron: qué es y qué usar en su lugar

El **UBEC 5 V / 5 A** es un regulador DC-DC que baja la batería del dron (2–6S,
hasta 25,2 V) a **5 V / 5 A** para la Raspberry Pi 5. Matek BEC12S-PRO es la
versión "de vuelo" (liviana, bajo ruido), por eso costaba ~S/ 120 importada.

| Opción local | Precio | Entrada | Nota |
|---|---:|---|---|
| **XL4005 5 A** (Electromanía) | S/ 6,59 | 4–38 V | Ya en la BOM; acepta 6S. Añadir capacitor y verificar ripple |
| XH-M249 5 A (Hifisac) | S/ 10,00 | 24/12 V nominal | Sirve para 4S; marginal para 6S |
| XL4015 5 A (Hifisac) | S/ 9,40 | 4–38 V | **Agotado** |

Se usa el **XL4005** (1 unidad para el dron). El Matek vuelve como alternativa
(+~S/ 113) si el ruido o el peso son críticos. Derratear a 3 A.

### 6.5 Consecuencias del pack 2S4P

| Efecto | Número | Comentario |
|---|---|---|
| Energía | **103,6 Wh** | vs 128 Wh de la LiFePO4 retirada; vs 78 Wh del 3S2P |
| Peso | **~420 g** | la LiFePO4 de 10 Ah pesaba ~1,5 kg |
| Con boost (decisión) | **83 rpm → 0,39 m/s** | recupera la velocidad original con rueda de 90 mm |
| Sin boost | 51 rpm → 0,24 m/s | era la situación previa a la v0.4 |
| Corriente | sube para la misma potencia | fusible **20–25 A**; BMS 25 A alcanza |

- **Sin HAT+ M.2 ni SSD**, el dron arranca desde **microSD**: más lento y más
  frágil ante cortes. Ya está como riesgo en `drone/docs/04-diseno/bom.md` §2.
- **Impresión 3D local:** ruedas, placas y soportes del dron se imprimen en casa.

### 6.6 Alternativas de motor: se elige el boost

El par no era el problema (28 kg·cm a 7,4 V); lo era la velocidad. Comparación:

| Opción | Qué cambia | Velocidad (rueda 90 mm) | Par | Costo | Decisión |
|---|---|---:|---:|---|---|
| Dejar el FIT0185 a 7,4 V | nada | 0,24 m/s | ~28 kg·cm | S/ 0 | descartada |
| Ruedas de 110–120 mm | impresión 3D | 0,30–0,32 m/s | 28 kg·cm | S/ 0 | reserva |
| **Boost 7,4 → 12 V** | módulo elevador | **0,39 m/s** | 45 kg·cm | **~S/ 55** | **elegida** |
| Pololu 25D 6 V con encoder | motor de 6 V sobrealimentado | 0,75 m/s | ~11 kg·cm | importación | descartada |
| FIT0492-A 12 V 50 rpm | sin encoder | 0,15 m/s | ~31 kg·cm | S/ 69,90 | descartada |

**Implementación:** el boost va **solo en el riel de tracción** (BTS7960 → motores);
la electrónica sigue directa a la batería. Consecuencias a documentar en el BOM del
mini-rover: nuevo subsistema de potencia, pérdidas ~10 %, y `max_vel_x` de Nav2 a
0,35–0,39 m/s. **Descartados los TT de 6 V tipo FIT0450** (0,8 kg·cm).

---

## 7. Exclusiones, supuestos y avisos

### 7.1 La copia de la BOM en `rover-principal/` **no se suma**

`rover-principal/docs/04-diseno/bom-peru.csv` se titula **"BOM de electrónica
cotizada en Perú (mini demo)"** y reproduce la BOM del mini-rover comprando Pi 5
y Active Cooler en lugar de reutilizar la Pi 4 y la Argon ONE. Total documentado:
**S/ 3.317,98**. **No se cotiza**, salvo decisión expresa. Quedó desactualizada
(incluye LiFePO4, SSD, caja USB, cargador y perfil).

### 7.2 No se cotiza (inventario existente o trabajo local)

| Ítem | Cant. | Fuente | Por qué |
|---|---:|---|---|
| Raspberry Pi 4 Model B 8 GB | 1 | Inventario de facultad | Se reutiliza (ADR-0010) |
| Carcasa Argon ONE V2 | 1 | Inventario de facultad | Se reutiliza; verificar CSI |
| Perfil V-Slot 2040 | 1 | Ya lo tiene el equipo | — |
| Impresión 3D (ruedas, placas, soportes) | 5 piezas | Taller local | Se imprimen en casa |
| Paneles solares 6 V / 720 mA | 4 | Inventario de facultad | **2 en serie** para el TP5100 |

### 7.3 Alternativas del dron (no incluidas)

| Alternativa | Reemplaza | Precio | Proveedor |
|---|---|---:|---|
| 2 × Camera Module 3 **Wide** | CM3 Standard | S/ 195 c/u | The Pi Box |
| ToF VL53L5CX 8×8 (4 m) | TFmini Plus | S/ 190 | Adafruit (importación) |
| ToF VL53L1X (4 m) | TFmini Plus | S/ 75 | Naylamp |
| 2 × cámara global shutter OV9281 | CM3 Standard | S/ 200 c/u | Electromanía |
| Matek BEC12S-PRO | XL4005 | ~S/ 120 landed | ZoneFPV |
| Memoria USB 3.0 128 GB | microSD | S/ 80 | The Pi Box |
| Raspberry Pi 5 16 GB | Pi 5 8 GB | S/ 1.699 | The Pi Box |

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
| Tercer LiDAR en el rover principal | +1 RPLIDAR A1M8 | +S/ 600 | **Alternativa aprobada como opción** (§6.3) |
| Ruedas de 110–120 mm | cambio mecánico | S/ 0 | Reserva si el boost no basta (§6.6) |
| Soldador de punto | Portátil 10 000 mAh | S/ 390 | Herramienta opcional (§6.2) |
| Estudio 6×6 | `mini-rover/docs/04-diseno/energia/bom-6x6.md` | — | Pendiente de `OQ-09`; **no comprar** |

### 7.6 Supuestos de este consolidado

> **Supuesto 1:** se construyen los tres bloques y se reutiliza la Pi 4 8 GB y la
> Argon ONE del inventario de facultad.
> **Supuesto 2:** el rover-principal usa la BOM de visión V-A (2 × Elgato + 2 ×
> TFmini Plus + **2 LiDAR** + montaje + cables).
> **Supuesto 3:** el pack del mini-rover es **2S4P (8 celdas, 7,4 V, 14 Ah)** con
> **BMS 2S de 25 A**, carga por **TP5100 desde 2 paneles de 6 V en serie** y
> **boost de 400 W a 12 V** para la tracción.
> **Supuesto 4:** los precios de producto son del catálogo web del 2026-11-21; las
> averiguaciones técnicas son del 2026-11-23 y están marcadas.
> **Supuesto 5:** no se suman envíos, aduanas, IGV no declarado ni tipo de cambio.
> **Supuesto 6:** las líneas con `~` o `ref.` son estimaciones o referencias.

---

## 8. Estado de los BOM de origen

Los BOM de cada subproyecto se actualizaron el **2026-11-23** para coincidir con
este consolidado:

| Subproyecto | Archivo | Estado |
|---|---|---|
| Mini-rover | `bom-peru.csv` · `bom-peru.md` · `bom.md` | Actualizados: subtotal **S/ 2.542,88** y total con 5 % **S/ 2.670,02** |
| Drone | `bom-peru.csv` · `bom-peru.md` | Actualizados: base **S/ 1.719,39** y total **S/ 1.805,36**; `check_bom.py` ajustado a las nuevas cifras |
| Rover-principal | `bom-vision.csv` · `bom-vision.md` | Actualizados: V-A **~S/ 3.916,00** (2 LiDAR + 2 ToF) |
| Rover-principal | `bom-peru.csv` · `bom-peru.md` | Marcados como **documento heredado** del mini demo: no se cotiza desde ahí |

Comprobado con los validadores del repositorio: `check_docs.py` y `check_bom.py`
del dron y del mini-rover pasan sin errores ni advertencias.

Pendiente y no bloqueante para la cotización: añadir la entrada de bitácora de
cada subproyecto y registrar en el `fuentes.md` del dron las fuentes nuevas
(XL4005) si se quieren citar con `F-xx`.

---

## 9. Trazabilidad

| Dato | Archivo de origen |
|---|---|
| Bloque MR | `mini-rover/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../mini-rover/docs/04-diseno/bom-peru.md) |
| Bloque DR | `drone/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../drone/docs/04-diseno/bom-peru.md) |
| Bloque RP visión | `rover-principal/docs/04-diseno/bom-vision.csv` y [`bom-vision.md`](../../rover-principal/docs/04-diseno/bom-vision.md) |
| Celdas, BMS, níquel y accesorios | `mini-rover/docs/04-diseno/bom-peru-addons.csv` |
| Variante excluida | `rover-principal/docs/04-diseno/bom-peru.csv` (copia del mini demo) |
| Fuentes `F-xx` | `docs/01-investigacion/fuentes.md` de cada subproyecto |
| TP5100 (5–18 V, 2 A, 1S/2S) | [Hoja de datos](https://www.utmel.com/components/understanding-of-tp5100-2a-lithium-battery-charger-module-faq?id=1856) · [Hifisac](https://hifisac.com/shop/category/baterias-240?search=cargador) |
| Boost DC-DC 150–400 W | [MTLAB](https://mtlab.pe/producto/modulo-step-up-dc-dc-elevador-de-voltaje-150w-200w-400w/) |
| BMS 2S | Referencia del BMS 3S de Bracsan; ficha genérica [2S 7,4 V 25 A](https://www.didacticaselectronicas.com/shop/bms-2s-7-4v25a-tarjeta-de-proteccion-para-baterias-18650-2s-7-4v-25a-19719) |
| Soldadura por punto | [Bracsan](https://bracsan.pe/producto/soldador-de-punto-portatil-recargable-10000mah-para-bateria/) · [Sodimac](https://www.sodimac.com.pe/sodimac-pe/articulo/132104688/Soldador-De-Puntos-Para-Baterias-y-pilas-18650-regulable-5000w/132104689) |
| Versión tabular | [`bom-consolidado.csv`](bom-consolidado.csv) |

---

## 10. Estado y control de cambios

- **No** se ha comprado, reservado ni consultado a ningún proveedor.
- Precios de producto: catálogo web al **2026-11-21**; averiguaciones técnicas del
  **2026-11-23**.
- Los BOM de origen están **actualizados al 2026-11-23** (§8) y los validadores
  `check_docs.py` y `check_bom.py` pasan sin errores.
- Las cotizaciones se archivan como evidencia cuando se abra la fase de compras.
