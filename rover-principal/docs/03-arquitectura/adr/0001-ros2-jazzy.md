# ADR-0001 — Usar ROS 2 Jazzy Jalisco

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Tech Lead · Reemplaza a: —

## Contexto

Necesitamos un middleware robótico con soporte a largo plazo, ecosistema de navegación maduro y compatibilidad con Raspberry Pi 5 (arm64) y Ubuntu 24.04. El proyecto arranca en noviembre de 2026 y el objetivo deportivo es el ERC 2027.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Soporte | Veredicto |
|---|---|---|---|---|
| **ROS 2 Jazzy** | LTS hasta mayo 2029; Ubuntu 24.04 Tier 1 arm64/amd64; Nav2 y Gazebo Harmonic maduros; muchos tutoriales | No es la versión más nueva; migración futura | Hasta 2029 | **Elegida** |
| ROS 2 Humble | Muy usado; Ubuntu 22.04 | Fin de soporte mayo 2027; Pi 5 requiere Ubuntu 23.10+; combinación incómoda | Hasta 2027 | Descartada |
| ROS 2 Lyrical | LTS hasta 2031; Ubuntu 26.04; Gazebo Jetty | Ecosistema más joven; menos tutoriales de Nav2; cambio de versión de Gazebo | Hasta 2031 | Evaluar en OQ-05 |
| ROS 1 Noetic | Legado | EOL; sin soporte moderno | EOL | Descartada |

## Decisión

Usar **ROS 2 Jazzy Jalisco** sobre **Ubuntu 24.04 LTS** (arm64 en Raspberry Pi 5, amd64 en el PC de desarrollo).

## Consecuencias

### Positivas

- Soporte hasta mayo de 2029, suficiente para el ERC 2027 y el ciclo siguiente.
- Binarios oficiales para arm64; no hay que compilar ROS desde fuente en el Pi.
- Nav2 Jazzy y Gazebo Harmonic están soportados y documentados.
- La mayoría de tutoriales y paquetes de la comunidad funcionan.

### Negativas

- Si el proyecto se alarga más allá de 2029, habrá que migrar.
- No se aprovechan las mejoras de Lyrical (Ubuntu 26.04, Gazebo Jetty).
- Algunas dependencias nuevas pueden priorizar Lyrical y no tener binarios para Jazzy.

### Neutrales

- El código de la misión es independiente de la distro; la migración se limita a dependencias y launch.

## Criterios de revisión

- Si una dependencia crítica no tiene binarios para Jazzy.
- Si el proyecto se extiende más allá de 2029.
- Si Lyrical alcanza madurez suficiente y el equipo decide migrar.
- Revisión obligatoria en OQ-05 antes de G2.

## Referencias

- [F-06] ROS 2 Jazzy Installation.
- [F-12] REP 2000.
- [F-14] Open Robotics — Jazzy released (LTS hasta mayo 2029).
- [F-09] Gazebo + ROS compatibility.
