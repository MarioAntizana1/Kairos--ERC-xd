# Rover Principal — Percepción y Visión (ERC 2027)

> Estado: Investigación · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: equipo de Visión
>
> Esta sección continúa el mini demo de navegación (`../rover`) y se ocupa de la **visión del rover grande**. No es todavía el rover completo: es el espacio de investigación, requisitos y pruebas del subsistema de percepción visual.

---

## Qué se está investigando

El rover grande ya tiene el **LiDAR** en su lista de sensores. Esta sección responde las preguntas que faltan:

1. ¿Qué **cámaras** conviene montar y dónde comprarlas en Perú?
2. ¿Qué **sensor ToF** complementa al LiDAR para obstáculos bajos, negativos y superficies sin textura?
3. ¿Cómo se combinan LiDAR + cámaras + ToF en una arquitectura ROS 2 verificable?
4. ¿Qué se puede demostrar con presupuesto local y qué hay que importar?

La primera investigación de campo está en
[`docs/01-investigacion/sensores-peru-2026-11-21.md`](docs/01-investigacion/sensores-peru-2026-11-21.md):
precios, stock y fichas de las cámaras Elgato de Memory Kings y de los ToF de Electromanía.

---

## Alcance de esta sección

| Incluido | Excluido por ahora |
|---|---|
| Selección y compra de cámaras y ToF | Brazo, ciencia, perforación |
| Arquitectura de percepción (LiDAR + cámaras + ToF) | Movilidad y chasis del rover grande |
| Calibración, sincronía y pruebas de profundidad | Operación BVLOS y autonomía de largo alcance |
| Integración ROS 2 y evidencia reproducible | Diseño mecánico definitivo del mástil |
| Comparación de proveedores en Perú | Compra sin aprobación de presupuesto |

> **LiDAR:** ya está en la lista del rover grande. Esta sección no reabre su elección; solo define cómo se fusiona con cámaras y ToF.

---

## Documentos clave

| Documento | Para qué |
|---|---|
| [`docs/01-investigacion/sensores-peru-2026-11-21.md`](docs/01-investigacion/sensores-peru-2026-11-21.md) | Evidencia de campo: Elgato Facecam 4K, TFmini Plus/S, LIDAR-Lite, alternativas y precios |
| [`docs/01-investigacion/vision-rover-grande.md`](docs/01-investigacion/vision-rover-grande.md) | Problema, casos de uso, arquitecturas candidatas e hipótesis |
| [`docs/01-investigacion/percepcion-3d.md`](docs/01-investigacion/percepcion-3d.md) | Base heredada: estéreo, sincronía, calibración y límites de CPU |
| [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md) | Fases, puertas y reglas de trabajo |
| [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md) | Fuentes F-xx con fecha, URL y confianza |
| [`docs/02-requisitos/vision-alcance.md`](docs/02-requisitos/vision-alcance.md) | Alcance, stakeholders y criterios de éxito de la sección |
| [`docs/04-diseno/bom-vision.md`](docs/04-diseno/bom-vision.md) | BOM del prototipo (2 × Elgato + TFmini Plus), alternativas y costes |

---

## Estado actual (2026-11-21)

- [x] Base documental y metodológica copiada del mini demo.
- [x] Investigación de campo en Memory Kings y Electromanía.
- [x] Fichas y precios de Elgato Facecam 4K, TFmini Plus, TFmini-S, LIDAR-Lite v3HP y alternativas.
- [x] Identificación de la brecha: no hay ToF multizona (VL53L8CX) en las tiendas peruanas consultadas.
- [ ] Decidir plataforma de cómputo del rover grande (Jetson, x86 o Raspberry Pi 5).
- [ ] Aprobar presupuesto de cámaras + ToF.
- [ ] Comprar y probar el par estéreo.
- [ ] Ejecutar el experimento de profundidad y sincronía.

> **No se ha comprado nada.** Los precios y el stock son una fotografía del 2026-11-21 y cambian sin aviso. Toda compra requiere confirmación del responsable del proyecto.

---

## Reglas rápidas

1. **Fuente primaria primero:** ficha del fabricante para especificaciones; tienda solo para precio/stock.
2. **Fecha y URL siempre:** cada precio lleva fecha de consulta. Sin fecha, no es evidencia.
3. **No inventar stock:** “disponible”, “últimas unidades” y “agotado” se copian textualmente y se fechan.
4. **Distingue precio de lista, precio internet y marketplace:** no son comparables sin decirlo.
5. **Los supuestos se escriben:** `> Supuesto: ...` y se abren como pregunta si bloquean una decisión.
6. **No comprar hardware** sin aprobación explícita de presupuesto.

La guía completa para agentes está en [`AGENTS.md`](AGENTS.md).
