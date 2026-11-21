---
name: documentacion-trazabilidad
description: Reglas para escribir y actualizar la documentación en español de rover-principal: citas F-xx, supuestos, ADR, OQ-V, matriz de trazabilidad, bitácora y evidencia. Úsala al crear o editar documentos en docs/.
---

# Documentación y trazabilidad

## Idioma y formato

- Documentación: **español**.
- Código, identificadores y logs: **inglés**.
- Fechas: ISO 8601 (`2026-11-21`).
- Unidades: SI (`m`, `cm`, `W`, `kg`, `°`).
- Archivos: `kebab-case.md`, sin tildes ni espacios.

## Convenciones de IDs

| Elemento | Formato | Dónde se registra |
|---|---|---|
| Fuente | `F-52`, `F-53`… | `docs/01-investigacion/fuentes.md` |
| Pregunta abierta | `OQ-V01`… | `docs/00-gobierno/registro-decisiones.md` |
| Decisión | `ADR-1001`… | `docs/00-gobierno/registro-decisiones.md` + ADR |
| Riesgo | `RSK-V01`… | `docs/00-gobierno/gestion-riesgos.md` |
| Hipótesis | `H-V1`… | `docs/01-investigacion/vision-rover-grande.md` |
| Experimento | `E-V1`… | `docs/01-investigacion/vision-rover-grande.md` |
| Caso de prueba | `TC-V01`… | `docs/06-pruebas/` |
| Evidencia | `EV-V01`… | `docs/08-evidencia/registro-evidencias.md` |

## Reglas de escritura

1. **Una afirmación, una fuente.** Si no hay `F-xx`, marca `> Supuesto:` o
   elimina la afirmación.
2. **Distingue dato de estimación.** Una tabla calculada se marca como
   estimación y se explica el modelo.
3. **Precio y stock con fecha.** Copia el texto de stock tal como aparece.
4. **Distingue precio de lista, internet y marketplace.** No los mezcles en una
   misma comparación sin decirlo.
5. **No prometas de más.** Nada de “tiempo real”, “precisión certificada” o
   “listo para competir” sin evidencia.
6. **Tablas antes que prosa** para comparar hardware, requisitos y pruebas.
7. **Supuestos explícitos.** Si falta un dato, escribe el supuesto y abre una
   pregunta; no rellenes con invenciones.

## Trazabilidad

Cada requisito debe recorrer:

```text
Requisito → fuente/dato → diseño → prueba → evidencia
```

- Si una feature no se traza a un requisito, no entra al alcance.
- Si un requisito no tiene evidencia, no está cumplido.
- Al cambiar un requisito, actualiza la matriz y el ADR.
- Al añadir una fuente, actualiza `fuentes.md`.

## Qué actualizar según el cambio

| Cambio | Documentos a tocar |
|---|---|
| Nueva fuente o precio | `01-investigacion/fuentes.md`, documento de investigación |
| Nueva decisión | `00-gobierno/registro-decisiones.md`, ADR, bitácora |
| Cambio de alcance | `02-requisitos/vision-alcance.md`, `registro-decisiones.md`, changelog |
| Nuevo riesgo | `00-gobierno/gestion-riesgos.md` |
| Nueva prueba | `06-pruebas/`, matriz de trazabilidad |
| Resultado de prueba | `08-evidencia/registro-evidencias.md`, bitácora |
| Cambio visible | `CHANGELOG.md`, `README.md` si aplica |

## Checklist antes de cerrar un cambio

- [ ] ¿Toda afirmación técnica tiene `F-xx` o `Supuesto`?
- [ ] ¿Las fechas son ISO 8601?
- [ ] ¿Los precios indican tienda, fecha y condición?
- [ ] ¿Se distinguió stock online de “consultar stock”?
- [ ] ¿Se actualizó `fuentes.md` si hubo fuente nueva?
- [ ] ¿Se actualizó `bitacora.md`?
- [ ] ¿Se actualizó `CHANGELOG.md` si es visible?
- [ ] ¿El documento enlaza a los documentos relacionados?
- [ ] ¿No hay secretos, tokens ni datos personales?
