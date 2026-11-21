# AGENTS.md — Guía para agentes de IA y colaboradores

> **Proyecto:** Rover Mini Demo — European Rover Challenge (ERC)
> **Alcance de esta fase:** demostración reducida de **navegación autónoma** sobre Raspberry Pi + ROS 2. El rover grande (brazo, ciencia, perforación) queda fuera de alcance.
> **Idioma:** documentación en español; código, identificadores y mensajes de log en inglés.
> **Última actualización:** 2026-11-21

---

## 0. Contexto que debes tener claro antes de tocar nada

Este repositorio no es un rover completo. Es un **producto mínimo verificable** para:

1. Aprender y demostrar el ciclo completo de ingeniería (SDLC) aplicado a robótica.
2. Validar la pila de navegación autónoma (ROS 2 + Nav2 + simulación) que luego escalará al rover grande del ERC.
3. Generar **evidencia reproducible** (documentos, pruebas, bags, métricas, vídeos) que sirva tanto para el jurado como para el equipo.

El objetivo deportivo es el **ERC 2027**. El ERC 2026 se celebró del 4 al 6 de septiembre de 2026 en Cracovia; las fechas de 2027 aún no están publicadas. No inventes fechas ni normas: consulta `docs/01-investigacion/fuentes.md`.

### Decisiones ya tomadas (no las cambies sin ADR)

| Decisión | Valor | ADR |
|---|---|---|
| Middleware | ROS 2 Jazzy Jalisco | [ADR-0001](docs/03-arquitectura/adr/0001-ros2-jazzy.md) |
| Cómputo de a bordo | Raspberry Pi 4 Model B (8 GB) + Argon ONE | [ADR-0010](docs/03-arquitectura/adr/0010-raspberry-pi-4.md) |
| Navegación | Nav2 | [ADR-0003](docs/03-arquitectura/adr/0003-nav2.md) |
| Simulador | Gazebo Harmonic + ros_gz | [ADR-0004](docs/03-arquitectura/adr/0004-gazebo-harmonic.md) |
| Localización del demo | Mapa estático + AMCL | [ADR-0005](docs/03-arquitectura/adr/0005-mapa-estatico-amcl.md) |
| Orquestador de misión | Nodo Python sobre la acción `NavigateToPose` | [ADR-0006](docs/03-arquitectura/adr/0006-python-mision.md) |
| Evidencia | Artefactos con metadatos y hash | [ADR-0007](docs/03-arquitectura/adr/0007-evidencia-reproducible.md) |

> **Variante 6×6 (estudio paralelo):** [`docs/04-diseno/energia/`](docs/04-diseno/energia/) reúne el cálculo energético, el diseño eléctrico y la BOM de una alternativa con 6 motores, 6 servos, pack Li-ion y solar. **No es la base del mini demo** (2 motores, LiFePO4 12,8 V) hasta que se apruebe OQ-09. No mezcles ambas BOM ni compres hardware de la variante sin decisión.

---

## 1. Reglas de oro

### 1.1 Consultar siempre

Antes de afirmar un dato técnico, una norma o una fecha:

1. **Consulta la fuente primaria** (documentación oficial de ROS, Nav2, Gazebo, ERC, fabricante del hardware). Si no existe, usa una fuente secundaria y márcala como tal.
2. **Registra la consulta** en [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md): URL, fecha de acceso, qué se extrajo y nivel de confianza.
3. **Consulta al usuario** antes de cualquier decisión irreversible: compra de hardware, cambio de alcance, cambio de distro, presupuesto, fechas, licencia o publicación.
4. Si falta información, **escribe el supuesto** de forma explícita (`> Supuesto: ...`) y abre una pregunta en el documento. Nunca rellenes huecos con invenciones.

### 1.2 No inventar evidencia

- Un test que no se ejecutó **no está aprobado**. Un PDF que no se descargó **no está citado**. Un vídeo que no existe **no se referencia**.
- Todo resultado debe indicar: fecha, entorno, comando, salida y artefacto asociado.
- Los estados permitidos de una evidencia son: `Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`.

### 1.3 Todo deja rastro

Cada cambio relevante debe actualizar, como mínimo:

- El documento afectado (requisito, arquitectura, diseño, guía).
- La matriz de trazabilidad si cambian requisitos o pruebas: [`docs/02-requisitos/trazabilidad.md`](docs/02-requisitos/trazabilidad.md).
- La bitácora: [`docs/05-implementacion/bitacora.md`](docs/05-implementacion/bitacora.md).
- `CHANGELOG.md` si el cambio es visible para el usuario.
- Evidencia en `docs/08-evidencia/artefactos/` si se ejecutó algo.

### 1.4 Seguridad primero

- No ejecutes comandos que puedan mover físicamente el rover sin autorización explícita y sin la parada de emergencia accesible.
- No desactives límites de velocidad, watchdog, fusibles ni la parada de emergencia.
- No publiques credenciales, claves WiFi, tokens ni datos personales. Usa variables de entorno o `~/.config`.
- Los scripts que requieren `sudo` deben avisar, comprobar el sistema operativo y fallar de forma segura.

---

## 2. Estado actual del proyecto

| Elemento | Estado |
|---|---|
| Documentación SDLC | En construcción (v0.1) |
| Paquete ROS 2 de simulación | Borrador, pendiente de validación en runtime |
| Paquete de misión (lógica pura) | Implementado con pruebas unitarias locales |
| Mapa y mundo de la arena | Generados por script determinista |
| Validación en Gazebo/Nav2 | **Pendiente** (no hay ROS 2 en el host de desarrollo actual) |
| Hardware físico | No adquirido |
| Fecha ERC 2027 | No publicada |

> **Host de desarrollo actual:** Fedora 43, Python 3.14, sin ROS 2, sin Docker, sin Gazebo. Por eso la validación de runtime se hace en Ubuntu 24.04 (VM, contenedor o Raspberry Pi) y se registra como evidencia separada. No presentes como “probado” lo que solo está diseñado.

---

## 3. Mapa del repositorio

```
AGENTS.md                     Este documento
README.md                     Puerta de entrada
Makefile                      Comandos de documentación, tests y evidencia
docs/                         Documentación SDLC e investigación
  00-gobierno/                Metodología, plan, riesgos, roles, ADR index
  01-investigacion/           ERC, estado del arte, benchmarking, fuentes
  02-requisitos/              RF, RNF, historias, trazabilidad
  03-arquitectura/            Arquitectura, interfaces, seguridad, ADRs
  04-diseno/                  Software, mecánica, electrónica, BOM
  05-implementacion/          Entorno, instalación, convenciones, bitácora
  06-pruebas/                 Plan, casos, protocolo, resultados
  07-operacion/               Operación, runbook, mantenimiento
  08-evidencia/               Política, registro y artefactos
  09-presentacion/            Guion de demo y FAQ de jurado
ros_ws/src/                   Workspace ROS 2 (description, bringup, mission)
scripts/                      Automatización reproducible
```

### Dónde va cada cosa

| Si vas a… | Escribe en… |
|---|---|
| Cambiar el alcance o los requisitos | `docs/02-requisitos/` y abre un ADR si es estructural |
| Cambiar la arquitectura o una interfaz | `docs/03-arquitectura/` + ADR |
| Añadir hardware o cambar el diseño | `docs/04-diseno/` + BOM |
| Cambiar código o launch files | `ros_ws/src/` + bitácora + tests |
| Añadir una prueba | `docs/06-pruebas/casos-prueba.md` + `ros_ws/src/**/test/` |
| Ejecutar una prueba o demo | `docs/08-evidencia/artefactos/<fecha>-<slug>/` |
| Preparar la presentación | `docs/09-presentacion/` |

---

## 4. Flujo de trabajo SDLC

El proyecto sigue un ciclo **iterativo e incremental** con puertas de calidad. La metodología completa está en [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md).

| Puerta | Objetivo | Artefactos mínimos | Criterio de salida |
|---|---|---|---|
| G0 — Concepción | Problema, alcance y viabilidad | Visión, contexto ERC, benchmarking | Alcance aprobado por el usuario |
| G1 — Requisitos | Qué debe hacer el sistema | RF, RNF, historias, trazabilidad | Requisitos verificables y priorizados |
| G2 — Arquitectura y diseño | Cómo se construye | Arquitectura, interfaces, ADRs, diseño | Revisión técnica sin bloqueantes |
| G3 — Implementación | Construir el incremento | Código, configuración, tests unitarios | Build + unit tests en verde |
| G4 — Verificación y validación | Demostrar que funciona | Casos ejecutados, bags, métricas | Criterios de aceptación cumplidos o desviación aceptada |
| G5 — Operación y demo | Operarlo de forma segura | Runbook, preflight, evidencia final | Demo reproducible y ensayada |

### Regla de las dos velocidades

- **Trabajo de producto:** siempre ligado a un requisito o a una decisión documentada.
- **Trabajo exploratorio:** permitido, pero se registra como *spike* con pregunta, tiempo máximo y conclusión. Si genera código, se etiqueta como prototipo y no se presenta como producto hasta pasar G4.

### Antes de implementar

1. Lee el requisito y su criterio de aceptación.
2. Comprueba si existe un ADR o una interfaz que lo condicione.
3. Escribe o actualiza el caso de prueba.
4. Implementa lo mínimo que satisface el criterio.
5. Ejecuta `make check`.
6. Registra evidencia.

---

## 5. Comandos habituales

```bash
make help            # lista de comandos
make check           # docs + assets + tests + lint (sin ROS)
make docs            # valida enlaces y trazabilidad
make assets-check    # verifica que mundo y mapa coinciden con arena.json
make test            # pruebas unitarias de la lógica de misión
make lint            # sintaxis Python/Bash/YAML/XML/JSON
make evidence        # crea una carpeta de evidencia con metadatos
make sim             # lanza Gazebo + Nav2 (requiere ROS 2 Jazzy)
make mission         # lanza la misión sobre la simulación
```

En un entorno ROS 2:

```bash
source /opt/ros/jazzy/setup.bash
cd ros_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
ros2 launch rover_bringup sim.launch.py
```

> En Fedora o en cualquier host sin Ubuntu 24.04, usa una VM/contenedor Ubuntu 24.04. Los binarios de ROS 2 Jazzy son para Ubuntu Noble. Ver [`docs/05-implementacion/entorno-desarrollo.md`](docs/05-implementacion/entorno-desarrollo.md).

---

## 6. Convenciones

### Documentación

- Un documento = una responsabilidad. No mezcles requisitos con diseño.
- Encabezado de control en documentos "vivos":

  ```markdown
  > Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: <rol>
  ```

- Enlaces relativos, nunca rutas absolutas del equipo.
- Diagramas en Mermaid dentro del Markdown; si hay imagen, guarda el fuente editable.
- Identificadores estables: `RF-01`, `RNF-01`, `TC-01`, `ADR-0001`, `RSK-01`.
- Toda afirmación técnica no obvia lleva fuente en `fuentes.md` o en el propio documento.
- No uses negritas para gritar; úsalas para resaltar decisiones.

### Código

- Python: PEP 8, `snake_case`, type hints en lógica de dominio, docstrings en inglés.
- ROS 2: nombres de paquetes en `snake_case`, topics en minúsculas con `/`, frames en `snake_case`.
- YAML: 2 espacios, sin tabs.
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- Ramas: `feat/<tema>`, `fix/<tema>`, `docs/<tema>`.
- No subas `build/`, `install/`, `log/`, bags grandes ni secretos.

### Seguridad y privacidad

- Los perfiles de red, credenciales y calibraciones locales van en `~/.config/rover/`, nunca en el repo.
- Los datos de pruebas con personas requieren consentimiento y anonimización.

---

## 7. Evidencia: qué cuenta y qué no

Una evidencia es válida si cumple **las cuatro condiciones**:

1. **Trazable:** enlaza requisito, caso de prueba y artefacto.
2. **Reproducible:** incluye comando, versión, commit y entorno.
3. **Íntegra:** incluye hash SHA-256 del artefacto.
4. **Verificable:** otra persona puede repetirla sin preguntarte.

Formato de carpeta:

```
docs/08-evidencia/artefactos/2026-11-21T120000-validacion-documental/
├── README.md          # qué se hizo, resultado, conclusión
├── metadata.json      # fecha, host, commit, versiones
├── MANIFEST.sha256    # hashes de los archivos
├── logs/              # salidas de consola
├── media/             # fotos, vídeos, capturas
└── bags/              # rosbag2 (o enlace externo + hash)
```

- Los bags grandes (> 50 MB) no se versionan: se guardan en almacenamiento externo y se registra URL + hash.
- No edites un artefacto después de sellarlo. Si necesitas corregir, crea una nueva ejecución y marca la anterior como `Obsoleta`.

---

## 8. Definición de “hecho” (Definition of Done)

Un incremento está terminado cuando:

- [ ] Cumple su criterio de aceptación y está enlazado a un requisito.
- [ ] Tiene pruebas automatizadas o un procedimiento manual documentado.
- [ ] `make check` pasa en el entorno objetivo.
- [ ] La documentación afectada está actualizada.
- [ ] La trazabilidad requisito → diseño → prueba → evidencia está completa.
- [ ] Hay evidencia registrada (o una excepción justificada).
- [ ] No introduce secretos, datos personales ni dependencias sin licencia compatible.
- [ ] La bitácora y el CHANGELOG reflejan el cambio.

---

## 9. Preguntas frecuentes del agente

**¿Puedo cambiar la distro de ROS?**
Solo con un ADR que compare alternativas y aprobación del usuario. La decisión actual es Jazzy por soporte LTS hasta 2029 y compatibilidad con Ubuntu 24.04 en Raspberry Pi 4 (ADR-0010).

**¿Puedo añadir un paquete de terceros?**
Sí, si tiene licencia compatible, está mantenido y se registra en el ADR o en la documentación de dependencias. Verifica la versión contra la distro.

**¿Puedo generar un mapa “a mano”?**
No. El mapa se genera desde `arena.json` con `scripts/docs/generate_arena.py` para garantizar que mundo y mapa coinciden.

**¿Puedo decir que la simulación funciona?**
Solo si existe una ejecución registrada en `docs/08-evidencia/` con logs y bag. Mientras no exista, el estado es `Pendiente`.

**¿Qué hago si el usuario pide algo fuera de alcance?**
Documenta la solicitud, explica el impacto y propón un ADR o una nueva fase. No lo implementes por iniciativa propia.

---

## 10. Checklist antes de cerrar una tarea

- [ ] Leí los requisitos y ADRs relacionados.
- [ ] Consultado las fuentes necesarias y las registré.
- [ ] Actualicé la documentación y la trazabilidad.
- [ ] Ejecuté `make check` y guardé la salida.
- [ ] Creé la evidencia con metadatos y hash.
- [ ] Anoté el cambio en la bitácora.
- [ ] Verifiqué que no hay secretos ni artefactos grandes versionados.
- [ ] Informé al usuario de supuestos, riesgos y siguiente paso.
