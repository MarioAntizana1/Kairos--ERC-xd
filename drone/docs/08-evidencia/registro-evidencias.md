# Registro de evidencias

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

| ID | Fecha | Tipo | Requisitos | Casos | Resultado | Ruta | Hash | Estado |
|---|---|---|---|---|---|---|---|---|
| EV-2026-11-21-01 | 2026-11-21 | docs/tests | RNF-13 | TC-15 | Aprobada con limitación | `artefactos/2026-11-21T145841-validacion-documental/README.md` | `c77635822697ec7c3f470e20e4344e7edd90d686c76e44a1ac3446d12efaea08` | Aprobada |
| EV-2026-11-21-02 | 2026-11-21 | docs/tests | RNF-13 | TC-15 | Aprobada con limitación | `artefactos/2026-11-21T145939-validacion-final-g0/README.md` | `ca7131265b7d2b150cdb6e96bad720b2ca309e475daa94e91b98eb18267113d3` | Aprobada |
| EV-2026-11-21-03 | 2026-11-21 | docs/design | RNF-13 | TC-15 | Aprobada con limitación | `artefactos/2026-11-21T153938-revision-tof-piso/README.md` | `4025a8c3d7e55edbdbe13deb3d88d05eea5b64992adaa3175eaad09442099a1d` | Aprobada |
| EV-2026-11-21-04 | 2026-11-21 | docs/design | RNF-13 | TC-15 | Aprobada con limitación | `artefactos/2026-11-21T165912-revision-6m-jaula/README.md` | `0c46ec9d4e325c4644d50ab1b428e3042e9767456f73f21d2c97eac778c98e8c` | Aprobada |

## Cómo añadir una entrada

1. Ejecutar `make evidence SLUG="<slug>"`.
2. Copiar la ruta devuelta.
3. Ejecutar la prueba o el comando.
4. Guardar logs y media.
5. Ejecutar `make seal DIR="<ruta>"`.
6. Copiar el hash del `MANIFEST.sha256`.
7. Añadir la fila a esta tabla.
8. Enlazar desde la matriz de trazabilidad.

## Convención de ID

`EV-YYYY-MM-DD-NN`, donde `NN` es secuencial por día.

## Estados

| Estado | Significado |
|---|---|
| Pendiente | Carpeta creada, sin ejecutar |
| Ejecutada | Comando ejecutado, sin revisar |
| Aprobada | Revisada y aceptada |
| Fallida | El resultado no cumple el criterio |
| Obsoleta | Reemplazada por otra evidencia |

## Evidencias actuales

Las evidencias se listan en la tabla superior. No hay resultados de hardware.

> **Nota de conteo:** el número de Markdown que reporta `make check` incluye los
> README de las propias evidencias. Por eso el conteo puede variar en 1–2 entre
> una ejecución y la siguiente; no afecta la validación.
