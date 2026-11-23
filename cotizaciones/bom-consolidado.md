# BOM consolidado por proveedor — solicitud de cotizaciones

> **Estado:** Borrador de planificación · **Versión:** 0.1 · **Fecha:** 2026-11-23
> **Responsable:** equipo Kairos (ERC) · **Moneda:** soles peruanos (PEN) salvo indicación
> **Precios:** catálogo web consultado el **2026-11-21** por cada subproyecto.
> **No autoriza compra ni reserva.** No se ha contactado a ningún proveedor.

Este documento reúne las líneas de BOM de los tres subproyectos
(`mini-rover/`, `drone/`, `rover-principal/`), las agrupa **por proveedor** y calcula
las **cantidades totales** para enviar una sola solicitud de cotización a cada
empresa. Los BOM de origen no se modifican: siguen siendo la fuente de verdad de
cada subproyecto.

---

## 1. Cómo usar este documento

1. Abre la sección del proveedor y copia su tabla en la plantilla
   [`solicitud-plantilla.md`](solicitud-plantilla.md).
2. Envía la solicitud por el canal indicado (web, WhatsApp o correo).
3. Registra la respuesta en la tabla de seguimiento de la plantilla.
4. Si una cotización cambia una cantidad o un modelo, actualiza **primero** el BOM
   del subproyecto y luego este consolidado.

Leyenda de proyecto: **MR** = Mini-rover · **DR** = Drone · **RP** = Rover-principal.
Leyenda de precio: `S/` verificado en catálogo · `~S/` **estimación de
planificación** (no es cotización).

---

## 2. Resumen por proveedor

| Proveedor | Líneas | Unidades | Verificado | Estimado | Canal | Prioridad |
|---|---:|---:|---:|---:|---|---|
| [Electromanía](#41-electromanía) | 10 | 14 | S/ 1.620,68 | ~S/ 25 | electromania.pe · WhatsApp | 1 |
| [The Pi Box](#42-the-pi-box) | 6 | 8 | S/ 1.271,90 | ~S/ 30 | thepibox.pe | 1 |
| [Memory Kings](#43-memory-kings) | 1 | 2 | S/ 1.656,00 | — | memorykings.pe | 1 |
| [Falabella](#44-falabella-marketplace) | 8 | 9 | S/ 792,10 | ~S/ 200 | falabella.com.pe | 2 |
| [Naylamp Mechatronics](#45-naylamp-mechatronics) | 5 | 6 | S/ 250,00 | ~S/ 110 | naylampmechatronics.com | 2 |
| [Electronics Peru](#46-electronics-peru) | 1 | 1 | S/ 100,00 | — | electronicsperu.com | 2 |
| [Cableado por decidir](#47-cableado-por-decidir) | 2 | 2 | — | ~S/ 140 | Naylamp o Electromanía | 2 |
| [Print3D.pe](#48-print3dpe) | 3 | 6 | — | ~S/ 300 | print3d.pe | 3 |
| [Importación ZoneFPV](#49-importación-zonefpv--matek) | 1 | 1 | — | ~S/ 120 | zonefpv.com | 3 |
| [Taller / tienda local](#410-taller--tienda-local) | 2 | 2 | — | ~S/ 400 | sin proveedor | 4 |
| [Varios / ferretería](#411-varios--ferretería) | 4 | 4 | — | ~S/ 120 | local | 4 |
| **Total** | **43** | **55** | **S/ 5.690,68** | **~S/ 1.445,00** | | |

> **Total consolidado: ~S/ 7.135,68** (sin envío, sin IGV adicional y sin aduanas).
> No incluye la copia de la BOM del mini demo que está en `rover-principal/`
> (ver §5.1), ni alternativas, ni add-ons, ni el estudio 6×6.

### 2.1 Totales por proyecto

| Escenario | Verificado | Estimado | Total |
|---|---:|---:|---:|
| Solo Mini-rover (MR) | S/ 1.930,08 | ~S/ 590 | S/ 2.520,08 |
| Solo Drone (DR) | S/ 1.774,60 | ~S/ 455 | S/ 2.229,60 |
| Solo Rover-principal, bloque visión (RP) | S/ 1.986,00 | ~S/ 400 | S/ 2.386,00 |
| Mini-rover + Drone | S/ 3.704,68 | ~S/ 1.045 | S/ 4.749,68 |
| **Los tres (MR + DR + RP)** | **S/ 5.690,68** | **~S/ 1.445** | **S/ 7.135,68** |

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
- **Prioridad:** 1 (LiDAR, motores, sensores, ToF y e-stop).
- **Ojo:** el TFmini Plus aparece como "solo quedan 8"; se piden **2** (uno del
  dron y uno del rover-principal).

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | LiDAR 2D 360° | RPLIDAR A1M8-R6 12 m | MR | 1 | S/ 600,00 | S/ 600,00 | Quedaban 12 | [ver](https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/) |
| 2 | Motorreductor 12 V con encoder | FIT0185 83 rpm 45 kg·cm | MR | 2 | S/ 145,00 | S/ 290,00 | En stock | [ver](https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/) |
| 3 | ToF de piso | TFmini Plus 12 m UART/I²C IP65 | DR + RP | 2 | S/ 330,00 | S/ 660,00 | Solo quedan 8 | [ver](https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/) |
| 4 | Cable FPC 22→15 | 300 mm para Pi 5 | DR | 2 | S/ 12,50 | S/ 25,00 | En stock | [ver](https://www.electromania.pe/producto/cable-para-camara-raspberry-pi-5-300mm/) |
| 5 | Monitor de batería | INA219 I²C | MR | 1 | S/ 12,50 | S/ 12,50 | En stock | [ver](https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/) |
| 6 | Regulador DC-DC | XL4005 5 A (5 V) | MR | 2 | S/ 6,59 | S/ 13,18 | En stock | [ver](https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/) |
| 7 | Fusibles de vidrio | Surtido 250 V | MR | 1 | S/ 12,00 | S/ 12,00 | En stock | [ver](https://www.electromania.pe/producto/100x-fusibles-de-vidrio-250v/) |
| 8 | Parada de emergencia | Seta enclavada 660 V 10 A | MR | 1 | S/ 8,00 | S/ 8,00 | En stock | [ver](https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/) |
| 9 | Capacitor 1000 µF low ESR | Protección del riel 5 V | DR | 1 | ~S/ 5,00 | ~S/ 5,00 | Estimado | — |
| 10 | Dupont / JST / termorretráctil | Arnés del dron | DR | 1 | ~S/ 20,00 | ~S/ 20,00 | Estimado | — |
| | **Total** | | | **14** | | **S/ 1.620,68 + ~S/ 25** | | |

### 4.2 The Pi Box

- **Canal:** <https://thepibox.pe/> · Lima (Chacarilla) · Olva Courier.
- **Prioridad:** 1 (cómputo y cámaras del dron).
- El Pi 5 es **solo del dron**: el mini-rover usa la Pi 4 del inventario de facultad.
- Confirmar el stock del **HAT+ M.2** antes de comprar el SSD 2242.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Raspberry Pi 5 8 GB | Placa oficial | DR | 1 | S/ 768,00 | S/ 768,00 | En stock | [ver](https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444) |
| 2 | Cámara estéreo | Camera Module 3 Standard (IMX708) | DR | 2 | S/ 140,00 | S/ 280,00 | En stock | [ver](https://thepibox.pe/shop/cam-rp-006-camara-v3-estandar-raspberry-pi-3368) |
| 3 | Fuente 27 W USB-C | 5,1 V / 5 A oficial | MR + DR | 2 | S/ 67,00 | S/ 134,00 | En stock | [ver](https://thepibox.pe/shop/fuente-de-poder-27-w-raspberry-pi-3458) |
| 4 | HAT+ M.2 | Oficial (SSD 2242) | DR | 1 | S/ 60,00 | S/ 60,00 | Por confirmar | [ver](https://thepibox.pe/shop/exp-rp-006-hat-m-2-raspberry-pi-3475) |
| 5 | Active Cooler | Oficial | DR | 1 | S/ 29,90 | S/ 29,90 | En stock | [ver](https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454) |
| 6 | Accesorios de caja | Ventilador / rejilla / espuma | MR | 1 | ~S/ 30,00 | ~S/ 30,00 | Estimado | [ver](https://thepibox.pe/) |
| | **Total** | | | **8** | | **S/ 1.271,90 + ~S/ 30** | | |

> Las dos cámaras deben ser **del mismo lote**: pedirlas juntas.

### 4.3 Memory Kings

- **Canal:** <https://www.memorykings.pe/> · Lima · precio con IGV, **flete no incluido**.
- **Prioridad:** 1 (es el ítem más caro del bloque de visión).
- Verificar que el SKU sea el **Facecam 4K** y no una "Genius Facecam" del bloque
  de productos relacionados.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Cámara web 4K | Elgato Facecam 4K · 040866 / 10WAF9901 | RP | 2 | S/ 828,00 | S/ 1.656,00 | > 10 | [ver](https://www.memorykings.pe/producto/354472/camara-webcam-elgato-facecam-4k-uhd-60fps) |
| | **Total** | | | **2** | | **S/ 1.656,00** | | |

> Pedir también precio de la **Creative Live! Cam Sync 4K (S/ 261)** y de la
> **Logitech Brio 4K (S/ 487)** como alternativas, por si el presupuesto se recorta.

### 4.4 Falabella (marketplace)

- **Canal:** <https://www.falabella.com.pe/> · despacho a domicilio; algunos
  productos se envían desde EE. UU.
- **Prioridad:** 2.
- **Ojo:** el vendedor puede ser un marketplace (p. ej. *oyetec peru*). Pedir
  cotización con el **vendedor real** y su RUC, no solo el precio de la publicación.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Batería LiFePO4 12 V 10 Ah | Goldenmate, BMS IP67 | MR | 1 | S/ 239,00 | S/ 239,00 | Importada EE. UU. | [ver](https://www.falabella.com.pe/falabella-pe/product/155618417/bateraa-lifepo4-goldenmate-12v-10ah-bms-ip67-5000-ciclos) |
| 2 | SSD SATA 2,5" 256 GB | ADATA SU650 | MR | 1 | S/ 185,90 | S/ 185,90 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/140636555/UNIDAD-DE-ESTADO-SOLIDO-SSD-25-SATA-256GB-ADATA-SU650) |
| 3 | SSD NVMe 128 GB | M.2 2242 | DR | 1 | S/ 149,80 | S/ 149,80 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/159932959/ssd-kingspec-128gb-m-2-2242-nvme-pcie-3-0-x2-bm-key) |
| 4 | microSD 64 GB A2 | SanDisk Extreme Pro | MR + DR | 2 | S/ 64,90 | S/ 129,80 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador) |
| 5 | Desconectador de batería | 12–48 V universal | MR | 1 | S/ 46,90 | S/ 46,90 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco) |
| 6 | Caja USB 3.0 para SSD | 2,5" SATA → USB 3.0 | MR | 1 | S/ 24,80 | S/ 24,80 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/159275261/case-externo-para-disco-duro-hdd-ssd-2-5-pulgadas-sata-usb-3-0-5gbps-con-cable-y-adaptador-tipo-c) |
| 7 | Portafusibles | Línea mini cuchilla 12 A | MR | 1 | S/ 15,90 | S/ 15,90 | Marketplace | [ver](https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a) |
| 8 | Cargador LiFePO4 | 14,6 V 5–10 A (a cotizar) | MR | 1 | ~S/ 200,00 | ~S/ 200,00 | Estimado | [ref. LVYUAN 20 A](https://www.falabella.com.pe/falabella-pe/product/155603105/cargador-bateraa-lifepo4-lvyuan-14-6v-20a-smart-12v) |
| | **Total** | | | **9** | | **S/ 792,10 + ~S/ 200** | | |

### 4.5 Naylamp Mechatronics

- **Canal:** <https://naylampmechatronics.com/> · envío gratis a todo el Perú desde S/ 200.
- **Prioridad:** 2 (drivers y estructura).
- El perfil **V-Slot 2020 está agotado**; se cotiza el **2040**, que es el sustituto.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | Driver de motor | BTS7960 43 A | MR | 2 | S/ 45,00 | S/ 90,00 | En stock | [ver](https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html) |
| 2 | Perfil de aluminio | V-Slot 2040, barra 3,2 m | MR | 1 | S/ 160,00 | S/ 160,00 | En stock | [ver](https://naylampmechatronics.com/perfiles-de-aluminio/688-perfil-v-slot-2040-l3200mm.html) |
| 3 | Aisladores de vibración | Silicona M3 (4–8 puntos) | DR | 1 | ~S/ 25,00 | ~S/ 25,00 | Estimado | [ver](https://naylampmechatronics.com/) |
| 4 | Tornillería e insertos | M2,5 / M3 | DR | 1 | ~S/ 35,00 | ~S/ 35,00 | Estimado | [ver](https://naylampmechatronics.com/72-tornillos-y-tuercas) |
| 5 | Tornillos y tuercas | M3/M4 + tuercas en T | MR | 1 | ~S/ 50,00 | ~S/ 50,00 | Estimado | [ver](https://naylampmechatronics.com/72-tornillos-y-tuercas) |
| | **Total** | | | **6** | | **S/ 250,00 + ~S/ 110** | | |

### 4.6 Electronics Peru

- **Canal:** <https://www.electronicsperu.com/> · **Ica** · envío a coordinar.
- **Prioridad:** 2 (única tienda con stock claro del BNO085).
- Es la única línea del consolidado con despacho desde Ica: confirmar plazo.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Stock 21-11 | Enlace |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | IMU 9-DOF | BNO085 (AHRS) | MR | 1 | S/ 100,00 | S/ 100,00 | En stock | [ver](https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/) |
| | **Total** | | | **1** | | **S/ 100,00** | | |

### 4.7 Cableado por decidir

Estas dos líneas figuran en los BOM como "Naylamp **o** Electromanía". Se piden a
**un solo proveedor** para no duplicar el envío; hay que elegir después de recibir
ambas cotizaciones.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Enlace |
|---:|---|---|---|---:|---:|---:|---|
| 1 | Cable y conectores | XT60/XT30, 14–18 AWG + termorretráctil | MR | 1 | ~S/ 80,00 | ~S/ 80,00 | [Naylamp XT60](https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html) |
| 2 | Conectores / cable / fusible / interruptor | XT60/XT30, 18–20 AWG, fusible 5 A | DR | 1 | ~S/ 60,00 | ~S/ 60,00 | [Naylamp conectores](https://naylampmechatronics.com/216-conectores-xt) |
| | **Total** | | | **2** | | **~S/ 140,00** | |

### 4.8 Print3D.pe

- **Canal:** <https://print3d.pe/> · **Trujillo** · servicio nacional · a coordinar.
- **Prioridad:** 3 (se puede fabricar después de cerrar cotas).
- Todos los importes son **estimaciones** de planificación: hay que pedir cotización
  por pieza, material (PETG/TPU) y plazo.

| # | Ítem | Modelo / material | Proy. | Cant. | P. unit. | Subtotal |
|---:|---|---|---|---:|---:|---:|
| 1 | Ruedas 90 mm | Buje PETG + banda TPU | MR | 4 | ~S/ 25,00 | ~S/ 100,00 |
| 2 | Placas estructurales | PETG o aluminio, corte/impresión | MR | 1 | ~S/ 80,00 | ~S/ 80,00 |
| 3 | Soportes del dron | Soportes, barra de baseline 150 mm, bandeja y ventana del ToF | DR | 1 | ~S/ 120,00 | ~S/ 120,00 |
| | **Total** | | | **6** | | **~S/ 300,00** |

### 4.9 Importación ZoneFPV / Matek

- **Canal:** <https://zonefpv.com/> · internacional.
- **Prioridad:** 3. No se encontró UBEC de dron 5 V/5 A verificado en Perú.
- El precio es **landed estimado** (producto + envío + aduana); hay que pedirlo
  desglosado.

| # | Ítem | Modelo / SKU | Proy. | Cant. | P. unit. | Subtotal | Enlace |
|---:|---|---|---|---:|---:|---:|---|
| 1 | UBEC 5 V / 5 A | Matek BEC12S-PRO (9–55 V → 5,2 V, 9 A pico) | DR | 1 | ~S/ 120,00 | ~S/ 120,00 | [ver](https://zonefpv.com/products/matek-bec12s-pro-9-55v-to-5v-8v-12v-5a-bec-voltage-regulator-fpv-drone) |
| | **Total** | | | **1** | | **~S/ 120,00** | |

### 4.10 Taller / tienda local

Sin proveedor definido: son piezas y cables a medida del bloque de visión del
rover-principal. Se cotizan en Lima (taller de la facultad o proveedor local).

| # | Ítem | Alcance | Proy. | Cant. | P. unit. | Subtotal |
|---:|---|---|---|---:|---:|---:|
| 1 | Montaje rígido de visión | Barra de aluminio + soportes a medida para 2 cámaras | RP | 1 | ~S/ 250,00 | ~S/ 250,00 |
| 2 | Cables USB 3.0 + hub | Cables certificados y hub alimentado | RP | 1 | ~S/ 150,00 | ~S/ 150,00 |
| | **Total** | | | **2** | | **~S/ 400,00** |

### 4.11 Varios / ferretería

Consumibles y repuestos. No se pide cotización formal: se compran localmente con
el remanente.

| # | Ítem | Proy. | Cant. | P. unit. | Subtotal | Nota |
|---|---|---:|---:|---:|---:|---|
| 1 | Repuestos: fusibles, cable, conectores | MR | 1 | ~S/ 50,00 | ~S/ 50,00 | Crítico para la demo |
| 2 | Repuestos: fusibles, cable, conectores | DR | 1 | ~S/ 30,00 | ~S/ 30,00 | — |
| 3 | USB-C corto + ferrita | DR | 1 | ~S/ 25,00 | ~S/ 25,00 | Alimentación del Pi 5 |
| 4 | Térmicos / espuma / velcro | DR | 1 | ~S/ 15,00 | ~S/ 15,00 | Almohadilla y fijación |
| | **Total** | | **4** | | **~S/ 120,00** | |

---

## 5. Exclusiones, supuestos y avisos

### 5.1 La copia de la BOM en `rover-principal/` **no se suma**

`rover-principal/docs/04-diseno/bom-peru.csv` se titula **"BOM de electrónica
cotizada en Perú (mini demo)"** y reproduce la BOM del mini-rover, con una
diferencia: compra el **Pi 5 (S/ 768)** y el **Active Cooler (S/ 29,90)** en lugar
de reutilizar la Pi 4 y la Argon ONE del inventario de facultad. Su total
documentado es **S/ 3.317,98**.

| Variante | Qué cambia | Total | ¿Se cotiza? |
|---|---|---:|---|
| BOM del mini demo comprando todo | Bloque MR completo + Pi 5 + Active Cooler + Fuente 27 W | S/ 3.317,98 | **No**, salvo decisión expresa |

Si el equipo decide **no reutilizar** la Pi 4 y la Argon ONE, esta variante
duplicaría todas las líneas del bloque MR y añadiría a The Pi Box: Pi 5 ×1,
Active Cooler ×1 y Fuente 27 W ×1. Hay que decidirlo antes de enviar la solicitud
(es la pregunta `OQ` del mini-rover sobre el cómputo).

### 5.2 No se cotiza (inventario existente)

| Ítem | Cant. | Fuente | Por qué |
|---|---:|---|---|
| Raspberry Pi 4 Model B 8 GB | 1 | Inventario de facultad (`mini-rover/inventario actual.txt`) | Se reutiliza (ADR-0010) |
| Carcasa Argon ONE V2 | 1 | Inventario de facultad | Se reutiliza; verificar acceso al CSI |

> Si el inventario falla, hay plan B en
> `mini-rover/docs/04-diseno/bom-peru.md` §9 (Pi 4B 4 GB agotada, Pi 5 8 GB
> S/ 768, importación).

### 5.3 Alternativas del dron (no incluidas)

Sustituyen líneas del bloque DR; **no** se suman.

| Alternativa | Reemplaza | Precio | Proveedor |
|---|---|---:|---|
| 2 × Camera Module 3 **Wide** | B07 (CM3 Standard) | S/ 195 c/u | The Pi Box |
| ToF VL53L5CX 8×8 (4 m) | B09 (TFmini Plus) | S/ 190 | Adafruit (importación) |
| ToF VL53L1X (4 m) | B09 | S/ 75 | Naylamp |
| 2 × cámara global shutter OV9281 | B07 | S/ 200 c/u | Electromanía |
| SSD 512 GB NVMe | B03 | S/ 260 | The Pi Box |
| Memoria USB 3.0 128 GB | B02 + B03 | S/ 80 | The Pi Box |
| Raspberry Pi 5 16 GB | B01 | S/ 1.699 | The Pi Box |

> Los ToF de 4 m **no sirven** para volar a 6 m: solo banco o vuelo ≤ 4 m.

### 5.4 Alternativas de visión del rover-principal (no incluidas)

| Alternativa | Reemplaza | Precio | Proveedor |
|---|---|---:|---|
| TFmini-S 12 m (C010A-SEN0259) | TFmini Plus | S/ 299 (quedan 3) | Electromanía |
| LIDAR-Lite v3HP | TFmini Plus (10–40 m) | S/ 850 (quedan 11) | Electromanía |
| DFRobot 4 m I²C IP67 | TFmini Plus (near-field) | S/ 115 (quedan 3) | Electromanía |
| VL53L1X | DFRobot 4 m | S/ 75 | Naylamp |
| VL53L8CX 8×8 carrier | TFmini Plus (multizona) | USD 24,95 + envío | Pololu (importación) |
| Creative Live! Cam Sync 4K | Elgato Facecam 4K | S/ 261 | Memory Kings |
| Logitech Brio 4K | Elgato Facecam 4K | S/ 487 | Memory Kings |

### 5.5 Add-ons y estudios del mini-rover (no incluidos)

| Bloque | Contenido | Monto | Estado |
|---|---|---:|---|
| Interfaz de tiempo real | ESP32-S3/C6/XIAO + TCA9548A + level shifter + PC817 + arnés | ~S/ 195 | Propuesta; depende de `OQ` de arquitectura |
| Pack Li-ion 3S2P / 3S3P | Celdas EVE 18650, BMS, nickel, espaciadores, XT60, cargador, relé | ~S/ 218 / ~S/ 306 | Alternativa a la LiFePO4; **no** comprar ambas |
| Herramienta | Soldador de punto portátil | S/ 390 | Opcional (Bracsan) |
| Estudio 6×6 | `mini-rover/docs/04-diseno/energia/bom-6x6.md` | — | Pendiente de `OQ-09`; **no comprar** |

Proveedores implicados si se aprueban: Bracsan (Lima, Jr. Paruro 1353), Tesla
Electronic (Trujillo), MTLAB (Lima/Callao) y Electromanía.

### 5.6 Supuestos de este consolidado

> **Supuesto 1:** se construyen los tres bloques (MR + DR + RP-visión) y se
> reutiliza la Pi 4 8 GB y la Argon ONE del inventario de facultad.
> **Supuesto 2:** el rover-principal usa la BOM de visión V-A (2 × Elgato + 1 ×
> TFmini Plus + montaje + cables), que es su escenario recomendado.
> **Supuesto 3:** los precios son los del catálogo web del 2026-11-21; no hubo
> reserva ni consulta a los vendedores.
> **Supuesto 4:** no se suman envíos, aduanas, IGV no declarado ni fluctuación
> del tipo de cambio (S/ 3,75 por USD en los estudios de origen).
> **Supuesto 5:** las líneas marcadas `~` son estimaciones de planificación y deben
> reemplazarse por la cotización real del proveedor.

---

## 6. Trazabilidad

| Dato | Archivo de origen |
|---|---|
| Bloque MR (26 líneas) | `mini-rover/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../mini-rover/docs/04-diseno/bom-peru.md) |
| Bloque DR (19 líneas base) | `drone/docs/04-diseno/bom-peru.csv` y [`bom-peru.md`](../../drone/docs/04-diseno/bom-peru.md) |
| Bloque RP visión (V-A) | `rover-principal/docs/04-diseno/bom-vision.csv` y [`bom-vision.md`](../../rover-principal/docs/04-diseno/bom-vision.md) |
| Variante excluida | `rover-principal/docs/04-diseno/bom-peru.csv` (copia del mini demo) |
| Alternativas y add-ons | `bom-peru-addons.csv` de cada subproyecto y §2 de `bom-vision.md` |
| Fuentes `F-xx` | `docs/01-investigacion/fuentes.md` de cada subproyecto |
| Versión tabular de este consolidado | [`bom-consolidado.csv`](bom-consolidado.csv) |

---

## 7. Estado y control de cambios

- **No** se ha comprado, reservado ni consultado nada: los precios son de catálogo
  web al 2026-11-21.
- Cualquier cambio de cantidad o modelo se registra antes en el BOM del
  subproyecto (`bom-peru.csv` / `bom-vision.csv`) y luego aquí.
- Las cotizaciones recibidas se archivan como evidencia **cuando se ejecute la
  fase de compras**; mientras tanto este documento queda en estado `Pendiente`.
