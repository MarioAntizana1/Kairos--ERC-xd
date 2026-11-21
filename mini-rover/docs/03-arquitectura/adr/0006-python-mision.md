# ADR-0006 — Nodo de misión en Python sobre `NavigateToPose`

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Software · Reemplaza a: —

## Contexto

Necesitamos orquestar una secuencia de waypoints, gestionar reintentos, timeouts, aborto, telemetría y resumen. Nav2 ya ofrece un `waypoint_follower`, pero su lógica de reintentos y estados es limitada para nuestras necesidades y difícil de testear sin ROS.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Testabilidad | Veredicto |
|---|---|---|---|---|
| **Nodo Python + `NavigateToPose`** | Simple, legible, acción estándar, lógica pura testeable | No tiempo real; GIL | Alta | **Elegida** |
| Nodo C++ | Rendimiento | Más código, más tiempo | Media | Descartada para el demo |
| `nav2_waypoint_follower` | Ya existe | Poca personalización de estados/reintentos | Baja | Descartada |
| Árbol de comportamiento XML | Potente, visual | Curva alta; difícil de testear | Media | Futuro |

## Decisión

Implementar un **nodo Python fino** (`mission_node.py`) que:

- Carga y valida los waypoints con lógica pura (`mission_planner.py`).
- Envía cada waypoint con `NavigateToPose`.
- Gestiona timeout, reintentos, aborto y pausa.
- Publica estado y progreso.
- Genera un resumen de misión.

La lógica de dominio no importa `rclpy`; así se prueba con `unittest` sin ROS.

## Consecuencias

### Positivas

- Fácil de leer, mantener y probar.
- La lógica de estados se testea sin simulador.
- La interfaz con Nav2 es estable y reemplazable.
- Permite evolucionar a un árbol de comportamiento sin reescribir todo.

### Negativas

- Python no es adecuado para control de alta frecuencia (no es su trabajo; Nav2 controla a 10–20 Hz).
- El GIL puede afectar si se añaden muchos hilos; se usa un solo executor.
- La gestión de timeouts con `rclpy` requiere cuidado.

### Neutrales

- El `waypoint_follower` de Nav2 sigue disponible para pruebas comparativas.

## Mitigaciones

- Mantener el nodo en 2 Hz; el control lo hace Nav2.
- Usar `MultiThreadedExecutor` solo si es necesario.
- Tests unitarios de la máquina de estados.
- Timeouts configurables y logs claros.

## Criterios de revisión

- Si la misión se vuelve muy compleja (ramas, condiciones, recuperación).
- Si se necesita tiempo real o latencia < 10 ms.
- Si se integra un brazo o ciencia con secuencias complejas.

## Referencias

- [`../../04-diseno/diseno-software.md`](../../04-diseno/diseno-software.md).
- [F-08] Nav2 params (acción `navigate_to_pose`).
- Código: `ros_ws/src/rover_mission/`.
