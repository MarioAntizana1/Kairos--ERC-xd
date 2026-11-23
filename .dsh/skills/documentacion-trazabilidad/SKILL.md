---
name: documentacion-trazabilidad
description: Reglas para escribir y actualizar la documentación en español de este workspace ERC (mini-rover, drone y rover-principal). Cubre citas F-xx, supuestos, ADR, preguntas abiertas, matriz de trazabilidad, bitácora y evidencia. Úsala al crear o editar cualquier documento bajo docs/.
---

# Documentación y trazabilidad — workspace ERC

## Ámbito

Esta skill es del workspace madre y aplica a los tres subproyectos:

| Carpeta | Registro de fuentes | Registro de decisiones |
|---|---|---|
| `mini-rover/` | `mini-rover/docs/01-investigacion/fuentes.md` | `mini-rover/docs/00-gobierno/registro-decisiones.md` |
| `drone/` | `drone/docs/01-investigacion/fuentes.md` | `drone/docs/00-gobierno/registro-decisiones.md` |
| `rover-principal/` | `rover-principal/docs/01-investigacion/fuentes.md` | `rover-principal/docs/00-gobierno/registro-decisiones.md` |

La regla específica de cada subproyecto está en su `AGENTS.md`; si hay conflicto,
gana el `AGENTS.md` más cercano al archivo que estás editando.

## Idioma y formato

- Documentación: **español**. Código, identificadores, topics y logs: **inglés**.
- Fechas: ISO 8601 (`2026-11-23`). Fechas de carpeta de evidencia: UTC.
- Unidades: SI (`m`, `cm`, `W`, `kg`, `°`). Decimal con coma en prosa, punto en CSV.
- Archivos: `kebab-case.md`, sin tildes ni espacios.
- Un documento = una responsabilidad. No mezcles requisitos con diseño.

## Convenciones de IDs por subproyecto

| Elemento | `mini-rover/` | `drone/` | `rover-principal/` |
|---|---|---|---|
| Fuente | `F-xx` / `F-001` (revisa el encabezado de `fuentes.md`) | `F-xx` | `F-xx`, continúa desde `F-52` |
| Requisito | `RF-01`, `RNF-01` | `RF-01`, `RNF-01` | `RF-xx`, `RNF-xx` |
| Decisión | `ADR-0001`…`ADR-0012` | `ADR-0001`…`ADR-0005` | `ADR-1xxx` (evita colisión con `ADR-0001`–`0009`) |
| Pregunta abierta | `OQ-xx` | `OQ-xx` | `OQ-Vxx` |
| Riesgo | `RSK-01` | `RSK-01` | `RSK-Vxx` |
| Hipótesis / experimento | `H-xx` / `E-xx` | `H-xx` / `E-xx` | `H-Vx` / `E-Vx` |
| Caso de prueba | `TC-01` | `TC-01` | `TC-Vxx` |
| Evidencia | `EV-2026-11-21-01` | `EV-2026-11-21-01` | `EV-Vxx` |

Si un prefijo no aparece en el registro del subproyecto, no lo inventes: mira cómo
está numerado el último asiento y continúa esa serie.

## Reglas de escritura

1. **Una afirmación, una fuente.** Si no hay `F-xx`, marca `> Supuesto:` o elimina
   la afirmación.
2. **Distingue dato de estimación.** Toda tabla calculada se marca como estimación
   y explica el modelo usado.
3. **Precio y stock con fecha y URL.** Copia el texto de stock tal como aparece.
4. **Distingue precio de lista, internet y marketplace**, y stock online de
   “consultar stock”.
5. **No prometas de más.** Nada de “tiempo real”, “precisión certificada” o
   “listo para competir” sin evidencia registrada.
6. **Tablas antes que prosa** para comparar hardware, requisitos y pruebas.
7. **Supuestos explícitos.** Si falta un dato, escribe el supuesto y abre una
   pregunta; no rellenes con invenciones.
8. **No reabras una decisión cerrada** sin evidencia nueva y sin un ADR que la
   sustituya.

## Trazabilidad

Cada requisito recorre:

```text
Requisito → fuente/dato → diseño → prueba → evidencia
```

- Si una feature no se traza a un requisito, no entra al alcance.
- Si un requisito no tiene evidencia, no está cumplido.
- Al cambiar un requisito, actualiza la matriz de trazabilidad y el ADR.
- Al añadir una fuente, actualiza `fuentes.md`.

## Qué actualizar según el cambio

| Cambio | Documentos a tocar |
|---|---|
| Nueva fuente o precio | `01-investigacion/fuentes.md` + documento de investigación |
| Nueva decisión | `00-gobierno/registro-decisiones.md` + ADR + bitácora |
| Cambio de alcance | `02-requisitos/vision-alcance.md` + `registro-decisiones.md` + changelog |
| Nuevo riesgo | `00-gobierno/gestion-riesgos.md` |
| Nueva prueba | `06-pruebas/` + matriz de trazabilidad |
| Resultado de prueba | `08-evidencia/registro-evidencias.md` + bitácora |
| Cambio visible | `CHANGELOG.md`, `README.md` si aplica |

Las rutas de esta tabla son relativas al `docs/` del subproyecto afectado.

## Evidencia

> **Fase de planificación (vigente):** no se crean carpetas de evidencia ni se
> ejecutan validadores. Se escribe el protocolo, el caso de prueba y el plan de
> verificación, y todo queda en estado `Pendiente`. La evidencia se genera cuando
> el usuario abra la fase de ejecución.

Formato de carpeta:

```text
docs/08-evidencia/artefactos/YYYY-MM-DDTHHMMSS-<slug>/
├── README.md          # qué se hizo, resultado, conclusión
├── metadata.json      # fecha, host, commit, versiones
├── MANIFEST.sha256    # hashes
├── logs/ media/ bags/
```

Una evidencia solo es válida si es **trazable**, **reproducible**, **íntegra**
(hash SHA-256) y **verificable** por otra persona. Estados permitidos:
`Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`.

- No edites un artefacto ya sellado. Si hay que corregir, crea una ejecución
  nueva y marca la anterior como `Obsoleta`.
- Los artefactos existentes en `docs/08-evidencia/artefactos/` están sellados:
  son historia, no borradores.

## Checklist antes de cerrar un cambio

- [ ] ¿Toda afirmación técnica tiene `F-xx` o `Supuesto`?
- [ ] ¿Las fechas son ISO 8601?
- [ ] ¿Los precios indican tienda, fecha y condición?
- [ ] ¿Se distinguió stock online de “consultar stock”?
- [ ] ¿Se actualizó `fuentes.md` si hubo fuente nueva?
- [ ] ¿Se actualizó `bitacora.md` del subproyecto?
- [ ] ¿Se actualizó `CHANGELOG.md` si es visible?
- [ ] ¿El documento enlaza a los documentos relacionados?
- [ ] ¿No hay secretos, tokens ni datos personales?
- [ ] ¿No se ejecutó nada (validadores, pruebas, scripts) para llegar a este estado?
