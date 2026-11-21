# Historias de usuario

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto

## 1. Formato

> Como **<rol>**, quiero **<capacidad>** para **<beneficio>**.
>
> **Criterios de aceptación:** Given/When/Then.
>
> **Requisitos:** RF/RNF asociados. **Prioridad:** MoSCoW.

## 2. Historias

### US-01 — Operador lanza una misión pregrabada

**Como** operador del rover, **quiero** lanzar una misión de waypoints pregrabada **para** demostrar navegación autónoma sin teleoperar.

**Criterios de aceptación**

- Dado un YAML válido con 5 waypoints, cuando ejecuto el comando de misión, entonces el rover inicia la navegación y publica `RUNNING`.
- Dado que la misión termina, cuando llega al último waypoint, entonces el estado es `COMPLETED` y el progreso es 1.0.
- Dado un YAML inválido, cuando intento lanzar, entonces recibo un error claro y el rover no se mueve.

**Requisitos:** RF-01, RF-02, RF-09. **Prioridad:** Must.

### US-02 — Operador aborta por seguridad

**Como** operador, **quiero** abortar la misión de inmediato **para** evitar un accidente.

**Criterios de aceptación**

- Dado que la misión está en curso, cuando pulso la e-stop, entonces la potencia de motores se corta y el rover se detiene.
- Dado que la misión está en curso, cuando ejecuto el comando de aborto, entonces se cancela el objetivo de Nav2 y el estado pasa a `ABORTED`.
- Dado un aborto, cuando reviso la evidencia, entonces encuentro el motivo y el waypoint en curso.

**Requisitos:** RF-06, RNF-04. **Prioridad:** Must.

### US-03 — Jurado ve evidencia reproducible

**Como** miembro del jurado, **quiero** ver datos y artefactos verificables **para** confiar en los resultados.

**Criterios de aceptación**

- Dada una misión, cuando se ejecuta, entonces se genera un bag y un resumen con métricas.
- Dado el registro de evidencias, cuando abro una entrada, entonces veo fecha, commit, comando y hashes.
- Dado el runbook, cuando lo sigue otra persona, entonces puede repetir la demo.

**Requisitos:** RF-07, RNF-08, RNF-11. **Prioridad:** Must.

### US-04 — Desarrollador prueba sin hardware

**Como** desarrollador, **quiero** ejecutar la pila en simulación **para** iterar sin riesgo y sin esperar al robot.

**Criterios de aceptación**

- Dado Ubuntu 24.04 + ROS 2 Jazzy, cuando ejecuto el launch de simulación, entonces Gazebo, Nav2 y RViz arrancan.
- Dada la misma misión, cuando la ejecuto en simulación, entonces se comporta igual que en hardware salvo drivers y tiempos.

**Requisitos:** RF-08, RNF-08. **Prioridad:** Must.

### US-05 — Rover evita un obstáculo

**Como** operador, **quiero** que el rover rodee obstáculos **para** no depender de una pista perfectamente despejada.

**Criterios de aceptación**

- Dado un obstáculo entre dos waypoints, cuando el rover navega, entonces lo evita y llega al objetivo.
- Dado el bag, cuando lo reviso, entonces la distancia mínima al obstáculo es mayor que el radio del robot.

**Requisitos:** RF-03, RNF-04. **Prioridad:** Must.

### US-06 — Técnico calibra y comprueba el sistema

**Como** técnico, **quiero** un preflight automatizado **para** detectar fallos antes de mover el rover.

**Criterios de aceptación**

- Dado el sistema encendido, cuando ejecuto el preflight, entonces comprueba nodos, TF, topics, disco y batería.
- Dado un fallo crítico, cuando el preflight termina, entonces devuelve código ≠ 0 y explica qué falta.
- Dado un preflight correcto, cuando termina, entonces guarda un log en la evidencia.

**Requisitos:** RF-10, RNF-05. **Prioridad:** Should.

### US-07 — Equipo compara simulación y realidad

**Como** ingeniero de pruebas, **quiero** comparar métricas de simulación y hardware **para** entender la brecha y priorizar mejoras.

**Criterios de aceptación**

- Dadas 10 ejecuciones en cada entorno, cuando analizo el CSV, entonces obtengo tasa de éxito, error medio y tiempo.
- Dado el informe, cuando lo leo, entonces veo la diferencia en puntos porcentuales y sus posibles causas.

**Requisitos:** RNF-01, RNF-02, RNF-12. **Prioridad:** Should.

### US-08 — Equipo presenta el proyecto

**Como** equipo, **quiero** un guion y una demo ensayada **para** comunicar el valor técnico al jurado.

**Criterios de aceptación**

- Dado el guion de 10 minutos, cuando lo ensayo, entonces cabe en el tiempo y cubre problema, solución, evidencia y lecciones.
- Dado el vídeo, cuando lo ve alguien externo, entonces entiende qué hace el rover y por qué es relevante.
- Dado el FAQ, cuando el jurado pregunta, entonces tenemos una respuesta fundamentada.

**Requisitos:** RF-09, RNF-11. **Prioridad:** Should.

## 3. Mapa historia → requisito

| Historia | RF | RNF |
|---|---|---|
| US-01 | RF-01, RF-02, RF-09 | RNF-08 |
| US-02 | RF-06 | RNF-04, RNF-10 |
| US-03 | RF-07 | RNF-08, RNF-11 |
| US-04 | RF-08 | RNF-08, RNF-09 |
| US-05 | RF-03 | RNF-02, RNF-04 |
| US-06 | RF-10 | RNF-05 |
| US-07 | RF-08 | RNF-01, RNF-02, RNF-12 |
| US-08 | RF-09 | RNF-11 |
