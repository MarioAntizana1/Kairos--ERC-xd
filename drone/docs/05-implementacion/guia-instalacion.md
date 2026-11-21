# Guía de instalación y puesta en marcha

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Software
>
> **No probada en hardware.** Los comandos son una guía; se validan y se
> registran como evidencia cuando exista la Pi 5. No presentar como “instalado”
> lo que no se ejecutó.

## 1. Materiales

- Raspberry Pi 5 8 GB.
- 2 × Camera Module 3 Standard + cables 22→15.
- ToF VL53L1X o VL53L5CX.
- HAT+ M.2 + SSD NVMe 128 GB (o USB/microSD).
- Fuente oficial 27 W (banco).
- Active Cooler.
- Monitor/SSH, teclado, mouse.
- Multímetro.

## 2. Sistema operativo

1. Descargar **Raspberry Pi OS Bookworm 64-bit** con Raspberry Pi Imager.
   Alternativa: Ubuntu 24.04 64-bit para ROS 2 Jazzy.
2. Configurar hostname, usuario, SSH y WiFi en el Imager (sin secretos en el
   repo).
3. Grabar la microSD o el NVMe.
4. Arrancar y actualizar:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

5. Verificar versión y kernel:

```bash
uname -a
cat /etc/os-release
```

## 3. Almacenamiento NVMe (si aplica)

1. Montar el HAT+ M.2 y el SSD **con la Pi apagada y desconectada**.
2. Verificar que el SSD es M.2 2242 y que el HAT lo soporta.
3. Arrancar y comprobar:

```bash
lsblk
sudo dmesg | grep -i nvme
```

4. Si se quiere arrancar por NVMe, actualizar la EEPROM y configurar el orden de
   arranque según la documentación oficial. **No** cambiar el orden sin una
   microSD de rescate.
5. Copiar el sistema a NVMe o instalar desde cero; registrar el método.

> Si el HAT no está disponible, usar USB 3.0 o microSD A2. Es más lento y menos
> robusto; registrarlo como limitación.

## 4. Cámaras

1. **Apagar y desconectar** la Pi antes de conectar/desconectar el FPC.
2. Conectar la cámara izquierda a `CAM0` y la derecha a `CAM1` con el cable
   22→15. Verificar que el lado de contactos esté correcto.
3. Arrancar y listar:

```bash
rpicam-hello --list-cameras
```

4. Probar cada cámara:

```bash
rpicam-still --camera 0 -o left.jpg --width 2304 --height 1296
rpicam-still --camera 1 -o right.jpg --width 2304 --height 1296
```

5. Probar captura dual (si la versión de `rpicam-apps` lo soporta) o Picamera2:

```python
from picamera2 import Picamera2
cam0 = Picamera2(0)
cam1 = Picamera2(1)
print(cam0.sensor_resolution, cam1.sensor_resolution)
```

6. Verificar foco, exposición y balance de blancos; bloquear el foco antes de
   calibrar.

> **No hot-plug del FPC.** Descargar estática y no forzar el conector.

## 5. ToF de piso (TFmini Plus)

1. Montar el **TFmini Plus** en la base, mirando al piso, con una
   ventana/abertura y el eje lo más vertical posible.
2. Alimentar a 5 V y GND; conectar UART (TX/RX) o I²C (SDA/SCL). Verificar el
   nivel lógico: si el módulo entrega 5 V en las líneas, usar **level shifter**
   antes de la Pi 5.
3. Habilitar el UART en `raspi-config` o `config.txt`; verificar el dispositivo:

```bash
ls /dev/ttyAMA* /dev/serial0 2>/dev/null
```

4. Si se usa I²C, instalar herramientas y detectar:

```bash
sudo apt install -y i2c-tools
i2cdetect -y 1
```

5. Leer a **0,5, 1, 2, 4 y 6 m** contra el piso; comparar con cinta métrica.
6. Configurar la tasa (50/100 Hz), unidades y umbral de validez en el driver.

> El **TFmini Plus** es de 12 m y es la base para 6 m; a 6 m el spot mide ~21 cm.
> El VL53L1X y el VL53L5CX son de 4 m y **no alcanzan** para la competencia;
> quedan para banco. El VL53L5CX requiere firmware (~90 KB) al arrancar.

## 6. OpenCV y Picamera2

```bash
sudo apt install -y python3-opencv python3-picamera2 python3-numpy
python3 -c "import cv2, picamera2; print(cv2.__version__, picamera2.__version__)"
```

- Si `cv2.ximgproc` no está disponible, usar SGBM sin WLS.
- Fijar las versiones en el `metadata.json` de la evidencia.
- No usar `pip install opencv-python` si ya existe el paquete del sistema; puede
  romper la integración con libcamera.

## 7. ROS 2 (si se decide)

En Ubuntu 24.04:

```bash
sudo apt install -y ros-jazzy-desktop
source /opt/ros/jazzy/setup.bash
ros2 run demo_nodes_cpp talker
```

En Raspberry Pi OS, ROS 2 Jazzy no tiene binarios oficiales; evaluar contenedor,
compilación o Python puro. **No** mezclar ROS 2 de Ubuntu con paquetes de
Raspberry Pi OS sin un plan.

## 8. MAVLink

1. Conectar la FC por UART o USB.
2. Instalar `pymavlink` o `mavros` según la decisión.
3. Verificar `HEARTBEAT`, `ATTITUDE` y `TIMESYNC`.
4. No enviar comandos de motor; solo leer pose y publicar estado/obstáculos.
5. Registrar el dialecto y la versión.

## 9. Energía de vuelo

1. **No** conectar el UBEC al dron sin fusible y sin verificar polaridad.
2. Ajustar el UBEC a 5,1–5,2 V; medir con multímetro.
3. Conectar USB-C o GPIO 5 V/GND con cable 20 AWG; capacitor 1000 µF.
4. Medir tensión en carga; debe mantenerse > 4,9 V.
5. Verificar `vcgencmd get_throttled` = `0x0`.
6. Hacer una prueba de 20 min con carga y registrar temperatura.

## 10. Calibración

1. Imprimir un tablero ChArUco (7×5, cuadros 30 mm) en papel rígido o ACMA.
2. Capturar 15–25 imágenes por cámara y 20–30 pares estéreo.
3. Ejecutar la calibración con OpenCV y guardar el YAML.
4. Verificar RMS, baseline y error epipolar.
5. Guardar el YAML con hash y registrar la evidencia.
6. Repetir después de 10 min de operación para medir deriva térmica.

## 11. Registro y evidencia

```bash
make evidence SLUG=instalacion-pi5
# ejecutar los comandos y guardar logs en la carpeta
make seal DIR=docs/08-evidencia/artefactos/<carpeta>
```

- Adjuntar `rpicam-hello --list-cameras`, `i2cdetect`, versión de OpenCV,
  temperatura y capturas.
- No declarar “aprobado” sin revisar los logs.

## 12. Problemas comunes

| Síntoma | Causa probable | Acción |
|---|---|---|
| No aparece la cámara | Cable 15 pines, lado incorrecto, CAM0/1 | Revisar cable y conector; probar otra cámara |
| Imagen verde/rosa | Formato o balance | Ajustar formato y balance; usar `rpicam` |
| No aparece el ToF | I²C, 3,3 V, dirección | `i2cdetect`; revisar soldadura |
| NVMe no arranca | EEPROM/orden | Actualizar EEPROM; rescatar por microSD |
| Throttling | Caja cerrada | Active Cooler, ventilación, bajar carga |
| Brownout | UBEC/cable | Medir tensión; cable más corto; UBEC mayor |

## 13. Referencias

- F-04, F-23, F-25, F-26, F-27.
- [`entorno-desarrollo.md`](entorno-desarrollo.md).
