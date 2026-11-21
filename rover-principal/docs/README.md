# Documentación del proyecto — Visión del rover grande

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Documentación

Índice maestro de esta sección. Cada carpeta corresponde a una fase o artefacto del SDLC. El estado global y las reglas de trabajo están en [`../AGENTS.md`](../AGENTS.md).

## Cómo leer este repositorio

Si vienes nuevo, lee en este orden:

1. [`../README.md`](../README.md) — qué es esta sección y qué no es.
2. [`01-investigacion/vision-rover-grande.md`](01-investigacion/vision-rover-grande.md) — el problema de visión y las arquitecturas candidatas.
3. [`01-investigacion/sensores-peru-2026-11-21.md`](01-investigacion/sensores-peru-2026-11-21.md) — qué se vende en Perú, a qué precio y con qué límites.
4. [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) — alcance y criterios de éxito.
5. [`01-investigacion/percepcion-3d.md`](01-investigacion/percepcion-3d.md) — base técnica heredada del mini demo.
6. [`06-pruebas/protocolo-experimentos.md`](06-pruebas/protocolo-experimentos.md) — cómo se mide y se demuestra.

## Índice por fase

### 00 — Gobierno

| Documento | Contenido | Estado |
|---|---|---|
| [`00-gobierno/metodologia.md`](00-gobierno/metodologia.md) | SDLC, DSR, puertas, cadencia y control de cambios (heredado) | Borrador |
| [`00-gobierno/registro-decisiones.md`](00-gobierno/registro-decisiones.md) | ADRs, preguntas abiertas `OQ-Vxx` y convención de numeración | Vivo |
| [`00-gobierno/gestion-riesgos.md`](00-gobierno/gestion-riesgos.md) | Riesgos `RSK-Vxx` de la visión | Vivo |
| [`00-gobierno/plan-proyecto.md`](00-gobierno/plan-proyecto.md) | Fases, WBS, hitos y esfuerzo del mini demo (heredado) | Borrador |
| [`00-gobierno/roles-y-raci.md`](00-gobierno/roles-y-raci.md) | Roles y matriz RACI del mini demo (heredado) | Borrador |
| [`00-gobierno/plantillas/`](00-gobierno/plantillas/) | Plantillas de ADR, requisito, prueba, evidencia, acta y revisión | Vivo |

### 01 — Investigación

| Documento | Contenido | Estado |
|---|---|---|
| [`01-investigacion/vision-rover-grande.md`](01-investigacion/vision-rover-grande.md) | Problema, casos de uso, arquitecturas, hipótesis y criterios | Borrador |
| [`01-investigacion/sensores-peru-2026-11-21.md`](01-investigacion/sensores-peru-2026-11-21.md) | Elgato Facecam 4K, TFmini Plus/S, LIDAR-Lite, precios y stock en Perú | Verificado con fuentes |
| [`01-investigacion/percepcion-3d.md`](01-investigacion/percepcion-3d.md) | Estéreo, sincronía, calibración, CPU y alternativas (heredado) | Investigación |
| [`01-investigacion/contexto-erc.md`](01-investigacion/contexto-erc.md) | Qué es el ERC y qué exige (heredado) | Verificado con fuentes |
| [`01-investigacion/marco-metodologico.md`](01-investigacion/marco-metodologico.md) | DSR, preguntas de investigación y validez (heredado) | Borrador |
| [`01-investigacion/estado-del-arte.md`](01-investigacion/estado-del-arte.md) | ROS 2, Nav2, SLAM y alternativas (heredado) | Borrador |
| [`01-investigacion/benchmarking-plataformas.md`](01-investigacion/benchmarking-plataformas.md) | Raspberry Pi vs Jetson vs x86 (heredado) | Borrador |
| [`01-investigacion/hipotesis-y-experimentos.md`](01-investigacion/hipotesis-y-experimentos.md) | Hipótesis, variables y métricas (heredado) | Borrador |
| [`01-investigacion/normativa-y-seguridad.md`](01-investigacion/normativa-y-seguridad.md) | Buenas prácticas, baterías, e-stop y RF (heredado) | Borrador |
| [`01-investigacion/fuentes.md`](01-investigacion/fuentes.md) | Fuentes `F-xx` con URL, fecha y confianza | Vivo |

### 02 — Requisitos

| Documento | Contenido | Estado |
|---|---|---|
| [`02-requisitos/vision-alcance.md`](02-requisitos/vision-alcance.md) | Problema, objetivos, alcance, stakeholders y criterios de éxito | Borrador |
| [`02-requisitos/requisitos-funcionales.md`](02-requisitos/requisitos-funcionales.md) | RF-01 a RF-12 del mini demo (heredado) | Borrador |
| [`02-requisitos/requisitos-no-funcionales.md`](02-requisitos/requisitos-no-funcionales.md) | RNF-01 a RNF-14 del mini demo (heredado) | Borrador |
| [`02-requisitos/historias-usuario.md`](02-requisitos/historias-usuario.md) | Historias y criterios del mini demo (heredado) | Borrador |
| [`02-requisitos/trazabilidad.md`](02-requisitos/trazabilidad.md) | Matriz de trazabilidad del mini demo (heredado) | Vivo |

> Los requisitos heredados son del **mini demo**. No son requisitos del rover grande; sirven como ejemplo de formato y como base de la futura matriz de visión.

### 03 — Arquitectura (referencia heredada)

| Documento | Contenido | Estado |
|---|---|---|
| [`03-arquitectura/arquitectura-sistema.md`](03-arquitectura/arquitectura-sistema.md) | Componentes, despliegue y modos del mini demo (heredado) | Borrador |
| [`03-arquitectura/interfaces.md`](03-arquitectura/interfaces.md) | Topics, acciones, TF y telemetría del mini demo (heredado) | Borrador |
| [`03-arquitectura/seguridad.md`](03-arquitectura/seguridad.md) | Cadena de parada, watchdog y FMEA del mini demo (heredado) | Borrador |
| [`03-arquitectura/adr/`](03-arquitectura/adr/) | ADR-0001 a ADR-0009 del mini demo; se conservan como referencia | Aceptadas + propuesta |

> Los ADR heredados explican decisiones del mini demo (ROS 2 Jazzy, Pi 5, Nav2, Gazebo, AMCL, misión Python, evidencia, ESP32 y spike 3D). No obligan al rover grande; sus lecciones se citan cuando aplican.

### 04 — Diseño (referencia heredada)

| Documento | Contenido | Estado |
|---|---|---|
| [`04-diseno/bom-vision.md`](04-diseno/bom-vision.md) | **BOM de visión del prototipo** (2 × Elgato + TFmini Plus) y alternativas | Estimado |
| [`04-diseno/bom-vision.csv`](04-diseno/bom-vision.csv) | BOM de visión en CSV | Estimado |
| [`04-diseno/bom.md`](04-diseno/bom.md) | BOM estimada del mini demo | Estimado |
| [`04-diseno/bom-peru.md`](04-diseno/bom-peru.md) | BOM base cotizada en Perú del mini demo, proveedores y alternativas | Estudio |
| [`04-diseno/bom-peru.csv`](04-diseno/bom-peru.csv) | BOM en CSV | Estudio |
| [`04-diseno/bom-peru-addons.csv`](04-diseno/bom-peru-addons.csv) | Add-ons ESP32/Li-ion | Estudio |
| [`04-diseno/diseno-mecanico.md`](04-diseno/diseno-mecanico.md) | Chasis, tracción y dimensiones del mini demo (heredado) | Conceptual |
| [`04-diseno/diseno-electrico.md`](04-diseno/diseno-electrico.md) | Bloques, potencia y protecciones del mini demo (heredado) | Conceptual |
| [`04-diseno/diseno-software.md`](04-diseno/diseno-software.md) | Paquetes, máquina de estados y errores del mini demo (heredado) | Borrador |

> La BOM y los diseños heredados son del mini demo. La BOM de visión del rover grande se construirá en esta sección y no se mezcla con la anterior.

### 05 — Implementación

| Documento | Contenido | Estado |
|---|---|---|
| [`05-implementacion/bitacora.md`](05-implementacion/bitacora.md) | Registro cronológico del trabajo de esta sección | Vivo |
| [`05-implementacion/entorno-desarrollo.md`](05-implementacion/entorno-desarrollo.md) | Host, VM/contenedor y versiones del mini demo (heredado) | Borrador |
| [`05-implementacion/guia-instalacion.md`](05-implementacion/guia-instalacion.md) | Instalación paso a paso del mini demo (heredado) | Borrador |
| [`05-implementacion/convenciones-codigo.md`](05-implementacion/convenciones-codigo.md) | Python, ROS 2, YAML y Git (heredado) | Borrador |

### 06 — Pruebas

| Documento | Contenido | Estado |
|---|---|---|
| [`06-pruebas/plan-pruebas.md`](06-pruebas/plan-pruebas.md) | Estrategia y criterios del mini demo (heredado) | Borrador |
| [`06-pruebas/casos-prueba.md`](06-pruebas/casos-prueba.md) | TC-01 a TC-18 del mini demo (heredado) | Borrador |
| [`06-pruebas/protocolo-experimentos.md`](06-pruebas/protocolo-experimentos.md) | Diseño de experimentos, métricas y análisis (heredado) | Borrador |
| [`06-pruebas/matriz-trazabilidad-pruebas.md`](06-pruebas/matriz-trazabilidad-pruebas.md) | Requisito → caso → resultado del mini demo (heredado) | Vivo |
| [`06-pruebas/resultados/`](06-pruebas/resultados/) | Plantilla de datos y resultados del mini demo (heredado) | Pendiente |

### 08 — Evidencia

| Documento | Contenido | Estado |
|---|---|---|
| [`08-evidencia/README.md`](08-evidencia/README.md) | Política, formato, integridad y retención (heredado) | Vivo |
| [`08-evidencia/registro-evidencias.md`](08-evidencia/registro-evidencias.md) | Índice de ejecuciones `EV-Vxx` | Vivo |

### 07 — Operación (referencia heredada)

| Documento | Contenido | Estado |
|---|---|---|
| [`07-operacion/manual-operacion.md`](07-operacion/manual-operacion.md) | Arranque, misión, abortado y apagado del mini demo (heredado) | Borrador |
| [`07-operacion/runbook-demo.md`](07-operacion/runbook-demo.md) | Guion, checklists y contingencias del mini demo (heredado) | Borrador |
| [`07-operacion/mantenimiento.md`](07-operacion/mantenimiento.md) | Inspección, calibración y vida útil del mini demo (heredado) | Borrador |

### 09 — Presentación (referencia heredada)

| Documento | Contenido | Estado |
|---|---|---|
| [`09-presentacion/guion-demo.md`](09-presentacion/guion-demo.md) | Guion de demo del mini demo (heredado) | Borrador |
| [`09-presentacion/faq-jurado.md`](09-presentacion/faq-jurado.md) | Preguntas del jurado del mini demo (heredado) | Borrador |

## Documentos transversales

- [`glosario.md`](glosario.md) — términos y siglas.
- [`../CHANGELOG.md`](../CHANGELOG.md) — cambios de la sección.
- [`../AGENTS.md`](../AGENTS.md) — reglas para agentes y colaboradores.

## Convenciones de estado

| Estado | Significado |
|---|---|
| Borrador | En elaboración; puede cambiar sin aviso |
| En revisión | Listo para revisión por pares |
| Aprobado | Revisado y aceptado; cambios requieren control |
| Vivo | Se actualiza continuamente (bitácora, registro, trazabilidad) |
| Obsoleto | Reemplazado; se conserva por trazabilidad |

## Nota sobre los documentos heredados

Los documentos de `00-gobierno` a `09-presentacion` se copiaron del mini demo como **base metodológica, técnica y de formato**. Pueden contener ejemplos, cifras y decisiones del mini demo (Raspberry Pi 5, Nav2, Camera Module 3, BOM de 2 motores). En esta sección son referencia: no se aplican automáticamente al rover grande. Toda decisión nueva se registra en `registro-decisiones.md` con prefijo `ADR-1xxx` u `OQ-Vxx`, y todo requisito nuevo se escribe en `02-requisitos/vision-alcance.md` y sus derivados.
