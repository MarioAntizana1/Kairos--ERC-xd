# Cotizaciones — consolidado transversal de los tres subproyectos

Esta carpeta reúne el **BOM de los tres subproyectos agrupado por proveedor**, con
cantidades totales, precios, enlaces y stock, para enviar una sola solicitud de
cotización a cada empresa.

No es un BOM nuevo ni reemplaza a los de cada subproyecto: es una **vista
consolidada** de compra. La fuente de verdad sigue siendo el BOM de cada uno.

## Archivos

| Archivo | Qué contiene |
|---|---|
| [`bom-consolidado.md`](bom-consolidado.md) | Documento principal: resumen por proveedor, totales por proyecto, detalle con enlaces, cambios de la revisión, respuestas técnicas, exclusiones y supuestos |
| [`bom-consolidado.csv`](bom-consolidado.csv) | Las mismas 39 líneas en formato tabular para filtrar o adjuntar |
| [`solicitud-plantilla.md`](solicitud-plantilla.md) | Asunto, correo, versión de WhatsApp, tabla de líneas para pegar y seguimiento de respuestas |

## Qué se cotiza

| Bloque | Subproyecto | Origen | Líneas propias |
|---|---|---|---:|
| MR | Mini-rover | `mini-rover/docs/04-diseno/bom-peru.csv` + pack de batería de `bom-peru-addons.csv` | 20 |
| DR | Drone | `drone/docs/04-diseno/bom-peru.csv` (solo filas `incluir = si`) | 12 |
| RP | Rover-principal | `rover-principal/docs/04-diseno/bom-vision.csv` + LiDAR + 2.º ToF | 4 |
| Compartidas | — | TFmini Plus (los tres), XL4005 (MR+DR), microSD (MR+DR) | 3 |
| | | **Total** | **39 líneas · 56 unidades** |

**Total consolidado: ~S/ 6.928,47** (S/ 6.033,47 verificados + ~S/ 895 estimados),
sin envío y sin aduanas.

## Qué **no** se cotiza aquí

- **La copia de la BOM del mini demo en `rover-principal/`**: su propio documento
  se titula "BOM de electrónica cotizada en Perú (mini demo)" y reproduce la BOM
  del mini-rover con Pi 5 en lugar de la Pi 4 del inventario. Sumarla duplicaría
  cantidades. Detalle en `bom-consolidado.md` §7.1.
- **Lo que la revisión del 2026-11-23 dio de baja**: HAT+ M.2, fuente de 27 W,
  SSD SATA y NVMe, caja USB, batería LiFePO4, cargador de red, perfil V-Slot y
  UBEC importado. Se explican en `bom-consolidado.md` §5.
- **Inventario y trabajo local**: Raspberry Pi 4 8 GB, Argon ONE V2, perfil
  V-Slot, impresión 3D (ruedas, placas, soportes) y los 4 paneles solares de 6 V.
- **Alternativas** de cámara, ToF, LiDAR y almacenamiento (§7.3 y §7.4 del
  consolidado).
- **Add-ons** del mini-rover (ESP32 de tiempo real, pack 3S3P, soldador de punto)
  y el **estudio 6×6**, pendiente de `OQ-09`.

## Decisiones abiertas antes de enviar

| Tema | Estado | Dónde |
|---|---|---|
| ¿El mini-rover necesita su propio LiDAR? | Abierto: ahora el único LiDAR va al rover principal. Si sí, +S/ 600 | §6.3 |
| Cargador del pack: ¿TP5100 o CN3722? | Resuelto: el TP5100 solo carga 1S/2S; para 3S va el CN3722 | §6.1 |
| ¿Pack 3S2P (78 Wh) o 3S3P (117 Wh)? | Abierto: +~S/ 88 por el 3S3P | §6.5 |
| Regulador del dron: ¿XL4005 local o Matek importado? | Propuesto XL4005 (S/ 6,59); el Matek sigue como alternativa | §6.4 |
| ¿Quién suelda el pack por punto? | Abierto: soldador Bracsan S/ 390, o pedirles que lo suelden | §6.2 |

## Estado de los precios

- Productos: **catálogo web del 2026-11-21**; hoy son referencia, no oferta.
- Averiguaciones técnicas: **2026-11-23** (TP5100, CN3722, reguladores locales,
  soldadura por punto) y están marcadas como tales.
- **No** se contactó a ningún proveedor, no se reservó y no se pagó nada.
- Las líneas con `~` son **estimaciones de planificación**.
- Sin envío, sin IGV no declarado y sin aduanas.

## Cómo mantenerlo

1. Si cambia una cantidad o un modelo, actualiza **primero** el BOM del
   subproyecto (`bom-peru.csv` o `bom-vision.csv`).
2. Luego refleja el cambio en `bom-consolidado.md`, `bom-consolidado.csv` y en las
   tablas de resumen (§2 y §2.1).
3. Cuando llegue una cotización, anótala en
   [`solicitud-plantilla.md`](solicitud-plantilla.md) §6. La evidencia formal se
   crea en la fase de compras, no ahora.
4. Los BOM de origen **todavía no tienen aplicados los cambios de la v0.2**: la
   lista de pendientes está en `bom-consolidado.md` §8.

## Fase

Estamos en **planificación e investigación**: este paquete se prepara, no se
ejecuta. Enviar las solicitudes es una acción de la fase de compras y requiere que
el usuario la abra explícitamente (ver `AGENTS.md` §0).
