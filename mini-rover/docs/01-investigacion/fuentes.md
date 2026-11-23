# Fuentes consultadas

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Investigación

Registro de las fuentes usadas en la documentación. Cada entrada indica qué se
extrajo, la fecha de acceso y el nivel de confianza. Las fuentes de fabricante se
consideran primarias para sus propias especificaciones; las estimaciones del
equipo se marcan como tales y no se presentan como datos medidos.

> **Convención de IDs:** `F-001`–`F-008` corresponden al estudio energético
> 6×6; `F-01`–`F-18` corresponden a la pila de navegación del mini demo;
> `F-19`–`F-29` a la cotización de la BOM base en Perú; `F-30`–`F-38` a la
> propuesta ESP32, batería Li-ion y revisión de Hifisac; `F-39`–`F-51` a la
> investigación de percepción 3D (cámaras, ToF y alternativas); `F-52`–`F-53`
> al inventario de facultad y al LilyGO T-SIM7600X; `F-54`–`F-56` a la
> Raspberry Pi 4, la carcasa Argon ONE y la Camera Module V2. Se mantienen
> separados para no romper las referencias existentes. Unificarlos requiere una
> revisión y un cambio controlado en todos los documentos.

| ID | Fuente | URL | Fecha de acceso | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-001 | Raspberry Pi Documentation — Power supply | <https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply> | 2026-11-21 | Raspberry Pi 5: fuente recomendada de 5 V / 5 A (27 W); consumo típico de placa activa 800 mA; cámara 250 mA; ventilador 60 mA a 5 V; con fuente de 3 A los USB se limitan a 600 mA | Alta |
| F-002 | Raspberry Pi 5 Product Brief | <https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf> | 2026-11-21 | Alimentación por USB-C de 5 V / 5 A con Power Delivery | Alta |
| F-003 | TowerPro — MG90S | <https://www.towerpro.com.tw/product/mg90s-3/> | 2026-11-21 | Servo MG90S: 13,4 g; par de bloqueo 1,8 kg·cm a 4,8 V y 2,2 kg·cm a 6,6 V; 0,10 s/60° a 4,8 V | Alta (fabricante) |
| F-004 | Adafruit — MG995 standard servo | <https://www.adafruit.com/product/1142> | 2026-11-21 | Servo MG995: 4,8–6 V; 8,5 kg·cm a 4,8 V y 10 kg·cm a 6 V; 62,41 g; usado como referencia de la clase MG996R | Alta para MG995; media como equivalente de MG996R |
| F-005 | Pololu — 25D metal gearmotors | <https://www.pololu.com/category/115/25d-metal-gearmotors> | 2026-11-21 | Motor de referencia 25D LP 6 V 99:1 con encoder: 2,0 A de bloqueo, 120 mA en vacío, 9,1 kg·cm de par de bloqueo, 130 rpm en vacío; límite continuo recomendado 4 kg·cm | Alta |
| F-006 | Pololu — TB6612FNG dual motor driver | <https://www.pololu.com/product/713> | 2026-11-21 | Driver TB6612FNG: 1 A continuo y 3 A de pico por canal; 4,5–13,5 V de motor; protecciones térmicas | Alta |
| F-007 | Slamtec — RPLIDAR A1 specifications | <https://www.slamtec.com/en/lidar/a1spec> | 2026-11-21 | LiDAR A1: 5 V, 100 mA, 0,5 W, 170 g | Alta |
| F-008 | Datos aportados por el responsable del proyecto | Sin URL (comunicación de 2026-11-21) | 2026-11-21 | 4 paneles solares de 600 mA a 7,2 V; celdas Li-ion de 3,6 V y 3500 mAh; 6 motores con reducción; 6 ruedas con giro independiente; 2 acelerómetros y 2 giroscopios | Media: son requisitos de entrada, no mediciones |

## Datos que faltan y deben medirse

- Modelo y curva del motor de tracción (corriente en vacío, corriente nominal y
  corriente de bloqueo). Es la variable dominante del cálculo.
- Masa real del rover y reparto de carga por rueda.
- Radio de giro real de la rueda respecto al eje de la columna de dirección
  (*scrub radius*) y par necesario para girar una rueda en la arena.
- Corriente de bloqueo real de los servos elegidos.
- Hoja de datos de los paneles: si los 600 mA son `Imp` o `Isc`, y su tensión
  de circuito abierto. El inventario de facultad declara 6 V/720 mA (F-52),
  mientras que F-008 declara 7,2 V/600 mA; confirmar cuáles son los reales.
- Modelo exacto del LilyGO 7600X (¿T-SIM7600X?) y del Arduino «XD»; el
  inventario no lo detalla.
- Capacidad de descarga continua de las celdas 18650 concretas.
- Radiación solar del lugar y fechas de la competición (usar PVGIS u otra
  fuente horaria cuando se conozca la sede).

## Fuentes pendientes de consultar

- Reglamento del ERC 2027: no publicado en la fecha de revisión. Cualquier
  límite de batería, química o energía debe verificarse contra el reglamento
  oficial cuando se publique.
- Normativa local sobre transporte y carga de baterías de litio.

---

## Fuentes de la pila de navegación (mini demo)

Las siguientes fuentes sostienen las decisiones de ROS 2, Nav2, Gazebo y
plataforma. Fueron consultadas el 2026-11-21.

| ID | Fuente | URL | Fecha | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-01 | ERC — Space & Robotics Competition | <https://roverchallenge.eu/robotics-competition/> | 2026-11-21 | Pruebas del ERC, navegación, cinco checkpoints, autonomía sin vídeo, dron | Alta |
| F-02 | ERC — Competitor Zone | <https://roverchallenge.eu/competitor-zone/> | 2026-11-21 | Registro, requisitos de equipo, enlace al rulebook | Alta |
| F-03 | ERC — EPFL Xplore wins 2026 | <https://roverchallenge.eu/the-epfl-xplore-team-from-switzerland-wins-the-2026-european-rover-challenge/> | 2026-11-21 | 25 finalistas, >120 candidaturas, ganador, Marsyard Hellas Planitia | Alta |
| F-04 | Olympus Mars — ERC tasks/timeline | <https://olympusmars.be/erc> | 2026-11-21 | Lista de pruebas y calendario orientativo (secundaria) | Media |
| F-05 | SpaceJobs.Now — competitions 2027 | <https://spacejobs.now/learn/student-space-and-rocketry-competitions-2027> | 2026-11-21 | Confirmación de que no hay fechas 2027 publicadas (secundaria) | Media-baja |
| F-06 | ROS 2 Jazzy — Ubuntu installation | <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html> | 2026-11-21 | Instalación de Jazzy en Ubuntu 24.04, repositorio y `ros-dev-tools` | Alta |
| F-07 | Nav2 — Quickstart (Jazzy) | <https://docs.nav2.org/jazzy/getting_started/quickstart/quickstart/> | 2026-11-21 | Paquetes `navigation2`/`nav2-bringup`, Gazebo moderno, AMCL | Alta |
| F-08 | Nav2 — `nav2_params.yaml` Jazzy | <https://raw.githubusercontent.com/ros-navigation/navigation2/jazzy/nav2_bringup/params/nav2_params.yaml> | 2026-11-21 | Baseline de parámetros de AMCL, costmaps, planner, behaviors y smoother | Alta |
| F-09 | Gazebo — Installing with ROS | <https://gazebosim.org/docs/latest/ros_installation/> | 2026-11-21 | Compatibilidad Jazzy + Harmonic; `ros-${ROS_DISTRO}-ros-gz` | Alta |
| F-10 | `ros_gz` — README | <https://github.com/gazebosim/ros_gz/> | 2026-11-21 | Bridges, tabla de compatibilidad Jazzy/Harmonic, sintaxis de topics | Alta |
| F-11 | Ubuntu for Raspberry Pi | <https://ubuntu.com/download/raspberry-pi> | 2026-11-21 | Imágenes Ubuntu 24.04/26.04 para Raspberry Pi 5 | Alta |
| F-12 | REP 2000 | <https://reps.openrobotics.org/rep-2000/> | 2026-11-21 | Jazzy: mayo 2024–mayo 2029; Ubuntu 24.04 amd64/arm64 Tier 1 | Alta |
| F-13 | Serial Hobbyism — ROS 2 en Pi 5 | <https://serialhobbyism.com/how-to-install-ros2-on-a-raspberry-pi-5> | 2026-11-21 | Combinación práctica Ubuntu 24.04 + Jazzy en Pi 5 (secundaria) | Media |
| F-14 | Open Robotics — Jazzy released | <https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released> | 2026-11-21 | LTS hasta mayo de 2029; Tier 1 arm64/amd64 | Alta |
| F-15 | Nav2 — First-Time Robot Setup | <https://docs.nav2.org/jazzy/configuration_and_development/first_time_robot_setup_guide/> | 2026-11-21 | TF, URDF, SDF, odometría, sensores, footprint, plugins | Alta |
| F-16 | Aalto Space Association — ERC 2027 | <https://www.aaltospace.com/projects/erc-2027> | 2026-11-21 | Equipo preparando el ERC 2027 (secundaria) | Media-baja |
| F-17 | Nav2 — `bringup_launch.py` Jazzy | <https://raw.githubusercontent.com/ros-navigation/navigation2/jazzy/nav2_bringup/launch/bringup_launch.py> | 2026-11-21 | Argumentos `map`, `use_sim_time`, `params_file`, `slam`, `use_localization` | Alta |
| F-18 | Ubuntu — soporte de placas Raspberry Pi | <https://ubuntu.com/hardware/docs/boards/how-to/ubuntu_supported/raspberry-pi/> | 2026-11-21 | Pi 5 soportado en 24.04/26.04; Pi 4B en 22.04/24.04/26.04 | Alta |

### Historial de consultas de navegación

| Fecha | Fuentes | Resultado |
|---|---|---|
| 2026-11-21 | F-01, F-02, F-03 | Contexto y reglas del ERC verificados |
| 2026-11-21 | F-06, F-07, F-08, F-17 | Stack ROS 2/Nav2 verificado |
| 2026-11-21 | F-09, F-10 | Compatibilidad Gazebo/ROS verificada |
| 2026-11-21 | F-11, F-12, F-14, F-18 | Plataforma Pi 5 y soporte verificados |
| 2026-11-21 | F-04, F-05, F-16 | Fechas 2027: sin dato oficial |

---

## Fuentes de abastecimiento en Perú (BOM base)

Consulta de catálogos, precios y stock del 2026-11-21. Los precios son los
publicados en la fecha; el stock es declarativo y debe confirmarse antes de
comprar. El detalle está en
[`04-diseno/bom-peru.md`](../04-diseno/bom-peru.md).

| ID | Fuente | URL | Fecha | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-19 | The Pi Box — Raspberry Pi 5, accesorios y HAT | <https://thepibox.pe/shop/cmp-rp-010-raspberry-pi-5-de-8gb-3444><br><https://thepibox.pe/shop/enf-rp-001-active-cooler-raspberry-pi-3454><br><https://thepibox.pe/shop/fuente-de-poder-27-w-raspberry-pi-3458><br><https://thepibox.pe/shop/exp-rp-006-hat-m-2-raspberry-pi-3475> | 2026-11-21 | Pi 5 8 GB S/ 768 con stock; Active Cooler S/ 29,90; fuente 27 W S/ 67; HAT+ M.2 S/ 60 agotado; envío nacional por Olva | Alta en precio; media en stock |
| F-20 | Electromanía — LiDAR, motores, sensores y protección | <https://www.electromania.pe/producto/escaner-lidar-de-360-grados-rplidar-a1m8-r6-12m/><br><https://www.electromania.pe/producto/rplidar-c1-sensor-lidar-360-dtof-12m/><br><https://www.electromania.pe/producto/motorreductor-de-metal-con-encoder-12v-83rpm-45kg/><br><https://www.electromania.pe/producto/dfrobot-motorreductor-metalico-12v-dc-50rpm-12kg-cm/><br><https://www.electromania.pe/producto/modulo-sensor-bidireccional-de-monitorizacion-de-corriente-potencia-mcu-219-ina219-i2c/><br><https://www.electromania.pe/producto/boton-de-parada-de-emergencia-ac660v-10a/><br><https://www.electromania.pe/producto/regulador-de-voltaje-dc-dc-step-down-xl4005e1-5a/> | 2026-11-21 | A1M8 S/ 600 (12 unidades); C1 S/ 450; FIT0185 83 rpm con encoder S/ 145 (30 unidades); FIT0492-A 50 rpm sin encoder S/ 69,90; INA219 S/ 12,50; e-stop S/ 8; XL4005 5 A S/ 6,59; envío nacional desde S/ 10 | Alta |
| F-21 | Naylamp Mechatronics — drivers, V-Slot, conectores y almacenamiento | <https://naylampmechatronics.com/drivers/590-driver-puente-h-bts7960-43a.html><br><https://naylampmechatronics.com/perfiles-de-aluminio/688-perfil-v-slot-2040-l3200mm.html><br><https://naylampmechatronics.com/perfiles-de-aluminio/687-perfil-v-slot-2020-l3200mm.html><br><https://naylampmechatronics.com/conectores-electricos/749-conector-xt60-macho.html><br><https://naylampmechatronics.com/almacenamiento/836-memoria-micro-sd-card-64gb-kingston-clase-10-a1-100mbs.html><br><https://naylampmechatronics.com/motores-dc/817-motor-dc-37d-12v-35rpm-con-encoder.html> | 2026-11-21 | BTS7960 43 A S/ 45 con stock; perfil 2040 3,2 m S/ 160; perfil 2020 3,2 m S/ 98 agotado; XT60 S/ 4; microSD 64 GB A1 S/ 60; motor 37D 35 rpm con encoder S/ 70 agotado; envío gratis desde S/ 200 | Alta en precio; media en stock |
| F-22 | Electronics Peru — BNO085 (Ica) | <https://www.electronicsperu.com/product/sensor-imu-9dof-bno085-ahrs-para-ar-vr-y-robotica/> | 2026-11-21 | BNO085 S/ 100 con stock; tienda en Ica; envío a coordinar | Alta en precio; media en envío |
| F-23 | Falabella — baterías, SSD, microSD, fusibles e interruptores | <https://www.falabella.com.pe/falabella-pe/product/155618417/bateraa-lifepo4-goldenmate-12v-10ah-bms-ip67-5000-ciclos><br><https://www.falabella.com.pe/falabella-pe/product/158630291/bateria-nermak-lifepo4-12v-20ah-ciclo-profundo-2000-ciclos><br><https://www.falabella.com.pe/falabella-pe/product/159932959/ssd-kingspec-128gb-m-2-2242-nvme-pcie-3-0-x2-bm-key><br><https://www.falabella.com.pe/falabella-pe/product/159238184/tarjeta-de-memoria-microsd-64gb-extreme-pro-4k-hdr-a2-v60-con-adaptador><br><https://www.falabella.com.pe/falabella-pe/product/157324117/interruptor-de-bateria-12v-48v-universal-para-auto-autocaravana-y-barco><br><https://www.falabella.com.pe/falabella-pe/product/155449922/1-juego-de-portafusibles-en-linea-mini-tipo-cuchilla-impermeable-con-fusible-10a><br><https://www.falabella.com.pe/falabella-pe/product/140636555/UNIDAD-DE-ESTADO-SOLIDO-SSD-25-SATA-256GB-ADATA-SU650><br><https://www.falabella.com.pe/falabella-pe/product/159275261/case-externo-para-disco-duro-hdd-ssd-2-5-pulgadas-sata-usb-3-0-5gbps-con-cable-y-adaptador-tipo-c><br><https://www.falabella.com.pe/falabella-pe/product/155603105/cargador-bateraa-lifepo4-lvyuan-14-6v-20a-smart-12v> | 2026-11-21 | Goldenmate 10 Ah S/ 239 y Nermak 20 Ah S/ 299, ambas importadas desde EE. UU.; KingSpec 128 GB S/ 149,80; SanDisk 64 GB A2 S/ 64,90; desconectador 12–48 V S/ 46,90; portafusibles S/ 15,90; ADATA 256 GB S/ 185,90; caja USB S/ 24,80; cargador LVYUAN 20 A S/ 359 | Alta en precio; media en stock y plazo |
| F-24 | Autosolar — LiFePO4 12 V 100 Ah | <https://autosolar.pe/baterias-de-litio-12v/bateria-de-litio-12v-128kwh-fla12100-felicity-solar> | 2026-11-21 | Batería LiFePO4 12 V 1,28 kWh (100 Ah) S/ 933,33; sobredimensionada para el mini demo | Alta en precio |
| F-25 | Adafruit — HAT M.2, BNO085 y RPLIDAR A1 | <https://www.adafruit.com/product/5902><br><https://www.adafruit.com/product/4754><br><https://www.adafruit.com/product/4010> | 2026-11-21 | HAT M.2+ US$ 17,40; BNO085 US$ 29,50; RPLIDAR A1 US$ 99,95; todos con stock | Alta |
| F-26 | Pololu — motor 37D, driver dual y ruedas | <https://www.pololu.com/product/4753><br><https://www.pololu.com/product/3751><br><https://www.pololu.com/product/1435> | 2026-11-21 | Motor 50:1 37D 12 V con encoder US$ 60,95; driver dual G2 18v18 para Pi US$ 74,95; ruedas 90 × 10 mm US$ 9,49 el par | Alta |
| F-27 | Print3D.pe — servicio de impresión 3D (Trujillo) | <https://print3d.pe/> | 2026-11-21 | Servicio de impresión 3D en Trujillo; vende TPU y materiales técnicos; precios por pieza a cotizar | Media |
| F-28 | Electrónica STEM — Pi 5 8 GB (referencia de precio) | <https://www.electronicastem.pe/product/raspberry-pi-5-8gb-ram> | 2026-11-21 | Pi 5 8 GB listada a S/ 440, pero agotada; sirve para mostrar que el precio bajo no implica stock | Media |
| F-29 | Litio Energy — packs de litio a medida | <https://litioperu.com/> | 2026-11-21 | Armado y reparación de baterías de litio; cotizar pack 4S LiFePO4 con BMS ≥ 20 A | Media |

### Historial de consultas de abastecimiento

| Fecha | Fuentes | Resultado |
|---|---|---|
| 2026-11-21 | F-19, F-20, F-21 | Cómputo, LiDAR, motores, drivers y perfil: precios y stock local verificados |
| 2026-11-21 | F-22, F-23, F-24, F-29 | IMU, baterías, almacenamiento y protección: opciones locales e importadas |
| 2026-11-21 | F-25, F-26, F-27, F-28 | Importación y impresión 3D: alternativas para los componentes sin stock exacto |

---

## Fuentes de la propuesta ESP32 y batería Li-ion (2026-11-21)

Consulta de hojas de datos, catálogos y disponibilidad local del 2026-11-21.
La propuesta no está aprobada; ver
[`03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md`](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md).

| ID | Fuente | URL | Fecha | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-30 | Bracsan — celda EVE INR18650/35V | <https://bracsan.pe/producto/bateria-de-litio-li-ion-recargable-3-7v-3500mah-eve-inr18650-35v/><br><https://bracsan.pe/wp-content/uploads/EVE-INR18650-35V.pdf> | 2026-11-21 | Celda Li-ion 18650, 3500 mAh, 3,6 V nominal, 50 g; descarga máxima 10,2 A “not for cycle life”; UN38.3/IEC62133; S/ 19 con stock | Alta |
| F-31 | Bracsan — BMS, cargador y materiales de pack | <https://bracsan.pe/producto/modulo-para-carga-de-baterias-de-li-ion-bms-3s-25a-11-1v-12v-12-6v-18650-bc-3s25a/><br><https://bracsan.pe/producto/cargador-para-bateria-de-litio-li-ion-12-6v-3a-jx-12630/><br><https://bracsan.pe/producto/platina-niquel-para-conexion-de-baterias-18650-x-metro-1mt/><br><https://bracsan.pe/producto/espaciadores-3x1-para-bateria-de-li-ion-3-celda-18650/><br><https://bracsan.pe/producto/soldador-de-punto-portatil-recargable-10000mah-para-bateria/> | 2026-11-21 | BMS 3S 25A S/ 18; cargador 12,6 V 3 A S/ 48; nickel 1 m S/ 5; espaciadores 3×1 S/ 0,60; soldador de punto S/ 390; todos con stock | Alta en precio; media en especificaciones |
| F-32 | Espressif — ESP32-C6 datasheet | <https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf> | 2026-11-21 | RISC-V 160 MHz; 512 KB SRAM; 30/22 GPIO; 6 LEDC; 1 MCPWM; 4 PCNT; 7 ADC; 2 I²C; Wi-Fi 6, BLE 5.3, 802.15.4 | Alta (fabricante) |
| F-33 | Espressif — ESP32-S3 datasheet | <https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf> | 2026-11-21 | Xtensa LX7 dual-core 240 MHz; 512 KB SRAM; 45 GPIO; 8 LEDC; 2 MCPWM; 4 PCNT; 20 ADC; 2 I²C; USB OTG; PSRAM opcional | Alta (fabricante) |
| F-34 | micro-ROS — ESP-IDF component | <https://github.com/micro-ROS/micro_ros_espidf_component> | 2026-11-21 | Soporte probado con ESP32, S2, S3, C3 y C6; ESP-IDF v5.4–v6.0; Jazzy (24.x) | Alta |
| F-35 | Disponibilidad local de DevKitC S3/C6 | <https://www.teslaelectronic.com.pe/producto/nodemcu-esp32-s3-devkitc-1-n16r8-tipo-usb-c/><br><https://mtlab.pe/producto/esp32-c6-devkitc-1-n8-placa-de-desarrollo-espressif/><br><https://naylampmechatronics.com/espressif-esp/1206-esp32-s3-devkitc-1-44-pin-esp32-s3-wifi-usb-c.html><br><https://www.electromania.pe/producto/seeed-studio-xiao-esp32-c6-tape-reel/> | 2026-11-21 | S3 DevKitC N16R8 S/ 110 en Tesla (4 unidades, Trujillo); C6 DevKitC N8 S/ 100 en MTLAB (últimas, Lima); S3 Naylamp S/ 50 agotado; XIAO C6 S/ 39 en Electromanía | Alta en precio; media en stock |
| F-36 | I²C, level shifter y optoacoplador en Perú | <https://www.electromania.pe/producto/modulo-i2c-8-canales-tca9548a/><br><https://www.electromania.pe/producto/convertidor-de-nivel-logico-3-3-5v-de-4-lineas/><br><https://www.teslaelectronic.com.pe/producto/multiplexor-i2c-tca9548a-8ch/><br><https://www.teslaelectronic.com.pe/producto/pc817-optocoplador-fototransistor/> | 2026-11-21 | TCA9548A S/ 5 (Electromanía) o S/ 10 (Tesla); level shifter 4 líneas S/ 3; PC817 S/ 2 | Alta |
| F-37 | ROS 2 Jazzy — `diff_drive_controller` | <https://control.ros.org/jazzy/doc/ros2_controllers/diff_drive_controller/doc/userdoc.html> | 2026-11-21 | Interfaz de control diferencial, `cmd_vel`, `odom`, `joint_states`, parámetros de rueda | Alta |
| F-38 | Hifisac — catálogo y venta por WhatsApp | <https://hifisac.com/shop><br><https://hifisac.com/shop/esp32-s3-n16r8-placa-de-desarrollo-esp32-s3-n16r8-de-44-pines-conector-tipo-c-16-mb-de-memoria-flash-y-8-mb-de-psram-5527><br><https://hifisac.com/shop/bc-3s25a-modulo-bms-para-proteccion-de-carga-y-descarga-de-baterias-de-litio-3s-11-1v-12v-12-6v-25a-18650-3104><br><https://hifisac.com/shop/ina219-sensor-programable-de-corriente-y-voltaje-de-0-to-26-dc-ina219-para-fuentes-de-alimentacion-4181> | 2026-11-21 | Catálogo con precios: ESP32-S3 N16R8 S/ 49, BMS 3S 25A S/ 9,90, INA219 S/ 8,20, level shifter S/ 2,70; **todas las fichas probadas marcan “Sin existencias”**; venta por WhatsApp (+51 964 104 648) | Media en precio; baja en stock |

### Historial de consultas de la propuesta ESP32/Li-ion

| Fecha | Fuentes | Resultado |
|---|---|---|
| 2026-11-21 | F-30, F-31 | Celda EVE 35V y materiales de pack 3S2P/3S3P verificados |
| 2026-11-21 | F-32, F-33, F-34 | C6 vs S3 y soporte micro-ROS Jazzy verificados |
| 2026-11-21 | F-35, F-36, F-37 | Disponibilidad local, I²C/level shifter/opto y control diferencial |

---

## Fuentes de percepción 3D (2026-11-21)

Consulta de documentación de Raspberry Pi, fabricantes de sensores y guías
prácticas para evaluar dos Camera Module 3 más un ToF multizona. La propuesta
no está aprobada; ver
[`percepcion-3d.md`](percepcion-3d.md) y la pregunta abierta OQ-11.

| ID | Fuente | URL | Fecha | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-39 | Raspberry Pi 5 Product Brief (RP-008348-DS-10) | <https://pip-assets.raspberrypi.com/categories/892-raspberry-pi-5/documents/RP-008348-DS-10-raspberry-pi-5-product-brief.pdf> | 2026-11-21 | Dos transceptores MIPI de 4 carriles y 1,5 Gbps; cualquier combinación de hasta dos cámaras o pantallas; dos puertos USB 3.0; PCIe 2.0 x1 | Alta (fabricante) |
| F-40 | Raspberry Pi Camera Module 3 Product Brief (RP-008151-DS-1) | <https://pip-assets.raspberrypi.com/categories/786-raspberry-pi-camera-module-3/documents/RP-008151-DS-1-camera-module-3-product-brief.pdf> | 2026-11-21 | IMX708 de 11,9 MP, 4608 × 2592, píxel 1,4 µm, diagonal 7,4 mm; 1080p50, 720p100, 480p120; RAW10; estándar 4,74 mm f/1,8 y 66° H (75° diagonal); wide 2,75 mm f/2,2 y 102° H (120° diagonal); enfoque 10 cm–∞ / 5 cm–∞; VCM con PDAF; FPC de 15 pines; 0–50 °C; producción hasta enero de 2030 | Alta (fabricante) |
| F-41 | Arducam — 12MP IMX708 / Camera Module 3 | <https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708><br><https://www.arducam.com/blog/official-camera-module-3-a-closer-look/> | 2026-11-21 | Obturación progresiva (rolling shutter); 2 carriles MIPI por defecto, configurable a 4; modos 2304 × 1296 a 56 fps, 2304 × 1296 a 30 fps HDR, 1536 × 864 a 120 fps; consumo máximo 1,16 W; precio de lista 25 USD (estándar) y 35 USD (wide) | Alta en especificaciones; media en precio (no es tienda oficial) |
| F-42 | Raspberry Pi Documentation — `rpicam-apps` multiple cameras | <https://www.raspberrypi.com/documentation/computers/camera_software.html#multiple-cameras><br><https://github.com/raspberrypi/documentation/blob/master/documentation/asciidoc/accessories/camera/rpicam-apps-multicam.adoc> | 2026-11-21 | `libcamera` no ofrece estéreo nativo; dos cámaras se ejecutan en procesos separados y no se sincroniza el 3A; existe sincronía software servidor/cliente con coincidencia de inicio de frame en «varias decenas de microsegundos»; se recomienda pasar el 3A a manual | Alta (fabricante) |
| F-43 | Raspberry Pi — Global Shutter Camera / documentación de cámara | <https://www.raspberrypi.com/documentation/accessories/camera.html#global-shutter-camera><br><https://www.raspberrypi.com/products/global-shutter-camera/> | 2026-11-21 | IMX296 mono de 1,6 MP (1456 × 1088), 60 fps, montura C/CS, entrada de disparo externo XTR; precio 50 USD; solo esta cámara tiene sincronía hardware en la documentación de Raspberry Pi | Alta (fabricante) |
| F-44 | `camera_ros` — nodo ROS 2 para libcamera | <https://github.com/christianrauch/camera_ros> | 2026-11-21 | En Ubuntu 24.04 + Jazzy, la CM3 requiere compilar el fork de `libcamera` de Raspberry Pi; el paquete upstream no detecta IMX708; un nodo abre una cámara; publica `image_raw`, `camera_info` y parámetros de calibración | Alta (documentación del proyecto) |
| F-45 | Pololu — VL53L8CX Time-of-Flight 8×8-Zone Carrier | <https://www.pololu.com/product/3419> | 2026-11-21 | 8 × 8 o 4 × 4 zonas; 65° diagonal (45° H/V); 20 mm–4 m; 4 m en oscuridad y ~2,8 m a 5 000 lx con blanco reflectante; 60 Hz; 1 mm; 100 mA típicos y 150 mA de pico; 3,2–5,5 V; I²C 1 MHz o SPI 3 MHz; 940 nm Class 1; 24,95 USD; recomienda cables de I²C < 8 cm | Alta (distribuidor; datos del fabricante) |
| F-46 | Luxonis — OAK-D Lite | <https://docs.luxonis.com/hardware/products/OAK-D%20Lite><br><https://shop.luxonis.com/products/oak-d-lite-1> | 2026-11-21 | Base estéreo de 7,5 cm; rango ideal 0,8–12 m; MinZ 20–80 cm; dos OV7251 mono global shutter 640 × 480; RGB IMX214; 4 TOPS; 2,5–3 W base + hasta 0,5 W de profundidad; USB 2/3; IMU BMI270; 269 USD | Alta (fabricante) |
| F-47 | Vadzo — Stereo Camera Raspberry Pi 5 Setup Guide | <https://www.vadzoimaging.com/post/stereo-camera-raspberry-pi-5> | 2026-11-21 | Guía práctica: dos puertos de 22 pines y 4 carriles; no hay sincronía hardware por defecto; emparejar por `SensorTimestamp`; bloquear exposición, ganancia y enfoque; base rígida de 50–100 mm; calibrar a la resolución de trabajo; ejemplo de error de 1 px a 3 m con f = 1 000 px y B = 60 mm | Media (guía de fabricante, no norma) |
| F-48 | Raspberry Pi — AI Camera | <https://www.raspberrypi.com/products/ai-camera/><br><https://www.raspberrypi.com/news/raspberry-pi-ai-camera-on-sale-now> | 2026-11-21 | Sensor IMX500 de 12 MP con inferencia en el sensor; 70 USD; no es estéreo; la profundidad requeriría un modelo monocular | Alta (fabricante) |
| F-49 | ROS 2 `image_pipeline` — `stereo_image_proc` | <https://github.com/ros-perception/image_pipeline/tree/jazzy/stereo_image_proc> | 2026-11-21 | Nodo de estéreo para ROS 2 Jazzy: rectificación, disparidad y nube de puntos; consume `camera_info` de ambas cámaras | Alta (ROS) |
| F-50 | `tof_imager_ros` — driver ROS 2 para VL53L5CX/L7CX | <https://github.com/adityakamath/tof_imager_ros> | 2026-11-21 | Driver ROS 2 para sensores ToF 8 × 8; publica nube de puntos; no lista VL53L8CX, que requeriría portar la API o usar la ULD de ST | Media (proyecto de terceros) |
| F-51 | ST — VL53L8CX datasheet y ULD API | <https://www.st.com/resource/en/datasheet/vl53l8cx.pdf><br><https://www.st.com/en/embedded-software/stsw-img040.html> | 2026-11-21 | Documentación de registro/API del sensor; el PDF no se pudo descargar directamente desde el host y los datos usados se contrastaron con F-45 | Media (fabricante; descarga bloqueada) |

### Historial de consultas de percepción 3D

| Fecha | Fuentes | Resultado |
|---|---|---|
| 2026-11-21 | F-39, F-40, F-41 | Pi 5 con dos CSI de 4 carriles; CM3 de 2 carriles, rolling shutter y autofocus |
| 2026-11-21 | F-42, F-43, F-44 | Estéreo no nativo; sincronía software; solo GS con XTR; fricción de `camera_ros` en Ubuntu |
| 2026-11-21 | F-45, F-50, F-51 | ToF 8 × 8: 4 m en oscuridad, 2,8 m a 5 klx, 100 mA; driver para L5CX/L7CX |
| 2026-11-21 | F-46, F-47, F-48, F-49 | Alternativas OAK-D Lite, GS, AI Camera y pipeline estéreo de ROS 2 |

---

## Fuentes del inventario de facultad (2026-11-21)

El inventario es una declaración del usuario, no una medición. Se registra para
que el análisis de reutilización y las brechas tengan trazabilidad; los modelos,
cantidades y el estado físico siguen pendientes de verificación.

| ID | Fuente | URL | Fecha de acceso | Qué se extrajo | Confianza |
|---|---|---|---|---|---|
| F-52 | Inventario de materiales de facultad | Sin URL (archivo `inventario actual.txt`, raíz del repositorio) | 2026-11-21 | Pi 4 B, Argon Pi 4, Arduino «XD», 3 × TB6612FNG, PCA9685, GY-271, VL53L0/1XV2, MPU-6050, LM2596/HW-411, Camera V2.1, 4 × SG90, 6 × MG90S, 6 × motorreductor 10F125 sin encoder, LilyGO 7600X, 4 × panel 6 V/720 mA, LiPo 3S 2200 mAh 25C | Media: declaración del usuario; sin verificar modelos, cantidades ni estado |
| F-53 | LilyGO — T-SIM7600X documentation | <https://wiki.lilygo.cc/products/t-sim-series/t-sim7600x> | 2026-11-21 | ESP32-WROVER-B (4 MB flash, 8 MB PSRAM) + SIM7600 LTE Cat-4; GNSS multi-constelación; Nano SIM; soporte 18650; 2 × 16 pines; 1 × USB-C del ESP32; el módem se controla por UART (GPIO26/27); variantes E/G/SA-H con bandas distintas; **no es ESP32-S3 ni módem USB directo** | Alta (fabricante) |
| F-54 | Raspberry Pi 4 Model B — specifications | <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/> | 2026-11-21 | BCM2711, 8 GB LPDDR4, Gigabit Ethernet, 2 × USB 3.0, 2 × USB 2.0, 1 × CSI, 1 × DSI, 2 × micro-HDMI, 5 V/3 A USB-C, 40 pines GPIO; sin PCIe expuesto (almacenamiento por USB 3.0 o microSD) | Alta (fabricante; ficha web) |
| F-55 | Argon 40 — Argon ONE V2 Case for Raspberry Pi 4 | <https://argon40.com/products/argon-one-v2-case-for-raspberry-pi-4> | 2026-11-21 | Carcasa de aluminio con función de disipador, ventilador, botón de encendido, GPIO accesible en la tapa, todos los puertos en la parte trasera y 2 × HDMI; **no documenta acceso al CSI** | Alta en características; media en acceso al CSI |
| F-56 | Raspberry Pi — Camera Module V2 | <https://www.raspberrypi.com/products/camera-module-v2/> | 2026-11-21 | Sensor Sony IMX219 de 8 MP, 3280 × 2464, CSI de 15 pines, enfoque fijo; obturador de rodillo (rolling shutter) | Alta (fabricante; rolling shutter por datasheet del sensor) |
| F-57 | Electromanía — TFmini Plus 12 m (ToF de piso) | <https://www.electromania.pe/producto/tfmini-plus-sensor-lidar-tof-de-distancia-de-punto-unico-12m-uart-i2c-ip65/> | 2026-11-21 | TFmini Plus de 12 m, UART/I²C, IP65; S/ 330; stock declarado 8 | Alta en precio; media en stock |
| F-58 | Memory Kings — cámara web 4K Logitech Brio | <https://www.memorykings.pe/listados/176/camaras-webcam> | 2026-11-21 | Brio 4K a S/ 487 (oferta; lista S/ 612), stock > 10; precio con IGV y sin flete | Alta en precio; media en stock |
| F-59 | Hifisac — módulo cargador TP5100-84 | <https://hifisac.com/shop/category/baterias-240?search=cargador> | 2026-11-23 | TP5100-84 seleccionable 4,2 / 8,4 V por S/ 5,60; entrada 5–18 V, buck, carga hasta 2 A; sirve para packs 1S/2S | Alta en precio; media en stock online |
| F-60 | MTLAB — módulo step-up DC-DC 150–400 W | <https://mtlab.pe/producto/modulo-step-up-dc-dc-elevador-de-voltaje-150w-200w-400w/> | 2026-11-23 | Step-up de 150 / 200 / 400 W con 10–15 A; rango de precio S/ 25–55; se elige el de 400 W para el riel de tracción | Media (precio por rango de potencia) |
