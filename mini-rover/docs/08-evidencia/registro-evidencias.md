# Registro de evidencias

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

| ID | Fecha | Tipo | Requisitos | Casos | Resultado | Ruta | Hash | Estado |
|---|---|---|---|---|---|---|---|---|
| EV-2026-11-21-01 | 2026-11-21 | docs/tests | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T123009-validacion-local/README.md` | `bcec912b938625108291b7cc7684074a7d6fa87bc3505b6601cd2e6d508724c3` | Aprobada |
| EV-2026-11-21-02 | 2026-11-21 | static/lint | RNF-09 | Soporte | Aprobada con limitación | `artefactos/2026-11-21T123309-validacion-estatica-urdf/README.md` | `4662cff7b37d59904bba3537f9570b1f64dca281db3c1494b49800141fe45fc9` | Aprobada |
| EV-2026-11-21-03 | 2026-11-21 | final/static | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T123448-validacion-final-pre-runtime/README.md` | `2b7b07c64af7edaccc954f28a57edf195b99466a358cd90927981b725e65af3f` | Aprobada |
| EV-2026-11-21-04 | 2026-11-21 | final/integration | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T123636-integracion-final/README.md` | `ce4c99496374ae241ee969a2100fd06de952762736b052d397c3b7e6c6448271` | Aprobada |
| EV-2026-11-21-05 | 2026-11-21 | docs/inventory | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T171912-inventario-facultad/README.md` | `f87c5b41f9bf608364dbadc188e0d7990b7e37b0e24bd54c3e67a1a13613f84e` | Aprobada |
| EV-2026-11-21-06 | 2026-11-21 | docs/design-change | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T180549-cambio-pi4-camera-lte/README.md` | `716aa12fb137bc7b7d428fee00e9343d0223a4a3ffbb3120f5419b7361c9b813` | Aprobada |
| EV-2026-11-21-07 | 2026-11-21 | docs/bom-pen | RNF-09, RNF-11 | TC-01..05, TC-21 | Aprobada con limitación | `artefactos/2026-11-21T183000-bom-pen/README.md` | `b8eb4219c41c1c7ef87cde78b1bc6955da6de7be00d5fa037121e5070166c912` | Aprobada |

## Cómo añadir una entrada

1. Ejecutar `bash scripts/evidence/new_evidence.sh "<slug>"`.
2. Copiar la ruta devuelta.
3. Ejecutar la prueba o el comando.
4. Guardar logs y media.
5. Ejecutar `bash scripts/evidence/seal_evidence.sh "<ruta>"`.
6. Copiar el hash del `MANIFEST.sha256`.
7. Añadir la fila a esta tabla.
8. Enlazar desde la matriz de trazabilidad.

## Convención de ID

`EV-YYYY-MM-DD-NN`, donde `NN` es secuencial por día.

## Estados

| Estado | Significado |
|---|---|
| Pendiente | Carpeta creada, sin ejecutar |
| Ejecutada | Comando ejecutado, sin revisar |
| Aprobada | Revisada y aceptada |
| Fallida | El resultado no cumple el criterio |
| Obsoleta | Reemplazada por otra evidencia |

## Evidencias actuales

| ID | Descripción | Conclusión |
|---|---|---|
| EV-2026-11-21-01 | Validación local de documentación, assets y tests unitarios | Aprobada con limitación: runtime ROS 2 pendiente |
| EV-2026-11-21-02 | URDF/Xacro, lint Python y modelo energético | Aprobada con limitación: Gazebo/Nav2 pendiente |
| EV-2026-11-21-03 | Validación final previa a runtime (34 tests, URDF, Ruff, energía) | Aprobada con limitación: runtime pendiente |
| EV-2026-11-21-04 | Integración final del mini demo y el estudio 6×6 | Aprobada con limitación: runtime pendiente |
| EV-2026-11-21-05 | Validación documental del inventario de facultad y sus brechas | Aprobada con limitación: inventario sin verificar físicamente |
| EV-2026-11-21-06 | Cambio a Pi 4, obsolescencia de ADR-0009 y propuestas de cámara/LTE | Aprobada con limitación: runtime, CSI y LTE sin verificar |
| EV-2026-11-21-07 | BOM base en soles con precios de Perú | **Vigente**; stock y compra sin confirmar |

> Nota de conteo: en EV-02 el log de `make check` cuenta 62 Markdown porque incluye el README de la propia evidencia; el informe cita 61 documentos del proyecto.
