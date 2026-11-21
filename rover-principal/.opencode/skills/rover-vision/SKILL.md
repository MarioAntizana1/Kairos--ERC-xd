---
name: rover-vision
description: Contexto, alcance y reglas de la sección de visión del rover grande (ERC 2027): cámaras, ToF, LiDAR, calibración y compras en Perú. Úsala al investigar, escribir o decidir sobre percepción visual en rover-principal.
---

# Rover Vision — contexto de la sección

## Qué es esta sección

`rover-principal` es la continuación del mini demo de navegación (`../rover`).
Aquí se diseña la **visión del rover grande**: cámaras, ToF, fusión con LiDAR,
calibración, pruebas y compras en Perú. No es el rover completo: chasis, brazo,
ciencia y perforación quedan fuera.

## Decisiones que no se reabren

| Decisión | Valor |
|---|---|
| Middleware | ROS 2 Jazzy (heredado) |
| LiDAR | Ya está en la lista del rover grande; es el sensor primario |
| Metodología | SDLC iterativo + Design Research |
| Evidencia | Artefactos con fecha, metadatos y hash |

## Lo que está abierto

- Plataforma de cómputo del rover grande (Jetson, x86, Pi 5).
- Cámaras definitivas (Elgato Facecam 4K local vs. estéreo global shutter/OAK-D).
- ToF definitivo (TFmini Plus/S, LIDAR-Lite v3HP, VL53L8CX importado).
- Si el 3D denso es requisito.
- Presupuesto.

## Documentos que debes leer

1. `docs/01-investigacion/sensores-peru-2026-11-21.md` — evidencia de campo.
2. `docs/01-investigacion/vision-rover-grande.md` — problema y arquitecturas.
3. `docs/01-investigacion/percepcion-3d.md` — base técnica heredada.
4. `docs/00-gobierno/registro-decisiones.md` — OQ-Vxx.
5. `docs/01-investigacion/fuentes.md` — fuentes F-xx.

## Reglas de trabajo

1. **Fuente primaria para especificaciones; tienda solo para precio/stock.**
2. **Fecha y URL siempre.** Sin fecha, no es evidencia.
3. **Distingue precio de lista, internet y marketplace**, y stock online vs.
   “consultar stock”.
4. **No inventes disponibilidad.** Escribe `No verificado` y la razón.
5. **Marca los supuestos** con `> Supuesto:` y abre una `OQ-Vxx` si bloquean.
6. **No compres hardware** sin aprobación de presupuesto.
7. **No asumas Raspberry Pi 5** para el rover grande.
8. **El LiDAR no se re-evalúa aquí.** Solo se define la fusión.

## Entregables esperados

- Investigación de sensores con precios, stock y fuentes.
- Arquitectura de percepción y ADR de selección (`ADR-1xxx`).
- BOM de visión con cotización local e importación.
- Protocolo de calibración y pruebas (E-V1…E-V5).
- Evidencia `EV-Vxx` con bags, CSV, logs y fotos.
- Informe de resultados y recomendación.

## Convenciones de IDs

`F-xx` fuente · `OQ-Vxx` pregunta · `ADR-1xxx` decisión · `RSK-Vxx` riesgo ·
`H-Vx` hipótesis · `E-Vx` experimento · `TC-Vxx` caso de prueba · `EV-Vxx`
evidencia.

## Cómo responder

- Si te piden una compra, primero verifica stock, precio, fecha y alternativa.
- Si te piden una especificación, cita fabricante y modelo exacto.
- Si no hay dato, dilo. No rellenes con blogs o suposiciones sin marcarlas.
- Si el cambio afecta alcance o presupuesto, actualiza `registro-decisiones.md`
  y `bitacora.md`.
