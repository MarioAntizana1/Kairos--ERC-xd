# Cotizaciones — consolidado transversal de los tres subproyectos

Esta carpeta reúne el **BOM de los tres subproyectos agrupado por proveedor**, con
cantidades totales, precios, enlaces y stock, para enviar una sola solicitud de
cotización a cada empresa.

No es un BOM nuevo ni reemplaza a los de cada subproyecto: es una **vista
consolidada** de compra. La fuente de verdad sigue siendo el BOM de cada uno.

## Archivos

| Archivo | Qué contiene |
|---|---|
| [`bom-consolidado.md`](bom-consolidado.md) | Documento principal: resumen por proveedor, totales por proyecto, detalle por proveedor con enlaces, exclusiones y supuestos |
| [`bom-consolidado.csv`](bom-consolidado.csv) | Las mismas 43 líneas en formato tabular (una fila por ítem y proveedor) para filtrar o adjuntar |
| [`solicitud-plantilla.md`](solicitud-plantilla.md) | Asunto, correo, versión de WhatsApp, tabla de líneas para pegar y seguimiento de respuestas |

## Qué se cotiza

| Bloque | Subproyecto | Origen | Líneas propias |
|---|---|---|---:|
| MR | Mini-rover | `mini-rover/docs/04-diseno/bom-peru.csv` (BOM base, sin add-ons ni 6×6) | 21 |
| DR | Drone | `drone/docs/04-diseno/bom-peru.csv` (solo filas `incluir = si`) | 16 |
| RP | Rover-principal | `rover-principal/docs/04-diseno/bom-vision.csv` (escenario V-A) | 3 |
| Compartidas | — | XT60 del MR, cableado del DR y el TFmini Plus que usan DR y RP | 3 |
| | | **Total** | **43 líneas · 55 unidades** |

**Total consolidado: ~S/ 7.135,68** (S/ 5.690,68 verificados + ~S/ 1.445 estimados),
sin envío y sin aduanas.

## Qué **no** se cotiza aquí

- **La copia de la BOM del mini demo en `rover-principal/`**: su propio documento
  se titula "BOM de electrónica cotizada en Perú (mini demo)" y reproduce la BOM
  del mini-rover con Pi 5 en lugar de la Pi 4 del inventario. Sumarla duplicaría
  cantidades. Detalle en `bom-consolidado.md` §5.1.
- **Inventario existente**: Raspberry Pi 4 8 GB y Argon ONE V2 (facultad).
- **Alternativas** de cámara, ToF y almacenamiento: se listan como opciones, no se
  suman.
- **Add-ons** del mini-rover (ESP32 de tiempo real, packs Li-ion) y el **estudio
  6×6** (`energia/bom-6x6.md`, pendiente de `OQ-09`).
- **Herramientas** (multímetro, soldador, etc.): ver `drone/docs/04-diseno/bom.md` §4.

## Estado de los precios

- Consultados en el **catálogo web el 2026-11-21**; hoy son referencia, no oferta.
- **No** se contactó a ningún proveedor, no se reservó y no se pagó nada.
- Las líneas con `~` son **estimaciones de planificación**: hay que reemplazarlas
  por la cotización real.
- Sin envío, sin IGV no declarado y sin aduanas.

## Cómo mantenerlo

1. Si cambia una cantidad o un modelo, actualiza **primero** el BOM del
   subproyecto (`bom-peru.csv` o `bom-vision.csv`).
2. Luego refleja el cambio en `bom-consolidado.md`, `bom-consolidado.csv` y, si
   afecta al paquete, en `bom-consolidado.md` §2 y §2.1.
3. Cuando llegue una cotización, anótala en
   [`solicitud-plantilla.md`](solicitud-plantilla.md) §6. La evidencia formal se
   crea en la fase de compras, no ahora.

## Fase

Estamos en **planificación e investigación**: este paquete se prepara, no se
ejecuta. Enviar las solicitudes es una acción de la fase de compras y requiere que
el usuario la abra explícitamente (ver `AGENTS.md` §0).
