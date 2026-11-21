# FAQ para el jurado

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Comunicación
> Regla: si no hay dato, se dice “no lo hemos medido todavía”.

## 1. Sobre el proyecto

**¿Qué habéis construido?**
Un rover mini demo de navegación autónoma: carga una misión de 5 waypoints, se localiza con AMCL, planifica con Nav2, evita obstáculos con LiDAR y registra evidencia. Es la base del rover completo del ERC 2027.

**¿Es el rover del ERC?**
No. Es un producto mínimo verificable. El rover grande añadirá brazo, ciencia, perforación y dron. Este demo valida la pila de navegación y seguridad.

**¿Por qué no habéis hecho el rover completo?**
Por gestión de riesgo: un sistema grande de golpe no se puede medir ni depurar. Preferimos validar la base, demostrarla y escalar.

**¿Qué tiene de innovador?**
No la tecnología por sí sola, sino la combinación: bajo coste, estándares abiertos, seguridad por diseño y evidencia reproducible. Cualquiera puede repetir la demo.

## 2. Sobre la autonomía

**¿Qué significa “autónomo” aquí?**
Nivel N2: la misión se carga antes; el rover planifica, navega y evita obstáculos sin recibir comandos de movimiento. El operador solo puede pausar o abortar.

**¿Usáis vídeo para teleoperar?**
No durante la misión. El vídeo es para observar y para la presentación.

**¿Qué pasa si se pierde la localización?**
AMCL deja de publicar `map → odom` de forma fiable; Nav2 falla y el nodo de misión aborta. Está documentado como fallo y se prueba en TC-13/TC-16.

**¿Qué pasa si hay un obstáculo nuevo?**
El costmap local lo detecta con el LiDAR y el controlador lo evita. Si bloquea completamente la ruta, se activa la recuperación de Nav2 o falla el waypoint.

**¿Habéis probado en terreno real?**
Todavía no. La validación en hardware es la siguiente fase (TC-17 a TC-20). No presentamos resultados de hardware que no existan.

## 3. Sobre la tecnología

**¿Por qué ROS 2 Jazzy?**
LTS hasta 2029, Ubuntu 24.04 Tier 1 en arm64, Nav2 y Gazebo Harmonic maduros. Ver ADR-0001.

**¿Por qué Nav2 y no un stack propio?**
Nav2 es el estándar, está probado y ofrece localización, planificación, control y recuperación. Un stack propio habría consumido el tiempo del equipo. Ver ADR-0003.

**¿Por qué Raspberry Pi 5?**
Suficiente para Nav2 y LiDAR, barato, bajo consumo y con binarios arm64. Ver ADR-0002.

**¿Por qué AMCL y no SLAM?**
La arena es conocida y repetible; AMCL es determinista y ligero. SLAM se usa para cartografiar. Ver ADR-0005.

**¿Por qué RPP y no MPPI?**
RPP es más ligero y predecible en un rover diferencial; MPPI es pesado para el Pi. Se puede comparar en E4.

**¿Qué simulador usáis?**
Gazebo Harmonic con `ros_gz`, la combinación soportada con Jazzy. Ver ADR-0004.

**¿Cómo garantizáis que el mapa coincide con el mundo?**
Ambos se generan desde `arena.json` con un script determinista. `make assets-check` lo verifica.

## 4. Sobre seguridad

**¿Qué pasa si el software se cuelga?**
La e-stop corta la potencia de motores. Además, el watchdog de hardware está especificado para cortar si el Pi no late. El watchdog de software para el driver si no llega `/cmd_vel`.

**¿La e-stop es real o simulada?**
En hardware es un pulsador normalmente cerrado en serie con la alimentación del driver. En simulación se prueba el aborto por software. La e-stop física se valida en TC-17.

**¿Qué velocidad máxima tenéis?**
0.45 m/s en operación normal; 0.30 m/s con público. Está en RNF-03.

**¿Cómo evitáis atropellar a alguien?**
Zona delimitada, observador con e-stop, velocidad limitada, visión directa y parada inmediata. No hay detección de personas en esta fase.

**¿Habéis hecho un FMEA?**
Sí, preliminar, en `docs/03-arquitectura/seguridad.md`. No sustituye a una evaluación formal.

## 5. Sobre evidencia y métricas

**¿Cómo sabemos que funciona?**
Con 10 ensayos, bag, CSV, informe y hash. La tasa de éxito y el error final se miden con un protocolo. Mientras no haya evidencia, el estado es “pendiente”.

**¿Cuál es la tasa de éxito?**
El objetivo es ≥ 80%. El resultado real se publicará en `docs/06-pruebas/resultados/` cuando se ejecute. No damos una cifra inventada.

**¿Qué es el error final?**
La distancia 2D entre la pose final y el waypoint objetivo. Objetivo: ≤ 0.30 m de media.

**¿Cómo evitáis el sesgo?**
Mismo operador, misma pista, mismo commit, 10 repeticiones, se reportan todos los ensayos, incluidos los fallidos.

**¿Por qué 10 ensayos?**
Es una estimación exploratoria viable para un equipo pequeño. Con 8/10, el intervalo de Wilson al 95% es aproximadamente [49%, 94%]; lo reportamos con esa incertidumbre.

## 6. Sobre el ERC y el futuro

**¿Vais a competir en el ERC 2027?**
El objetivo es preparar la base para el rover completo y evaluar la participación. Las fechas de 2027 no están publicadas; el registro se estima entre febrero y marzo, según el patrón de 2026.

**¿Qué prueba del ERC replica este demo?**
La subtarea **Traverse** de Navigation: cinco checkpoints, autonomía y evitación. No incluye dron ni GNSS.

**¿Qué falta para el rover completo?**
Brazo, ciencia, perforación, dron, gestión energética, carcasa, calibración fina y validación en el Marsyard.

**¿Cómo escaláis el software?**
La misión y Nav2 son modulares; el brazo y la ciencia se añaden como paquetes ROS 2. La evidencia y el método se mantienen.

**¿Cuál es el mayor riesgo?**
La integración en hardware y la brecha sim-real. Por eso priorizamos la validación temprana y la seguridad.

## 7. Preguntas incómodas

**¿No es solo un TurtleBot con otro nombre?**
La pila es estándar, pero el diseño, la arena, la misión, la seguridad y la evidencia son propios. No pretendemos inventar Nav2; pretendemos aplicarlo con rigor.

**¿Qué pasa si no funciona en la demo?**
Tenemos un vídeo pregrabado, bags y métricas. La demo en vivo es una demostración, no la única prueba.

**¿Por qué deberíamos financiaros?**
Porque el demo reduce el riesgo del rover grande, genera evidencia y forma al equipo en el ciclo completo. El retorno es un sistema validado, documentación y visibilidad.

**¿Qué habéis aprendido?**
Que la autonomía no es solo el algoritmo: es seguridad, calibración, evidencia y operación. Y que documentar a tiempo ahorra retrabajo.
