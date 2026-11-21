# Matriz de trazabilidad de pruebas

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Caso → requisito

| Caso | Requisitos | Nivel | Estado | Evidencia |
|---|---|---|---|---|
| TC-01 | RF-01 | Unitario | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |
| TC-02 | RF-02, RF-06 | Unitario | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |
| TC-03 | RF-11 | Unitario | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |
| TC-04 | RF-05 | Unitario | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |
| TC-05 | RF-01 | Unitario | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |
| TC-06 | RF-08, RNF-08 | Integración | Pendiente | — |
| TC-07 | RF-04 | Integración | Pendiente | — |
| TC-08 | RF-05, RNF-03, RNF-13 | Integración | Pendiente | — |
| TC-09 | RF-02, RF-04 | Integración | Pendiente | — |
| TC-10 | RF-02, RF-07 | Sistema | Pendiente | — |
| TC-11 | RF-03 | Sistema | Pendiente | — |
| TC-12 | RF-11 | Sistema | Pendiente | — |
| TC-13 | RF-06 | Sistema | Pendiente | — |
| TC-14 | RF-09, RF-10, RNF-05, RNF-08 | Sistema | Pendiente | — |
| TC-15 | RNF-01 | Sistema | Pendiente | — |
| TC-16 | RNF-02 | Sistema | Pendiente | — |
| TC-17 | RNF-04, RNF-10 | Hardware | Pendiente | — |
| TC-18 | RF-13, RNF-06 | Hardware | Pendiente | — |
| TC-19 | RF-09, RNF-12 | Aceptación | Pendiente | — |
| TC-20 | RNF-07 | Análisis | Pendiente | — |
| TC-21 | RNF-11 | Documentación | Aprobado | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |

## 2. Requisito → caso

| Requisito | Casos | Cobertura |
|---|---|---|
| RF-01 | TC-01, TC-05 | Completa |
| RF-02 | TC-02, TC-09, TC-10 | Completa |
| RF-03 | TC-11 | Completa |
| RF-04 | TC-07, TC-09 | Completa |
| RF-05 | TC-04, TC-08 | Completa |
| RF-06 | TC-02, TC-13 | Completa |
| RF-07 | TC-10 | Completa |
| RF-08 | TC-06 | Completa |
| RF-09 | TC-14, TC-19 | Completa |
| RF-10 | TC-14 | Completa |
| RF-11 | TC-03, TC-12 | Completa |
| RF-12 | TC-10 (opcional) | Parcial |
| RF-13 | TC-18 | Completa |
| RNF-01 | TC-15 | Completa |
| RNF-02 | TC-16 | Completa |
| RNF-03 | TC-08 | Completa |
| RNF-04 | TC-17 | Completa |
| RNF-05 | TC-14 | Completa |
| RNF-06 | TC-18 | Completa |
| RNF-07 | TC-20 | Completa |
| RNF-08 | TC-06, TC-14 | Completa |
| RNF-09 | TC-01..05 + lint | Completa |
| RNF-10 | TC-17 | Completa |
| RNF-11 | TC-21 | Completa |
| RNF-12 | TC-19 | Completa |
| RNF-13 | TC-08 | Completa |
| RNF-14 | TC-14 | Completa |

## 3. Resultados por campaña

| Campaña | Fecha | Entorno | Casos | Aprobados | Fallidos | Evidencia |
|---|---|---|---|---|---|---|
| Validación local | 2026-11-21 | Fedora 43, sin ROS | TC-01..05, TC-21 | 6 | 0 | [EV-2026-11-21-01](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md) |
| Validación final pre-runtime | 2026-11-21 | Fedora 43, sin ROS | TC-01..05, TC-21 | 6 | 0 | [EV-2026-11-21-03](../08-evidencia/artefactos/2026-11-21T123448-validacion-final-pre-runtime/README.md) |
| Integración final (mini demo + 6×6) | 2026-11-21 | Fedora 43, sin ROS | TC-01..05, TC-21 | 6 | 0 | [EV-2026-11-21-04](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md) |

> La evidencia [EV-2026-11-21-02](../08-evidencia/artefactos/2026-11-21T123309-validacion-estatica-urdf/README.md) valida estáticamente el URDF, el lint y el modelo energético; no cuenta como caso de prueba de navegación.

## 4. Defectos abiertos

| ID | Título | Severidad | Caso | Estado |
|---|---|---|---|---|
| — | — | — | — | — |

## 5. Notas

- RF-12 es `Could`; su cobertura es parcial y no bloquea G4.
- RNF-09 se verifica con la suite unitaria y el lint; no tiene un TC único.
- Los casos de hardware (TC-17, TC-18, TC-20) requieren el rover montado.
- La evidencia se enlaza cuando se ejecuta, no cuando se planifica.
