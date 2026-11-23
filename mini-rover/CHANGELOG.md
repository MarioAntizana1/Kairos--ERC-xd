# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y versionado semántico.

## [No publicado]

### Añadido

- Estructura inicial del proyecto y guía para agentes (`AGENTS.md`).
- Documentación SDLC: gobierno, investigación, requisitos, arquitectura, diseño, pruebas, operación, evidencia y presentación.
- Paquete ROS 2 `rover_description` con URDF/Xacro del rover.
- Paquete ROS 2 `rover_bringup` con launch de simulación, configuración de Nav2, mundo y mapa generados.
- Paquete ROS 2 `rover_mission` con lógica de misión pura y nodo ROS 2.
- Scripts de instalación, simulación, pruebas, validación documental y evidencia.
- Pruebas unitarias de la lógica de misión.
- Evidencia EV-2026-11-21-01: validación documental, assets y 32 pruebas unitarias.
- Evidencia EV-2026-11-21-02: URDF/Xacro, lint Python y modelo energético.
- Evidencia EV-2026-11-21-03: validación final pre-runtime (34 pruebas, URDF, Ruff, energía).
- Evidencia EV-2026-11-21-04: integración final del mini demo y el estudio 6×6.
- Estudio energético 6×6 en `docs/04-diseno/energia/` (variante pendiente de OQ-09).
- Cálculo energético preliminar y dimensionado del pack 2S2P de 4 celdas
  (`docs/04-diseno/energia/calculo-energetico.md`).
- Diseño eléctrico de la variante 6×6
  (`docs/04-diseno/energia/diseno-electrico-6x6.md`) y BOM separada
  (`docs/04-diseno/energia/bom-6x6.md`), sin mezclar con la BOM base.
- Variante 6×6 actualizada a pack **2S4P de 8 celdas** (100,8 Wh), cargador de
  5 A y BOM ajustada (+24 EUR en celdas).
- Script reproducible `scripts/energy/calculo_energia.py` y objetivo `make energy`.
- Registro de fuentes (`docs/01-investigacion/fuentes.md`) y bitácora
  (`docs/05-implementacion/bitacora.md`).
- Cotización de la BOM base en Perú (`docs/04-diseno/bom-peru.md`) con precios
  en PEN, stock, proveedores, alternativas locales y riesgos de suministro.
- Nota de revisión en `docs/04-diseno/bom.md`: la suma de las 23 líneas da
  740 EUR, no 705 EUR; corrección pendiente de aprobación.
- ADR-0008 propuesto: ESP32-S3 como interfaz de tiempo real entre la Pi 5 y
  actuadores/sensores, con micro-ROS sobre USB.
- Add-ons de la BOM Perú: interfaz ESP32-S3 (~S/ 195) y pack Li-ion 3S2P/3S3P
  a medida con celdas EVE INR18650/35V de Bracsan.
- Fuentes F-30 a F-38: celda EVE, BMS/cargador, datasheets ESP32-C6/S3,
  micro-ROS, disponibilidad local, `diff_drive_controller` y Hifisac.
- Revisión de Hifisac: precios de referencia más bajos (ESP32-S3 S/ 49, BMS
  3S 25A S/ 9,90, INA219 S/ 8,20), pero **sin stock online**; venta por WhatsApp.
- Investigación de percepción 3D
  (`docs/01-investigacion/percepcion-3d.md`): dos Camera Module 3 + ToF
  VL53L8CX, alternativas OAK-D Lite y Global Shutter, límites de sincronía,
  calibración, CPU y energía.
- Fuentes F-39 a F-51: Pi 5, Camera Module 3, `libcamera` multicámara,
  Global Shutter, `camera_ros`, VL53L8CX, OAK-D Lite, guía de estéreo,
  AI Camera y pipeline `stereo_image_proc`.
- Preguntas abiertas OQ-11 a OQ-15 sobre percepción 3D, presupuesto y
  calibración.
- ADR-0009 aceptado con alcance de spike: 2 × Camera Module 3 + ToF VL53L8CX,
  A (1 CM3 + ToF) como fallback y 10 semanas efectivas de ejecución con hitos
  de 2 semanas; la compra tiene un plazo estimado de 10 días laborables,
  separado del desarrollo y dentro del horizonte de ~10 meses hasta el ERC 2027.
- BOM del spike de percepción 3D (`docs/04-diseno/bom.md`, sección 9):
  ~105 USD en materiales y ~130 USD con importación, fuera del total base.
- H6 y experimento E5 para medir fps, error de profundidad, CPU, temperatura
  y potencia del spike.
- Inventario de materiales disponible en facultad
  (`docs/04-diseno/inventario-facultad.md`), con mapeo a la BOM base y a la
  variante 6×6, brechas y datos pendientes; no cambia BOM, alcance ni ADR.
- RSK-19: el inventario no cubre LiDAR, encoders ni seguridad eléctrica.
- Fuentes F-52 y F-53 (inventario de facultad y LilyGO T-SIM7600X).
- Evidencia EV-2026-11-21-05: validación documental del inventario.
- README raíz: enlace al inventario de facultad y actualización del registro
  de evidencias a cinco ejecuciones.
- ADR-0010 aceptado: Raspberry Pi 4 Model B de 8 GB + Argon ONE como
  computadora de a bordo; reemplaza a ADR-0002. RNF-07, TC-20, arquitectura,
  diseño eléctrico, instalación y presentación actualizados.
- BOM revisada para Pi 4: Pi 4 y Argon reutilizadas, SSD USB 3.0 en lugar de
  HAT NVMe; subtotal 610 EUR y total 671 EUR, pendiente de aprobación.
- ADR-0009 marcado obsoleto por el cambio a Pi 4 (un solo CSI).
- ADR-0011 propuesto: spike de estéreo aproximado con Camera V2.1 + USB; no es
  estéreo sincronizado ni sensor de seguridad.
- ADR-0012 propuesto: LilyGO T-SIM7600X como gateway LTE/GNSS opcional, fuera
  del lazo de control; el SIM7600 va por UART al ESP32.
- Fuentes F-54 a F-56 (Pi 4, Argon ONE, Camera Module V2).
- OQ-16 a OQ-18 y riesgos RSK-20 a RSK-22.
- Evidencia EV-2026-11-21-06: validación documental del cambio a Pi 4 y las
  propuestas de cámara/LTE.
- BOM base reescrita en soles (PEN) con precios de Perú: **S/ 2.520,08** de
  subtotal y **S/ 2.646,08** con 5 % de imprevistos; Pi 4 y Argon reutilizadas,
  SSD USB y cargador incluidos. `bom-peru.csv` actualizado a la ruta Pi 4.
- `bom-peru.md` con ruta vigente 5.2 en PEN y la ruta Pi 5 marcada como
  histórica; `bom-6x6.md` sigue en EUR como estudio hasta resolver OQ-09.
- Evidencia EV-2026-11-21-07: validación documental de la BOM en soles y del
  total S/ 2.646,08.

### Cambiado

- BOM en soles reescrita el **2026-11-23**: subtotal **S/ 2.542,88** y
  **S/ 2.670,02** con 5 % de imprevistos. Se sustituye la batería LiFePO4 y su
  cargador de red por un **pack Li-ion 2S4P** de 8 celdas (7,4 V / 14 Ah /
  103,6 Wh) con celdas de Bracsan, soldadura por punto y carga con **TP5100 +
  2 paneles de 6 V en serie**.
- Se eliminan el SSD SATA, la caja USB y el HAT M.2: el arranque va por
  **microSD**. También sale el perfil V-Slot 2040 (ya se tenía).
- Se añade un **boost DC-DC de 400 W** en el riel de tracción para volver a
  12 V (83 rpm y 0,39 m/s); sin él la tracción queda en ~51 rpm y 0,24 m/s.
- Se añaden un **ToF TFmini Plus** y una **webcam Logitech Brio 4K** (la Pi 4 no
  tiene doble CSI, así que la visión va por USB).
- Ruedas y placas pasan a **impresión 3D local**; el portafusibles se mueve a
  Bracsan. El fusible se recalcula a 20–25 A por la corriente del pack de 2S.
- `check_docs.py` sigue en verde (78 documentos, 356 enlaces).
- El consolidado de compras de los tres subproyectos vive en
  `cotizaciones/bom-consolidado.md`, en la raíz del workspace.

### Pendiente

- Confirmar estado del Pi 4, acceso al CSI con la carcasa Argon,
  especificaciones de los motores 10F125, modelo/variante del LilyGO,
  estado/cargador de la LiPo y Vmp/Imp de los paneles.
- Aprobar la BOM revisada (**S/ 2.670,02**) antes de comprar y confirmar stock.
- Ejecutar los spikes ADR-0011 (CSI + USB) y ADR-0012 (LTE/GNSS).
- Validación de integración en Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic.
- Ejecución de la misión de 5 waypoints y registro de rosbag2.
- Cotización y compra del hardware.
- Ensayo en pista física.
- Licencia del proyecto.
