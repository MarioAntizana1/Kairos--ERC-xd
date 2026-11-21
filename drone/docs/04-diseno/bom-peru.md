# BOM de visión cotizada en Perú

> Estado: Estudio de abastecimiento · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
>
> **No autoriza compra.** Precios en soles peruanos (PEN) con IGV, consultados el
> **2026-11-21** en catálogos públicos. No incluyen envío local, envío
> internacional, embalaje, aduanas ni fluctuaciones. El stock es el que declaraba
> la tienda en línea en ese momento; no se reservó ningún artículo.
>
> Esta cotización cubre el **payload de visión** del dron: Raspberry Pi 5,
> 2 × Camera Module 3, **ToF de piso**, almacenamiento, energía de vuelo y
> montaje. **No** cotiza el dron completo (frame, controladora de vuelo, ESCs,
> motores, batería, radio, estación de tierra).

## 1. Resumen ejecutivo

**Sí se puede comprar casi todo en Perú**, con dos excepciones claras y una
decisión de alcance:

1. **ToF para 6 m:** el **TFmini Plus 12 m** está en Electromanía y es la base.
   El VL53L1X (4 m) y el VL53L5CX 8×8 (4 m) **no alcanzan** para 6 m; quedan
   como alternativas solo para banco o vuelo bajo (≤4 m).
2. **UBEC 5 V/5 A para 2–6S:** no se encontró un modelo de dron verificado en
   Naylamp ni Electromanía. Se estima un Matek BEC12S-PRO importado (~S/ 120
   puesto en Lima) o se reutiliza el BEC de 5 V del dron si ya existe.
3. **HAT+ M.2:** el catálogo de The Pi Box lo lista a S/ 60, pero el stock no
   estaba confirmado al momento de la consulta. Si no hay, la ruta local es SSD
   por USB 3.0 o microSD A2.

La **ruta base** del payload —con **TFmini Plus 12 m**, HAT/SSD local y **UBEC
importado**— cuesta **S/ 2.229,60** antes de contingencia y **S/ 2.341,08** con
5 % de imprevistos. El **núcleo de visión** —Pi 5, dos cámaras, TFmini Plus y
cables— cuesta **S/ 1.403,00**. El **núcleo operativo de banco** —añade
refrigeración, fuente y microSD— cuesta **S/ 1.564,80**.

**Recomendación:** comprar primero en **The Pi Box** (Pi 5, cámaras, HAT,
refrigeración, fuente), **Electromanía** (cables FPC, **TFmini Plus**, conectores)
y **Naylamp** (tornillería, aisladores). Dejar para una segunda orden el UBEC y
la impresión 3D. El VL53L1X o el VL53L5CX 8×8 solo tienen sentido si se vuela a
≤4 m; para 6 m, el TFmini Plus es la opción. Confirmar stock del HAT antes de
comprar el SSD M.2 2242.

> **La base ya incluye el TFmini Plus por la altura de 6 m.** El VL53L1X ahorra
> S/ 255 (total ~S/ 2.073,33) pero **no ve el piso a 6 m**; el VL53L5CX 8×8
> ahorra S/ 140 (total ~S/ 2.194,08) y tampoco alcanza. No comprar un ToF de
> 4 m para esta misión salvo que sea para banco.

> **Aclaración técnica:** el ToF va **mirando al piso**. Mide la distancia
> cámara–suelo y sirve como referencia métrica para escalar y validar la
> calibración (plano del suelo, homografía, comparación con \(Z_{stereo}\)).
> **No** calcula geometría epipolar: eso lo hace el par estéreo calibrado. Una
> sola distancia no sustituye la calibración con tablero. Ver
> [`diseno-vision.md`](diseno-vision.md), sección 6.4.

## 2. Método y alcance

- Búsqueda en tiendas peruanas con envío nacional, marketplaces y tiendas de
  provincia, además de canales de importación.
- Se contrastó precio, moneda, IGV declarado, disponibilidad y, cuando estaba
  publicado, ciudad de despacho.
- Se priorizó el **componente exacto o funcionalmente equivalente**, no el más
  barato a cualquier costo.
- No se hicieron compras, reservas ni consultas por WhatsApp. Los precios son
  los del catálogo web.
- Los enlaces y las fechas de acceso están en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md), fuentes
  `F-06` a `F-22`.
- Tipo de cambio supuesto para importaciones: **S/ 3,75 por USD**. No es una
  cotización de tipo de cambio; sirve solo para comparar órdenes de magnitud.

> **Sobre el stock:** “En stock” significa que el catálogo lo declaraba así. En
> Falabella, “sin stock en tienda” puede convivir con “despacho a domicilio”
> porque el vendedor es un marketplace. Confirmar antes de pagar.

## 3. Proveedores encontrados

| Proveedor | Ubicación | Cobertura | Especialidad | Envío | Enlace |
|---|---|---|---|---|---|
| **The Pi Box** | Lima (Chacarilla) | Todo el Perú | Raspberry Pi, cámaras, HAT, accesorios | Olva Courier; tarifa en checkout | <https://thepibox.pe/> |
| **Electromanía** | Lima | Todo el Perú | Cámaras, cables FPC, sensores, conectores | Desde S/ 10; agencia o domicilio | <https://www.electromania.pe/> |
| **Naylamp Mechatronics** | Trujillo | Todo el Perú | ToF, tornillería, aisladores, conectores | Gratis desde S/ 200 | <https://naylampmechatronics.com/> |
| **Falabella** | Lima / marketplace | Todo el Perú | SSD, microSD | Domicilio; algunos productos se envían desde EE. UU. | <https://www.falabella.com.pe/> |
| **Print3D.pe** | Trujillo | Servicio nacional | Impresión 3D, PETG, TPU, piezas técnicas | A coordinar | <https://print3d.pe/> |
| **Adafruit** | EE. UU. | Importación | VL53L5CX, VL53L1X, cables Qwiic | Internacional | <https://www.adafruit.com/> |
| **ZoneFPV / Matek** | EE. UU. / internacional | Importación | UBEC/BEC para drones | Internacional | <https://zonefpv.com/> |

> No se encontró una tienda peruana con el **VL53L5CX** ni con un **UBEC de
> dron 5 V/5 A** verificado. Las tiendas de Lima despachan a provincia; confirmar
> plazo y costo antes de pagar.

## 4. BOM cotizada: ruta recomendada (base local + UBEC importado)

### 4.1 Cómputo y almacenamiento

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B01 | Raspberry Pi 5 8 GB | Placa oficial | 1 | The Pi Box | S/ 768,00 | S/ 768,00 | En stock (oferta) | <https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444> |
| B02 | HAT+ M.2 | Oficial, PCIe NVMe | 1 | The Pi Box | S/ 60,00 | S/ 60,00 | Stock por confirmar | <https://thepibox.pe/shop/exp-rp-006-hat-m-2-raspberry-pi-3475> |
| B03 | SSD NVMe 128 GB | KingSpec M.2 2242, PCIe 3.0 ×2 | 1 | Falabella (oyetec peru) | S/ 149,80 | S/ 149,80 | Marketplace; despacho a domicilio | <https://www.falabella.com.pe/falabella-pe/product/159932959/ssd-kingspec-128gb-m-2-2242-nvme-pcie-3-0-x2-bm-key> |
| B04 | Refrigeración | Active Cooler oficial | 1 | The Pi Box | S/ 29,90 | S/ 29,90 | En stock | <https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454> |
| B05 | microSD de respaldo | 64 GB A2 (SanDisk Extreme Pro) | 1 | Falabella (urge) | S/ 64,90 | S/ 64,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador> |
| B06 | Fuente de banco | 27 W USB-C (5,1 V 5 A) | 1 | The Pi Box | S/ 67,00 | S/ 67,00 | En stock | <https://thepibox.pe/shop/fuente-de-poder-27-w-raspberry-pi-3458> |

**Subtotal A: S/ 1.139,60.**

> **Por qué NVMe y no microSD:** el registro de dos cámaras a 10 fps y la nube de
> puntos generan escritura continua; una microSD A2 se degrada y se corrompe con
> facilidad. El HAT+ M.2 con un SSD 2242 es la opción compacta. Si el HAT no
> tiene stock, la alternativa es un SSD SATA/USB 3.0 (más pesado) o arrancar por
> microSD y aceptar el riesgo. **No comprar el SSD antes de confirmar el HAT y
> que el M.2 sea de 2242 mm.**
>
> **La fuente de 27 W es de banco, no de vuelo.** Entrega 5,1 V y 5 A, pero no
> acepta 2–6S ni tiene cables para el dron. Para volar hace falta el UBEC (B10).

### 4.2 Percepción

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B07 | Cámara estéreo | Camera Module 3 Standard, IMX708 12 MP | 2 | The Pi Box | S/ 140,00 | S/ 280,00 | En stock | <https://thepibox.pe/shop/cam-rp-006-camara-v3-estandar-raspberry-pi-3368> |
| B08 | Cable FPC 22→15 | 300 mm, para Pi 5 | 2 | Electromanía | S/ 12,50 | S/ 25,00 | En stock | <https://www.electromania.pe/producto/cable-para-camara-raspberry-pi-5-300mm/> |
| B09 | ToF de piso | TFmini Plus, 12 m, haz ~2°, UART/I²C, IP65 | 1 | Electromanía | S/ 330,00 | S/ 330,00 | En stock | <https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/> |

**Subtotal B: S/ 635,00.**

> **Cada Camera Module 3 incluye un cable de 200 mm de 15→22 pines.** Por eso
> B08 es un repuesto/alargue, no un requisito absoluto. Si la baseline de 150 mm
> y la posición de la Pi permiten usar el cable incluido, se pueden restar
> S/ 25. La cámara también incluye un cable de 150 mm de 15→15 pines, que no
> sirve para la Pi 5.
>
> **Standard vs Wide:** la Standard tiene 66° horizontales y 4,74 mm de focal;
> la Wide tiene 102° horizontales y 2,75 mm. Para profundidad a distancia, la
> Standard tiene mejor resolución angular y menos distorsión. La Wide es útil
> para interiores y cobertura, pero exige más calibración y una baseline mayor
> para la misma precisión. **La BOM usa Standard**; la Wide está en alternativas.
>
> **La base es el TFmini Plus de 12 m.** A 6 m de altura, el piso está a 6 m;
> el VL53L1X (4 m) y el VL53L5CX 8×8 (4 m) **saturan**. El TFmini Plus tiene un
> haz estrecho (~2°), mide un spot de ~21 cm a 6 m y es IP65. Para calibrar,
> usar una superficie plana y mate. El VL53L1X (4 m, 27°) queda como alternativa
> de banco o vuelo ≤4 m; su cono promedia una zona grande del piso. El VL53L5CX
> 8×8 (4 m) sirve para ajustar un plano del suelo, pero tampoco alcanza a 6 m.
> Ver sección 9.2.

### 4.3 Energía de vuelo

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B10 | UBEC 5 V/5 A | Matek BEC12S-PRO, 9–55 V → 5,2 V/5 A | 1 | Importación | ~S/ 120,00 | ~S/ 120,00 | Estimado; cotizar | <https://zonefpv.com/products/matek-bec12s-pro-9-55v-to-5v-8v-12v-5a-bec-voltage-regulator-fpv-drone> |
| B11 | Conectores, cable y protección | XT60/XT30, 18–20 AWG, fusible 5 A, interruptor | 1 | Naylamp / Electromanía | ~S/ 60,00 | ~S/ 60,00 | Estimado | <https://naylampmechatronics.com/216-conectores-xt> |
| B12 | Capacitor | 1000 µF low ESR en riel 5 V | 1 | Electromanía | ~S/ 5,00 | ~S/ 5,00 | Estimado | <https://www.electromania.pe/> |

**Subtotal C: S/ 185,00.**

> **Presupuesto de potencia:** Pi 5 típico 8–12 W (pico 25 W), SSD 2–3 W,
> cámaras ~0,6 W, ToF ~0,5 W, ventilador ~0,5 W. Total típico **12–16 W** a 5 V
> = **2,4–3,2 A**; el UBEC de 5 A continuos deja margen. El Matek declara 5 A
> continuos y 9 A de pico, entrada 9–55 V (2–12S), 5 g. Es una estimación
> importada; si el dron ya tiene un BEC de 5 V/5 A, eliminar B10.
>
> **Alimentar la Pi 5 desde un UBEC:** usar 5,1–5,2 V, cable corto de 20 AWG,
> fusible de 5 A y capacitor de 1000 µF. La Pi 5 espera Power Delivery por
> USB-C; con un UBEC “tonto” arranca, pero puede limitar la corriente USB. Las
> cámaras son CSI y el SSD es PCIe, así que el límite USB no es crítico. Si se
> necesita, añadir `usb_max_current_enable=1` en `config.txt` y verificar que la
> tensión no caiga por debajo de 4,9 V. Medir con osciloscopio o registro de
> `vcgencmd`.
>
> **No alimentar la Pi 5 desde el BEC de 5 V del receptor o de la controladora**
> sin comprobar que entrega 5 A. Un brownout en vuelo reinicia la Pi y se pierde
> el registro, aunque la controladora de vuelo siga volando.

### 4.4 Mecánica y montaje

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B13 | Soportes, barra de baseline, bandeja y ventana ToF | Impresión 3D PETG/PA-CF; baseline 150 mm | 1 | Print3D.pe / taller | ~S/ 120,00 | ~S/ 120,00 | Estimado; cotizar | <https://print3d.pe/> |
| B14 | Aisladores de vibración | Silicona M3, 4–8 puntos | 1 | Naylamp | ~S/ 25,00 | ~S/ 25,00 | Estimado | <https://naylampmechatronics.com/> |
| B15 | Tornillería e insertos | M2.5/M3, separadores, insertos térmicos | 1 | Naylamp / ferretería | ~S/ 35,00 | ~S/ 35,00 | Estimado | <https://naylampmechatronics.com/72-tornillos-y-tuercas> |
| B16 | Térmicos, espuma y velcro | Almohadilla térmica, espuma, fijación | 1 | Varios | ~S/ 15,00 | ~S/ 15,00 | Estimado | — |

**Subtotal D: S/ 195,00.**

> **La barra de baseline es la pieza más crítica.** Debe mantener las dos
> cámaras rígidas y paralelas; cualquier flexión relativa invalida la
> calibración. Usar perfil de aluminio 2020, tubo de carbono o PETG/PA-CF grueso;
> no usar una barra impresa fina. Los agujeros de la cámara son M2.5 y el
> montaje debe permitir ajustar la separación entre 100 y 200 mm. La baseline
> nominal es 150 mm.
>
> **Aisladores:** la CM3 tiene autofoco por voice-coil; la vibración del dron
> puede hacer que el foco “cace” y que las imágenes se vean borrosas. Aislar el
> payload del frame con silicona y **bloquear el foco** en vuelo (ver
> [`diseno-vision.md`](diseno-vision.md), sección 4).

### 4.5 Cableado y varios

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B17 | USB-C corto + ferrita | Alimentación Pi 5 | 1 | Varios | ~S/ 25,00 | ~S/ 25,00 | Estimado | — |
| B18 | Dupont/JST/termorretráctil | ToF, señales, protección | 1 | Electromanía | ~S/ 20,00 | ~S/ 20,00 | Estimado | <https://www.electromania.pe/> |
| B19 | Repuestos | Fusibles, cable, conectores | 1 | Varios | ~S/ 30,00 | ~S/ 30,00 | Estimado | — |

**Subtotal E: S/ 75,00.**

## 5. Totales

### 5.1 Ruta recomendada (base local + UBEC importado)

| Bloque | Subtotal |
|---|---:|
| Cómputo y almacenamiento | S/ 1.139,60 |
| Percepción | S/ 635,00 |
| Energía de vuelo | S/ 185,00 |
| Mecánica y montaje | S/ 195,00 |
| Cableado y varios | S/ 75,00 |
| **Subtotal** | **S/ 2.229,60** |
| Imprevistos / envío local (5 %) | ~S/ 111,48 |
| **Total estimado** | **~S/ 2.341,08** |

> La **fuente de 27 W** (S/ 67) es de banco: si se excluye del kit de vuelo, el
> total baja a **~S/ 2.270,73**. Si los cables de 200 mm incluidos alcanzan, se
> restan S/ 25 y el total baja a **~S/ 2.314,83**. La horquilla realista es
> **S/ 2.200–2.450** según stock, envío y si se reutiliza el BEC del dron.

### 5.2 Escenarios

| Escenario | Qué añade / cambia | Total |
|---|---|---:|
| **Núcleo de visión** | Pi 5 + 2 × CM3 + TFmini Plus 12 m + 2 cables 300 mm | **S/ 1.403,00** |
| **Núcleo operativo de banco** | + Active Cooler + fuente 27 W + microSD 64 GB | **S/ 1.564,80** |
| **Kit completo (banco + vuelo)** | + HAT/SSD + UBEC + montaje + cableado + 5 % | **S/ 2.341,08** |
| Sin fuente de banco | — S/ 67,00 | **S/ 2.270,73** |
| Sin cables extra | — S/ 25,00 | **S/ 2.314,83** |
| ToF local ≤4 m | VL53L1X (−S/ 255) | **S/ 2.073,33** |
| ToF 8×8 ≤4 m | VL53L5CX (−S/ 140) | **S/ 2.194,08** |
| Cámaras Wide | Reemplaza B07 (+S/ 110) | **S/ 2.456,58** |
| Cámaras global shutter | Reemplaza B07 (+S/ 120) | **S/ 2.467,08** |
| SSD 512 GB | Reemplaza B03 (+S/ 110,20) | **S/ 2.456,79** |
| USB 128 GB sin HAT | Reemplaza B02+B03 (−S/ 129,80) | **S/ 2.204,79** |

> Los totales con upgrade incluyen el 5 % de contingencia sobre la base
> modificada. Son estimaciones, no una cotización formal.

## 6. Disponibilidad: exacto vs. sustituto vs. importación

| Componente | ¿Exacto en Perú? | Sustituto local | Importación | Impacto / decisión |
|---|---|---|---|---|
| Raspberry Pi 5 8 GB | **Sí** (The Pi Box) | Pi 5 4 GB (S/ 488) o 16 GB (S/ 1.699) | Adafruit / tiendas Pi | 8 GB es el punto medio; 16 GB no se justifica para este pipeline |
| Camera Module 3 Standard | **Sí** (The Pi Box) | CM3 Wide (S/ 195) o CM3 NoIR | Adafruit / The Pi Hut | Standard es la base; Wide solo si se prioriza cobertura |
| Cable 22→15 | **Sí** (Electromanía, The Pi Box) | Cable incluido de 200 mm | — | Incluido con cada cámara; B08 es repuesto |
| ToF de piso TFmini Plus 12 m | **Sí** (Electromanía) | VL53L1X 4 m (S/ 75); DFRobot 4 m IP67 (S/ 115) | TF-Luna 8 m; VL53L5CX 8×8 4 m | **Base para 6 m**; haz ~2°, IP65, UART/I2C |
| ToF VL53L1X 4 m | **Sí** (Naylamp) | VL53L0X (1,2 m); DFRobot 4 m | — | Solo banco/vuelo ≤4 m; **no sirve a 6 m** |
| ToF VL53L5CX 8×8 4 m | **No** | Ninguno local | Adafruit US$ 19,95 + envío | Plano del suelo ≤4 m; **no sirve a 6 m**; ~S/ 190 landed |
| HAT+ M.2 | **Stock por confirmar** | SSD USB 3.0 + caja; microSD A2 | HAT oficial | No comprar SSD 2242 antes de confirmar el HAT |
| SSD NVMe 128 GB 2242 | **Sí** (Falabella) | SSD 512 GB oficial (S/ 260) | — | Verificar que el HAT acepte 2242 |
| UBEC 5 V/5 A | **No verificado** | BEC del dron; módulo XL4005 (no recomendado para 6S) | Matek BEC12S-PRO | Preferir UBEC de dron con 5 A continuos; fusible |
| Montaje 3D | **Servicio local** | Perfil 2020 + soportes | — | Cotizar por pieza y material; PETG/PA-CF |
| Aisladores/tornillería | **Sí** (Naylamp) | Ferretería local | — | Comprar surtido y repuestos |

## 7. Riesgos y verificaciones antes de comprar

1. **HAT+ M.2 sin stock.** No comprar el SSD 2242 hasta confirmar que el HAT
   está disponible y que el módulo entra físicamente. Si no, usar USB 3.0.
2. **ToF de piso a 6 m.** El TFmini Plus (12 m) cubre la altura de la
   competencia con margen. Verificarlo a 6 m sobre un piso plano y mate antes de
   volar. El VL53L1X y el VL53L5CX son de 4 m: **no comprarlos para 6 m**.
   El TFmini Plus es local (Electromanía); el 8×8 se importa y no alcanza.
3. **UBEC y corriente.** La Pi 5 puede pedir 25 W en pico. Verificar que el UBEC
   entregue 5 A continuos a 5,1 V y que el cable/fusible soporten 5 A. Medir la
   tensión en carga; un brownout reinicia la Pi.
4. **Peso y centro de gravedad.** El payload estimado es 250–300 g. Pesarlo y
   verificar que el dron pueda compensarlo sin cambiar la batería. Montar cerca
   del CG.
5. **Vibración y autofoco.** La CM3 tiene lente móvil; la vibración puede
   arruinar el estéreo. Usar aisladores, bloquear el foco y probar con hélices
   puestas en banco antes de volar.
6. **Rolling shutter y falta de genlock.** La CM3 no tiene conector de
   sincronización de hardware; la Pi 5 captura dos cámaras, pero no con un
   trigger común. En movimiento rápido habrá skew. Mitigar con vuelo lento,
   exposición corta y, si hace falta, cámaras global shutter.
7. **Interferencia WiFi/Bluetooth.** La Pi 5 transmite en 2,4/5 GHz. Puede
   interferir con la radio del dron. Deshabilitar WiFi/BT en vuelo o usar un
   módulo externo blindado; probar en tierra con la radio encendida.
8. **Calibración y temperatura.** La baseline y el foco pueden derivar con el
   calor. Calibrar a temperatura de operación y reverificar después de 10 min.
9. **Precios volátiles.** Todos los precios son del 2026-11-21. Volver a cotizar
   antes de la orden de compra.
10. **Aduanas.** Los envíos internacionales pueden sumar flete, IGV, derechos y
    gastos del courier. Confirmar el régimen aplicable con SUNAT y el courier;
    este documento no incluye esos costos.
11. **No hay compra aprobada.** Esta lista es un estudio de abastecimiento. La
    compra requiere aprobación del PO y del responsable de Hardware.
12. **La visión no es un sistema de seguridad.** No confiar en el ToF de piso
    ni en el estéreo para evitar obstáculos críticos; la controladora de vuelo y
    el piloto conservan la autoridad.
13. **Entorno cerrado / jaula.** Sin GPS, con iluminación artificial, red o
    paredes cercanas y radiofrecuencia confinada. Verificar posicionamiento
    local/optical flow de la FC, anti-flicker de las cámaras (50 Hz en Perú),
    WiFi/BT apagados y protecciones de hélices. La jaula no sustituye el
    preflight ni el seguro.

## 8. Plan de compra sugerido

| Orden | Qué comprar | Dónde | Por qué primero |
|---|---|---|---|
| 1 | Pi 5 8 GB, 2 × CM3 Standard, Active Cooler, fuente 27 W | The Pi Box | Núcleo de visión y banco; stock declarado |
| 2 | 2 × cable FPC 300 mm, conectores, capacitor | Electromanía | Cables y protección; envío combinado |
| 3 | TFmini Plus 12 m, aisladores, tornillería | Electromanía / Naylamp | ToF de piso para 6 m y montaje |
| 4 | HAT+ M.2 + SSD 128 GB 2242 | The Pi Box + Falabella | Solo si el HAT está disponible |
| 5 | UBEC 5 V/5 A, XT60/XT30, fusible | Importación / tienda de drones | Energía de vuelo; cotizar landed |
| 6 | Soportes/barra/bandeja impresos | Print3D.pe / taller | Se fabrica después de cerrar la baseline |
| 7 | Opcional solo para banco/≤4 m: VL53L1X o VL53L5CX 8×8 | Naylamp / Adafruit | No sirven para 6 m; no comprar para la competencia |
| 8 | Repuestos y consumibles | Varios | Al final, con el remanente |

> **Antes de pagar:** pedir por WhatsApp/correo la confirmación de stock, el
> precio final con envío y el plazo a la ciudad del equipo. Guardar la cotización
> como evidencia de la compra.

## 9. Alternativas y upgrades

### 9.1 Cámaras

- **Camera Module 3 Wide (S/ 195):** 102° horizontales, más cobertura y menos
  resolución angular; útil para interiores. Requiere recalibrar y aceptar más
  distorsión.
- **Cámara global shutter OV9281 1 MP (S/ 200, Electromanía):** monocroma,
  global shutter, 79°; evita el skew de las escenas dinámicas. Menor resolución
  y sin color. Verificar si el módulo permite sincronización hardware; si no,
  sigue siendo rolling-free pero no genlock.
- **Camera Module 3 NoIR:** para luz infrarroja; no es la base porque el filtro
  IR es útil para profundidad con luz visible.

### 9.2 ToF de piso

- **TFmini Plus (S/ 330, Electromanía):** 12 m, IP65, UART/I²C, 100 Hz, haz
  estrecho (~2°). **Base para 6 m**: a 6 m el spot mide ~21 cm y el margen al
  límite de 12 m es amplio. Un solo punto; ~11 g. Verificar nivel lógico
  UART/I²C (3,3 V) y usar level shifter si hace falta.
- **VL53L1X (S/ 75, Naylamp):** 4 m, 27°, un punto, I²C, 50 Hz. **Solo banco o
  vuelo ≤4 m**; a 6 m satura y no ve el piso. Su cono promedia una zona grande;
  para calibrar, superficie plana y mate.
- **VL53L5CX (US$ 19,95 + envío, Adafruit):** 8×8 zonas, 4 m, 63°, 60 Hz, I²C,
  0,5 g. Útil para ajustar un plano del suelo a ≤4 m, pero **no sirve a 6 m**.
  Requiere firmware al arrancar y cambio de dirección I²C.
- **VL53L4CX (US$ 14,95, Adafruit):** 6 m, 18°, un punto; llega justo a 6 m, sin
  margen. Importado; no recomendado para la altura de la competencia.
- **TF-Luna (importado, ~US$ 20):** 8 m, 100 Hz, UART/I²C, ~5 g; alternativa
  más liviana que el TFmini Plus, pero hay que importarla y validar el driver.
- **DFRobot 4 m IP67 (S/ 115, Electromanía):** robusto y local, pero de 4 m y
  con un cono ancho; **no sirve a 6 m**.

### 9.3 Cómputo

- **Pi 5 4 GB (S/ 488):** suficiente para captura y SGBM a baja resolución;
  más justo para ROS 2 y para grabar. No recomendado si se quiere 3D denso.
- **Pi 5 16 GB (S/ 1.699):** no aporta al pipeline actual; el cuello es CPU/ISP,
  no RAM. Solo si se añaden modelos de IA.
- **Jetson Orin Nano:** más potencia para IA y profundidad densa, pero mayor
  costo, consumo y peso; fuera de esta fase.

### 9.4 Almacenamiento

- **SSD 512 GB oficial (S/ 260):** más capacidad y garantía; +S/ 110.
- **USB 3.0 128 GB (S/ 80):** evita el HAT; más pesado y con peor sujeción.
- **microSD A2 64 GB (S/ 64,90):** solo respaldo; no para registro continuo.

### 9.5 Energía

- **Matek BEC12S-PRO:** 9–55 V → 5,2 V/5 A, 5 g; robusto para 6S.
- **BEC del dron:** si ya entrega 5 V/5 A, reutilizarlo; medir ripple y caída.
- **XL4005 (S/ 6,59):** módulo de laboratorio, no recomendado para 6S ni para
  vibración; no tiene la protección de un UBEC de dron.

## 10. Fuentes y trazabilidad

- Fuentes de precios y stock: `F-06` a `F-22` en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Especificaciones de Pi 5 y Camera Module 3: `F-01` a `F-04`.
- Especificaciones de ToF: `F-13`, `F-14`, `F-15`, `F-16`.
- Referencia internacional: [`bom.md`](bom.md).
- Diseño de visión: [`diseno-vision.md`](diseno-vision.md).
- Datos crudos: [`bom-peru.csv`](bom-peru.csv).

> **Evidencia:** consulta web del 2026-11-21. No se ejecutaron pruebas de
> hardware ni se realizaron compras. Los precios deben revalidarse antes de la
> orden de compra.
