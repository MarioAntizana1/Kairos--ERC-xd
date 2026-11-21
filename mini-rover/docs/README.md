# Documentación del proyecto

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Documentación

Índice maestro. Cada carpeta corresponde a una fase o artefacto del SDLC. El estado global y las reglas de trabajo están en [`../AGENTS.md`](../AGENTS.md).

## Cómo leer este repositorio

Si vienes nuevo, lee en este orden:

1. [`../README.md`](../README.md) — qué es y cómo se ejecuta.
2. [`01-investigacion/contexto-erc.md`](01-investigacion/contexto-erc.md) — por qué existe el proyecto.
3. [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) — qué se va a construir y qué no.
4. [`03-arquitectura/arquitectura-sistema.md`](03-arquitectura/arquitectura-sistema.md) — cómo encaja todo.
5. [`06-pruebas/plan-pruebas.md`](06-pruebas/plan-pruebas.md) — cómo se demuestra que funciona.
6. [`08-evidencia/README.md`](08-evidencia/README.md) — cómo se registra la evidencia.

## Índice por fase

### 00 — Gobierno

| Documento | Contenido | Estado |
|---|---|---|
| [`00-gobierno/metodologia.md`](00-gobierno/metodologia.md) | SDLC, DSR, puertas, cadencia y control de cambios | Borrador |
| [`00-gobierno/plan-proyecto.md`](00-gobierno/plan-proyecto.md) | Fases, WBS, hitos, esfuerzo y camino crítico | Borrador |
| [`00-gobierno/roles-y-raci.md`](00-gobierno/roles-y-raci.md) | Roles, responsabilidades y matriz RACI | Borrador |
| [`00-gobierno/gestion-riesgos.md`](00-gobierno/gestion-riesgos.md) | Registro de riesgos y matriz de exposición | Borrador |
| [`00-gobierno/registro-decisiones.md`](00-gobierno/registro-decisiones.md) | Índice de ADRs y decisiones abiertas | Vivo |
| [`00-gobierno/plantillas/`](00-gobierno/plantillas/) | Plantillas de ADR, requisito, prueba, evidencia, acta y revisión | Vivo |

### 01 — Investigación

| Documento | Contenido | Estado |
|---|---|---|
| [`01-investigacion/contexto-erc.md`](01-investigacion/contexto-erc.md) | Qué es el ERC, pruebas, navegación y autonomía | Verificado con fuentes |
| [`01-investigacion/marco-metodologico.md`](01-investigacion/marco-metodologico.md) | DSR, preguntas de investigación, experimentos y validez | Borrador |
| [`01-investigacion/estado-del-arte.md`](01-investigacion/estado-del-arte.md) | ROS 2, Nav2, SLAM, localización y alternativas | Borrador |
| [`01-investigacion/benchmarking-plataformas.md`](01-investigacion/benchmarking-plataformas.md) | Raspberry Pi vs Jetson vs x86 | Borrador |
| [`01-investigacion/hipotesis-y-experimentos.md`](01-investigacion/hipotesis-y-experimentos.md) | Hipótesis, variables, métricas y análisis | Borrador |
| [`01-investigacion/normativa-y-seguridad.md`](01-investigacion/normativa-y-seguridad.md) | Buenas prácticas, baterías, e-stop, RF | Borrador |
| [`01-investigacion/fuentes.md`](01-investigacion/fuentes.md) | Fuentes consultadas, fecha de acceso y confianza | Vivo |

### 02 — Requisitos

| Documento | Contenido | Estado |
|---|---|---|
| [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) | Problema, objetivos, alcance, stakeholders | Borrador |
| [`02-requisitos/requisitos-funcionales.md`](02-requisitos/requisitos-funcionales.md) | RF-01 a RF-12 con prioridad MoSCoW | Borrador |
| [`02-requisitos/requisitos-no-funcionales.md`](02-requisitos/requisitos-no-funcionales.md) | RNF-01 a RNF-14 medibles | Borrador |
| [`02-requisitos/historias-usuario.md`](02-requisitos/historias-usuario.md) | Historias y criterios Given/When/Then | Borrador |
| [`02-requisitos/trazabilidad.md`](02-requisitos/trazabilidad.md) | Requisito → diseño → prueba → evidencia | Vivo |

### 03 — Arquitectura

| Documento | Contenido | Estado |
|---|---|---|
| [`03-arquitectura/arquitectura-sistema.md`](03-arquitectura/arquitectura-sistema.md) | Contexto, componentes, despliegue y modos | Borrador |
| [`03-arquitectura/interfaces.md`](03-arquitectura/interfaces.md) | Topics, acciones, TF, YAML, telemetría | Borrador |
| [`03-arquitectura/seguridad.md`](03-arquitectura/seguridad.md) | Cadena de parada, watchdog, FMEA | Borrador |
| [`03-arquitectura/adr/`](03-arquitectura/adr/) | Decisiones arquitectónicas (0001–0012) | Aceptadas, propuestas y obsoletas |

### 04 — Diseño

| Documento | Contenido | Estado |
|---|---|---|
| [`04-diseno/diseno-software.md`](04-diseno/diseno-software.md) | Paquetes, máquina de estados, secuencias, errores | Borrador |
| [`04-diseno/diseno-mecanico.md`](04-diseno/diseno-mecanico.md) | Chasis, tracción, dimensiones, masas | Conceptual |
| [`04-diseno/diseno-electrico.md`](04-diseno/diseno-electrico.md) | Bloques, potencia, protecciones, cableado | Conceptual |
| [`04-diseno/bom.md`](04-diseno/bom.md) | Lista de materiales y presupuesto estimado | Estimado |
| [`04-diseno/bom-peru.md`](04-diseno/bom-peru.md) | BOM base cotizada en Perú, proveedores, add-ons ESP32/Li-ion y alternativas | Estudio |
| [`04-diseno/inventario-facultad.md`](04-diseno/inventario-facultad.md) | Material disponible en facultad, reutilización y brechas frente a la BOM | Borrador |
| [`04-diseno/energia/calculo-energetico.md`](04-diseno/energia/calculo-energetico.md) | Estudio 6×6: energía, batería, servos y solar (variante) | Borrador |
| [`04-diseno/energia/diseno-electrico-6x6.md`](04-diseno/energia/diseno-electrico-6x6.md) | Estudio 6×6: arquitectura eléctrica y protecciones | Estudio |
| [`04-diseno/energia/bom-6x6.md`](04-diseno/energia/bom-6x6.md) | Estudio 6×6: lista de materiales y coste estimado | Estudio |

### 05 — Implementación

| Documento | Contenido | Estado |
|---|---|---|
| [`05-implementacion/entorno-desarrollo.md`](05-implementacion/entorno-desarrollo.md) | Host Fedora, VM/contenedor, Pi, versiones | Borrador |
| [`05-implementacion/guia-instalacion.md`](05-implementacion/guia-instalacion.md) | Instalación paso a paso y verificación | Borrador |
| [`05-implementacion/convenciones-codigo.md`](05-implementacion/convenciones-codigo.md) | Python, ROS 2, YAML, Git, commits | Borrador |
| [`05-implementacion/bitacora.md`](05-implementacion/bitacora.md) | Registro cronológico de trabajo | Vivo |

### 06 — Pruebas

| Documento | Contenido | Estado |
|---|---|---|
| [`06-pruebas/plan-pruebas.md`](06-pruebas/plan-pruebas.md) | Estrategia, niveles, criterios de entrada/salida | Borrador |
| [`06-pruebas/casos-prueba.md`](06-pruebas/casos-prueba.md) | TC-01 a TC-18 con procedimiento | Borrador |
| [`06-pruebas/protocolo-experimentos.md`](06-pruebas/protocolo-experimentos.md) | 10 repeticiones, métricas y análisis | Borrador |
| [`06-pruebas/matriz-trazabilidad-pruebas.md`](06-pruebas/matriz-trazabilidad-pruebas.md) | Requisito → caso → resultado | Vivo |
| [`06-pruebas/resultados/`](06-pruebas/resultados/) | Resultados por campaña | Pendiente |

### 07 — Operación

| Documento | Contenido | Estado |
|---|---|---|
| [`07-operacion/manual-operacion.md`](07-operacion/manual-operacion.md) | Arranque, misión, abortado, apagado | Borrador |
| [`07-operacion/runbook-demo.md`](07-operacion/runbook-demo.md) | Guion, checklists y contingencias | Borrador |
| [`07-operacion/mantenimiento.md`](07-operacion/mantenimiento.md) | Inspección, calibración, vida útil | Borrador |

### 08 — Evidencia

| Documento | Contenido | Estado |
|---|---|---|
| [`08-evidencia/README.md`](08-evidencia/README.md) | Política, formato, integridad y retención | Vivo |
| [`08-evidencia/registro-evidencias.md`](08-evidencia/registro-evidencias.md) | Índice de ejecuciones y artefactos | Vivo |
| [`08-evidencia/artefactos/`](08-evidencia/artefactos/) | Carpetas de evidencia por ejecución | Vivo |

### 09 — Presentación

| Documento | Contenido | Estado |
|---|---|---|
| [`09-presentacion/guion-demo.md`](09-presentacion/guion-demo.md) | Guion de 5 y 10 minutos | Borrador |
| [`09-presentacion/faq-jurado.md`](09-presentacion/faq-jurado.md) | Preguntas probables y respuestas | Borrador |

## Documentos transversales

- [`glosario.md`](glosario.md) — términos y siglas.
- [`../CHANGELOG.md`](../CHANGELOG.md) — cambios del proyecto.
- [`../AGENTS.md`](../AGENTS.md) — reglas para agentes y colaboradores.

## Convenciones de estado

| Estado | Significado |
|---|---|
| Borrador | En elaboración; puede cambiar sin aviso |
| En revisión | Listo para revisión por pares |
| Aprobado | Revisado y aceptado; cambios requieren control |
| Vivo | Se actualiza continuamente (bitácora, registro, trazabilidad) |
| Obsoleto | Reemplazado; se conserva por trazabilidad |
