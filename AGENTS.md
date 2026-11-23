# AGENTS.md — Workspace Kairos ERC (madre)

> **Workspace:** `D:\ERC-UNMSM-Rover` — checkout de
> [`MarioAntizana1/Kairos--ERC-xd`](https://github.com/MarioAntizana1/Kairos--ERC-xd),
> rama `main`, commit `3a44e15` (`feat(mini-rover): import autonomous navigation demo`).
> **Ámbito:** los tres subproyectos del ERC (Mini-rover, Drone, Rover-principal) y
> la capa central de skills.
> **Fase actual:** planificación e investigación. **No se ejecuta nada.**
> **Idioma:** documentación en español; código, identificadores, topics y logs en inglés.
> **Última actualización:** 2026-11-23

---

## 0. Política de la fase actual — solo planificación e investigación

Esta fase del proyecto es **documental**. Hasta que el usuario diga explícitamente
que se abre la ejecución, rige esta regla por encima de cualquier otra rutina del
repo:

| Prohibido en esta fase | Permitido en esta fase |
|---|---|
| Ejecutar scripts, validadores, `make`, `check_docs.py`, `check_bom.py` | Leer y analizar el código y la documentación existente |
| Lanzar simulaciones, ROS 2, Gazebo, `colcon`, `ros2 launch` | Documentar, planificar, diseñar y revisar |
| Correr pruebas, medir, calibrar, generar bags o datos | Investigar fuentes (fabricantes, normativa, tiendas, estado del arte) |
| Instalar paquetes o dependencias (`pip`, `apt`, `pnpm`) | Escribir requisitos, arquitectura, ADR, riesgos, BOM y cotizaciones |
| Tocar hardware (rover, dron, Raspberry Pi, cámaras, sensores) | Diseñar el plan de pruebas, los casos y los protocolos de experimento |
| Crear carpetas de evidencia de ejecución | Diseñar el plan de proyecto, los guiones de demo y el FAQ del jurado |
| Abrir una terminal para “comprobar que funciona” | Editar documentos Markdown, CSV de BOM y borradores de código como propuesta |

Regla de oro: **si algo se ejecuta, se mide o se prueba, no es de esta fase.** Si
una tarea lo pide, la respuesta correcta es entregar el **plan** de esa ejecución
(qué se haría, con qué comando, en qué entorno, qué evidencia produciría) y
preguntar antes de pasar a ejecutarla.

La fase de ejecución y pruebas se abrirá después, y con ella las puertas G3
(implementación) y G4 (verificación). Hasta entonces **nada se declara probado,
aprobado ni calibrado**.

---

## 1. Qué es este workspace

Es el **monorepo madre** del equipo Kairos para el European Rover Challenge. No es
un rover: es el paraguas donde conviven tres subproyectos autónomos, cada uno con
su propio `AGENTS.md`, su documentación SDLC, sus scripts y su evidencia histórica.

Este archivo da las reglas **comunes**. No repite lo que ya está en el `AGENTS.md`
de cada carpeta: lo que sigue es lo que aplica en las tres a la vez.

Regla de convivencia: **cada subproyecto se trabaja desde su carpeta**. No mezcles
BOM, evidencias ni decisiones de dos subproyectos en el mismo documento.

---

## 2. Mapa y las tres carpetas de trabajo

```text
D:\ERC-UNMSM-Rover\
├── AGENTS.md                  Este documento (madre de las instrucciones)
├── README.md                  Puerta de entrada del repositorio
├── .dsh\                      Capa central de skills (madre de las skills)
│   ├── README.md
│   ├── SOURCES.md
│   └── skills\
│       ├── documentacion-trazabilidad\
│       ├── investigacion-proveedores-peru\
│       └── rover-vision\
├── cotizaciones\              BOM consolidado por proveedor (transversal)
├── mini-rover\                Subproyecto 1 — navegación autónoma
├── drone\                     Subproyecto 2 — payload de visión del dron
└── rover-principal\           Subproyecto 3 — visión del rover grande
```

| Carpeta | Nombre de trabajo | Qué es | Estado | Entrada |
|---|---|---|---|---|
| `mini-rover/` | **Mini-rover** | Producto mínimo verificable de navegación autónoma: Pi 4 8 GB + Argon ONE, ROS 2 Jazzy, Nav2, Gazebo Harmonic, LiDAR 2D | Documentación y simulación en borrador; runtime nunca validado | `mini-rover/README.md` |
| `drone/` | **Drone** | Payload de visión estéreo + ToF de piso: Pi 5, 2 × Camera Module 3, TFmini Plus 12 m, calibración, profundidad, BOM Perú | Documentación y cotización hechas; pipeline y calibración diseñados, no ejecutados | `drone/README.md` |
| `rover-principal/` | **Rover-principal** | Visión del rover grande: sensores en Perú (Elgato Facecam 4K, TFmini Plus/S, LIDAR-Lite v3HP), arquitectura de percepción, requisitos, BOM | Documental; sin pruebas de runtime | `rover-principal/README.md` |

> **Sobre los nombres.** Las carpetas conservan el nombre canónico del repositorio
> (`mini-rover`, `drone`, `rover-principal`) en minúsculas y kebab-case porque los
> `README.md`, los `AGENTS.md`, la trazabilidad, los scripts y el CI dependen de
> esas rutas. En la conversación se llaman **Mini-rover**, **Drone** y
> **Rover-principal**. Si alguna vez se renombran, hay que actualizar enlaces
> internos, `Makefile`, CI y este archivo en el mismo commit.

---

## 3. Jerarquía de instrucciones

Cuando dos reglas se contradicen, gana la más cercana al conflicto:

1. Instrucciones del usuario en la conversación.
2. **La política de fase de este documento (§0)**: mientras dure la fase de
   planificación, bloquea la ejecución aunque un `AGENTS.md` de subproyecto diga
   “ejecuta `make check`”.
3. `AGENTS.md` del subproyecto (`mini-rover/`, `drone/`, `rover-principal/`).
4. El resto de este `AGENTS.md` (reglas del workspace).
5. Skills de `.dsh/skills/` (procedimientos; no sustituyen reglas).

Si trabajas en `drone/docs/04-diseno/bom.md`, mandan `drone/AGENTS.md` y este
documento; no apliques convenciones del mini-rover a ese archivo.

---

## 4. Skills madre: `.dsh/skills/`

Las skills del workspace viven en `.dsh/skills/` y están disponibles para los
tres subproyectos y para cualquier subagente que trabaje dentro del workspace
(DeepSeek Harness las descubre por la raíz `.git` del repositorio).

| Skill | Cuándo usarla |
|---|---|
| `documentacion-trazabilidad` | Crear o editar cualquier documento bajo `docs/`: citas `F-xx`, supuestos, ADR, `OQ`, matriz de trazabilidad, bitácora. Incluye la tabla de IDs de los tres proyectos y la regla de que la evidencia queda `Pendiente` en esta fase |
| `investigacion-proveedores-peru` | Investigar precios, stock y disponibilidad en tiendas peruanas, y registrar la fuente antes de tocar una BOM |
| `rover-vision` | Contexto y reglas de `rover-principal/`: cámaras, ToF, LiDAR, calibración, decisiones abiertas del rover grande |

Detalles de procedencia, licencia y mantenimiento: `.dsh/SOURCES.md`.
Cómo funciona la capa y cómo añadir una skill: `.dsh/README.md`.

> `rover-principal/.opencode/skills/` es la copia original para el cliente
> opencode. **La madre es `.dsh/skills/`**: si cambias una convención compartida,
> actualiza ambas y anótalo en `.dsh/SOURCES.md`.

---

## 5. Reglas globales (válidas en las tres carpetas)

### 5.1 No ejecutar

- No se ejecuta nada de lo listado en §0. Si dudas, pregunta antes de teclear un
  comando.
- No se crea evidencia de ejecución: los protocolos se diseñan y se marcan
  `Pendiente`.
- No se declara “probado”, “aprobado”, “calibrado” ni “funciona” nada en esta fase.

### 5.2 Evidencia antes que afirmaciones (aplicada a documentación)

- Un test que no se ejecutó **no está aprobado**; una calibración que no se hizo
  **no existe**; un PDF que no se descargó **no se cita**.
- Estados permitidos de evidencia: `Pendiente`, `Ejecutada`, `Aprobada`,
  `Fallida`, `Obsoleta`. En esta fase todo queda en `Pendiente`.
- Los artefactos ya sellados en `docs/08-evidencia/artefactos/` son historia del
  proyecto: se leen, no se editan.
- El diseño de un experimento debe indicar qué evidencia producirá y con qué
  criterio se aceptaría, para que la fase de ejecución sea reproducible.

### 5.3 Fuentes

- Especificaciones: ficha del fabricante. Precio y stock: tienda, con URL y fecha.
- Toda fuente nueva se registra en el `docs/01-investigacion/fuentes.md` del
  subproyecto que la usa.
- Si no hay dato, se escribe `> Supuesto:` y se abre una pregunta. **No se
  inventa.**

### 5.4 Idioma, formato y unidades

- Documentación en español; código, identificadores y logs en inglés.
- Fechas ISO 8601; carpetas de evidencia en UTC.
- Unidades SI; tablas antes que prosa para comparar.
- Archivos `kebab-case.md`, enlaces relativos, diagramas en Mermaid.

### 5.5 Git

- Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- Ramas `feat/<tema>`, `fix/<tema>`, `docs/<tema>`.
- No se suben `build/`, `install/`, `log/`, bags > 50 MB ni secretos.
- Un cambio que afecte a varios subproyectos se explica en el mensaje del commit.

### 5.6 Dinero, hardware y alcance

- **No se compra hardware** ni se compromete presupuesto sin aprobación explícita
  del usuario.
- No se cambia el alcance de un subproyecto por iniciativa propia: se documenta la
  solicitud, se explica el impacto y se propone un ADR o una fase nueva.
- No se cambian decisiones ya aceptadas (distro, plataforma de cómputo, sensor
  base) sin un ADR que compare alternativas.
- En esta fase los ADR se **proponen**; no se marcan como aceptados sin evidencia
  ni aprobación.

### 5.7 Seguridad y privacidad

- Nada de pruebas que muevan el rover o el dron sin autorización, preflight y
  parada de emergencia accesible — y en esta fase, simplemente no se ejecutan.
- ToF y LiDAR son láser clase 1: no se apunta al ojo ni se retira la carcasa.
- Sin credenciales, tokens, claves WiFi ni datos personales en el repo; los
  perfiles locales van en `~/.config/rover/` o `~/.config/drone/`.
- No se graban personas sin consentimiento; se anonimizan rostros y matrículas.

---

## 6. Qué sí se produce en esta fase

Entregables documentales, en el `docs/` del subproyecto correspondiente:

| Trabajo | Dónde |
|---|---|
| Visión, alcance y contexto (G0) | `docs/02-requisitos/vision-alcance.md`, `docs/01-investigacion/` |
| Requisitos RF/RNF, historias y trazabilidad (G1) | `docs/02-requisitos/` |
| Arquitectura, interfaces y ADR propuestos (G2) | `docs/03-arquitectura/` |
| Diseño, BOM y cotización | `docs/04-diseno/` |
| Plan de pruebas, casos y protocolos (sin ejecutar) | `docs/06-pruebas/` |
| Operación y runbooks previstos | `docs/07-operacion/` |
| Riesgos, decisiones, plan de proyecto (G0–G2) | `docs/00-gobierno/` |
| Investigación de campo: proveedores, normativa, estado del arte | `docs/01-investigacion/` |
| Guion de demo y FAQ del jurado | `docs/09-presentacion/` |
| BOM consolidado de los tres subproyectos, por proveedor | `cotizaciones/` |

Un caso de prueba redactado en esta fase no cuenta como prueba ejecutada: se
marca `Pendiente` y se enlaza a la evidencia que producirá.

---

## 7. Comandos reservados para la fase de ejecución — ⚠️ NO EJECUTAR AHORA

Esta tabla es **documentación de referencia** para cuando el usuario abra la fase
de ejecución. No es una invitación a correr nada. Se incluye aquí para que el plan
de validación futura sea reproducible.

| Acción | Mini-rover | Drone |
|---|---|---|
| Validar documentación | `python mini-rover/scripts/docs/check_docs.py` | `python drone/scripts/docs/check_docs.py` |
| Validar BOM | — | `python drone/scripts/docs/check_bom.py` |
| Coherencia arena/mapa | `python mini-rover/scripts/docs/generate_arena.py --check` (requiere PyYAML) | — |
| Tests unitarios | `bash mini-rover/scripts/test/run_tests.sh` | — (alias de `check`) |
| Lint | `bash mini-rover/scripts/test/lint.sh` | — |
| Crear evidencia | `bash mini-rover/scripts/evidence/new_evidence.sh <slug>` | `bash drone/scripts/evidence/new_evidence.sh <slug>` |
| Sellar evidencia | `bash mini-rover/scripts/evidence/seal_evidence.sh <dir>` | `bash drone/scripts/evidence/seal_evidence.sh <dir>` |
| Equivalente POSIX | `cd mini-rover && make check` | `cd drone && make check` |

- `rover-principal/` es documental: no tiene `Makefile` ni validadores.
- ROS 2 Jazzy, Gazebo y colcon no están instalados en el host de trabajo; todo lo
  que requiera runtime se planifica para Ubuntu 24.04 (VM, contenedor o Raspberry
  Pi) y se ejecutará en la fase correspondiente.

---

## 8. Estado del workspace y línea base

Línea base levantada al preparar el workspace el **2026-11-23**, antes de fijar la
política de no ejecución. Es un dato histórico de referencia, no se repite en
esta fase.

| Elemento | Estado |
|---|---|
| Clon del repositorio | Completo, rama `main`, commit `3a44e15`, árbol limpio |
| Carpetas de trabajo | `mini-rover/`, `drone/`, `rover-principal/` presentes |
| Skills madre | `.dsh/skills/` con 3 skills, descubiertas por el agente |
| `drone` docs + BOM | 52 documentos, 129 enlaces, 0 errores; BOM S/ 2,341.08 |
| `mini-rover` docs | 78 documentos, 356 enlaces, 0 errores |
| `mini-rover` assets-check | No ejecutable en el host: faltaba PyYAML |
| `rover-principal` | Documental, sin validadores automáticos |
| Host | Windows 11 Pro 26200 (AMD64), Python 3.11.9, Git 2.56.0 |
| Sin instalar | `make`, ROS 2 Jazzy, Gazebo Harmonic, colcon, PyYAML |

---

## 9. Criterio de cierre en esta fase (“planeado”)

Un documento o cambio está terminado cuando:

- [ ] Cumple su criterio de aceptación documental y está enlazado a un requisito.
- [ ] Toda afirmación técnica tiene fuente `F-xx` o `> Supuesto:` explícito.
- [ ] Los enlaces relativos resuelven y los IDs siguen la convención del proyecto.
- [ ] La trazabilidad requisito → diseño → prueba → evidencia está completa **en
      su parte documental**, con la evidencia marcada `Pendiente`.
- [ ] Se indicó qué pruebas harán falta, en qué entorno y con qué criterio de
      aceptación.
- [ ] Bitácora y `CHANGELOG.md` del subproyecto reflejan el cambio.
- [ ] No se ejecutó nada ni se instaló nada para llegar a este estado.
- [ ] Si cambió una convención compartida, `.dsh/skills/` y `.dsh/SOURCES.md` están actualizados.

---

## 10. Cómo abordar una tarea en esta fase

1. Identifica el subproyecto y lee su `AGENTS.md`, su `README.md` y el documento
   relacionado.
2. Formula la pregunta y el criterio de aceptación.
3. Investiga con fuentes primarias y regístralas con fecha y URL.
4. Escribe o actualiza requisitos, arquitectura, diseño, riesgo o plan de pruebas.
5. Si hace falta evidencia para decidir, **propón el experimento** (protocolo,
   entorno, comando, criterio) y márcalo `Pendiente`; no lo ejecutes.
6. Anota el cambio en bitácora y changelog.
7. Informa al usuario de supuestos, riesgos, preguntas abiertas y qué habría que
   ejecutar cuando se abra la fase de pruebas.

---

## 11. Preguntas frecuentes del agente

**¿Puedo ejecutar `make check` o los validadores para ver si está bien?**
No. En esta fase no se ejecuta nada. Si crees que hace falta, di qué validaría y
espera autorización.

**¿Puedo instalar PyYAML, ROS 2 o cualquier dependencia?**
No. Las dependencias de desarrollo se documentan en `requirements-dev.txt`; se
instalan en la fase de ejecución.

**¿Puedo crear una carpeta en `docs/08-evidencia/artefactos/`?**
No. En esta fase se diseña el protocolo y se deja la plantilla; las carpetas de
evidencia se crean cuando se ejecute la prueba.

**¿Puedo escribir código nuevo?**
Como propuesta o borrador dentro de un documento de diseño, sí (pseudocódigo,
interfaces, firmas). No se implementa ni se ejecuta código de runtime en esta fase.

**¿Puedo investigar en internet?**
Sí: es parte de la fase. Registra cada fuente con URL, fecha y confianza.

**¿Puedo crear una skill nueva?**
Sí, en `.dsh/skills/<nombre>/SKILL.md` siguiendo `.dsh/README.md`. Primero
comprueba que la regla no esté ya en un `AGENTS.md`.

**¿Puedo tocar la copia de `rover-principal/.opencode/skills/`?**
Solo para mantenerla en sintonía con `.dsh/skills/`. No la uses como fuente de
verdad.

**¿Puedo decir que la simulación o el estéreo funcionan?**
No. Mientras no exista evidencia sellada y ejecutada, el estado es `Pendiente`.

**¿Qué hago si el usuario pide algo fuera de alcance?**
Documéntalo, explica el impacto y propón un ADR o una fase nueva. No lo
implementes por iniciativa propia.
