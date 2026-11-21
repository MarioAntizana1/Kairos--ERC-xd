# ADR-0008 — ESP32-S3 como interfaz de tiempo real

> Estado: Propuesta · Fecha: 2026-11-21 · Responsable: Hardware / Tech Lead · Reemplaza a: —

## Contexto

La Raspberry Pi 4 es el cerebro de navegación: ejecuta Ubuntu 24.04, ROS 2
Jazzy, Nav2, AMCL y los nodos de misión. No es una plataforma de tiempo real:
el control de motores a 100 Hz compite con Nav2, la pila USB y el sistema
operativo. Además, la Pi 4 no tiene suficientes canales PWM hardware para los
motores, los servos y los sensores de la variante 6×6.

La BOM base necesita controlar dos motores, leer dos encoders, consultar una
IMU y un monitor de batería por I²C, y leer la parada de emergencia. La variante
6×6 añade seis motores, seis encoders y seis servos. Todo eso es de baja tasa
comparado con el LiDAR, pero exige un bucle determinista y un *watchdog* que
detenga los motores si la Pi se cuelga o se pierde la comunicación.

La propuesta es añadir un microcontrolador entre la Pi 4 y los actuadores:
**la Pi 4 decide, el MCU ejecuta**. La Pi conserva Nav2, SLAM, LiDAR, cámara y
registro; el MCU se encarga de PWM, encoders, IMU, batería, e-stop y
expansiones I²C.

Restricciones:

- Lógica de 3,3 V; los encoders FIT0185 entregan 5 V y necesitan adaptación.
- Entorno con motores y ruido eléctrico; conviene una alimentación de 5 V
  separada para la lógica.
- La parada de emergencia debe cortar potencia en hardware; el MCU solo la
  supervisa.
- El ERC 2027 no tiene reglamento publicado; cualquier cambio de batería o
  electrónica debe revisarse cuando salga.
- Hay stock local de ESP32-S3 y ESP32-C6, pero con disponibilidad irregular.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste local | Madurez |
|---|---|---|---|---|
| **A. ESP32-S3-DevKitC-1 N16R8** | 45 GPIO; 8 canales LEDC; 2 MCPWM; 4 PCNT; 20 ADC; 2 I²C; doble núcleo 240 MHz; 8 MB PSRAM; USB nativo; micro-ROS Jazzy | Más caro que C6; más pines que los necesarios para el demo; consumo algo mayor | S/ 110 (Tesla, stock) / S/ 49 (Hifisac, cotizar; web sin stock) | Alta |
| **B. ESP32-C6-DevKitC-1 N8** | 30/22 GPIO; 6 LEDC; 1 MCPWM; 4 PCNT; 7 ADC; 2 I²C; RISC-V 160 MHz; Wi-Fi 6, BLE 5.3, Thread/Zigbee; bajo consumo | Un solo núcleo; 6 LEDC justos para 6 motores; menos margen para 6×6; stock limitado en Lima | S/ 100 (MTLAB, últimas unidades) | Alta |
| **C. Seeed XIAO ESP32-C6** | Muy compacto; 11 GPIO/PWM; 7 ADC; 1 I²C; USB-C; S/ 39 | 11 GPIO no alcanzan para 2 motores con BTS7960 + 2 encoders + I²C + e-stop + LED; sin margen | S/ 39 (Electromanía) | Alta |
| **D. ESP32 DevKit V1 clásico** | 16 LEDC; 4 PCNT; 2 I²C; ~25 GPIO; muy disponible y barato | Arquitectura antigua; sin Wi-Fi 6/Thread; menos ADC; no es la placa objetivo | S/ 32–35 | Alta |
| **E. RP2040 / Teensy 4.1** | PWM/PIO determinista; muy buen control de motores; bajo coste; ya previsto en la variante 6×6 | Sin Wi-Fi/BLE; menos ADC/I²C; requiere puente serie y otro firmware | S/ 30–60 | Alta |
| **F. GPIO directo de la Pi 4** | Sin placa extra; menos piezas | PWM y tiempo real limitados; más carga para la Pi; pocos pines; frágil ante reinicios | S/ 0 | Media |

## Decisión

**Adoptar un ESP32-S3-DevKitC-1 N16R8 como interfaz de tiempo real entre la
Pi 4 y los actuadores/sensores de baja tasa, con micro-ROS sobre USB.** La Pi 4
sigue siendo el cerebro de navegación. La variante C6 queda como alternativa
válida para el demo de 2 motores; el RP2040/Teensy queda como alternativa si no
se necesita Wi-Fi y se prioriza el determinismo puro.

La decisión es **propuesta**: no cambia la BOM base ni la arquitectura aceptada
hasta que el PO y el responsable de Hardware la aprueben. La e-stop hardware
sigue siendo la protección primaria; el MCU solo la supervisa y publica su
estado.

### Reparto de responsabilidades

| Función | Pi 4 | ESP32-S3 |
|---|---|---|
| Nav2, AMCL, planificación | Sí | No |
| SLAM / LiDAR | Sí (USB) | No |
| Cámara / visión | Sí (CSI/USB) | No |
| `cmd_vel` → motores | Publica | Ejecuta PWM y dirección |
| Encoders → odometría | Publica `odom` o EKF | Lee PCNT y publica ticks/odom |
| IMU | Fusiona / EKF | Lee BNO085 por I²C y publica |
| Monitor de batería | Aborta por batería baja | Lee INA219/INA226 y publica |
| E-stop | Recibe estado | Lee contacto auxiliar; **no sustituye** el corte hardware |
| Servos 6×6 | Ordena ángulos | PCA9685 por I²C o PWM directo |
| Watchdog de comunicación | Heartbeat | Corta motores si no hay `cmd_vel`/heartbeat |
| Telemetría y logs | rosbag2 | Diagnóstico del MCU |

### Enlace Pi 4 ↔ ESP32-S3

- **Físico:** USB CDC (preferible el puerto USB nativo del DevKitC-1), cable
  corto y con ferrita; masa común y alimentación de 5 V separada para el MCU.
- **Middleware:** micro-ROS con `micro_ros_espidf_component` (ESP-IDF v5.4+,
  Jazzy). La Pi ejecuta `micro_ros_agent`.
- **Dispositivo estable:** regla udev por número de serie para
  `/dev/rover_mcu`; no depender de `/dev/ttyACM0`.
- **Topics:** ver [`interfaces.md`](../interfaces.md), sección 11.
- **Frecuencias:** control de motores 100 Hz; encoders 100 Hz; IMU 50–100 Hz;
  batería 1–5 Hz; heartbeat 10 Hz.
- **Watchdog:** si no llega `cmd_vel` en 500 ms, el MCU rampa a cero y deshabilita
  los drivers. Si la Pi se cuelga, el heartbeat también desaparece.
- **TF:** el MCU no publica `odom → base_footprint`; publica `/odom` y la Pi
  publica la transformada con `robot_localization` o un broadcaster. Así se
  evita duplicar TF.

### Alimentación y señal

- El ESP32-S3 se alimenta desde el rail de **5 V 3 A**, no desde el USB de la
  Pi, para evitar reinicios por ruido de motores. Masa común en estrella.
- Los encoders FIT0185 son de **5 V**: usar un adaptador de nivel de 4 canales
  (por ejemplo, TXB0104) antes de los GPIO de 3,3 V. No conectar 5 V directo.
- I²C a 3,3 V con pull-ups de 2,2–4,7 kΩ. BNO085 e INA219 pueden compartir bus;
  el TCA9548A se añade si hay direcciones repetidas o más sensores.
- La e-stop corta la potencia del driver en hardware. Un contacto auxiliar,
  mediante optoacoplador PC817, informa al MCU; el MCU no corta la potencia por
  software.
- Añadir precarga de 100 Ω / 5 W para los condensadores del driver y fusibles
  de rama.

## Consecuencias

### Positivas

- Bucle de motores y encoders a 100 Hz independiente de Linux y de Nav2.
- 45 GPIO, 8 LEDC, 2 MCPWM y 4 PCNT: margen para la variante 6×6 y para
  sensores adicionales.
- I²C ordenado con TCA9548A; sensores de baja tasa fuera de la Pi.
- La Pi 4 queda libre para Nav2, SLAM, cámara y evidencia.
- Hay stock local del S3 (Tesla Electronic, Trujillo) y del C6 (MTLAB, Lima).
- micro-ROS Jazzy está soportado en ESP-IDF para S3 y C6.
- El _watchdog_ y el estado de e-stop se pueden publicar como diagnósticos.

### Negativas / deuda asumida

- Placa, firmware, arnés y, más adelante, PCB propia: +S/ 180–200 y tiempo de
  integración.
- El S3 es de 3,3 V; los encoders de 5 V obligan a level shifter.
- micro-ROS añade agente, udev, versión de firmware y depuración.
- El MCU no es un controlador certificado de seguridad; la e-stop hardware y el
  fusible siguen siendo la protección primaria.
- USB puede ser sensible al ruido; conviene cable corto, ferrita y 5 V separado.
- La variante C6 de 6 LEDC puede quedarse corta para 6 motores + 6 servos; para
  6×6 se recomienda S3 o PCA9685 para los servos.

### Neutrales

- El LiDAR y la cámara siguen conectados a la Pi; el MCU no maneja alta tasa.
- Wi-Fi/BLE del ESP32 se puede dejar deshabilitado en operación para reducir
  latencia y consumo; el enlace principal es USB.
- La decisión de batería Li-ion 3S es independiente de este ADR, pero comparte
  el mismo diseño eléctrico y de protección.

## Criterios de revisión

Reabrir este ADR si:

1. La variante 6×6 necesita más de 8 PWM o más de 45 GPIO.
2. La latencia de micro-ROS supera 10 ms o el CPU del MCU supera 70 % en el
   bucle de control.
3. El reglamento del ERC 2027 exige una arquitectura o certificación distinta.
4. El S3 no está disponible a un precio razonable y el C6 sí.
5. Se decide que no se necesita Wi-Fi/telemetría y se prefiere RP2040/Teensy.
6. La e-stop o el _watchdog_ no pasan las pruebas de fallo seguro.

## Referencias

- F-32: ESP32-C6 datasheet, Espressif.
- F-33: ESP32-S3 datasheet, Espressif.
- F-34: micro-ROS component for ESP-IDF (soporta ESP32-S3 y ESP32-C6, Jazzy).
- F-35: disponibilidad local de DevKitC S3/C6.
- F-38: Hifisac, precios de referencia sin stock online.
- F-36: TCA9548A, level shifter y optoacoplador en tiendas peruanas.
- F-37: `diff_drive_controller` de ROS 2 Jazzy.
- [`interfaces.md`](../interfaces.md), sección 11.
- [`../../04-diseno/diseno-electrico.md`](../../04-diseno/diseno-electrico.md),
  sección 12.
- [`../../04-diseno/bom-peru.md`](../../04-diseno/bom-peru.md), secciones 4.6 y 4.7.
