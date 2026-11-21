# Entorno de desarrollo

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Software

## 1. Host de desarrollo actual

| Campo | Valor |
|---|---|
| SO | Linux (host de desarrollo) |
| Python | 3.14 |
| Git | Sí (repo local; commit puede ser `no-git` si no se inicializa) |
| Raspberry Pi | **No conectada** |
| Cámaras / ToF | **No conectados** |
| ROS 2 | No instalado en el host |
| OpenCV | No validado en el host |

> El host actual sirve para documentación, BOM y validadores. **No** sirve para
> declarar probada la captura, la calibración ni el pipeline.

## 2. Entorno objetivo

| Campo | Valor |
|---|---|
| Cómputo | Raspberry Pi 5 8 GB |
| Cámaras | 2 × Camera Module 3 Standard |
| ToF de piso | TFmini Plus 12 m (base); VL53L1X/8×8 ≤4 m (alternativas) |
| Almacenamiento | HAT+ M.2 + SSD NVMe 128 GB (o USB 3.0/microSD) |
| Energía | UBEC 5 V/5 A, fusible 5 A, capacitor 1000 µF |
| SO | **Raspberry Pi OS Bookworm 64-bit** o **Ubuntu 24.04 + ROS 2 Jazzy** (decisión abierta, OQ-06) |
| Cámara | `rpicam-apps`, libcamera, Picamera2 |
| Visión | OpenCV 4.x |
| Middleware | ROS 2 Jazzy (propuesto) |
| Vuelo | MAVLink / MAVROS |
| Python | 3.11/3.12 (el que traiga la distro) |

### Trade-off de sistema operativo

| Opción | Ventajas | Desventajas |
|---|---|---|
| **Raspberry Pi OS Bookworm** | Mejor soporte de cámara/Picamera2; estable | ROS 2 Jazzy no tiene binarios oficiales para Bookworm |
| **Ubuntu 24.04 + ROS 2 Jazzy** | Stack del rover; binarios ROS 2 | Soporte de cámara/Picamera2 más frágil; más dependencias |

**Propuesta:** empezar con Raspberry Pi OS para validar cámara y calibración;
decidir ROS 2 vs Python puro después de medir. Si se necesita ROS 2, evaluar
Ubuntu 24.04 o un contenedor. No instalar ambos en la misma tarjeta sin un plan
de arranque.

## 3. Versiones a fijar

| Componente | Versión | Cómo se registra |
|---|---|---|
| OS | Imagen oficial (fecha) | `metadata.json` |
| Kernel | `uname -r` | `metadata.json` |
| libcamera / rpicam-apps | `rpicam-hello --version` | `metadata.json` |
| Picamera2 | `python3 -c "import picamera2; print(picamera2.__version__)"` | `metadata.json` |
| OpenCV | `python3 -c "import cv2; print(cv2.__version__)"` | `metadata.json` |
| ROS 2 | `ros2 --version` / distro | `metadata.json` |
| MAVLink | `pymavlink` / dialecto | `metadata.json` |
| Calibración | `calibration_id` | YAML + hash |

## 4. Hardware de banco

- Pi 5 + fuente oficial 27 W (banco).
- 2 × CM3 + cables 22→15.
- ToF + cables Dupont/JST.
- Monitor HDMI, teclado, mouse o SSH.
- Ventilador externo para pruebas térmicas.
- Multímetro y fuente regulable (deseable).

## 5. Red

- SSH por Ethernet o WiFi 5 GHz.
- Clave pública; no contraseñas débiles.
- Firewall; no exponer SSH a Internet.
- Deshabilitar WiFi/BT en vuelo si interfieren (RNF-11).

## 6. Herramientas

```bash
# Cámara
rpicam-hello --list-cameras
rpicam-still -o test.jpg --width 2304 --height 1296

# I²C
sudo apt install -y i2c-tools
i2cdetect -y 1

# Térmica/tensión
vcgencmd measure_temp
vcgencmd get_throttled

# ROS 2 (si aplica)
ros2 topic list
ros2 topic hz /vision/depth
```

## 7. Estructura del repo

```text
docs/                  Documentación SDLC
scripts/docs/          Validadores
scripts/evidence/      Evidencia
vision_ws/             (futuro) workspace ROS 2 / Python
config/calibration/    (futuro) YAML de calibración, fuera de git si es local
```

> Las calibraciones locales y secretos van en `~/.config/drone/` o
> `config/calibration/` ignorado por git. No subir claves.

## 8. Riesgos del entorno

| Riesgo | Mitigación |
|---|---|
| Ubuntu 24.04 no detecta la CM3 | Probar Raspberry Pi OS; registrar | 
| OpenCV sin `ximgproc` | Usar SGBM sin WLS; compilar extra si hace falta |
| ROS 2 consume demasiada CPU | Perfilar; fallback Python |
| NVMe no arranca | Actualizar EEPROM; probar USB/microSD |
| TFmini Plus no aparece | UART/I²C, 5 V, level shifter, puerto | `ls /dev/ttyAMA*`; `i2cdetect`; revisar cable |
| Reloj sin RTC | Sincronizar por NTP/MAVLink; registrar offset |

## 9. Referencias

- F-04, F-23, F-25, F-26, F-27.
- [`guia-instalacion.md`](guia-instalacion.md).
