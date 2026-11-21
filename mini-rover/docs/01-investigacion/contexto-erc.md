# Contexto del European Rover Challenge (ERC)

> Estado: Verificado con fuentes · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Investigación

## 1. Qué es el ERC

El **European Rover Challenge (ERC)** es una competición internacional universitaria de robótica espacial organizada por la European Space Foundation, con la AGH University of Krakow como coorganizadora. Los equipos diseñan, construyen y operan un rover inspirado en misiones planetarias reales de NASA y ESA sobre un **Marsyard** artificial: un terreno con cráteres, dunas, valles secos y materiales volcánicos, rediseñado cada año para representar una región distinta de Marte.

- Participación gratuita.
- Al menos el **75%** del equipo debe ser estudiantado, doctorando o egresado reciente.
- Se pueden combinar varias universidades y un mismo centro puede presentar varios equipos.
- Los finalistas reciben certificación **SpaceCert** si su contribución queda documentada y verificada.

Fuentes: [F-01], [F-02].

## 2. Edición 2026 (referencia más reciente)

| Dato | Valor | Fuente |
|---|---|---|
| Fechas | 4–6 de septiembre de 2026 | [F-01] |
| Sede | Cracovia, Polonia | [F-01] |
| Equipos finalistas | 25, seleccionados entre más de 120 candidaturas | [F-03] |
| Ganador | EPFL Xplore (Suiza) | [F-03] |
| Marsyard | Recreación de Hellas Planitia | [F-03] |
| Registro | 20 de febrero – 15 de marzo de 2026 | [F-02] |

> **Nota de triangulación:** una fuente secundaria ([F-04]) indica un calendario distinto (registro 1 de febrero – 2 de marzo). Se prioriza la web oficial del ERC ([F-02]) y se registra la discrepancia. Para 2027 hay que volver a comprobar las fechas.

## 3. Pruebas de la competición

| Prueba | Qué evalúa | Relevancia para el mini demo |
|---|---|---|
| **Navigation** | Traverse entre checkpoints + dron | **Alta**: es el núcleo del demo |
| **Probing** | Localizar y recoger sondas | Baja (requiere brazo) |
| **Maintenance** | Operar panel con manipulador | Baja (requiere brazo) |
| **Science** | Exploración, muestreo superficial y profundo | Baja (requiere instrumentos) |
| **Presentation** | Presentar el proyecto ante el jurado | **Alta**: se prepara desde ahora |
| **Astro-Bio** | Detección de signos de vida | Baja (fuera de alcance) |

Fuentes: [F-01], [F-03], [F-04].

### 3.1 Prueba de navegación en detalle

Según la descripción oficial de la prueba:

- **Traverse:** el rover debe alcanzar **cinco checkpoints**. Se permite GNSS.
- Se obtiene **puntuación extra si se hace de forma autónoma y sin realimentación de vídeo**.
- **Droning:** el equipo opera un dron (comercial o propio) siguiendo instrucciones de vuelo y captura dos fotos. Se permite GNSS y se valora la autonomía con MATLAB/Simulink.
- La organización describe la navegación como la capacidad de moverse de forma autónoma por un entorno marciano, detectar y evitar obstáculos y alcanzar puntos objetivo con precisión y fiabilidad.

Fuente: [F-01].

> **Lectura para el demo:** no necesitamos replicar el dron ni el GNSS. Necesitamos demostrar la base: waypoints, evitación de obstáculos, localización robusta, autonomía sin vídeo y telemetría. Eso es exactamente lo que un jurado valora como “autonomous operation”.

## 4. Qué significa “autónomo” aquí

El ERC no publica en su web una definición normativa cerrada de autonomía; el rulebook de cada edición sí detalla los criterios y penalizaciones. Para este proyecto se adopta una definición operativa conservadora:

| Nivel | Descripción | Uso en el demo |
|---|---|---|
| N0 | Teleoperado con vídeo | Solo para recuperación |
| N1 | Waypoints enviados por el operador, rover navega solo | **Objetivo mínimo** |
| N2 | Misión pregrabada, rover decide ruta y evita obstáculos | **Objetivo del demo** |
| N3 | Rover detecta objetivos y replanifica sin intervención | Futuro |

El demo se certifica internamente como **N2**: la lista de waypoints se carga antes de la misión, el rover planifica, evita obstáculos y no recibe comandos de movimiento durante la ejecución. El operador solo puede **abortar** o **pausar** por seguridad.

## 5. Implicaciones para el proyecto

| Implicación | Consecuencia en el diseño | Artefacto |
|---|---|---|
| La autonomía puntúa más | Misión pregrabada y ejecución sin teleoperación | RF-01, RF-02 |
| Hay obstáculos y terreno irregular | LiDAR 2D + costmaps + evitación | RF-03, RNF-04 |
| Se permiten cinco checkpoints | Misión de 5 waypoints con tolerancia | RF-02 |
| Se valora la fiabilidad | 10 ensayos y tasa de éxito ≥ 80% | RNF-01 |
| Hay límite de tiempo | Velocidad y planificación eficiente | RNF-03, RNF-05 |
| La presentación importa | Guion, vídeo, FAQ y evidencia | Fase 09 |
| El presupuesto es limitado | COTS, Pi 4 8 GB, LiDAR 2D | BOM |

## 6. Estado de la edición 2027

| Dato | Estado | Acción |
|---|---|---|
| Fechas | **No publicadas** a 2026-11-21 | Revisar mensualmente [F-01], [F-02] |
| Reglamento | No publicado | Descargar y archivar cuando salga |
| Categorías | Por confirmar | Preguntar al Team Coordinator |
| Registro | Se estima febrero–marzo, según patrón 2026 | **Supuesto**, no fecha oficial |

Fuentes secundarias confirman que hay equipos preparando el ERC 2027 ([F-05], [F-16]), lo que respalda que la edición existirá, pero no aporta fechas oficiales.

## 7. Preguntas abiertas

| ID | Pregunta | Impacto | Cómo resolverla |
|---|---|---|---|
| Q-ERC-01 | ¿Dimensiones y peso máximos del rover? | Alto | Descargar rulebook 2026 y 2027 |
| Q-ERC-02 | ¿Tiempo máximo de la prueba de navegación? | Alto | Rulebook |
| Q-ERC-03 | ¿Qué se considera exactamente “autónomo” y qué penaliza? | Alto | Rulebook + preguntas al coordinador |
| Q-ERC-04 | ¿Restricciones de comunicaciones y bandas? | Medio | Rulebook |
| Q-ERC-05 | ¿Categoría on-site o remote para 2027? | Alto | Web oficial |
| Q-ERC-06 | ¿Se permite GNSS en todas las subtareas? | Medio | Rulebook |

> **No inventes respuestas.** Mientras estas preguntas estén abiertas, el diseño debe ser conservador y modular.

## 8. Fuentes de este documento

- [F-01] European Rover Challenge — Space & Robotics Competition.
- [F-02] European Rover Challenge — Competitor Zone.
- [F-03] European Rover Challenge — The EPFL Xplore team wins ERC 2026.
- [F-04] Olympus Mars — ERC tasks and timeline (secundaria).
- [F-05] SpaceJobs.Now — Student space competitions 2027 (secundaria).
- [F-16] Aalto Space Association — ERC 2027 Team (secundaria).

Detalle, URL y fecha de acceso en [`fuentes.md`](fuentes.md).
