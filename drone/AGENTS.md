# AGENTS.md — Guía para agentes de IA y colaboradores

> **Proyecto:** Drone — Payload de visión estéreo + ToF de piso
> **Alcance de esta fase:** visión a bordo (2 × Camera Module 3 + ToF de piso + Raspberry Pi 5). El dron completo queda fuera.
> **Idioma:** documentación en español; código, identificadores, topics y logs en inglés.
> **Última actualización:** 2026-11-21

---

## 0. Contexto que debes tener claro antes de tocar nada

Este repositorio **no es un dron completo**. Es el **payload de visión** de un dron de inspección/mapeo 3D. Su producto mínimo verificable es:

1. Un par estéreo calibrado que entrega profundidad y nube de puntos.
2. Un ToF de piso que da una referencia de altura/escala y valida el estéreo.
3. Un registro reproducible de frames, profundidad, pose y calibración.
4. Documentación y evidencia que permitan a otra persona repetir el experimento.

El dron (frame, controladora de vuelo, ESCs, motores, batería, radio) es responsabilidad de otro equipo. **La visión es advisory:** nunca sustituye los failsafes ni la autoridad de la controladora de vuelo.

### Decisiones y propuestas vigentes (no las cambies sin ADR)

| Decisión | Valor | Estado | ADR |
|---|---|---|---|
| Cómputo de a bordo | Raspberry Pi 5, 8 GB | Aceptada | [ADR-0001](docs/03-arquitectura/adr/0001-pi5-computo.md) |
| Par estéreo | 2 × Camera Module 3 Standard, baseline 150 mm | Aceptada | [ADR-0002](docs/03-arquitectura/adr/0002-stereo-cm3.md) |
| ToF de piso | TFmini Plus 12 m (base, 6 m) / VL53L1X o VL53L5CX 8×8 (≤4 m, alternativas) | Aceptada | [ADR-0003](docs/03-arquitectura/adr/0003-tof-vl53l5cx.md) |
| Pipeline | Picamera2 + OpenCV SGBM + ROS 2 Jazzy | Propuesta | [ADR-0004](docs/03-arquitectura/adr/0004-pipeline-stereo.md) |
| Evidencia | Artefactos con metadatos y hash SHA-256 | Aceptada | [ADR-0005](docs/03-arquitectura/adr/0005-evidencia-reproducible.md) |

> **Aclaración recurrente:** el ToF va montado en la base, **mirando al piso**, y la base es **TFmini Plus 12 m** porque la competencia vuela a **6 m**. Da una referencia métrica de altura/distancia al suelo para escalar y validar la calibración. **No** implementa geometría epipolar: eso lo hace el par estéreo. Una sola distancia no sustituye una calibración con tablero; se usa como restricción/verificación y para estimar el plano del suelo. Los ToF de 4 m (VL53L1X/VL53L5CX) no alcanzan a 6 m.

---

## 1. Reglas de oro

### 1.1 Consultar siempre

Antes de afirmar un dato técnico, una norma o un precio:

1. **Consulta la fuente primaria** (Raspberry Pi, STMicroelectronics, OpenCV, MAVLink, tienda). Si no existe, usa una fuente secundaria y márcala.
2. **Registra la consulta** en [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md): URL, fecha, qué se extrajo y confianza.
3. **Consulta al usuario** antes de una decisión irreversible: compra, cambio de alcance, cambio de baseline, cambio de ToF, vuelo real.
4. Si falta información, escribe el supuesto (`> Supuesto: ...`) y abre una pregunta. **No inventes.**

### 1.2 No inventar evidencia

- Un test que no se ejecutó no está aprobado. Una calibración que no se hizo no existe.
- Toda evidencia debe indicar fecha, entorno, comando, salida y artefacto.
- Estados permitidos: `Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`.
- Los resultados de hardware solo son válidos si se ejecutaron en el hardware real, no en una simulación.

### 1.3 Todo deja rastro

Cada cambio relevante actualiza:

- El documento afectado (requisito, arquitectura, diseño, guía).
- La trazabilidad: [`docs/02-requisitos/trazabilidad.md`](docs/02-requisitos/trazabilidad.md).
- La bitácora: [`docs/05-implementacion/bitacora.md`](docs/05-implementacion/bitacora.md).
- `CHANGELOG.md` si es visible para el usuario.
- Evidencia en `docs/08-evidencia/artefactos/` si se ejecutó algo.

### 1.4 Seguridad primero

- **No vueles** sin preflight, geofence, failsafe, spotter y autorización. La visión no controla motores.
- No desactives failsafes, límites de batería, RTL ni la autoridad de la controladora de vuelo.
- No conectes el UBEC al dron sin fusible y sin verificar polaridad.
- No publiques credenciales, claves WiFi, tokens ni datos personales. Usa variables de entorno o `~/.config`.
- Los scripts que requieren `sudo` deben avisar, comprobar el sistema operativo y fallar de forma segura.

### 1.5 Privacidad y normativa

- No grabes personas sin consentimiento; anonimiza rostros y matrículas en la evidencia publicada.
- Respeta las reglas locales de operación de RPAS y las zonas prohibidas. Este repositorio no sustituye el permiso aeronáutico.
- No publiques datos de vuelo que revelen ubicaciones sensibles.

---

## 2. Estado actual

| Elemento | Estado |
|---|---|
| Documentación SDLC | Borrador v0.1 |
| Cotización Perú | Estudio de abastecimiento 2026-11-21 |
| Hardware | No adquirido |
| `check_docs.py` / `check_bom.py` | Implementados y ejecutados localmente |
| Pipeline de visión | Diseñado, no implementado |
| Calibración | Diseñada, no ejecutada |
| Pruebas de hardware/vuelo | Pendientes |
| Evidencia de hardware | Pendiente |

> **Host de desarrollo actual:** Linux, Python 3.14. No hay Raspberry Pi ni cámaras conectadas. Por eso el código de captura no se declara “probado” hasta que exista evidencia en `docs/08-evidencia/`.

---

## 3. Mapa del repositorio

```text
AGENTS.md                     Este documento
README.md                     Puerta de entrada y cotización resumida
Makefile                      Comandos de validación y evidencia
docs/
  00-gobierno/                Metodología, plan, riesgos, roles, ADR index, plantillas
  01-investigacion/           Contexto, estado del arte, hipótesis, normativa, fuentes
  02-requisitos/              RF, RNF, historias, trazabilidad
  03-arquitectura/            Arquitectura, interfaces, seguridad, ADRs
  04-diseno/                  Diseño de visión, BOM y cotización
  05-implementacion/          Entorno, instalación, bitácora
  06-pruebas/                 Plan, casos, protocolo, matriz y resultados
  07-operacion/               Runbook de vuelo y mantenimiento
  08-evidencia/               Política, registro y artefactos
  09-presentacion/            Guion de demo y FAQ
scripts/
  docs/check_docs.py          Valida enlaces, IDs, ADRs y evidencia
  docs/check_bom.py           Valida los totales del CSV de cotización
  evidence/                   Crea y sella carpetas de evidencia
```

### Dónde va cada cosa

| Si vas a… | Escribe en… |
|---|---|
| Cambiar el alcance o los requisitos | `docs/02-requisitos/` + ADR si es estructural |
| Cambiar la arquitectura o una interfaz | `docs/03-arquitectura/` + ADR |
| Añadir hardware o cambiar la cotización | `docs/04-diseno/` + CSV |
| Cambiar código o launch files | `vision_ws/` (cuando exista) + bitácora + tests |
| Añadir una prueba | `docs/06-pruebas/casos-prueba.md` + test automatizado |
| Ejecutar una prueba o demo | `docs/08-evidencia/artefactos/<fecha>-<slug>/` |
| Preparar la presentación | `docs/09-presentacion/` |

---

## 4. Flujo SDLC y puertas

| Puerta | Objetivo | Artefactos mínimos | Criterio de salida |
|---|---|---|---|
| G0 — Concepción | Problema, alcance, viabilidad, costo | Visión, contexto, BOM, riesgos | Alcance y presupuesto aprobados |
| G1 — Requisitos | Qué debe hacer | RF, RNF, historias, trazabilidad | Requisitos verificables y priorizados |
| G2 — Arquitectura y diseño | Cómo se construye | Arquitectura, interfaces, ADRs, diseño | Revisión técnica sin bloqueantes |
| G3 — Implementación | Construir el incremento | Captura, calibración, pipeline, tests | Build + unit tests en verde |
| G4 — Verificación | Demostrar que funciona | Casos ejecutados, métricas, evidencia | Criterios cumplidos o desviación aceptada |
| G5 — Operación | Volarlo de forma segura | Runbook, preflight, ensayos | Demo reproducible y autorizada |

### Regla de las dos velocidades

- **Producto:** ligado a un requisito o decisión documentada.
- **Exploratorio (spike):** pregunta concreta, tiempo máximo (4 h por defecto), conclusión escrita aunque sea “no funciona”. No se presenta como producto hasta G4.

### Antes de implementar

1. Lee el requisito y su criterio de aceptación.
2. Comprueba ADRs e interfaces.
3. Escribe o actualiza el caso de prueba.
4. Implementa lo mínimo que satisface el criterio.
5. Ejecuta `make check`.
6. Registra evidencia.

---

## 5. Comandos habituales

```bash
make help       # lista de comandos
make check      # docs + BOM
make docs       # valida enlaces, IDs, ADRs y evidencia
make bom        # valida los totales del CSV
make evidence   # crea una carpeta de evidencia con metadatos
make seal       # sella una carpeta de evidencia (sha256)
make clean      # limpia artefactos temporales
```

En la Raspberry Pi (cuando exista):

```bash
# Ver cámaras detectadas
rpicam-hello --list-cameras

# Captura de prueba
rpicam-still -o test.jpg --width 2304 --height 1296

# Estado térmico
vcgencmd measure_temp
vcgencmd get_throttled
```

---

## 6. Convenciones

### Documentación

- Un documento = una responsabilidad. No mezcles requisitos con diseño.
- Encabezado de control en documentos vivos:

  ```markdown
  > Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: <rol>
  ```

- Enlaces relativos, nunca rutas absolutas del equipo.
- Diagramas Mermaid dentro del Markdown.
- IDs estables: `RF-01`, `RNF-01`, `TC-01`, `ADR-0001`, `RSK-01`, `EV-2026-11-21-01`.
- Toda afirmación técnica no obvia lleva fuente en `fuentes.md` o en el propio documento.
- No uses negritas para gritar; úsalas para resaltar decisiones.

### Código (cuando exista)

- Python: PEP 8, `snake_case`, type hints en lógica de dominio, docstrings en inglés.
- ROS 2: paquetes en `snake_case`, topics en minúsculas con `/`, frames en `snake_case`.
- YAML: 2 espacios, sin tabs.
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- Ramas: `feat/<tema>`, `fix/<tema>`, `docs/<tema>`.
- No subas `build/`, `install/`, `log/`, bags grandes ni secretos.

### Seguridad y privacidad

- Perfiles de red, credenciales y calibraciones locales van en `~/.config/drone/`, nunca en el repo.
- Los datos de pruebas con personas requieren consentimiento y anonimización.
- Las calibraciones y los vuelos deben registrar ubicación aproximada, no coordenadas sensibles.

---

## 7. Evidencia: qué cuenta y qué no

Una evidencia es válida si cumple **cuatro condiciones**:

1. **Trazable:** enlaza requisito, caso de prueba y artefacto.
2. **Reproducible:** incluye comando, versión, commit y entorno.
3. **Íntegra:** incluye hash SHA-256 del artefacto.
4. **Verificable:** otra persona puede repetirla sin preguntarte.

Formato:

```text
docs/08-evidencia/artefactos/YYYY-MM-DDTHHMMSS-<slug>/
├── README.md          # qué se hizo, resultado, conclusión
├── metadata.json      # fecha, host, SO, versiones, commit, comando, operador
├── MANIFEST.sha256    # hashes
├── logs/              # salidas de consola
├── media/             # fotos, vídeos, capturas
└── bags/              # rosbag2 o datos crudos (o enlace + hash)
```

- Los datos > 50 MB no se versionan: se guardan fuera y se registra URL + hash.
- No edites un artefacto sellado. Si necesitas corregir, crea otra ejecución y marca la anterior como `Obsoleta`.

---

## 8. Definición de “hecho” (DoD)

Un incremento está terminado cuando:

- [ ] Cumple su criterio de aceptación y está enlazado a un requisito.
- [ ] Tiene pruebas automatizadas o un procedimiento manual documentado.
- [ ] `make check` pasa.
- [ ] La documentación afectada está actualizada.
- [ ] La trazabilidad requisito → diseño → prueba → evidencia está completa.
- [ ] Hay evidencia registrada (o una excepción justificada).
- [ ] No introduce secretos, datos personales ni dependencias con licencia incompatible.
- [ ] La bitácora y el `CHANGELOG.md` reflejan el cambio.

---

## 9. Preguntas frecuentes del agente

**¿Puedo cambiar la Raspberry Pi 5 por una Jetson?**
Solo con ADR que compare CPU, potencia, precio, CSI, soporte de cámaras y consumo. La decisión actual prioriza coste, disponibilidad local y doble CSI.

**¿Puedo cambiar las Camera Module 3 por cámaras global shutter?**
Sí, con ADR. Las GS eliminan el rolling shutter pero son monocromas y de menor resolución. La decisión actual es CM3 Standard con foco bloqueado; las GS son la alternativa para escenas dinámicas.

**¿Puedo usar el ToF para la geometría epipolar?**
No. El ToF de piso no calcula líneas epipolares. La geometría epipolar se obtiene del par estéreo calibrado. El ToF da una referencia de altura/distancia al suelo para escalar y validar la calibración, y para estimar el plano del suelo.

**¿Puedo decir que la calibración funciona?**
Solo si existe una ejecución registrada en `docs/08-evidencia/` con el YAML, las imágenes, el error RMS y el comando. Mientras no exista, el estado es `Pendiente`.

**¿Puedo volar para probar?**
Solo con autorización del responsable de seguridad, preflight completo, geofence, failsafe, spotter y seguro/permiso aplicable. La visión no es un sistema de seguridad de vuelo.

**¿Qué hago si el usuario pide algo fuera de alcance?**
Documenta la solicitud, explica el impacto y propón un ADR o una nueva fase. No lo implementes por iniciativa propia.

---

## 10. Checklist antes de cerrar una tarea

- [ ] Leí los requisitos y ADRs relacionados.
- [ ] Consulté las fuentes necesarias y las registré.
- [ ] Actualicé la documentación y la trazabilidad.
- [ ] Ejecuté `make check` y guardé la salida.
- [ ] Creé la evidencia con metadatos y hash (si aplica).
- [ ] Anoté el cambio en la bitácora.
- [ ] Verifiqué que no hay secretos ni artefactos grandes versionados.
- [ ] Informé al usuario de supuestos, riesgos y siguiente paso.
