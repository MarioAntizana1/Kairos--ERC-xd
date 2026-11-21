# Matriz de trazabilidad de pruebas

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
>
> Todos los resultados están **Pendientes**. La columna `Evidencia` se llena
> cuando exista una carpeta sellada.

| Caso | Nombre | Requisitos | Resultado | Evidencia |
|---|---|---|---|---|
| TC-01 | Detección y captura dual | RF-01, RNF-05 | Pendiente | — |
| TC-02 | Timestamps y sincronización | RF-01, RF-12, RNF-10 | Pendiente | — |
| TC-03 | Calibración intrínseca | RF-07, RNF-09 | Pendiente | — |
| TC-04 | Calibración estéreo y baseline | RF-07, RNF-09 | Pendiente | — |
| TC-05 | Rectificación y disparidad | RF-02, RNF-05 | Pendiente | — |
| TC-06 | Exactitud de profundidad | RF-02, RNF-03, RNF-04 | Pendiente | — |
| TC-07 | ToF de piso: altitud y referencia | RF-04, RF-10, RNF-03 | Pendiente | — |
| TC-08 | Nube de puntos y exportación | RF-03, RF-08 | Pendiente | — |
| TC-09 | Detección de obstáculos y latencia | RF-05, RNF-06 | Pendiente | — |
| TC-10 | Registro, apagado y recuperación | RF-06, RF-11, RNF-08, RNF-14 | Pendiente | — |
| TC-11 | Térmica y potencia | RNF-02, RNF-07 | Pendiente | — |
| TC-12 | Vibración y estabilidad | RNF-01, RNF-09, RF-02 | Pendiente | — |
| TC-13 | Interferencia WiFi/BT | RNF-11 | Pendiente | — |
| TC-14 | Vuelo cautivo end-to-end | RF-03, RF-05, RF-09, RNF-14 | Pendiente | — |
| TC-15 | Auditoría de BOM y reproducibilidad | RNF-12, RNF-13 | Pendiente | — |

## Cobertura por requisito

| Requisito | Casos |
|---|---|
| RF-01 | TC-01, TC-02 |
| RF-02 | TC-05, TC-06, TC-12 |
| RF-03 | TC-08, TC-14 |
| RF-04 | TC-07 |
| RF-05 | TC-09, TC-14 |
| RF-06 | TC-10 |
| RF-07 | TC-03, TC-04 |
| RF-08 | TC-08 |
| RF-09 | TC-14 |
| RF-10 | TC-07 |
| RF-11 | TC-10 |
| RF-12 | TC-02 |
| RNF-01 | TC-12 |
| RNF-02 | TC-11 |
| RNF-03 | TC-06, TC-07 |
| RNF-04 | TC-06 |
| RNF-05 | TC-01, TC-05 |
| RNF-06 | TC-09 |
| RNF-07 | TC-11 |
| RNF-08 | TC-10 |
| RNF-09 | TC-03, TC-04, TC-12 |
| RNF-10 | TC-02 |
| RNF-11 | TC-13 |
| RNF-12 | TC-15 |
| RNF-13 | TC-15 |
| RNF-14 | TC-10, TC-14 |

## Estados

| Estado | Significado |
|---|---|
| Pendiente | No ejecutado |
| Ejecutada | Ejecutado, sin revisar |
| Aprobada | Cumple el criterio |
| Fallida | No cumple |
| Obsoleta | Reemplazado por otra versión |
