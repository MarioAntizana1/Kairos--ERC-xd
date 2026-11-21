# ADR-0010 — Raspberry Pi 4 Model B (8 GB) + Argon ONE como computadora de a bordo

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: Hardware · Reemplaza a: [ADR-0002](0002-raspberry-pi-5.md)

## Contexto

La decisión anterior ([ADR-0002](0002-raspberry-pi-5.md)) fijaba una Raspberry
Pi 5 de 8 GB. El inventario de facultad (**F-52**) confirma una **Raspberry Pi 4
Model B de 8 GB** y una carcasa **Argon ONE V2** disponibles, sin coste de
compra. El responsable del proyecto decidió el 2026-11-21 cambiar la base a ese
hardware.

La Pi 4 de 8 GB:

- Está soportada por Ubuntu 24.04 y ROS 2 Jazzy arm64 (F-18).
- Tiene 8 GB de RAM, suficiente para el límite de RNF-07 (< 6 GB en uso).
- Tiene Gigabit Ethernet y 2 × USB 3.0 (F-54), útiles para LiDAR, SSD y
  periféricos.
- **No expone PCIe/NVMe**: el almacenamiento va por USB 3.0 o microSD (F-54).
- Tiene **un solo puerto CSI de 15 pines** (F-54), no dos como la Pi 5.
- Se alimenta con **5 V/3 A** por USB-C (F-54), no con 5 V/5 A.
- Tiene menos CPU que la Pi 5; el rendimiento de Nav2 debe medirse.

La carcasa Argon ONE V2 es de aluminio, con ventilador, botón de encendido, GPIO
accesible y todos los puertos en la parte trasera (F-55). No documenta acceso al
CSI: hay que verificar que el cable de cámara pueda salir.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste | Madurez |
|---|---|---|---|---|
| **Raspberry Pi 4 B 8 GB + Argon ONE** | Disponible en facultad; 8 GB RAM; Ubuntu 24.04/Jazzy; Gigabit Ethernet; 2 × USB 3.0; carcasa con ventilador | CPU menor que Pi 5; sin NVMe; un solo CSI; 5 V/3 A; acceso al CSI por verificar | 0 (reutilizada) | Alta |
| Raspberry Pi 5 8 GB (ADR-0002) | Más CPU; PCIe/NVMe; dos CSI; 5 V/5 A | No disponible en facultad; coste; sin ventaja medida para Nav2 2D | ~90 EUR | Alta |
| Raspberry Pi 4 B 4 GB | Menor coste | RAM justa para Nav2 + rosbag2; no es la unidad disponible | ~0 si se cambia | Alta |
| Mini PC x86 N100 | Más CPU; NVMe; Ubuntu nativo | Consumo, tamaño, precio, alimentación | ~180 EUR | Alta |
| Jetson Orin Nano | GPU para visión | Precio, consumo, stack distinto | ~250 EUR | Media |

## Decisión

Usar la **Raspberry Pi 4 Model B de 8 GB con carcasa Argon ONE V2** como
computadora de a bordo, con **Ubuntu 24.04 LTS + ROS 2 Jazzy**, **SSD USB 3.0 de
128 GB** (o microSD A2 de 64 GB como mínimo) y fuente de **5 V/3 A**. No se
instala HAT NVMe. Se mantiene el resto de la pila (Nav2, Gazebo Harmonic,
LiDAR 2D, mapa estático + AMCL).

## Consecuencias

### Positivas

- Se usa hardware ya disponible; el coste de cómputo baja a 0.
- 8 GB de RAM cumplen el umbral de RNF-07 con margen.
- Menor consumo que la Pi 5; mejora la autonomía teórica.
- Gigabit Ethernet y USB 3.0 siguen siendo suficientes para LiDAR, SSD y
  telemetría.
- La carcasa Argon ONE aporta disipador y ventilador, y deja el GPIO accesible.
- El software es el mismo; no cambia el modelo de programación de ROS 2.

### Negativas / deuda asumida

- CPU más lenta: Nav2, AMCL y rosbag2 compiten por menos recursos. Hay que
  medir CPU, RAM y temperatura (TC-20) y ajustar frecuencias/controladores.
- Sin NVMe: el sistema arranca desde USB 3.0 o microSD; el SSD USB añade un
  cable y un punto de fallo. Hay que asegurar el conector y el apagado.
- Un solo CSI: **no se pueden conectar dos Camera Module 3** como en ADR-0009.
  La percepción estéreo se replantea en [ADR-0011](0011-estereo-csi-usb.md).
- Fuente de 5 V/3 A: el DC-DC de 5 V/5 A de la BOM sigue siendo válido, pero
  no se debe asumir el presupuesto de 5 A de la Pi 5.
- La carcasa Argon ONE no documenta acceso al CSI (F-55); verificar antes de
  montar la cámara.
- El estudio 6×6 y su cálculo energético asumen Pi 5; si se adopta la variante,
  hay que recalcular consumo y BOM.

### Neutrales

- La Pi 4 puede migrar a Pi 5 o mini PC si el rendimiento medido no cumple.
- El árbol TF, los frames y los topics no cambian.
- La evidencia de simulación sigue siendo válida; la de hardware cambia de
  plataforma.

## Impacto documental

| Documento | Cambio |
|---|---|
| `AGENTS.md` | Decisión de cómputo: Pi 4 8 GB + Argon ONE, ADR-0010 |
| `README.md` | Tabla de hardware y texto de plataforma |
| `02-requisitos/requisitos-no-funcionales.md` | RNF-07 se mide en Pi 4 8 GB |
| `02-requisitos/trazabilidad.md` | Fila de RNF-07 |
| `03-arquitectura/arquitectura-sistema.md` | Diagramas y sección Pi 4 + ESP32-S3 |
| `04-diseno/bom.md` | Líneas de cómputo, almacenamiento y refrigeración |
| `04-diseno/diseno-electrico.md` | Riel de 5 V y presupuesto de potencia |
| `05-implementacion/entorno-desarrollo.md` | Opción Pi 4 y almacenamiento USB |
| `06-pruebas/casos-prueba.md` | TC-20 en Pi 4 |
| `07-operacion/` y `09-presentacion/` | Referencias a la plataforma |
| `01-investigacion/benchmarking-plataformas.md` | Nota de revisión; la comparación se conserva |
| `01-investigacion/hipotesis-y-experimentos.md` | H3/H5 en Pi 4; H6/E5 suspendidos |
| `03-arquitectura/adr/0009-spike-percepcion-3d.md` | Obsoleta por el cambio de plataforma |

## Criterios de revisión

- CPU media > 80% o pico > 95% durante 30 min de misión.
- Temperatura > 80 °C con la carcasa Argon y el ventilador en funcionamiento.
- RNF-01 (éxito ≥ 80%) o RNF-02 (error ≤ 0.30 m) no se cumplen por falta de CPU.
- Se necesita NVMe, dos CSI o más de 8 GB para una función aprobada.
- La Pi 4 falla o no arranca de forma estable con Ubuntu 24.04 + Jazzy.
- El coste/plazo de una Pi 5 baja lo suficiente como para reabrir la decisión.

## Referencias

- F-18: Ubuntu — soporte de placas Raspberry Pi (Pi 4B en 24.04).
- F-52: inventario de facultad (Pi 4 8 GB + Argon ONE).
- F-54: Raspberry Pi 4 Model B — specifications.
- F-55: Argon ONE V2 Case for Raspberry Pi 4.
- [ADR-0002](0002-raspberry-pi-5.md) — decisión reemplazada.
- [ADR-0009](0009-spike-percepcion-3d.md) — spike de percepción 3D afectado.
- [ADR-0011](0011-estereo-csi-usb.md) — alternativa de percepción con CSI + USB.
