# ADR-0005 — Localización con mapa estático y AMCL

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Navegación · Reemplaza a: —

## Contexto

La demo se ejecuta en una arena conocida y repetible. Necesitamos una localización determinista, ligera y fácil de evaluar, que permita comparar ensayos y medir el error final. El entorno no cambia entre ejecuciones (salvo obstáculos añadidos a propósito).

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Determinismo | Veredicto |
|---|---|---|---|---|
| **AMCL + mapa estático** | Ligero, probado, repetible, fácil de medir | Requiere mapa y pose inicial; no se adapta a cambios | Alto | **Elegida** |
| SLAM Toolbox online | No requiere mapa; se adapta | Deriva; mapa no determinista; más CPU | Bajo | Solo para cartografiar |
| Cartographer | Robusto; loop closure | Complejo; más recursos | Medio | Descartada |
| GNSS + IMU | Global; ERC lo permite | No indoor; coste; precisión métrica | Medio | Futuro |
| VIO | Sin LiDAR | Luz, calibración, CPU | Bajo | Futuro |

## Decisión

Usar **AMCL** con un **mapa estático** generado desde `arena.json` mediante `scripts/docs/generate_arena.py`. La pose inicial se configura en los parámetros (`set_initial_pose: true`) para que la demo sea determinista y no dependa de un clic en RViz.

El mapa se genera con resolución 0.05 m/px, origen conocido y umbrales estándar (`occupied_thresh: 0.65`, `free_thresh: 0.196`).

## Consecuencias

### Positivas

- Localización reproducible y fácil de comparar entre ensayos.
- Bajo consumo de CPU.
- El mapa y el mundo están garantizados coherentes por construcción.
- No depende de que el operador haga clic en la pose inicial.

### Negativas

- Si la arena cambia, hay que regenerar el mapa.
- AMCL puede perderse si la pose inicial es incorrecta o el LiDAR es pobre.
- No hay adaptación a obstáculos permanentes nuevos (solo temporales, vía costmap).

### Neutrales

- SLAM Toolbox se puede usar fuera de línea para generar un mapa si se quiere una arena más realista.

## Mitigaciones

- Generar mapa y mundo desde la misma fuente.
- Validar que los waypoints están en zona libre.
- Añadir un procedimiento de re-localización manual.
- Registrar el error de localización en las pruebas.

## Criterios de revisión

- Si la arena es dinámica o desconocida.
- Si AMCL no converge en el 90% de los ensayos.
- Si se añade GNSS y se quiere fusión global.
- Si se necesita SLAM 3D.

## Referencias

- [F-07] Nav2 Quickstart (AMCL).
- [F-08] Parámetros de AMCL.
- [F-15] Nav2 setup (mapeo y localización).
- [`../interfaces.md`](../interfaces.md).
