# BOM de electrónica cotizada en Perú (mini demo)

> ⚠️ **Documento heredado, no vigente.** Es la copia de la BOM del **mini demo** que
> se trajo a esta sección como referencia metodológica. El mini-rover cambió su
> energía y su almacenamiento el **2026-11-23** (pack Li-ion 2S4P en lugar de
> LiFePO4, sin SSD ni HAT, con boost de tracción), así que este archivo quedó
> desfasado. La BOM vigente del rover grande es
> [`bom-vision.md`](bom-vision.md); la del mini demo está en
> `mini-rover/docs/04-diseno/bom-peru.md`; y el consolidado de compras de los tres
> subproyectos, en [`../../../cotizaciones/bom-consolidado.md`](../../../cotizaciones/bom-consolidado.md).
> No se cotiza desde aquí.
>
> Estado: Estudio de abastecimiento · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
>
> **No autoriza compra.** Precios en soles peruanos (PEN) con IGV, consultados el
> 2026-11-21 en catálogos públicos. No incluyen envío, embalaje, aduanas ni
> fluctuaciones. El stock es el que declaraba la tienda en línea en ese momento;
> no se reservó ningún artículo.
>
> Esta cotización cubre la **BOM base del mini demo** (2 motores, LiFePO4 12,8 V)
> de [`bom.md`](bom.md). **No** cotiza la variante 6×6 de
> [`energia/bom-6x6.md`](energia/bom-6x6.md), que sigue pendiente de OQ-09 y no
> debe comprarse.

## 1. Resumen ejecutivo

**Sí se puede comprar casi toda la electrónica en Perú**, con cuatro excepciones
claras:

1. **Batería LiFePO4 12,8 V 6 Ah exacta:** no se encontró con stock local. Hay
   sustitutos de 10 Ah y 20 Ah, o pack a medida.
2. **Motorreductor 12 V 50 rpm con encoder exacto:** no se encontró con stock.
   Hay un DFRobot de 83 rpm con encoder, apto, o el 50 rpm sin encoder.
3. **Driver Cytron MDD10A:** no se encontró en tiendas peruanas. Se sustituye
   por dos BTS7960 o se importa.
4. **Perfil V-Slot 2020 y HAT NVMe:** el 2020 está agotado y el HAT oficial no
   tiene stock en las tiendas consultadas. Hay sustitutos locales (perfil 2040,
   SSD por USB o microSD) o importación.

La ruta **100 % Perú** cuesta aproximadamente **S/ 3.250–3.750** para la parte
electromecánica, con una parte estimada de impresión 3D, cableado y cargador.
Es del mismo orden de magnitud que los 775 EUR publicados en la BOM base,
aunque la suma de líneas de esa BOM da 740 EUR (ver sección 5.2); incluye
componentes que la BOM original no desglosaba (cargador de batería, cableado y
ruedas impresas). Los **add-ons propuestos** —ESP32-S3 como interfaz de tiempo
real y pack Li-ion 3S2P/3S3P— van aparte: ~S/ 195 y ~S/ 218/306,
respectivamente. El detalle verificable está en la sección 4 y en
[`bom-peru.csv`](bom-peru.csv).

**Recomendación:** comprar primero en The Pi Box (cómputo), Electromanía
(LiDAR, motores, sensores, e-stop), Naylamp (drivers, perfil, conectores) y
Electronics Peru (IMU, en Ica). Dejar para una segunda orden la batería, el
almacenamiento y los elementos importados.

## 2. Método y alcance

- Búsqueda en tiendas peruanas con envío nacional, marketplaces y tiendas de
  provincia, además de canales de importación.
- Se contrastó precio, moneda, IVA declarado, disponibilidad y, cuando estaba
  publicado, ciudad de despacho.
- Se priorizó el **componente exacto o funcionalmente equivalente**, no el más
  barato a cualquier costo.
- No se hicieron compras, reservas ni consultas por WhatsApp. Los precios son
  los del catálogo web.
- Los enlaces y las fechas de acceso están en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md), fuentes
  `F-19` a `F-38`.

> **Sobre el stock:** “En stock” significa que el catálogo lo declaraba así. En
> Falabella, “sin stock en tienda” puede convivir con “despacho a domicilio”
> porque el vendedor es un marketplace. Confirmar antes de pagar.

## 3. Proveedores encontrados

| Proveedor | Ubicación | Cobertura | Especialidad | Envío | Enlace |
|---|---|---|---|---|---|
| **The Pi Box** | Lima (Chacarilla) | Todo el Perú | Raspberry Pi, HAT, accesorios | Olva Courier; tarifa en checkout; express solo Lima | <https://thepibox.pe/> |
| **Electromanía** | Lima | Todo el Perú | DFRobot, LiDAR, motores, sensores, drivers | Desde S/ 10; agencia o domicilio | <https://www.electromania.pe/> |
| **Naylamp Mechatronics** | Perú | Todo el Perú | Robótica, V-Slot, drivers, conectores, Raspberry Pi | Gratis desde S/ 200 | <https://naylampmechatronics.com/> |
| **Electronics Peru** | **Ica** | Nacional, a coordinar | Componentes, módulos, IMU | A coordinar con la tienda | <https://www.electronicsperu.com/> |
| **Bracsan** | Lima (Jr. Paruro 1353) | Recojo / envío a coordinar | Celdas 18650, BMS, cargadores, fusibles, conectores, cable | A coordinar | <https://bracsan.pe/> |
| **Tesla Electronic** | **Trujillo** | Nacional | ESP32-S3, módulos, sensores | Envío al interior en 24 h hábiles | <https://www.teslaelectronic.com.pe/> |
| **MTLAB** | Lima (San Martín de Porres) | Lima y Callao | ESP32-C6, shields, módulos | Olva; S/ 10; solo Lima/Callao | <https://mtlab.pe/> |
| **Hifisac** | Lima (venta por WhatsApp) | Nacional, a coordinar | Catálogo amplio: ESP32, BMS, INA219, pasivos, herramientas | WhatsApp/email; web sin stock online | <https://hifisac.com/shop> |
| **Falabella** | Lima / marketplace | Todo el Perú | Baterías, SSD, microSD, fusibles, interruptores | Domicilio; algunos productos se envían desde EE. UU. | <https://www.falabella.com.pe/> |
| **Autosolar** | Lima | Todo el Perú | Solar, LiFePO4, cargadores | A coordinar | <https://autosolar.pe/> |
| **Print3D.pe** | **Trujillo** | Servicio nacional | Impresión 3D, TPU, piezas técnicas | A coordinar | <https://print3d.pe/> |
| **Adafruit** | EE. UU. | Importación | HAT M.2, BNO085, RPLIDAR | Internacional | <https://www.adafruit.com/> |
| **Pololu** | EE. UU. | Importación | Motores 37D, drivers, ruedas | Internacional | <https://www.pololu.com/> |

> No se encontró una tienda de robótica “todo en uno” fuera de Lima. Lo que sí
> existe es electrónica en **Ica** (Electronics Peru) y servicio de impresión 3D
> en **Trujillo** (Print3D.pe). Las tiendas de Lima despachan a provincia.
>
> **Hifisac (revisión 2026-11-21):** el catálogo muestra precios, pero todas las
> fichas que probé —ESP32-S3, BMS, INA219, level shifter, e-stop, fusibles—
> aparecen **“Sin existencias”** y el carrito está deshabilitado. La venta es por
> WhatsApp/email; usa sus precios solo como referencia y confirma stock. El
> listado “Disponible” no es fiable.

## 4. BOM cotizada: ruta recomendada 100 % Perú

### 4.1 Cómputo y almacenamiento

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 1 | Raspberry Pi 5 8 GB | Placa oficial | 1 | The Pi Box | S/ 768,00 | S/ 768,00 | En stock | <https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444> |
| 2 | Almacenamiento | SSD SATA 2.5" 256 GB + caja USB 3.0 | 1 | Falabella | S/ 185,90 + S/ 24,80 | S/ 210,70 | Marketplace; despacho a domicilio | <https://www.falabella.com.pe/falabella-pe/product/140636555/UNIDAD-DE-ESTADO-SOLIDO-SSD-25-SATA-256GB-ADATA-SU650> · <https://www.falabella.com.pe/falabella-pe/product/159275261/case-externo-para-disco-duro-hdd-ssd-2-5-pulgadas-sata-usb-3-0-5gbps-con-cable-y-adaptador-tipo-c> |
| 3 | Refrigeración | Active Cooler oficial | 1 | The Pi Box | S/ 29,90 | S/ 29,90 | En stock | <https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454> |
| 4 | microSD de respaldo | 64 GB A2 (SanDisk Extreme Pro) | 1 | Falabella | S/ 64,90 | S/ 64,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador> |
| 5 | Fuente de banco / pruebas | Fuente oficial 27 W USB-C (5,1 V 5 A) | 1 | The Pi Box | S/ 67,00 | S/ 67,00 | En stock | <https://thepibox.pe/shop/fuente-de-poder-27-w-raspberry-pi-3458> |

> **Por qué no NVMe directo:** el HAT+ M.2 de The Pi Box (S/ 60–75) estaba
> **agotado** al momento de la consulta. La alternativa local es arrancar por
> USB 3.0 con un SSD SATA de 2,5" y una caja USB; es más robusto que la microSD y
> no depende del HAT. Si se prefiere NVMe, importar el HAT oficial
> ([Adafruit, US$ 17,40](https://www.adafruit.com/product/5902)) y usar un SSD
> M.2 2242 local; el KingSpec de 128 GB está a S/ 149,80 en Falabella.
>
> La microSD A2 es respaldo y medio de arranque de emergencia. Naylamp tiene una
> Kingston de 64 GB A1 a S/ 60, pero la A2 de Falabella es mejor para el sistema
> operativo.
>
> La fuente oficial de 27 W sustituye a la **fuente de banco** solo para las
> pruebas iniciales: entrega 5,1 V y 5 A, pero no permite limitar corriente ni
> tensión. Para banco de laboratorio hace falta una fuente regulable aparte.

### 4.2 Percepción

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 6 | LiDAR 2D 360° | RPLIDAR A1M8-R6 (12 m) | 1 | Electromanía | S/ 600,00 | S/ 600,00 | En stock; quedaban 12 | <https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/> |
| 7 | IMU 9-DOF | Módulo BNO085 | 1 | Electronics Peru (Ica) | S/ 100,00 | S/ 100,00 | En stock | <https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/> |
| 8 | Monitor de batería | INA219 I²C | 1 | Electromanía | S/ 12,50 | S/ 12,50 | En stock | <https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/> |

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

### 4.3 Tracción y dirección

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 9 | Motorreductor 12 V con encoder | DFRobot FIT0185, 83 rpm, 45 kg·cm, encoder Hall | 2 | Electromanía | S/ 145,00 | S/ 290,00 | En stock; quedaban 30 | <https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/> |
| 10 | Driver doble | BTS7960 43 A (un módulo por motor) | 2 | Naylamp | S/ 45,00 (oferta; normal S/ 55) | S/ 90,00 | En stock | <https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html> |
| 11 | Ruedas 90 mm | Impresión 3D: buje PETG + banda TPU | 4 | Print3D.pe / taller local | ~S/ 25,00 | ~S/ 100,00 | Estimado; cotizar | <https://print3d.pe/> |

> **El motor exacto no está:** la BOM pide 50 rpm con encoder. El FIT0185 da
> 83 rpm y 45 kg·cm (4,4 N·m) con encoder de 2096 pulsos/vuelta; se puede
> limitar por PWM a la velocidad de diseño. Es la mejor opción local “lista
> para usar”.
>
> Si se quiere el eje de 50 rpm, el DFRobot FIT0492-A (50 rpm, 50 kg·cm, sin
> encoder) está a S/ 69,90, pero habría que añadir encoder y acoplarlo. Naylamp
> tiene el 37D de 35 rpm con encoder a S/ 70, **agotado**.
>
> **El driver exacto tampoco:** el Cytron MDD10A no aparece en las tiendas
> peruanas consultadas. Dos BTS7960 cuestan S/ 90 y sobran para 7 A de bloqueo
> por motor, pero requieren más cableado y lógica de enable. Si se importa el
> MDD10A, es la solución más compacta.
>
> **Advertencia de corriente:** el FIT0185 declara unos **7 A de bloqueo por
> motor**. Dos motores pueden pedir 14 A en una situación de bloqueo. La batería
> de 10 Ah de la sección 4.4 tiene BMS de 10 A; para ese motor es marginal. Ver
> la sección 7.

### 4.4 Energía y protección

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 12 | Batería LiFePO4 12 V | Goldenmate 10 Ah, BMS, IP67, 5000 ciclos | 1 | Falabella | S/ 239,00 | S/ 239,00 | Importada desde EE. UU.; despacho a domicilio | <https://www.falabella.com.pe/falabella-pe/product/155618417/bateraa-lifepo4-goldenmate-12v-10ah-bms-ip67-5000-ciclos> |
| 13 | Cargador LiFePO4 | 14,6 V, 5–10 A (a cotizar) | 1 | Falabella / importación | ~S/ 150–359 | ~S/ 200,00 | No hay modelo pequeño verificado | <https://www.falabella.com.pe/falabella-pe/product/155603105/cargador-bateraa-lifepo4-lvyuan-14-6v-20a-smart-12v> |
| 14 | DC-DC 5 V 5 A | XL4005 5 A | 1 | Electromanía | S/ 6,59 | S/ 6,59 | En stock | <https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> |
| 15 | DC-DC 5 V 3 A | XL4005 5 A (segundo módulo, regulado a 5 V) | 1 | Electromanía | S/ 6,59 | S/ 6,59 | En stock | <https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> |
| 16 | Portafusibles | Portafusibles en línea mini cuchilla, con fusible 12 A | 1 | Falabella | S/ 15,90 | S/ 15,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a> |
| 17 | Fusibles | Surtido de vidrio 250 V (para laboratorio) | 1 | Electromanía | S/ 12,00 | S/ 12,00 | En stock | <https://www.electromania.pe/producto/100x-fusibles-de-vidrio-250v/> |
| 18 | Parada de emergencia | Seta roja enclavada, contactos NC/NO, 660 V 10 A | 1 | Electromanía | S/ 8,00 | S/ 8,00 | En stock; 10 A; ver riesgo 11 | <https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/> |
| 19 | Interruptor general | Desconectador de batería 12–48 V | 1 | Falabella | S/ 46,90 | S/ 46,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco> |

> **La batería exacta de 6 Ah no está.** La Goldenmate de 10 Ah es la opción
> más cercana y ligera (1,5 kg; 6,5 × 15 × 9,3 cm; BMS de 10 A; 5000 ciclos).
> La Nermak de 20 Ah (S/ 299; 2,5 kg; BMS integrado, verificar corriente
> máxima) es más segura para los 7 A de bloqueo por motor, a costa de masa.
> Autosolar tiene una LiFePO4 de 12 V 100 Ah a S/ 933,33: sobredimensionada
> para el mini demo.
>
> **El cargador no estaba en la BOM base.** Es obligatorio para una LiFePO4:
> 14,6 V con perfil de carga. El LVYUAN de 20 A (S/ 359) es correcto en tensión
> pero sobredimensionado para una batería de 10 Ah; conviene uno de 5–10 A o un
> cargador ajustable. No usar un cargador de plomo-ácido genérico sin perfil
> LiFePO4.
>
> **Fusibles:** el portafusibles de Falabella sirve para el circuito principal;
> para 3 A y 2 A conviene comprar un surtido de fusibles de cuchilla en una
> tienda de repuestos automotrices. Los fusibles de vidrio son para el banco,
> no para el arnés de potencia.

### 4.5 Chasis, cableado y montaje

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---:|---|---:|---:|---|---|
| 20 | Perfil de aluminio | V-Slot 2040, longitud 3,2 m (sustituye 2020) | 1 | Naylamp | S/ 160,00 | S/ 160,00 | En stock | <https://naylampmechatronics.com/perfiles-de-aluminio/688-perfil-v-slot-2040-l3200mm.html> |
| 21 | Placas PETG / aluminio | Corte o impresión 3D de placas | 1 | Print3D.pe / taller local | ~S/ 80,00 | ~S/ 80,00 | Estimado; cotizar | <https://print3d.pe/> |
| 22 | Cableado y conectores | XT60 macho/hembra, XT30, cable 14–18 AWG, termorretráctil | 1 | Naylamp / Electromanía | ~S/ 80,00 | ~S/ 80,00 | Parcialmente verificado | <https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html> · <https://www.electromania.pe/producto/conector-amass-xt60-con-cable-siliconado-macho-14awg-10cm/> |
| 23 | Tornillería | M3/M4, tuercas en T, separadores | 1 | Naylamp / ferretería | ~S/ 50,00 | ~S/ 50,00 | Estimado | <https://naylampmechatronics.com/72-tornillos-y-tuercas> |
| 24 | Ventilador, rejilla, espuma | Accesorios de caja | 1 | The Pi Box / ferretería | ~S/ 30,00 | ~S/ 30,00 | Estimado | <https://thepibox.pe/> |
| 25 | Repuestos críticos | Fusibles, cable, conectores | 1 | Varios | ~S/ 50,00 | ~S/ 50,00 | Estimado | — |

> **Perfil 2020:** agotado en Naylamp (S/ 98 la barra de 3,2 m). El 2040 de
> 3,2 m cuesta S/ 160, es más rígido y más pesado; cambia masa y cotas. Si se
> necesita el 2020 exacto, importar o buscar en otra carpintería de aluminio.
> No se encontró una tienda peruana con V-Slot 2020 en stock.
>
> **Ruedas:** la rueda de 80 mm de Electromanía (S/ 27) tiene buje hexagonal,
> no eje D de 6 mm; no es “plug and play”. La ruta recomendada es imprimir el
> buje a medida y la banda en TPU. Si se prefiere comprar, Pololu vende pares
> de 90 × 10 mm por US$ 9,49, pero también requiere adaptar el buje.

### 4.6 Interfaz ESP32 (propuesta ADR-0008, add-on)

> **No incluido en el total base.** Es una propuesta en revisión
> ([ADR-0008](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md)). La Pi
> 5 sigue siendo el cerebro; el ESP32 ejecuta PWM, encoders, IMU, batería,
> e-stop y expansión I²C. Añadir ~S/ 195 al total si se aprueba.

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
> **Alimentación:** usar el rail de 5 V 3 A, no el USB de la Pi, para evitar
> reinicios por ruido de motores. Masa común en estrella.
>
> **Hifisac (cotizar):** ESP32-S3 N16R8 S/ 49; INA219 S/ 8,20; level shifter
> S/ 2,70; BMS 3S 25A S/ 9,90. Si confirman stock, el add-on baja ~S/ 60; pero
> la web marca “Sin existencias” en todos esos productos. No está contabilizado
> en el subtotal.

### 4.7 Batería Li-ion a medida (opcional, reemplaza la Goldenmate)

> **No incluido en el total base.** Es una alternativa a la LiFePO4 Goldenmate
> de 10 Ah. La celda es **Li-ion 18650**, no LiFePO4: requiere BMS, carga
> supervisada y un diseño de pack competente. La seguridad y el reglamento del
> ERC deben revisarse antes de adoptarla.

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

| Comparación | Goldenmate LiFePO4 10 Ah | 3S2P Li-ion 7 Ah | 3S3P Li-ion 10,5 Ah |
|---|---:|---:|---:|
| Precio materiales | S/ 239 | ~S/ 218 | ~S/ 306 |
| Energía | 128 Wh | ~75,6 Wh | ~113,4 Wh |
| Peso de celda | 1,5 kg (pack) | ~0,30 kg | ~0,45 kg |
| Corriente máxima | 10 A (BMS) | 20,4 A (2P × 10,2 A); BMS 25 A | 25 A (BMS); celdas 30,6 A (3P × 10,2 A) |
| Voltaje | 12,8 V nominal | 11,1 V nominal; 9,0–12,6 V | 11,1 V nominal; 9,0–12,6 V |
| Riesgo | LiFePO4, más estable | Li-ion, requiere BMS y cuidado | Li-ion, requiere BMS y cuidado |

> **Energía:** el pack 3S2P iguala a la BOM base de **6 Ah** (75,6 Wh vs
> 76,8 Wh), no a la Goldenmate de 10 Ah (128 Wh). Si se quiere la autonomía de
> la Goldenmate, usar 3S3P (113,4 Wh) o una LiFePO4 de 10 Ah.

> **Corriente:** la celda EVE 35V declara 10,2 A máximos “not for cycle life”.
> Para vida útil, tratar 8 A por celda como techo continuo. 2P da ~16 A
> continuos; 3P da ~24 A. Los 7 A de bloqueo por motor justifican 3P si se va a
> exigir el rover, pero 2P es suficiente para el demo con límite de corriente.
>
> **Protección:** fusible principal de 15 A para 3S2P (25 A para 3S3P),
> fusibles de rama de 10 A por motor, precarga de 100 Ω / 5 W y BMS con
> balanceo. Confirmar que el BMS de Bracsan balancea; si no, usar uno con
> balanceo o un cargador balanceador.
>
> **E-stop:** la seta de S/ 8 está rated 10 A; no debe cortar 15–25 A. Usar el
> relé de 30 A (B8) para la potencia y dejar que la seta corte solo la bobina
> del relé. La e-stop sigue siendo hardware, no software.
>
> **Carga:** 12,6 V 3 A, supervisada, sobre superficie ignífuga, fuera del rover.
> La celda tiene UN38.3/IEC62133; el pack ensamblado no hereda automáticamente
> esa certificación. Revisar transporte y reglamento ERC.
>
> **Armado:** medir capacidad y resistencia interna de cada celda antes de
> armar; agrupar las más parecidas. Usar portaceldas/espaciadores, nickel y
> soldador de punto. No soldar celdas 18650 con cautín. Aislar el pack con
> termorretráctil y carcasa ignífuga; fijarlo al chasis con soporte, no con
> velcro.
>
> **Hifisac (cotizar):** BMS 3S 25A S/ 9,90 y portaceldas 18650 S/ 1,90; sus
> celdas de 3000 mAh cuestan S/ 24,50, peor relación precio/capacidad que la EVE
> 35V de Bracsan (S/ 19). La web marca “Sin existencias”; confirmar por
> WhatsApp. Si el BMS se consigue a S/ 9,90, el pack 3S2P baja ~S/ 8.

## 5. Totales

### 5.1 Ruta recomendada (100 % Perú)

| Bloque | Subtotal |
|---|---:|
| Cómputo y almacenamiento | S/ 1.140,50 |
| Percepción | S/ 712,50 |
| Tracción (motores + drivers + ruedas) | S/ 480,00 |
| Energía y protección | S/ 534,98 |
| Chasis, cableado y montaje | S/ 450,00 (estimado) |
| **Subtotal** | **S/ 3.317,98** |
| Imprevistos / envío local (5 %) | ~S/ 165,90 |
| **Total estimado** | **~S/ 3.484** |

> El total sube a **~S/ 3.700–3.750** si se elige la batería de 20 Ah
> (S/ 299), un cargador de S/ 359 y ruedas impresas a S/ 120. La horquilla
> realista es **S/ 3.250–3.750**.
>
> Si se arranca solo con microSD (sin SSD USB), se descuentan ~S/ 146 y el
> total baja a ~S/ 3.260–3.600. Si se importa el HAT NVMe y se usa el SSD
> KingSpec de 128 GB, el coste es similar al SSD USB, pero el plazo sube.
>
> **Add-ons no incluidos:** la interfaz ESP32 suma ~S/ 195; la batería Li-ion
> 3S2P cuesta ~S/ 218 y reemplaza a la Goldenmate (S/ 239), mientras que la 3S3P
> cuesta ~S/ 306. Con ESP32-S3 + 3S2P el total sube ~S/ 174; con ESP32-S3 +
> 3S3P sube ~S/ 262. Ninguna de estas variantes está aprobada todavía.

### 5.2 Comparación con la BOM base

| Concepto | BOM base (EUR, suma de líneas) | Ruta Perú (PEN) | Comentario |
|---|---:|---:|---|
| Cómputo y almacenamiento | 187 | ~1.140,50 | Incluye SSD USB y fuente; el HAT NVMe no está disponible |
| Percepción | 133 | ~712,50 | LiDAR y BNO085 son los rubros dominantes |
| Tracción (motores + drivers + ruedas) | 147 | ~480,00 | Motores con encoder reales, no genéricos |
| Energía y protección | 128 | ~534,98 | Incluye cargador, que la BOM base no listaba |
| Chasis, cableado y montaje | 145 | ~450,00 | Perfil 2040 y piezas impresas; estimado |
| **Subtotal** | **740** | **~3.317,98** | |
| Envío / imprevistos | 70 | ~165,90 | 10 % en la BOM base; 5 % en la ruta Perú |
| **Total** | **810** | **~3.484** | La BOM base publica 775 EUR; ver nota de revisión |

> **Hallazgo de la revisión:** la BOM base publica **705 EUR** de subtotal y
> **775 EUR** con envío, pero la suma de sus 23 líneas da **740 EUR** (810 EUR
> con envío). La diferencia de 35 EUR está documentada en
> [`bom.md`](bom.md) y queda pendiente de aprobación; esta comparación usa la
> suma de líneas, no el total publicado.

> La BOM base no incluía cargador de batería, cableado detallado ni ruedas
> impresas. Al comparar, hay que sumar esos conceptos.

## 6. Disponibilidad: exacto vs. sustituto vs. importación

| Componente | ¿Exacto en Perú? | Sustituto local | Importación | Impacto / decisión |
|---|---|---|---|---|
| Raspberry Pi 5 8 GB | **Sí** (The Pi Box) | Pi 5 4 GB (S/ 488) o Pi 4B 4 GB (S/ 471,50), ambas listadas pero **agotadas** | Adafruit / tiendas Pi | 8 GB es lo recomendado para Nav2; no recortar sin medir |
| HAT NVMe + SSD 128 GB | **No con stock** | SSD USB 3.0 + caja, o microSD A2 | HAT oficial US$ 17,40 + SSD local | USB es la ruta local más robusta; NVMe requiere importar |
| LiDAR A1M8 | **Sí** (Electromanía) | RPLIDAR C1 (S/ 450) | Adafruit US$ 99,95 / LD19 | A1M8 tiene más soporte; C1 es más moderno |
| BNO085 | **Sí** (Ica) | MPU9250 (S/ 85) / MPU6050 (S/ 18) | Adafruit US$ 29,50 / Mouser | BNO085 ahorra calibración; el MPU exige más trabajo |
| INA219 | **Sí** | INA226 (S/ 29) | — | INA219 es suficiente para el bus de 12 V |
| Motor 50 rpm con encoder | **No con stock** | FIT0185 83 rpm con encoder (S/ 145) | Pololu 4753 US$ 60,95 | El FIT0185 es la mejor relación precio/plazo |
| Cytron MDD10A | **No** | 2 × BTS7960 (S/ 90) | Cytron / RobotShop | BTS7960 exige más cableado; MDD10A es más compacto |
| Ruedas 90 mm | **No exactas** | 3D print TPU/PETG; rueda 80 mm con adaptador | Pololu 90 × 10 mm US$ 9,49/par | El buje es el problema, no la rueda |
| LiFePO4 12,8 V 6 Ah | **No** | Goldenmate 10 Ah (S/ 239) / Nermak 20 Ah (S/ 299) | AliExpress / tiendas de litio | Verificar BMS ≥ 20 A si se usa el FIT0185 |
| DC-DC 5 V 5 A | **Sí** | XL4005 5 A (S/ 6,59) | Pololu / Mouser | Verificar ripple y temperatura; derratear |
| E-stop | **Sí** | Seta 22 mm de Naylamp (S/ 15, agotada) | Schneider / Eaton | El de Electromanía es lento de liberar girando, pero cumple |
| Interruptor general | **Sí** | Desconectador de batería 12–48 V | — | Verificar corriente continua, no solo pico |
| Perfil 2020 | **No con stock** | 2040 (S/ 160 la barra de 3,2 m) | AliExpress / OpenBuilds | El 2040 cambia masa y cotas |
| Placas PETG | **Servicio local** | Print3D.pe (Trujillo) | — | Cotizar por pieza y material |
| Fusibles / cable / conectores | **Sí** | Falabella, Naylamp, Electromanía | — | Comprar surtido y repuestos |
| MCU de interfaz | **Sí** | ESP32-S3 S/ 110 (Trujillo); C6 S/ 100 (Lima); XIAO C6 S/ 39 | Adafruit / Mouser | S3 recomendado; C6 para base; XIAO sin margen |
| Batería Li-ion 3S2P | **Sí, a medida** | Celdas EVE 35V + BMS 3S 25A en Bracsan | Pack LiFePO4 listo | 3S2P ~S/ 218; 3S3P ~S/ 306; requiere armado y BMS |

## 7. Riesgos y verificaciones antes de comprar

1. **Corriente de bloqueo vs. BMS.** Dos FIT0185 pueden pedir ~14 A en bloqueo.
   La Goldenmate de 10 Ah declara 10 A máximos; la Nermak de 20 Ah es más
   segura. Si se queda la Goldenmate, limitar corriente por software y usar
   fusible principal de 10–15 A; validar que el BMS no corte en arranque.
2. **PWM en Raspberry Pi 5.** Dos BTS7960 necesitan PWM y enable. La Pi 5 no
   tiene tantos canales PWM hardware; validar `lgpio`/ROS 2 o añadir un RP2040
   como controlador de tracción. El MDD10A no elimina este problema.
3. **HAT NVMe agotado.** No comprar el SSD M.2 antes de tener el HAT. Si se
   opta por USB, confirmar que la Pi 5 arranca desde USB 3.0 con la versión de
   firmware/Ubuntu 24.04.
4. **Perfil 2020.** El 2040 es más pesado y ancho. Revisar el diseño mecánico y
   la masa antes de cortar. No mezclar cotas de 2020 con 2040.
5. **Batería importada.** La Goldenmate y la Nermak se envían desde EE. UU.;
   confirmar plazo, garantía y devolución. Las baterías de litio tienen
   restricciones de transporte.
6. **Cargador.** No está en la BOM base. Comprar uno con perfil LiFePO4
   (14,6 V) o usar una fuente de laboratorio con corriente limitada.
7. **Stock de marketplace.** “Sin stock en tienda” no significa “sin stock para
   despacho”. Confirmar vendedor, precio final y fecha de entrega.
8. **Precios volátiles.** Todos los precios son del 2026-11-21. Volver a cotizar
   antes de emitir la orden de compra.
9. **Aduanas.** Los envíos internacionales pueden sumar flete, IGV, derechos y
   gastos del courier. Confirmar el régimen aplicable con SUNAT y el courier;
   este documento no incluye esos costos.
10. **No hay compra aprobada.** Esta lista es un estudio de abastecimiento. La
    compra requiere aprobación del PO y del responsable de Hardware.
11. **E-stop de 10 A.** La seta de Electromanía está rated 10 A. Con la
    Goldenmate de 10 A y fusible de 10 A queda en el límite; si se sube a 15 A
    o se usa Li-ion 3S2P/3S3P, añadir el relé de 30 A y dejar que la seta corte
    solo la bobina. No usar la seta para cortar 15–25 A directo.

## 8. Plan de compra sugerido

| Orden | Qué comprar | Dónde | Por qué primero |
|---|---|---|---|
| 1 | Pi 5 8 GB, Active Cooler, fuente 27 W | The Pi Box | Es el núcleo y tiene stock |
| 2 | RPLIDAR A1M8, 2 × FIT0185, INA219, e-stop, 2 × XL4005 | Electromanía | Sensores y tracción; evita dos envíos |
| 3 | 2 × BTS7960, perfil 2040, XT60, microSD | Naylamp | Drivers y estructura; envío gratis > S/ 200 |
| 4 | BNO085 | Electronics Peru (Ica) | Única tienda con stock claro del módulo |
| 5 | Batería, portafusibles, interruptor, SSD USB + caja | Falabella | Marketplace; confirmar vendedor y plazo |
| 6 | Ruedas y placas PETG/TPU | Print3D.pe (Trujillo) | Se puede fabricar después de cerrar cotas |
| 7 | Cargador LiFePO4 | Falabella / importación | No bloquea el resto, pero sí la primera carga |
| 8 | Repuestos y consumibles | Varios | Al final, con el remanente |

> **Antes de pagar:** pedir por WhatsApp/correo la confirmación de stock, el
> precio final con envío y el plazo a la ciudad del equipo. Guardar la
> cotización como evidencia de la compra.

## 9. Alternativas si no se consigue algo

### 9.1 Si no hay Pi 5 8 GB

- **Pi 5 4 GB** (S/ 488 en The Pi Box): suficiente para Nav2 en el robot, pero
  más justo para compilar y para ROS 2 + herramientas. Estaba **agotada** al
  momento de la consulta.
- **Pi 4B 4 GB** (S/ 471,50 en The Pi Box): compatible con Ubuntu 24.04, menor
  rendimiento; también **agotada**. No recomendado para el escenario ampliado.
- **Importar** la Pi 5 8 GB; sumar flete e impuestos.

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

### 9.5 Si no hay batería de 6 Ah

- **Goldenmate 10 Ah** (S/ 239): la más cercana en masa; BMS de 10 A.
- **Nermak 20 Ah** (S/ 299): más autonomía y BMS presumiblemente mayor, pero
  2,5 kg.
- **Pack a medida 4S LiFePO4** con BMS ≥ 20 A: cotizar en Litio Energy
  (<https://litioperu.com/>) o en un taller de baterías de Lima.
- **LiFePO4 100 Ah** de Autosolar: solo si se acepta el peso y el costo.

### 9.6 Si no hay perfil 2020

- **2040** de Naylamp: más rígido y pesado; revisar diseño.
- **Chasis impreso en PETG reforzado**: válido para el mini demo, no para
  cargas altas.
- **Importar 2020** de AliExpress/OpenBuilds: largo plazo, pero mantiene el
  diseño original.

### 9.7 Si no hay HAT NVMe

- **SSD USB 3.0** + caja: la ruta local recomendada.
- **microSD A2**: la más simple; aceptar riesgo de corrupción y tener respaldo.
- **HAT oficial importado**: US$ 17,40 en Adafruit + flete.

### 9.8 Si no hay ESP32-S3

- **ESP32-C6-DevKitC-1 N8** (S/ 100, MTLAB): suficiente para 2 motores; menos
  margen para 6×6.
- **XIAO ESP32-C6** (S/ 39): compacto, pero 11 GPIO; solo con MDD10A y sin
  margen para LEDs o sensores extra.
- **ESP32 DevKit V1 clásico** (S/ 32–35): interino, más disponible; sin Wi-Fi 6
  ni Thread.
- **RP2040 / Teensy 4.1**: si no se necesita Wi-Fi y se prioriza determinismo.

### 9.9 Si no se quiere armar la batería Li-ion

- **Goldenmate 10 Ah LiFePO4** (S/ 239): lista para usar, más pesada, BMS 10 A.
- **Nermak 20 Ah LiFePO4** (S/ 299): más autonomía y masa.
- **Pack a medida en Litio Energy**: cotizar 3S2P/3S3P con BMS y certificación.
- **No usar celdas 18650 sin BMS, sin fusible y sin carcasa ignífuga.**

## 10. Fuentes y trazabilidad

- Fuentes de precios y stock: `F-19` a `F-38` en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Fuentes de la propuesta ESP32/Li-ion y Hifisac: `F-30` a `F-38`.
- BOM base: [`bom.md`](bom.md).
- Diseño eléctrico base: [`diseno-electrico.md`](diseno-electrico.md).
- Variante 6×6 (no comprar): [`energia/bom-6x6.md`](energia/bom-6x6.md).
- Datos crudos de esta cotización: [`bom-peru.csv`](bom-peru.csv).
- Add-ons de ESP32 y batería a medida:
  [`bom-peru-addons.csv`](bom-peru-addons.csv).

> **Evidencia:** consulta web del 2026-11-21. No se ejecutaron pruebas de
> hardware ni se realizaron compras. Los precios deben revalidarse antes de la
> orden de compra.
