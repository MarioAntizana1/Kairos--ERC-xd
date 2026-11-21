# Matriz de trazabilidad

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Cómo se lee

Cada fila enlaza un requisito con el componente de diseño que lo satisface, el caso de prueba que lo verifica y la evidencia que lo demuestra. Si falta una columna, el requisito **no está listo** para G4.

Estados de evidencia: `Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`.

## 2. Requisitos funcionales

| Requisito | Diseño / componente | Caso de prueba | Evidencia | Estado |
|---|---|---|---|---|
| RF-01 | `rover_mission/mission_planner.py`, `waypoints.py` | TC-01, TC-05 | [EV-2026-11-21-01](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md) | Ejecutada |
| RF-02 | `mission_node.py` + Nav2 `NavigateToPose` | TC-09, TC-10, TC-15 | Bag de misión | Pendiente |
| RF-03 | Nav2 costmaps + LiDAR + Navfn | TC-11 | Bag + vídeo | Pendiente |
| RF-04 | AMCL + mapa estático + TF | TC-07, TC-09, TC-16 | Bag + informe de error | Pendiente |
| RF-05 | `mission_node.py` (status/progress) | TC-08, TC-10 | [EV-2026-11-21-01](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md) (solo lógica de progreso) | Ejecutada |
| RF-06 | Servicios `start`/`abort`, cancelación de Nav2 | TC-13 | Bag + log | Pendiente |
| RF-07 | `scripts/evidence/record_bag.sh`, `summary.json` | TC-10, TC-19 | Carpeta de evidencia | Pendiente |
| RF-08 | `sim.launch.py`, `bringup.launch.py`, `nav2_params.yaml` | TC-06, TC-10, TC-19 | Evidencia sim + hw | Pendiente |
| RF-09 | RViz + CLI + runbook | TC-14, TC-19 | Vídeo + runbook | Pendiente |
| RF-10 | `scripts/demo/preflight.sh` | TC-14 | Log de preflight | Pendiente |
| RF-11 | `MissionPlanner.mark_failed` + `max_retries` | TC-03, TC-12 | [EV-2026-11-21-01](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md) (solo unitario) | Ejecutada |
| RF-12 | Waypoint `BASE` + lógica de retorno | TC-10 (opcional) | Bag | Pendiente |
| RF-13 | Nodo de batería (futuro) | TC-18 | Pendiente de hardware | Pendiente |

## 3. Requisitos no funcionales

| Requisito | Diseño / componente | Caso de prueba | Evidencia | Estado |
|---|---|---|---|---|
| RNF-01 | Pila Nav2 + mapa + calibración | TC-15 | CSV + informe | Pendiente |
| RNF-02 | AMCL + controlador + goal checker | TC-16 | CSV + medición | Pendiente |
| RNF-03 | `nav2_params.yaml`, `velocity_smoother` | TC-08, inspección | Bag + config | Pendiente |
| RNF-04 | E-stop hardware + watchdog | TC-17 | Vídeo + medición | Pendiente |
| RNF-05 | Launch + systemd (futuro) | TC-14 | Log de tiempos | Pendiente |
| RNF-06 | Pack 2S2P + BMS + cálculo energético (ver nota) | TC-18 | Prueba de descarga | Pendiente |
| RNF-07 | Pi 4 8 GB + Argon ONE + configuración | TC-20 | Logs de CPU/temperatura | Pendiente |
| RNF-08 | Scripts + documentación + versiones | TC-06, TC-14 | Evidencia de build | Pendiente |
| RNF-09 | Tests + lint + docs check | TC-01..05, lint | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) | Aprobada |
| RNF-10 | Fusibles + e-stop + BMS | TC-17, inspección | Checklist + foto | Pendiente |
| RNF-11 | `check_docs.py` + esta matriz | TC-21 | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) | Aprobada |
| RNF-12 | Separación launch sim/hw | TC-10, TC-19 | Evidencia comparada | Pendiente |
| RNF-13 | Publicación de estado a 2 Hz | TC-08 | Bag + timestamps | Pendiente |
| RNF-14 | Runbook + scripts idempotentes | TC-14 | Log de rearranque | Pendiente |

## 4. Cobertura

| Métrica | Valor | Objetivo |
|---|---|---|
| RF con prueba | 13/13 | 100% |
| RNF con prueba | 14/14 | 100% |
| RF con evidencia aprobada | 0/13 | 100% en G4 |
| RNF con evidencia aprobada | 0/14 | 100% en G4 |

> La columna “con prueba” cuenta la existencia del caso; la columna “con evidencia” cuenta la ejecución. No confundir una con otra.
>
> **RNF-06:** el dimensionado preliminar del pack 2S2P y el presupuesto
> energético están en
> [`docs/04-diseno/energia/calculo-energetico.md`](../04-diseno/energia/calculo-energetico.md).
> La autonomía real sigue `Pendiente` hasta ejecutar TC-18 con telemetría.

## 5. Mantenimiento

- Al añadir un requisito, añadir su fila y su caso de prueba.
- Al cambiar un requisito, actualizar el caso y marcar la evidencia anterior como `Obsoleta`.
- `scripts/docs/check_docs.py` verifica que todos los IDs definidos aparecen aquí y que los casos referenciados existen.
