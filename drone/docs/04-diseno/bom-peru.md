# BOM de visión cotizada en Perú

> Estado: Estudio de abastecimiento · Versión: 0.2 · Revisión: 2026-11-23 · Responsable: rol de Hardware
>
> **No autoriza compra.** Precios en soles peruanos (PEN) con IGV cuando la
> tienda lo indica, consultados el **2026-11-23** en catálogos públicos. No
> incluyen envío local, envío internacional, embalaje, aduanas ni fluctuaciones.
> El stock es el que declaraba la tienda en línea en ese momento; no se reservó
> ningún artículo.
>
> Esta cotización cubre el **payload de visión** del dron: Raspberry Pi 5,
> 2 × Camera Module 3, **ToF de piso**, microSD de arranque, energía de vuelo y
> montaje. **No** cotiza el dron completo (frame, controladora de vuelo, ESCs,
> motores, batería, radio, estación de tierra). Son **15 filas** con
> `incluir=si`; las 7 alternativas quedan fuera del presupuesto.

## Cambios del 2026-11-23

- **Fuera el HAT+ M.2** (B02, S/ 60,00) y el **SSD NVMe 128 GB** (B03,
  S/ 149,80): no se usan en ninguno de los tres proyectos y, sin HAT, no hay
  M.2. El arranque y el registro pasan a la **microSD** (B05).
- **Fuera la fuente de 27 W** (B06, S/ 67,00): no se compra.
- **Fuera la impresión 3D de proveedor** (B13, S/ 120,00): las piezas se
  imprimen en local.
- **El UBEC importado de la v0.1 (B10, ~S/ 120,00) se reemplaza por un XL4005
  de S/ 6,59**, regulador DC-DC 4–38 V → 5 V/5 A que cubre 4S y 6S; se derratea
  a 3 A y se filtra con el capacitor de 1000 µF (B12). El **Matek BEC12S-PRO**
  queda como alternativa importada si el ripple o el peso fueran críticos.
- La **microSD es ahora el medio de arranque**, no solo un respaldo: asume el
  riesgo de lentitud y corrupción que antes cubría el SSD.
- La base queda en **S/ 1.719,39** y el total con 5 % en **S/ 1.805,36**.
  **Dato histórico, no vigente:** la v0.1 cerraba en S/ 2.341,08.

## 1. Resumen ejecutivo

**Sí se puede abastecer el payload en Perú.** Las 15 filas incluidas se compran
en el país; varias (B11, B12 y B14 a B19) son estimaciones de compra local, no
cotizaciones cerradas. La única importación prevista es la alternativa Matek
BEC12S-PRO, no la base.

1. **ToF para 6 m:** el **TFmini Plus 12 m** está en Electromanía y es la base.
   El VL53L1X (4 m) y el VL53L5CX 8×8 (4 m) **no alcanzan** para 6 m; quedan
   como alternativas solo para banco o vuelo bajo (≤4 m).
2. **Energía:** el **XL4005** (S/ 6,59) es un regulador DC-DC local de 4–38 V →
   5 V/5 A que cubre 4S y 6S, pero **no es un UBEC de dron**: hay que derratearlo
   a 3 A, filtrarlo con 1000 µF y verificar el ripple. Si el ruido o el peso
   fueran críticos, la alternativa es el Matek BEC12S-PRO importado.
3. **Arranque:** sin HAT+ M.2 no hay SSD. La Pi 5 arranca y registra en la
   **microSD A2 de 64 GB** (B05). Es la concesión del recorte de costo; una
   microSD se degrada y se corrompe con escritura continua. Segmentar el
   registro, sincronizar y respaldar.

La **ruta base** —15 filas, sin fuente de 27 W, sin HAT y sin SSD— cuesta
**S/ 1.719,39** antes de contingencia y **S/ 1.805,36** con 5 % de imprevistos.
El **núcleo de visión** —Pi 5, dos cámaras, TFmini Plus y cables— cuesta
**S/ 1.403,00**. El **núcleo operativo de banco** —añade refrigeración y
microSD— cuesta **S/ 1.497,80**.

**Recomendación:** comprar primero en **The Pi Box** (Pi 5, cámaras,
refrigeración), **Electromanía** (cables FPC, **TFmini Plus**, XL4005,
capacitor, conectores), **Falabella** (microSD) y **Naylamp** (aisladores,
tornillería). La impresión 3D se hace en local. Dejar el Matek para el final,
solo si la medición de ripple del XL4005 no convence.

> **La base ya incluye el TFmini Plus por la altura de 6 m.** El VL53L1X ahorra
> S/ 255 y el VL53L5CX 8×8 ahorra S/ 140, pero **no ven el piso a 6 m**. No
> comprar un ToF de 4 m para esta misión salvo que sea para banco.

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
  `F-06` a `F-22`. La lista vigente, con `incluir` y notas, es
  [`bom-peru.csv`](bom-peru.csv): **15 filas incluidas** y **7 alternativas**.
- Tipo de cambio supuesto para importaciones: **S/ 3,75 por USD**. No es una
  cotización de tipo de cambio; sirve solo para comparar órdenes de magnitud.

> **Sobre el stock:** “En stock” significa que el catálogo lo declaraba así. En
> Falabella, “sin stock en tienda” puede convivir con “despacho a domicilio”
> porque el vendedor es un marketplace. Confirmar antes de pagar.

## 3. Proveedores encontrados

| Proveedor | Ubicación | Cobertura | Especialidad | Envío | Enlace |
|---|---|---|---|---|---|
| **The Pi Box** | Lima (Chacarilla) | Todo el Perú | Raspberry Pi, cámaras, accesorios | Olva Courier; tarifa en checkout | <https://thepibox.pe/> |
| **Electromanía** | Lima | Todo el Perú | Cámaras, cables FPC, sensores, reguladores, conectores | Desde S/ 10; agencia o domicilio | <https://www.electromania.pe/> |
| **Naylamp Mechatronics** | Trujillo | Todo el Perú | ToF, tornillería, aisladores, conectores | Gratis desde S/ 200 | <https://naylampmechatronics.com/> |
| **Falabella** | Lima / marketplace | Todo el Perú | microSD y almacenamiento | Domicilio; algunos productos se envían desde EE. UU. | <https://www.falabella.com.pe/> |
| **Adafruit** | EE. UU. | Importación | VL53L5CX, VL53L1X, cables Qwiic | Internacional | <https://www.adafruit.com/> |
| **ZoneFPV / Matek** | EE. UU. / internacional | Importación | BEC/UBEC para drones | Internacional | <https://zonefpv.com/> |

> La impresión 3D se hace en local; **Print3D.pe** queda solo como respaldo si
> el taller no puede fabricar una pieza. No se encontró una tienda peruana con
> el **VL53L5CX** ni con un **UBEC de dron 5 V/5 A** verificado. El XL4005 es un
> regulador de laboratorio, no un UBEC de dron: verificar ripple antes de volar.
> Las tiendas de Lima despachan a provincia; confirmar plazo y costo antes de
> pagar.

## 4. BOM cotizada: ruta recomendada (base local, arranque por microSD)

> **Lectura de las tablas:** `(est.)` = estimación; `En stock` y `Marketplace`
> son el estado que declaraba el catálogo el 2026-11-23, no una reserva.

### 4.1 Cómputo y almacenamiento (grupo A)

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B01 | Raspberry Pi 5 8 GB | Placa oficial | 1 | The Pi Box | S/ 768,00 | S/ 768,00 | En stock (oferta) | <https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444> |
| B04 | Refrigeración | Active Cooler oficial | 1 | The Pi Box | S/ 29,90 | S/ 29,90 | En stock | <https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454> |
| B05 | microSD de arranque | 64 GB A2 (SanDisk Extreme Pro) | 1 | Falabella (urge) | S/ 64,90 | S/ 64,90 | Marketplace | <https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador> |

**Subtotal A: S/ 862,80.**

> **Arranque por microSD, no por SSD.** Sin HAT+ M.2 no hay M.2: la Pi 5
> arranca y registra en la microSD A2 (B05). Es más lenta que un SSD y se
> desgasta con escritura continua; conviene segmentar el registro, hacer
> `sync` periódico y copiar a un USB o al equipo de tierra. Si más adelante se
> compra el HAT, ver sección 9.4.
>
> **Supuesto de banco:** no se compra fuente de 27 W. Para las pruebas de banco
> se usará una fuente de laboratorio de 5 V/5 A o el XL4005 (B10) alimentado
> desde una fuente de 4–38 V del taller. Confirmar que el taller dispone de ella
> antes de la orden de compra.

### 4.2 Percepción (grupo B)

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

### 4.3 Energía de vuelo (grupo C)

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B10 | Regulador DC-DC | XL4005, 4–38 V → 5 V/5 A, derrateo a 3 A | 1 | Electromanía | S/ 6,59 | S/ 6,59 | En stock | <https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> |
| B11 | Conectores, cable y protección | XT60/XT30, 18–20 AWG, fusible 5 A, interruptor | 1 | Naylamp / Electromanía | S/ 60,00 | S/ 60,00 (est.) | Estimado | <https://naylampmechatronics.com/216-conectores-xt> |
| B12 | Capacitor | 1000 µF low ESR en riel 5 V | 1 | Electromanía | S/ 5,00 | S/ 5,00 (est.) | Estimado | <https://www.electromania.pe/> |

**Subtotal C: S/ 71,59.**

> **Presupuesto de potencia:** Pi 5 típico 8–12 W (pico 25 W), cámaras ~0,6 W,
> ToF ~0,5 W, ventilador ~0,5 W y microSD ~0,3 W. Total típico **10–14 W** a
> 5 V = **2,0–2,8 A**. El XL4005 declara 5 A, pero se derratea a **3 A** por
> disipación y por ser un módulo de laboratorio; el margen es estrecho. El pico
> de 25 W (~5 A) es transitorio y puede exceder el derrateo: probar en banco con
> las dos cámaras y medir la caída. Si el consumo sostenido pasa de 3 A o la
> temperatura sube, usar el Matek (5 A continuos) o reducir la carga.
>
> **Alimentar la Pi 5 desde el XL4005:** ajustar a 5,1–5,2 V antes de conectar,
> cable corto de 20 AWG, fusible de 5 A (B11) y capacitor de 1000 µF (B12) en
> el riel. La Pi 5 espera Power Delivery por USB-C; con un regulador “tonto”
> arranca, pero puede limitar la corriente USB. Las cámaras son CSI y el
> almacenamiento es microSD, así que el límite USB no es crítico. Si se
> necesita, añadir `usb_max_current_enable=1` en `config.txt` y verificar que la
> tensión no caiga por debajo de 4,9 V. Medir con osciloscopio o registro de
> `vcgencmd`.
>
> **Ripple:** el XL4005 es un buck de módulo abierto; el capacitor de 1000 µF
> filtra transitorios, no sustituye una medición. Verificar ripple y estabilidad
> con la Pi 5 y las dos cámaras en carga antes de montarlo en el dron; si el
> ripple es alto o la tensión oscila, usar el Matek BEC12S-PRO.
>
> **No alimentar la Pi 5 desde el BEC de 5 V del receptor o de la controladora**
> sin comprobar que entrega 5 A. Un brownout en vuelo reinicia la Pi y se pierde
> el registro, aunque la controladora de vuelo siga volando.

### 4.4 Mecánica y montaje (grupo D)

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B14 | Aisladores de vibración | Silicona M3, 4–8 puntos | 1 | Naylamp | S/ 25,00 | S/ 25,00 (est.) | Estimado | <https://naylampmechatronics.com/> |
| B15 | Tornillería e insertos | M2.5/M3, separadores, insertos térmicos | 1 | Naylamp / ferretería | S/ 35,00 | S/ 35,00 (est.) | Estimado | <https://naylampmechatronics.com/72-tornillos-y-tuercas> |
| B16 | Térmicos, espuma y velcro | Almohadilla térmica, espuma, fijación | 1 | Varios | S/ 15,00 | S/ 15,00 (est.) | Estimado | — |

**Subtotal D: S/ 75,00.**

> **La barra de baseline es la pieza más crítica.** Debe mantener las dos
> cámaras rígidas y paralelas; cualquier flexión relativa invalida la
> calibración. Usar perfil de aluminio 2020, tubo de carbono o PETG/PA-CF grueso;
> no usar una barra impresa fina. Los agujeros de la cámara son M2.5 y el
> montaje debe permitir ajustar la separación entre 100 y 200 mm. La baseline
> nominal es 150 mm.
>
> **Impresión local:** las piezas se imprimen en el taller del equipo, no se
> compran a un proveedor. Si el taller no puede fabricar una pieza crítica,
> Print3D.pe queda como respaldo.
>
> **Aisladores:** la CM3 tiene autofoco por voice-coil; la vibración del dron
> puede hacer que el foco “cace” y que las imágenes se vean borrosas. Aislar el
> payload del frame con silicona y **bloquear el foco** en vuelo (ver
> [`diseno-vision.md`](diseno-vision.md), sección 4).

### 4.5 Cableado y varios (grupo E)

| # | Componente | Modelo / sustitución | Cant. | Proveedor | Precio unit. | Subtotal | Estado | Enlace |
|---|---|---|---|---:|---|---:|---:|---|---|
| B17 | USB-C corto + ferrita | Alimentación Pi 5 | 1 | Varios | S/ 25,00 | S/ 25,00 (est.) | Estimado | — |
| B18 | Dupont/JST/termorretráctil | ToF, señales, protección | 1 | Electromanía | S/ 20,00 | S/ 20,00 (est.) | Estimado | <https://www.electromania.pe/> |
| B19 | Repuestos | Fusibles, cable, conectores | 1 | Varios | S/ 30,00 | S/ 30,00 (est.) | Estimado | — |

**Subtotal E: S/ 75,00.**

## 5. Totales

### 5.1 Ruta recomendada (base local, arranque por microSD)

| Bloque | Subtotal |
|---|---:|
| Cómputo y almacenamiento | S/ 862,80 |
| Percepción | S/ 635,00 |
| Energía de vuelo | S/ 71,59 |
| Mecánica y montaje | S/ 75,00 |
| Cableado y varios | S/ 75,00 |
| **Subtotal** | **S/ 1.719,39** |
| Imprevistos / contingencia (5 %) | S/ 85,97 |
| **Total estimado** | **S/ 1.805,36** |

> La base incluye las **15 filas con `incluir=si`** del CSV y excluye las 7
> alternativas. No incluye envío local ni internacional; el 5 % es un colchón
> de imprevistos, no una cotización de flete. Si los cables de 200 mm incluidos
> alcanzan, se pueden restar **S/ 25** de B08; si se reutiliza el BEC del dron,
> se puede restar B10 (S/ 6,59). Cualquiera de los dos ajustes baja el total,
> pero no se recalcula aquí para no mezclar escenarios.

### 5.2 Escenarios

| Escenario | Qué añade / cambia | Total |
|---|---|---:|
| **Núcleo de visión** | Pi 5 + 2 × CM3 + TFmini Plus 12 m + 2 cables 300 mm | **S/ 1.403,00** |
| **Núcleo operativo de banco** | + Active Cooler + microSD 64 GB (arranque) | **S/ 1.497,80** |
| **Kit completo con 5 %** | 15 filas + contingencia | **S/ 1.805,36** |
| Sin cables FPC extra | Si alcanzan los de 200 mm (−S/ 25) | **S/ 1.779,11** |
| Cámaras Wide | Reemplaza B07 (+S/ 110) | **S/ 1.920,86** |
| Cámaras global shutter | Reemplaza B07 (+S/ 120) | **S/ 1.931,36** |
| ToF local ≤4 m | VL53L1X (−S/ 255) | **S/ 1.537,61** |
| ToF 8×8 ≤4 m | VL53L5CX (−S/ 140) | **S/ 1.658,36** |
| Arranque USB 3.0 128 GB | Reemplaza B05 (+S/ 15,10) | **S/ 1.821,21** |

> Los dos núcleos son sumas de hardware sin contingencia. Los totales
> alternativos aplican el mismo 5 % sobre la base modificada; son aritmética
> sobre los precios de la tabla, no cotizaciones nuevas.

## 6. Disponibilidad: exacto vs. sustituto vs. importación

| Componente | ¿Exacto en Perú? | Sustituto local | Importación | Impacto / decisión |
|---|---|---|---|---|
| Raspberry Pi 5 8 GB | **Sí** (The Pi Box) | Pi 5 4 GB (S/ 488) o 16 GB (S/ 1.699) | Adafruit / tiendas Pi | 8 GB es el punto medio; 16 GB no se justifica para este pipeline |
| Camera Module 3 Standard | **Sí** (The Pi Box) | CM3 Wide (S/ 195) o CM3 NoIR; GS OV9281 (S/ 200) | Adafruit / The Pi Hut | Standard es la base; Wide solo si se prioriza cobertura |
| Cable 22→15 | **Sí** (Electromanía, The Pi Box) | Cable incluido de 200 mm | — | Incluido con cada cámara; B08 es repuesto |
| ToF de piso TFmini Plus 12 m | **Sí** (Electromanía) | VL53L1X 4 m (S/ 75); DFRobot 4 m IP67 (S/ 115) | TF-Luna 8 m; VL53L5CX 8×8 4 m | **Base para 6 m**; haz ~2°, IP65, UART/I2C |
| ToF VL53L1X 4 m | **Sí** (Naylamp) | VL53L0X (1,2 m); DFRobot 4 m | — | Solo banco/vuelo ≤4 m; **no sirve a 6 m** |
| ToF VL53L5CX 8×8 4 m | **No** | Ninguno local | Adafruit US$ 19,95 + envío | Plano del suelo ≤4 m; **no sirve a 6 m**; ~S/ 190 landed |
| microSD 64 GB A2 | **Sí** (Falabella, marketplace) | USB 3.0 128 GB (S/ 80); microSD de repuesto | — | Arranque y registro; respaldar y llevar repuesto |
| Regulador XL4005 5 A | **Sí** (Electromanía) | BEC del dron; Matek BEC12S-PRO | Matek (ZoneFPV) | Derratear a 3 A; verificar ripple; no es UBEC de dron |
| Montaje 3D | **Local** (taller del equipo) | Perfil 2020 + soportes | — | Imprimir en PETG/PA-CF; baseline rígida; sin proveedor |
| Aisladores/tornillería | **Sí** (Naylamp) | Ferretería local | — | Comprar surtido y repuestos |

## 7. Riesgos y verificaciones antes de comprar

1. **Arranque por microSD y corrupción.** Sin HAT/SSD, la Pi 5 arranca y escribe
   en la microSD (B05). El desgaste y un corte de energía pueden corromper el
   sistema o el registro. Mitigar con imagen mínima, registro segmentado con
   `sync`, copia periódica a USB o al equipo de tierra y una microSD de repuesto
   ya flasheada. Si el registro continuo resulta crítico, pasar a USB 3.0
   (sección 9.4) o al HAT/SSD (futuro).
2. **ToF de piso a 6 m.** El TFmini Plus (12 m) cubre la altura de la
   competencia con margen. Verificarlo a 6 m sobre un piso plano y mate antes de
   volar. El VL53L1X y el VL53L5CX son de 4 m: **no comprarlos para 6 m**.
   El TFmini Plus es local (Electromanía); el 8×8 se importa y no alcanza.
3. **XL4005: ripple, corriente y protección.** Es un regulador de laboratorio,
   no un UBEC de dron: no trae la protección ni el filtrado de un BEC de vuelo.
   Derratear a 3 A, montar el capacitor de 1000 µF (B12) cerca de la carga,
   fusible de 5 A (B11), cable corto de 20 AWG y verificar con osciloscopio el
   ripple y la caída con la Pi 5 y las dos cámaras en carga. Si el ripple es
   alto, la temperatura sube o el consumo sostenido pasa de 3 A, usar el Matek
   BEC12S-PRO (sección 9.5).
4. **Peso y centro de gravedad.** El payload estimado de v0.1 era 250–300 g; al
   quitar HAT y SSD baja, pero hay que pesarlo. Verificar que el dron pueda
   compensarlo sin cambiar la batería. Montar cerca del CG.
5. **Vibración y autofoco.** La CM3 tiene lente móvil; la vibración puede
   arruinar el estéreo. Usar aisladores, bloquear el foco y probar en banco con
   el dron asegurado antes de volar.
6. **Rolling shutter y falta de genlock.** La CM3 no tiene conector de
   sincronización de hardware; la Pi 5 captura dos cámaras, pero no con un
   trigger común. En movimiento rápido habrá skew. Mitigar con vuelo lento,
   exposición corta y, si hace falta, cámaras global shutter.
7. **Interferencia WiFi/Bluetooth.** La Pi 5 transmite en 2,4/5 GHz. Puede
   interferir con la radio del dron. Deshabilitar WiFi/BT en vuelo o usar un
   módulo externo blindado; probar en tierra con la radio encendida.
8. **Calibración y temperatura.** La baseline y el foco pueden derivar con el
   calor. Calibrar a temperatura de operación y reverificar después de 10 min.
9. **Precios volátiles.** Todos los precios son del 2026-11-23. Volver a cotizar
   antes de la orden de compra.
10. **Aduanas.** Solo aplica a las alternativas importadas (Matek, VL53L5CX).
    Los envíos internacionales pueden sumar flete, IGV, derechos y gastos del
    courier. Confirmar el régimen aplicable con SUNAT y el courier; este
    documento no incluye esos costos.
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
| 1 | Pi 5 8 GB, 2 × CM3 Standard, Active Cooler | The Pi Box | Núcleo de visión y banco; stock declarado |
| 2 | 2 × cable FPC 300 mm, TFmini Plus, XL4005, capacitor | Electromanía | Percepción y energía; envío combinado |
| 3 | microSD 64 GB A2 | Falabella | Arranque; confirmar el vendedor marketplace |
| 4 | Aisladores, tornillería | Naylamp | Montaje; comprar surtido y repuestos |
| 5 | Impresión 3D local + térmicos/espuma/velcro | Taller local / varios | Se fabrica después de cerrar la baseline |
| 6 | USB-C corto + ferrita, fusible, interruptor, conectores, Dupont/JST | Varios / Electromanía | Cableado y protección |
| 7 | Opcional solo para banco/≤4 m: VL53L1X o VL53L5CX 8×8 | Naylamp / Adafruit | No sirven para 6 m; no comprar para la competencia |
| 8 | Matek BEC12S-PRO | Importación | Solo si el ripple o el peso del XL4005 no convencen |

> **Antes de pagar:** pedir por WhatsApp/correo la confirmación de stock, el
> precio final con envío y el plazo a la ciudad del equipo. Guardar la cotización
> para la evidencia de la compra.

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

- **SSD 512 GB oficial (S/ 260):** **futuro.** Requiere el HAT+ M.2, que no está
  en la BOM. Hoy no aplica: no hay M.2 sin HAT. Reevaluar solo si más adelante
  se compra el HAT.
- **USB 3.0 128 GB (S/ 80):** **alternativa de arranque sin HAT**. Reemplaza la
  microSD (+S/ 15,10); más pesado y con peor sujeción, pero evita el desgaste de
  la microSD.
- **microSD A2 64 GB (S/ 64,90):** medio de arranque actual, no solo respaldo.
  No usarla para registro continuo sin copias y repuesto.

### 9.5 Energía

- **XL4005 (S/ 6,59, Electromanía):** base actual. 4–38 V → 5 V/5 A nominal,
  derrateado a 3 A; exige capacitor de 1000 µF y verificación de ripple y
  temperatura. No tiene la protección de un UBEC de dron.
- **Matek BEC12S-PRO:** 9–55 V → 5,2 V/5 A, 5 g; alternativa importada si el
  ripple o el peso del XL4005 fueran críticos.
- **BEC del dron:** si ya entrega 5 V/5 A, reutilizarlo; medir ripple y caída
  antes de conectar la Pi 5.

## 10. Fuentes y trazabilidad

- Fuentes de precios y stock: `F-06` a `F-22` en
  [`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md).
- Regulador XL4005: catálogo de Electromanía, consulta del 2026-11-23 (URL en
  la tabla 4.3 y en [`bom-peru.csv`](bom-peru.csv)).
- Especificaciones de Pi 5 y Camera Module 3: `F-01` a `F-04`.
- Especificaciones de ToF: `F-13`, `F-14`, `F-15`, `F-16`.
- Referencia internacional: [`bom.md`](bom.md).
- Diseño de visión: [`diseno-vision.md`](diseno-vision.md).
- Datos crudos: [`bom-peru.csv`](bom-peru.csv).

> **Evidencia:** consulta web del 2026-11-23. No se ejecutaron pruebas de
> hardware ni se realizaron compras. Los precios deben revalidarse antes de la
> orden de compra.
>
> **Pendiente de alinear:** `fuentes.md` aún no registra el XL4005 ni la memoria
> USB 3.0; `README.md`, el plan de proyecto, `bom.md` y el guion de demo citan
> la BOM v0.1. Este documento y `bom-peru.csv` son la fuente vigente desde el
> 2026-11-23.
