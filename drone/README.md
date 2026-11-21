# Drone — Payload de visión estéreo + ToF de piso

![Estado](https://img.shields.io/badge/estado-borrador%20v0.1-orange)
![Cómputo](https://img.shields.io/badge/cómputo-Raspberry%20Pi%205-green)
![Cámaras](https://img.shields.io/badge/cámaras-2%20×%20Camera%20Module%203-blue)
![ToF](https://img.shields.io/badge/ToF-VL53L1X%20%2F%20VL53L5CX-purple)
![Metodología](https://img.shields.io/badge/SDLC%20%2B%20DSR-puertas%20G0–G5-lightgrey)

Payload de visión para un dron de **inspección y mapeo 3D**. El proyecto reutiliza la metodología del rover —SDLC iterativo, Design Science Research, requisitos IEEE 29148, riesgos ISO 31000 y evidencia reproducible— pero aquí el alcance se limita a la visión: **dos Raspberry Pi Camera Module 3, un ToF de piso, una Raspberry Pi 5 y el pipeline de profundidad, nube de puntos y referencia de calibración**.

El dron completo (frame, controladora de vuelo, ESCs, motores, batería, radio) queda **fuera de este repositorio**. La visión es un payload informativo: la controladora de vuelo conserva la autoridad final y los failsafes.

> **Aclaración técnica importante:** el ToF va en la base, **mirando al piso**. Mide la distancia vertical cámara–suelo y sirve como **referencia métrica** para validar la calibración (plano del suelo, homografía, comparación con la profundidad estéreo y extrínseca ToF–cámara). Un estéreo calibrado ya es métrico; el ToF no le “da” la escala, la verifica. **No calcula geometría epipolar**: eso lo hace el par estéreo calibrado. Una sola distancia **no** sustituye la calibración con tablero; se usa como restricción y verificación. Para la altura de **6 m** se usa **TFmini Plus 12 m**; el VL53L1X y el VL53L5CX son de 4 m y no alcanzan. Ver [`docs/04-diseno/diseno-vision.md`](docs/04-diseno/diseno-vision.md).

---

## Cotización en una página

Precios en soles peruanos (PEN) con IGV, consultados el **2026-11-21** en catálogos públicos. No incluyen envío internacional, aduanas ni fluctuaciones. **No autoriza compra.**

| Escenario | Qué incluye | Total |
|---|---|---:|
| **Núcleo de visión** | Pi 5 8 GB, 2 × Camera Module 3 Standard, ToF de piso TFmini Plus 12 m, 2 cables FPC de 300 mm | **S/ 1.403,00** |
| **Núcleo operativo de banco** | Lo anterior + Active Cooler, fuente oficial 27 W y microSD 64 GB A2 | **S/ 1.564,80** |
| **Kit completo (banco + vuelo)** | Lo anterior + HAT+ M.2, SSD NVMe 128 GB, UBEC 5 V/5 A, montaje, cableado y 5 % de contingencia | **S/ 2.341,08** |
| **ToF local ≤4 m** | VL53L1X (4 m) en lugar del TFmini Plus; **no sirve a 6 m** | **− S/ 255** → S/ 2.073,33 |
| **ToF 8×8 ≤4 m** | VL53L5CX importado (64 zonas, 4 m); **no sirve a 6 m** | **− S/ 140** → S/ 2.194,08 |

- Detalle verificable, enlaces, stock y alternativas: [`docs/04-diseno/bom-peru.md`](docs/04-diseno/bom-peru.md).
- Datos crudos para re-cotizar: [`docs/04-diseno/bom-peru.csv`](docs/04-diseno/bom-peru.csv).
- Referencia internacional en USD: [`docs/04-diseno/bom.md`](docs/04-diseno/bom.md).

> **Si los cables de 200 mm incluidos con cada cámara alcanzan** para la baseline de 150 mm, se pueden restar S/ 25 del núcleo. La fuente de 27 W es de banco: no vuela; sin ella, el kit de vuelo queda en **S/ 2.270,73**. El UBEC y el montaje son estimaciones que deben cotizarse antes de comprar. La base usa **TFmini Plus** porque la competencia vuela a **6 m**; el VL53L1X y el VL53L5CX son de 4 m y no alcanzan.

---

## Qué hace el payload

```text
Camera Module 3 izquierda ─┐
                           ├─ CSI ─→ ISP Pi 5 ─→ captura ─→ rectificación ─→ estéreo ─→ profundidad
Camera Module 3 derecha ───┘                                                        │
                                                                                    ├─→ nube de puntos 3D
ToF de piso ─────────────── I²C ─→ distancia al suelo ─→ escala / calibración ──────┤
                                                                                    ├─→ detección de obstáculos
Controladora de vuelo ──── MAVLink ─→ actitud / posición ─→ georreferencia ─────────┘
                                                                                    └─→ registro en NVMe
```

| Incluido en esta fase | Excluido (fase dron completo) |
|---|---|
| Par estéreo con dos Camera Module 3 | Frame, motores, ESCs y hélices |
| ToF de piso para altitud y referencia de calibración | Controladora de vuelo y firmware de vuelo |
| Calibración intrínseca/estéreo y rectificación | Batería, PDB y sistema de potencia del dron |
| Mapa de disparidad y nube de puntos | Radio, telemetría y estación de tierra |
| Detección de obstáculos y telemetría | Autonomía de vuelo y planificación de trayectoria |
| Registro de datos y evidencia | Certificación aeronáutica y operación BVLOS |

---

## Hardware propuesto

| Componente | Modelo | Nota |
|---|---|---|
| Cómputo | Raspberry Pi 5, 8 GB | Doble CSI, PCIe, ISP; Ubuntu 24.04 o Raspberry Pi OS |
| Cámaras | 2 × Camera Module 3 Standard | IMX708 12 MP, rolling shutter, autofocus; foco bloqueado en vuelo |
| Baseline | 150 mm nominal (100–200 mm ajustable) | Barra rígida; error de calibración < 0,5 px |
| ToF de piso | TFmini Plus 12 m (base, 6 m); VL53L1X o VL53L5CX ≤4 m (alternativas) | Montado en la base, mirando al suelo; ventana y extrínseca calibrada |
| Almacenamiento | HAT+ M.2 + SSD NVMe 128 GB | Arranque y registro; microSD A2 de respaldo |
| Energía | UBEC 5 V/5 A (2–6S) | 5,1–5,2 V, fusible, capacitor; consumo típico 12–16 W |
| Refrigeración | Active Cooler oficial | Necesario en caja; monitorizar throttling |
| Peso estimado | ~250–300 g con montaje | Debe validarse en báscula |

---

## Inicio rápido

```bash
make check      # valida enlaces, IDs, trazabilidad y totales de la BOM
make docs       # solo validación documental
make bom        # verifica que el CSV suma lo que dice el documento
make help       # lista de comandos
```

No hay código de visión todavía: primero se cierra la concepción (G0), los requisitos (G1) y el diseño (G2). El código y las pruebas de hardware se añadirán cuando exista el equipo y se registren como evidencia.

---

## Metodología

- **SDLC iterativo e incremental** con puertas G0–G5, inspirado en ISO/IEC 12207.
- **Design Science Research** para construir y evaluar el artefacto (payload + documentación + evidencia).
- **Ingeniería de requisitos** estilo IEEE 29148, con IDs y criterios de aceptación medibles.
- **Gestión de riesgos** inspirada en ISO 31000.
- **Verificación y validación** con trazabilidad requisito → diseño → prueba → evidencia.

Detalle en [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md). Las reglas de trabajo para personas y agentes están en [`AGENTS.md`](AGENTS.md).

---

## Estado y siguientes pasos

| Elemento | Estado |
|---|---|
| Documentación SDLC | Borrador v0.1 |
| Cotización Perú | Estudio de abastecimiento 2026-11-21 |
| Hardware | No adquirido |
| Calibración / pipeline | Diseñado, no implementado |
| Pruebas de vuelo | Pendientes |
| Evidencia | Validación documental registrada; hardware pendiente |

1. Aprobar el alcance y el presupuesto de la fase de banco (G0).
2. Confirmar stock del HAT+ M.2 y del ToF; decidir VL53L1X local vs VL53L5CX importado.
3. Comprar el núcleo operativo de banco y montar el par estéreo.
4. Capturar, calibrar y medir error de profundidad (G3/G4).
5. Integrar pose MAVLink y probar en el dron con hélices quitadas; después, vuelo cautivo.
6. Registrar evidencia y actualizar el runbook de vuelo.

Ver el plan completo en [`docs/00-gobierno/plan-proyecto.md`](docs/00-gobierno/plan-proyecto.md).

---

## Licencia

**Pendiente de decisión.** No se distribuye bajo ninguna licencia hasta que el equipo y la universidad lo aprueben. Las dependencias de terceros conservan sus licencias originales (Raspberry Pi OS, libcamera, OpenCV, ROS 2, MAVLink).

## Créditos y fuentes

Consultar [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md). Este proyecto no está afiliado oficialmente a Raspberry Pi Ltd, STMicroelectronics ni a ninguna autoridad aeronáutica.
