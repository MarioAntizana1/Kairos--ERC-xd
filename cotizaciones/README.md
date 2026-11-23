# Cotizaciones — consolidado transversal de los tres subproyectos

Esta carpeta reúne el **BOM de los tres subproyectos agrupado por proveedor**, con
cantidades totales y cantidades por proyecto, precios, enlaces y stock, para enviar
una sola solicitud de cotización a cada empresa.

No es un BOM nuevo ni reemplaza a los de cada subproyecto: es una **vista
consolidada** de compra. La fuente de verdad sigue siendo el BOM de cada uno.

## Archivos

| Archivo | Qué contiene |
|---|---|
| [`bom-consolidado.md`](bom-consolidado.md) | Documento principal: resumen por proveedor, totales por proyecto, detalle con columnas MR / DR / RP, cambios acumulados, respuestas técnicas y supuestos |
| [`bom-consolidado.csv`](bom-consolidado.csv) | Las mismas 40 líneas en formato tabular (`cant_mr`, `cant_dr`, `cant_rp`) |
| [`solicitud-plantilla.md`](solicitud-plantilla.md) | Asunto, correo, versión de WhatsApp, tabla de líneas para pegar y seguimiento de respuestas |

## Qué se cotiza

| Bloque | Subproyecto | Origen | Líneas propias | Unidades |
|---|---|---|---:|---:|
| MR | Mini-rover | `mini-rover/docs/04-diseno/bom-peru.csv` + pack 2S4P de `bom-peru-addons.csv` | 21 | 38 |
| DR | Drone | `drone/docs/04-diseno/bom-peru.csv` (solo filas `incluir = si`) | 12 | 17 |
| RP | Rover-principal | `rover-principal/docs/04-diseno/bom-vision.csv` + 2 LiDAR + 2.º ToF | 3 | 8 |
| Compartidas | — | LiDAR (MR+RP), TFmini Plus (los tres), XL4005 (MR+DR), microSD (MR+DR) | 4 | — |
| | | **Total** | **40 líneas · 63 unidades** | |

**Total consolidado: ~S/ 8.178,27** (S/ 7.278,27 verificados + ~S/ 900 estimados),
sin envío y sin aduanas.

| Bloque | Verificado | Estimado | Total |
|---|---:|---:|---:|
| Mini-rover | S/ 2.257,88 | ~S/ 285 | S/ 2.542,88 |
| Drone | S/ 1.504,39 | ~S/ 215 | S/ 1.719,39 |
| Rover-principal (visión) | S/ 3.516,00 | ~S/ 400 | S/ 3.916,00 |

## Decisiones cerradas el 2026-11-23

| Tema | Decisión |
|---|---|
| LiDAR | **3 unidades**: 1 para el mini-rover y **2 para el rover-principal**. Alternativa aprobada: 3 en el rover principal (total 4, +S/ 600) |
| Tracción del mini-rover | **Boost 7,4 → 12 V** (módulo de 400 W, ~S/ 55): recupera 83 rpm y 0,39 m/s |
| Pack de energía | **2S4P de 8 celdas** (7,4 V / 14 Ah / 103,6 Wh) con BMS 2S |
| Cargador | **TP5100-84** (S/ 5,60): carga 2S a 8,4 V; el CN3722 de 3S ya no aplica |
| Solar | **2 paneles de 6 V en serie** (12 V); nunca 3 en serie |
| Pi Box | Sin HAT+ M.2 y sin fuente de 27 W; el dron arranca por microSD |
| Impresión 3D | Local; no se cotiza |

## El pack de energía (2S4P)

| Dato | Valor |
|---|---|
| Configuración | 2 series × 4 paralelo = **8 celdas** |
| Tensión | **7,4 V** nominal / **8,4 V** de carga |
| Capacidad | **14 Ah** |
| Energía | **103,6 Wh** |
| BMS | **2S**, 25 A (confirmar SKU en Bracsan) |
| Cargador | TP5100-84 (entrada 5–18 V, 2 A) |
| Solar | 2 paneles de 6 V en serie → ~0,8 A → ~16 h |
| Red | Fuente 12 V / 2 A → 2 A → ~7 h |
| Peso aprox. | ~420 g (vs ~1,5 kg de la LiFePO4 retirada) |

## Qué **no** se cotiza aquí

- **La copia de la BOM del mini demo en `rover-principal/`** (su documento se
  titula "mini demo"): suma cantidades duplicadas. Detalle en §7.1 del consolidado.
- **Lo que la revisión dio de baja**: HAT+ M.2, fuente de 27 W, SSD SATA y NVMe,
  caja USB, batería LiFePO4, cargador de red, perfil V-Slot y UBEC importado.
- **Inventario y trabajo local**: Raspberry Pi 4 8 GB, Argon ONE V2, perfil
  V-Slot, impresión 3D y los 4 paneles solares de 6 V.
- **Alternativas** de cámara, ToF, LiDAR y almacenamiento (§7.3 y §7.4).
- **Add-ons**: ESP32 de tiempo real, ruedas de 110–120 mm (reserva), soldador de
  punto y el estudio 6×6 (`OQ-09`).

## Pendiente antes de enviar

| Tema | Estado | Dónde |
|---|---|---|
| BMS 2S de 25 A en Bracsan | A confirmar SKU y precio (referencia S/ 18 del 3S) | §4.4 |
| Portafusible en Bracsan | A confirmar (referencia Falabella S/ 15,90) | §4.4 |
| ¿Quién suelda el pack por punto? | Abierto: soldador Bracsan S/ 390, o pedirles que lo suelden | §6.2 |
| Regulador del dron | XL4005 local (S/ 6,59); el Matek queda como alternativa | §6.4 |
| BOM de origen | Ya actualizados el 2026-11-23; queda la bitácora y el registro de fuentes | §8 |

## Estado de los precios

- Productos: **catálogo web del 2026-11-21**; hoy son referencia, no oferta.
- Averiguaciones técnicas: **2026-11-23** (TP5100, BMS 2S, boost, reguladores,
  soldadura) y están marcadas como tales.
- **No** se contactó a ningún proveedor, no se reservó y no se pagó nada.
- Las líneas con `~` o `ref.` son **estimaciones o precios de referencia**.
- Sin envío, sin IGV no declarado y sin aduanas.

## Cómo mantenerlo

1. Si cambia una cantidad o un modelo, actualiza **primero** el BOM del
   subproyecto (`bom-peru.csv` o `bom-vision.csv`).
2. Luego refleja el cambio en `bom-consolidado.md`, `bom-consolidado.csv` y en las
   tablas de resumen (§2 y §2.1).
3. Cuando llegue una cotización, anótala en
   [`solicitud-plantilla.md`](solicitud-plantilla.md) §6. La evidencia formal se
   crea en la fase de compras, no ahora.

## Fase

Estamos en **planificación e investigación**: este paquete se prepara, no se
ejecuta. Enviar las solicitudes es una acción de la fase de compras y requiere que
el usuario la abra explícitamente (ver `AGENTS.md` §0).
