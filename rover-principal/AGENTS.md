# AGENTS.md — Guía para agentes y colaboradores

> **Proyecto:** Rover Principal — Percepción y Visión (ERC 2027)
> **Alcance de esta sección:** investigación, requisitos y pruebas del subsistema de visión del rover grande. El chasis, el brazo, la ciencia y la perforación quedan fuera.
> **Idioma:** documentación en español; código, identificadores y mensajes de log en inglés.
> **Última actualización:** 2026-11-21

---

## 0. Contexto antes de tocar nada

Esta carpeta es una **sección del proyecto Rover**, no un repositorio aislado. Hereda del mini demo (`../rover`) la metodología, las plantillas y la investigación de percepción 3D. La diferencia es el objeto de estudio: aquí se diseña la **visión del rover grande**, no la navegación mínima.

### Lo que ya está decidido (no reabrir sin evidencia)

| Decisión | Valor | Origen |
|---|---|---|
| Middleware | ROS 2 Jazzy Jalisco | Heredado del mini demo (ADR-0001) |
| LiDAR | **Ya está en la lista del rover grande**; no se re-evalúa aquí | Lista de hardware del rover principal |
| Metodología | SDLC iterativo + Design Science Research | `docs/00-gobierno/metodologia.md` |
| Evidencia | Artefactos con metadatos, fecha y hash | `docs/08-evidencia/README.md` |

### Lo que **no** está decidido

| Tema | Estado | Pregunta |
|---|---|---|
| Plataforma de cómputo del rover grande | Abierta | ¿Jetson Orin, x86 o Raspberry Pi 5? |
| Cámaras definitivas | En evaluación | ¿Dos Elgato Facecam 4K, estéreo global shutter u OAK-D? |
| ToF definitivo | En evaluación | ¿TFmini Plus, TFmini-S, LIDAR-Lite v3HP o VL53L8CX importado? |
| 3D denso | Abierta | ¿Es requisito o línea de aprendizaje? |
| Presupuesto | Abierta | ¿Se aprueban dos cámaras + ToF? |

> **No asumas Raspberry Pi 5 para el rover grande.** El mini demo la usa; el rover grande puede necesitar más cómputo. Cualquier arquitectura que dependa de una plataforma concreta debe declararlo.

---

## 1. Reglas de oro

### 1.1 Fuentes y precios

1. **Especificaciones:** usa la ficha del fabricante (Elgato, Benewake, ST, Garmin, DFRobot). La tienda no es fuente primaria de especificaciones.
2. **Precio y stock:** usa la tienda, con URL y fecha de consulta. Copia el texto de stock tal como aparece (“> 10”, “Solo quedan 3”, “Agotado”).
3. **Distingue:**
   - precio de lista vs. precio internet vs. precio marketplace;
   - producto vendido por la tienda vs. marketplace;
   - stock online vs. “consultar stock”;
   - precio con IGV vs. sin IGV.
4. **No inventes disponibilidad.** Si no se pudo verificar, escribe `No verificado` y la razón.
5. **Toda fuente nueva** se registra en [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md) con ID `F-xx`, URL, fecha, qué se extrajo y confianza.

### 1.2 No inventar evidencia

- Un precio que no se abrió no está verificado.
- Un experimento que no se ejecutó no está aprobado.
- Un datasheet que no se consultó no se cita.
- Los estados permitidos de evidencia son: `Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`.

### 1.3 Todo deja rastro

Cada cambio relevante actualiza:

- El documento afectado.
- [`docs/05-implementacion/bitacora.md`](docs/05-implementacion/bitacora.md).
- [`CHANGELOG.md`](CHANGELOG.md) si es visible para el usuario.
- [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md) si se consultó una fuente nueva.
- [`docs/00-gobierno/registro-decisiones.md`](docs/00-gobierno/registro-decisiones.md) si se abre o cierra una pregunta.

### 1.4 Seguridad

- No ejecutes pruebas físicas que muevan el rover sin autorización y sin parada de emergencia accesible.
- Los ToF y LiDAR son láser clase 1; no apuntes al ojo humano ni retires la carcasa.
- No publiques credenciales, tokens ni datos personales.
- No compres hardware ni comprometas presupuesto sin aprobación explícita.

---

## 2. Estado actual

| Elemento | Estado |
|---|---|
| Base documental y metodológica | Copiada y adaptada (v0.1) |
| Investigación de sensores en Perú | Ejecutada el 2026-11-21 |
| Selección de cámaras | Pendiente de decisión |
| Selección de ToF | Pendiente de decisión |
| Plataforma de cómputo | Pendiente de decisión |
| Pruebas de estéreo/sincronía | No iniciadas |
| Evidencia de runtime | No existe todavía |

---

## 3. Cómo trabajar

1. **Lee** `README.md`, `docs/README.md` y el documento de investigación relacionado.
2. **Formula** la pregunta y el criterio de aceptación antes de buscar.
3. **Investiga** con fuentes primarias y registra la consulta.
4. **Escribe** el hallazgo con fecha, URL, incertidumbre y alternativa.
5. **Decide** solo si hay evidencia; si no, abre una `OQ-Vxx`.
6. **Actualiza** bitácora, changelog y fuentes.
7. **No cierres** una pregunta con una opinión sin fuente.

### Convenciones de IDs de esta sección

| Prefijo | Uso |
|---|---|
| `F-xx` | Fuente (continúa la numeración del mini demo desde F-52) |
| `OQ-Vxx` | Pregunta abierta de Visión |
| `ADR-1xxx` | Decisión de arquitectura de esta sección (evita colisión con ADR-0001–0009) |
| `RSK-Vxx` | Riesgo de Visión |
| `H-Vx` / `E-Vx` | Hipótesis / experimento de Visión |
| `TC-Vxx` | Caso de prueba de Visión |
| `EV-Vxx` | Evidencia de Visión |

---

## 4. Documentos que debes consultar

- [`docs/01-investigacion/sensores-peru-2026-11-21.md`](docs/01-investigacion/sensores-peru-2026-11-21.md) — investigación de campo.
- [`docs/01-investigacion/vision-rover-grande.md`](docs/01-investigacion/vision-rover-grande.md) — problema y arquitecturas.
- [`docs/01-investigacion/percepcion-3d.md`](docs/01-investigacion/percepcion-3d.md) — base técnica heredada.
- [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md) — fases y puertas.
- [`docs/00-gobierno/plantillas/`](docs/00-gobierno/plantillas/) — ADR, requisito, prueba y evidencia.
- [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md) — registro de fuentes.

---

## 5. Skills del proyecto

Las skills están en `.opencode/skills/`:

| Skill | Cuándo usarla |
|---|---|
| `rover-vision` | Contexto, alcance y reglas de esta sección |
| `documentacion-trazabilidad` | Escribir o actualizar documentación, citas y trazabilidad |
| `investigacion-proveedores-peru` | Buscar precios, stock y disponibilidad en tiendas peruanas |
