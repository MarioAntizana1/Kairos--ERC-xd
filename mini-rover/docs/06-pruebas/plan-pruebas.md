# Plan de pruebas

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Objetivo

Demostrar, con evidencia reproducible, que el rover cumple los requisitos funcionales y no funcionales definidos, y que la demo es segura y repetible.

## 2. Alcance

| Incluido | Excluido |
|---|---|
| Lógica de misión (unitarias) | Brazo, ciencia, dron |
| Integración ROS 2 + Nav2 + Gazebo | Operación BVLOS |
| Misión nominal y con obstáculos | Terreno extremo |
| Aborto y reintentos | Múltiples robots |
| E-stop y batería (hardware) | Certificación normativa |
| Rendimiento en Pi 4 8 GB | Estrés de 24 h |

## 3. Niveles

| Nivel | Qué verifica | Entorno | Responsable |
|---|---|---|---|
| Unitario | Validación, estados, reintentos, progreso | Host con Python | Software |
| Integración | Launch, TF, topics, goal simple | Ubuntu + ROS 2 + Gazebo | Software/QA |
| Sistema | Misión completa, evitación, aborto | Simulación y hardware | QA |
| Aceptación | Demo de 10 min y runbook | Pista | PO/QA |
| Regresión | Todo lo anterior tras cambios | Ambos | QA |

## 4. Entornos

| Entorno | Versión | Uso |
|---|---|---|
| E-A | Fedora 43, Python 3.14, sin ROS | Tests unitarios y docs |
| E-B | Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic | Integración y sistema sim |
| E-C | Raspberry Pi 4 8 GB + rover físico | Sistema y aceptación |
| E-D | Pista de 8 × 6 m | Aceptación y demo |

## 5. Criterios de entrada

- Código compila en E-B.
- `make check` pasa en E-A.
- Assets (mundo/mapa) generados y coherentes.
- Hardware montado, calibrado y con e-stop probada (E-C).
- Runbook disponible (E-D).

## 6. Criterios de salida

- 100% de casos Must ejecutados.
- ≥ 80% de éxito en TC-15.
- Error final ≤ 0.30 m en TC-16.
- E-stop verificada en TC-17.
- Sin defectos críticos abiertos.
- Evidencia sellada para cada caso.
- Trazabilidad actualizada.

## 7. Estrategia

1. **Unitarias primero:** validar la lógica sin ROS.
2. **Integración por capas:** launch → TF → topics → goal simple → misión.
3. **Sistema en simulación:** 10 repeticiones.
4. **Hardware:** calibración, luego misión.
5. **Aceptación:** ensayo general con el guion.
6. **Regresión:** tras cada cambio relevante.

## 8. Datos y métricas

| Métrica | Herramienta | Umbral |
|---|---|---|
| Éxito de misión | Logs + CSV | ≥ 80% |
| Error final | Gazebo / cinta métrica | ≤ 0.30 m |
| Tiempo | Cronómetro / logs | ≤ 10 min |
| Colisiones | Observación + bag | 0 |
| CPU/RAM/Temperatura | `psutil`, `top`, `vcgencmd` | CPU < 80%, T < 80 °C |
| Latencia de estado | Timestamps | ≤ 1 s |

## 9. Gestión de defectos

| Severidad | Definición | Acción |
|---|---|---|
| Crítico | Riesgo para personas, pérdida de control, corrupción de datos | Bloquea pruebas; corregir ya |
| Alto | Misión imposible, fallo reproducible | Corregir antes de G4 |
| Medio | Fallo intermitente, degradación | Corregir o documentar |
| Bajo | Cosmético, log, documentación | Backlog |

Cada defecto se registra con: ID, título, pasos, esperado, obtenido, entorno, evidencia, severidad, estado.

## 10. Riesgos de las pruebas

| Riesgo | Mitigación |
|---|---|
| Batería baja durante el ensayo | Cargar al 100%, registrar voltaje |
| Superficie irregular | Barrer y marcar la pista |
| Operador distinto | Mismo operador en la campaña |
| Simulación no representa la realidad | Documentar la brecha |
| Tiempo insuficiente | Priorizar Must |
| Pérdida de evidencia | Guardar bag y logs al terminar cada ensayo |

## 11. Calendario

| Fase | Semana | Entregable |
|---|---|---|
| Unitarias | T1 | TC-01..05 |
| Integración sim | T2 | TC-06..09 |
| Sistema sim | T3–T4 | TC-10..13, TC-20 |
| Hardware | T5–T6 | TC-14..18 |
| Aceptación | T7 | TC-19, TC-21 |
| Regresión | T8 | Reejecución |

Las semanas son relativas; se ajustan al calendario real.

## 12. Herramientas

- `unittest` (unitarias).
- `ros2 launch`, `ros2 topic`, `ros2 action`, `tf2_echo`.
- `rosbag2`.
- `psutil`, `top`, `vcgencmd`.
- `scripts/analysis/analyze_runs.py`.
- `scripts/docs/check_docs.py`.

## 13. Roles

| Actividad | Responsable | Aprueba |
|---|---|---|
| Ejecutar unitarias | Software | QA |
| Ejecutar integración | Software | QA |
| Ejecutar sistema | QA | Tech Lead |
| E-stop | Seguridad | PO |
| Aceptación | QA | PO |

## 14. Documentos relacionados

- [`casos-prueba.md`](casos-prueba.md).
- [`protocolo-experimentos.md`](protocolo-experimentos.md).
- [`matriz-trazabilidad-pruebas.md`](matriz-trazabilidad-pruebas.md).
- [`../08-evidencia/README.md`](../08-evidencia/README.md).
