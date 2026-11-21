# Rover Mini Demo — European Rover Challenge

![Estado](https://img.shields.io/badge/estado-borrador%20v0.1-orange)
![ROS 2](https://img.shields.io/badge/ROS%202-Jazzy%20Jalisco-blue)
![Plataforma](https://img.shields.io/badge/plataforma-Raspberry%20Pi%205-green)
![Licencia](https://img.shields.io/badge/licencia-pendiente-lightgrey)

Demostración mínima de **navegación autónoma** para preparar un rover de competición del [European Rover Challenge (ERC)](https://roverchallenge.eu/). El rover completo —brazo, ciencia, perforación, dron— queda fuera de esta fase; aquí se valida la base: localización, planificación, control, seguridad y evidencia reproducible.

> **Objetivo deportivo:** ERC 2027. La edición 2026 se celebró del 4 al 6 de septiembre de 2026 en Cracovia. Las fechas de 2027 todavía no están publicadas.

---

## Qué hace el demo

El rover recibe una lista de waypoints, navega de forma autónoma por una arena tipo Marsyard reducida, evita obstáculos con LiDAR, registra telemetría y bags, y devuelve un informe de misión. Todo se puede ejecutar primero en **Gazebo Harmonic** y después en la **Raspberry Pi 4 Model B de 8 GB** con la misma pila ROS 2.

```
Misión YAML → Nodo de misión → Nav2 (planificador + controlador)
                    ↑                    ↓
              telemetría/logs      /cmd_vel → base
                    ↑                    ↓
                 LiDAR ←──────────── odometría
```

### Alcance de esta fase

| Incluido | Excluido (fase rover grande) |
|---|---|
| Navegación autónoma por waypoints | Brazo manipulador |
| Evitación de obstáculos 2D | Perforación y ciencia |
| Localización AMCL con mapa estático | Dron |
| Telemetría, logs y rosbag2 | Visión estereoscópica |
| Parada de emergencia y watchdog | Operación BVLOS |
| Simulación Gazebo + hardware Pi | Autonomía de largo alcance |

---

## Inicio rápido

### Solo documentación y validaciones (funciona en Fedora/macOS/Linux)

```bash
git clone <url-del-repo> rover
cd rover
make check          # valida enlaces, IDs, assets y pruebas unitarias
make energy         # ejecuta el modelo energético preliminar
make urdf-check     # genera el URDF desde Xacro y valida su estructura
make help           # lista todos los comandos
```

> `make urdf-check` requiere `xacro`. En un host sin ROS 2 puedes instalarlo con
> `pip install -r requirements-dev.txt`. La integración continua
> (`.github/workflows/ci.yml`) ejecuta estas validaciones en cada push.

### Simulación completa (requiere Ubuntu 24.04 + ROS 2 Jazzy)

```bash
# 1. Instalar ROS 2 Jazzy y dependencias
bash scripts/setup/install_ros_jazzy.sh --dry-run   # revisa primero
bash scripts/setup/install_ros_jazzy.sh

# 2. Compilar
bash scripts/sim/build.sh

# 3. Lanzar Gazebo + Nav2 + RViz
bash scripts/sim/run_sim.sh

# 4. En otra terminal, lanzar la misión
bash scripts/sim/run_mission.sh
```

La guía detallada está en [`docs/05-implementacion/guia-instalacion.md`](docs/05-implementacion/guia-instalacion.md).

> **Aviso de estado:** el paquete ROS 2 está en estado *borrador*. La lógica de misión tiene pruebas unitarias ejecutadas; la integración con Gazebo/Nav2 está pendiente de validación en un host Ubuntu 24.04. No se presenta como “probada” hasta que exista evidencia en `docs/08-evidencia/`.

**Evidencia local:** siete ejecuciones selladas con SHA-256, incluida la integración del estudio 6×6, el inventario de facultad, el cambio a Pi 4 y la BOM en soles. Consulta [`docs/08-evidencia/registro-evidencias.md`](docs/08-evidencia/registro-evidencias.md). La más reciente es `EV-2026-11-21-07`; el runtime ROS 2 sigue pendiente.

---

## Estructura

```
.
├── AGENTS.md                 Guía operativa para agentes de IA y colaboradores
├── docs/                     SDLC completo: investigación, requisitos, diseño, pruebas, evidencia
├── ros_ws/src/
│   ├── rover_description/    URDF/Xacro del rover
│   ├── rover_bringup/        Launch files, Nav2, mundo, mapa, RViz
│   └── rover_mission/        Lógica de misión y nodo ROS 2
├── scripts/                  Instalación, simulación, pruebas y evidencia
└── Makefile                  Atajos reproducibles
```

### Documentos clave

| Documento | Para qué |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Reglas de trabajo, SDLC y definición de “hecho” |
| [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md) | Metodología SDLC + investigación |
| [`docs/01-investigacion/contexto-erc.md`](docs/01-investigacion/contexto-erc.md) | Qué pide el ERC y qué aplica al demo |
| [`docs/02-requisitos/vision-alcance.md`](docs/02-requisitos/vision-alcance.md) | Alcance y criterios de éxito |
| [`docs/03-arquitectura/arquitectura-sistema.md`](docs/03-arquitectura/arquitectura-sistema.md) | Arquitectura y flujos |
| [`docs/06-pruebas/plan-pruebas.md`](docs/06-pruebas/plan-pruebas.md) | Cómo se verifica |
| [`docs/07-operacion/runbook-demo.md`](docs/07-operacion/runbook-demo.md) | Guion y contingencias de la demo |
| [`docs/08-evidencia/README.md`](docs/08-evidencia/README.md) | Política de evidencia |

---

## Requisitos de hardware (propuesta)

| Componente | Modelo propuesto | Nota |
|---|---|---|
| Cómputo | Raspberry Pi 4 Model B, 8 GB RAM + Argon ONE | Ubuntu 24.04 Server 64-bit |
| Almacenamiento | SSD USB 3.0 128–256 GB (o SD A2 64 GB) | La Pi 4 no expone NVMe |
| LiDAR | RPLIDAR A1M8 / LD19 / similar 2D | 360°, 10 Hz, alcance ≥ 8 m |
| IMU | BNO085 o MPU-9250 | Fusión opcional con `robot_localization` |
| Tracción | 4 ruedas, 2 motores con encoders | Driver con control de velocidad |
| Energía | LiFePO4 12 V 10 Ah + cargador + DC-DC 5 V | Fusible, interruptor y e-stop; 6 Ah no disponible |
| Chasis | Aluminio o impresión 3D reforzada | Base 0.55 × 0.45 m |
| Cámara | Camera Module V2.1 (CSI) + USB opcional | Teleoperación; el estéreo CSI + USB es solo un spike (ADR-0011) |
| Conectividad | Wi-Fi/Ethernet; LilyGO T-SIM7600X LTE/GNSS opcional | Telemetría remota; no control (ADR-0012) |

Lista completa y presupuesto en soles (PEN) en [`docs/04-diseno/bom.md`](docs/04-diseno/bom.md): **S/ 2.646,08** con 5 % de imprevistos, pendiente de aprobación. Los precios son de Perú a 2026-11-21 y deben cotizarse antes de comprar. El detalle de proveedores y alternativas está en [`docs/04-diseno/bom-peru.md`](docs/04-diseno/bom-peru.md).

> **Inventario de facultad:** parte del material ya está disponible (Pi 4,
> TB6612, IMU, ToF, cámara, LiPo y paneles), pero no cubre LiDAR, encoders ni
> seguridad eléctrica. No se descuenta de la BOM ni cambia el alcance. Ver
> [`docs/04-diseno/inventario-facultad.md`](docs/04-diseno/inventario-facultad.md).

> **Variante 6×6 (estudio):** el cálculo, el diseño eléctrico y la BOM de un
> rover de 6 ruedas con tracción y dirección independientes están en
> [`docs/04-diseno/energia/`](docs/04-diseno/energia/). No es la base del mini
> demo (2 motores, LiFePO4 12,8 V) hasta que se apruebe OQ-09. La tabla anterior
> corresponde a la base; no mezclar ambas BOM.
>
> **Propuesta ADR-0008 (en revisión):** añadir un ESP32-S3 como interfaz de
> tiempo real para PWM, encoders, IMU, batería y expansión I²C, dejando la Pi 4
> como cerebro. No está incluido en la tabla ni en la BOM base hasta que se
> apruebe. Ver
> [`docs/03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md`](docs/03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md).

---

## Metodología

- **SDLC iterativo e incremental** con puertas G0–G5, inspirado en ISO/IEC 12207.
- **Design Science Research** para construir y evaluar el artefacto.
- **Ingeniería de requisitos** estilo IEEE 29148, con identificadores y criterios de aceptación.
- **Gestión de riesgos** inspirada en ISO 31000.
- **Verificación y validación** con trazabilidad requisito → diseño → prueba → evidencia.

Detalle en [`docs/00-gobierno/metodologia.md`](docs/00-gobierno/metodologia.md) y [`docs/01-investigacion/marco-metodologico.md`](docs/01-investigacion/marco-metodologico.md).

---

## Estado y siguientes pasos

1. Validar el paquete ROS 2 en Ubuntu 24.04 + Gazebo Harmonic (G3).
2. Ejecutar la batería de pruebas y registrar evidencia (G4).
3. Cotizar y adquirir el hardware mínimo (ver [`docs/04-diseno/bom-peru.md`](docs/04-diseno/bom-peru.md)).
4. Montar el rover, calibrar LiDAR/odometría y repetir la misión en pista.
5. Ensayar el guion de demo y grabar el vídeo de presentación.

Ver el plan completo en [`docs/00-gobierno/plan-proyecto.md`](docs/00-gobierno/plan-proyecto.md).

---

## Licencia

**Pendiente de decisión.** No se distribuye bajo ninguna licencia hasta que el equipo y la universidad lo aprueben. Las dependencias de terceros conservan sus licencias originales (ROS 2: Apache-2.0; Gazebo: Apache-2.0; Nav2: Apache-2.0).

## Créditos y fuentes

Consultar [`docs/01-investigacion/fuentes.md`](docs/01-investigacion/fuentes.md). Este proyecto no está afiliado oficialmente al European Rover Challenge ni a la European Space Foundation.
