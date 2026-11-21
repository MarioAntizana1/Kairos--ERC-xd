# Documentación del proyecto

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Documentación

Índice maestro. Cada carpeta corresponde a una fase o artefacto del SDLC. El
estado global y las reglas de trabajo están en [`../AGENTS.md`](../AGENTS.md).

## Cómo leer este repositorio

1. [`../README.md`](../README.md) — qué es y cuánto cuesta.
2. [`01-investigacion/contexto-drone.md`](01-investigacion/contexto-drone.md) — por qué existe.
3. [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) — qué se va a construir.
4. [`03-arquitectura/arquitectura-vision.md`](03-arquitectura/arquitectura-vision.md) — cómo encaja.
5. [`04-diseno/diseno-vision.md`](04-diseno/diseno-vision.md) — geometría y pipeline.
6. [`04-diseno/bom-peru.md`](04-diseno/bom-peru.md) — cotización.
7. [`06-pruebas/plan-pruebas.md`](06-pruebas/plan-pruebas.md) — cómo se verifica.

## Índice por fase

### 00 — Gobierno

| Documento | Contenido | Estado |
|---|---|---|
| [`00-gobierno/metodologia.md`](00-gobierno/metodologia.md) | SDLC, DSR, puertas, cadencia | Borrador |
| [`00-gobierno/plan-proyecto.md`](00-gobierno/plan-proyecto.md) | Fases, WBS, hitos, presupuesto | Borrador |
| [`00-gobierno/roles-y-raci.md`](00-gobierno/roles-y-raci.md) | Roles y RACI | Borrador |
| [`00-gobierno/gestion-riesgos.md`](00-gobierno/gestion-riesgos.md) | Riesgos y FMEA inicial | Vivo |
| [`00-gobierno/registro-decisiones.md`](00-gobierno/registro-decisiones.md) | ADRs y preguntas abiertas | Vivo |
| [`00-gobierno/plantillas/`](00-gobierno/plantillas/) | Plantillas de ADR, requisito, prueba y evidencia | Vivo |

### 01 — Investigación

| Documento | Contenido | Estado |
|---|---|---|
| [`01-investigacion/contexto-drone.md`](01-investigacion/contexto-drone.md) | Problema, alcance, stakeholders | Borrador |
| [`01-investigacion/estado-del-arte.md`](01-investigacion/estado-del-arte.md) | Estéreo, ToF de piso, cámaras, cómputo | Borrador |
| [`01-investigacion/hipotesis-y-experimentos.md`](01-investigacion/hipotesis-y-experimentos.md) | Hipótesis y métricas | Borrador |
| [`01-investigacion/normativa-y-seguridad.md`](01-investigacion/normativa-y-seguridad.md) | Operación, privacidad, seguridad | Borrador |
| [`01-investigacion/fuentes.md`](01-investigacion/fuentes.md) | Fuentes, fecha y confianza | Vivo |

### 02 — Requisitos

| Documento | Contenido | Estado |
|---|---|---|
| [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) | Problema, alcance, criterios | Borrador |
| [`02-requisitos/requisitos-funcionales.md`](02-requisitos/requisitos-funcionales.md) | RF-01 a RF-12 | Borrador |
| [`02-requisitos/requisitos-no-funcionales.md`](02-requisitos/requisitos-no-funcionales.md) | RNF-01 a RNF-14 | Borrador |
| [`02-requisitos/historias-usuario.md`](02-requisitos/historias-usuario.md) | Historias y Given/When/Then | Borrador |
| [`02-requisitos/trazabilidad.md`](02-requisitos/trazabilidad.md) | Requisito → diseño → prueba | Vivo |

### 03 — Arquitectura

| Documento | Contenido | Estado |
|---|---|---|
| [`03-arquitectura/arquitectura-vision.md`](03-arquitectura/arquitectura-vision.md) | Componentes, nodos, modos, fallos | Borrador |
| [`03-arquitectura/interfaces.md`](03-arquitectura/interfaces.md) | Topics, MAVLink, YAML, red | Borrador |
| [`03-arquitectura/seguridad.md`](03-arquitectura/seguridad.md) | FMEA, watchdog, energía, EMI | Borrador |
| [`03-arquitectura/adr/`](03-arquitectura/adr/) | ADR-0001 a ADR-0005 | Aceptadas/propuesta |

### 04 — Diseño

| Documento | Contenido | Estado |
|---|---|---|
| [`04-diseno/diseno-vision.md`](04-diseno/diseno-vision.md) | Geometría, calibración, pipeline, ToF | Borrador |
| [`04-diseno/bom.md`](04-diseno/bom.md) | Referencia USD | Estimado |
| [`04-diseno/bom-peru.md`](04-diseno/bom-peru.md) | Cotización Perú, stock y alternativas | Estudio |
| [`04-diseno/bom-peru.csv`](04-diseno/bom-peru.csv) | Datos crudos de la cotización | Vivo |

### 05 — Implementación

| Documento | Contenido | Estado |
|---|---|---|
| [`05-implementacion/entorno-desarrollo.md`](05-implementacion/entorno-desarrollo.md) | Host, target, versiones | Borrador |
| [`05-implementacion/guia-instalacion.md`](05-implementacion/guia-instalacion.md) | Instalación y puesta en marcha | Borrador |
| [`05-implementacion/bitacora.md`](05-implementacion/bitacora.md) | Registro cronológico | Vivo |

### 06 — Pruebas

| Documento | Contenido | Estado |
|---|---|---|
| [`06-pruebas/plan-pruebas.md`](06-pruebas/plan-pruebas.md) | Estrategia, niveles, criterios | Borrador |
| [`06-pruebas/casos-prueba.md`](06-pruebas/casos-prueba.md) | TC-01 a TC-15 | Borrador |
| [`06-pruebas/protocolo-experimentos.md`](06-pruebas/protocolo-experimentos.md) | 10 repeticiones y métricas | Borrador |
| [`06-pruebas/matriz-trazabilidad-pruebas.md`](06-pruebas/matriz-trazabilidad-pruebas.md) | Caso → requisito → estado | Vivo |
| [`06-pruebas/resultados/`](06-pruebas/resultados/) | Resultados por campaña | Pendiente |

### 07 — Operación

| Documento | Contenido | Estado |
|---|---|---|
| [`07-operacion/runbook-vuelo.md`](07-operacion/runbook-vuelo.md) | Preflight, vuelo, contingencias | Borrador |
| [`07-operacion/mantenimiento.md`](07-operacion/mantenimiento.md) | Inspección y calibración | Borrador |

### 08 — Evidencia

| Documento | Contenido | Estado |
|---|---|---|
| [`08-evidencia/README.md`](08-evidencia/README.md) | Política y formato | Vivo |
| [`08-evidencia/registro-evidencias.md`](08-evidencia/registro-evidencias.md) | Índice de ejecuciones | Vivo |
| [`08-evidencia/artefactos/`](08-evidencia/artefactos/) | Carpetas por ejecución | Vivo |

### 09 — Presentación

| Documento | Contenido | Estado |
|---|---|---|
| [`09-presentacion/guion-demo.md`](09-presentacion/guion-demo.md) | Guion y FAQ | Borrador |

## Documentos transversales

- [`glosario.md`](glosario.md) — términos y siglas.
- [`../CHANGELOG.md`](../CHANGELOG.md) — cambios.
- [`../AGENTS.md`](../AGENTS.md) — reglas para agentes y colaboradores.

## Convenciones de estado

| Estado | Significado |
|---|---|
| Borrador | En elaboración; puede cambiar |
| En revisión | Listo para revisión |
| Aprobado | Revisado y aceptado |
| Vivo | Se actualiza continuamente |
| Obsoleto | Reemplazado; se conserva |
