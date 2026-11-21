# Guía de instalación

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Software
> **Entorno soportado:** Ubuntu 24.04 LTS (amd64 o arm64). En otro SO, usar VM o contenedor.

## 1. Requisitos

- Ubuntu 24.04 LTS.
- 4 GB RAM mínimo (8 GB recomendado para simulación).
- 20 GB de disco libre.
- Conexión a internet para la instalación inicial.
- Usuario con `sudo`.

## 2. Instalación de ROS 2 Jazzy

### 2.1 Revisar el script

```bash
cd rover
bash scripts/setup/install_ros_jazzy.sh --dry-run
```

El script muestra los comandos sin ejecutarlos. Revisa que la versión de ROS y los paquetes sean los esperados.

### 2.2 Ejecutar

```bash
bash scripts/setup/install_ros_jazzy.sh
```

El script:

1. Comprueba que el SO es Ubuntu 24.04 y la arquitectura es amd64 o arm64.
2. Configura el locale UTF-8.
3. Habilita `universe`.
4. Añade el repositorio oficial de ROS 2.
5. Instala `ros-dev-tools` y `ros-jazzy-ros-base`.
6. Instala Nav2, `ros_gz`, `slam_toolbox`, `robot_localization`, `xacro` y RViz.
7. Añade el `source` a `~/.bashrc` (opcional, con confirmación).

> El script es idempotente: se puede volver a ejecutar. No instala drivers de hardware.

### 2.3 Verificar

```bash
source /opt/ros/jazzy/setup.bash
ros2 doctor
ros2 pkg list | grep -E 'nav2|ros_gz' | head
gz sim --versions
```

## 3. Obtener el proyecto

```bash
cd ~
git clone <url-del-repo> rover
cd rover
```

Si ya existe:

```bash
cd rover
git pull --ff-only
```

## 4. Compilar el workspace

```bash
cd ros_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

### Verificación

```bash
ros2 pkg list | grep rover
# rover_bringup
# rover_description
# rover_mission
```

## 5. Generar mundo y mapa

```bash
cd ..
make assets
make assets-check
```

Esto crea:

- `ros_ws/src/rover_bringup/worlds/mini_marsyard.sdf`
- `ros_ws/src/rover_bringup/maps/mini_marsyard.pgm`
- `ros_ws/src/rover_bringup/maps/mini_marsyard.yaml`

Si `assets-check` falla, no continúes: el mundo y el mapa no coinciden.

## 6. Lanzar la simulación

```bash
source /opt/ros/jazzy/setup.bash
source ros_ws/install/setup.bash
ros2 launch rover_bringup sim.launch.py
```

Deberías ver:

- Gazebo con la arena.
- RViz con mapa, robot, LiDAR y TF.
- Nav2 activo.
- El nodo de misión en `IDLE`.

### Verificación en otra terminal

```bash
source /opt/ros/jazzy/setup.bash
source ros_ws/install/setup.bash

ros2 topic list
ros2 topic hz /scan
ros2 run tf2_ros tf2_echo map base_footprint
ros2 action list | grep navigate_to_pose
```

## 7. Lanzar la misión

```bash
ros2 launch rover_bringup mission.launch.py
```

O con un archivo distinto:

```bash
ros2 launch rover_bringup mission.launch.py \
  waypoints:=$PWD/ros_ws/src/rover_mission/config/waypoints_demo.yaml
```

Para iniciar manualmente:

```bash
ros2 service call /rover/mission/start std_srvs/srv/Trigger
```

Para abortar:

```bash
ros2 service call /rover/mission/abort std_srvs/srv/Trigger
```

## 8. Registrar evidencia

```bash
bash scripts/evidence/new_evidence.sh "mision-nominal-sim"
bash scripts/evidence/record_bag.sh docs/08-evidencia/artefactos/<carpeta>
bash scripts/evidence/seal_evidence.sh docs/08-evidencia/artefactos/<carpeta>
```

La carpeta debe contener `metadata.json`, `MANIFEST.sha256`, logs y bag.

## 9. Instalación en Raspberry Pi 5

1. Flashear Ubuntu 24.04 Server 64-bit con Raspberry Pi Imager.
2. Configurar WiFi/SSH en el primer arranque.
3. Actualizar y clonar el repo.
4. Ejecutar `scripts/setup/install_ros_jazzy.sh`.
5. Compilar (`colcon build`).
6. Conectar LiDAR, IMU y driver.
7. Verificar dispositivos: `ls /dev/ttyUSB*`, `ls /dev/i2c*`, `dmesg`.
8. Ejecutar el preflight.
9. Lanzar `bringup.launch.py` (hardware).

> El launch de hardware es un esqueleto: los drivers concretos dependen del hardware elegido. Documentar cada driver y sus topics.

## 10. Solución de problemas

| Problema | Causa | Solución |
|---|---|---|
| `rosdep` falla | Faltan dependencias del sistema | `sudo apt update`, revisar el error |
| `colcon build` falla por `setup.py` | Falta `setuptools` | `sudo apt install python3-setuptools` |
| Gazebo no encuentra el mundo | Ruta incorrecta | Usar `get_package_share_directory` |
| `map_server` no carga el mapa | YAML con ruta relativa mal | Revisar `image:` y permisos |
| AMCL no publica `map→odom` | Falta `/scan` o pose inicial | Revisar topics y `set_initial_pose` |
| La misión no arranca | Action server no disponible | Esperar a Nav2 o revisar logs |
| El robot no se mueve | `/cmd_vel` no llega al simulador | Revisar bridge y plugin |
| RViz muestra “No transform” | `use_sim_time` o `/clock` | Reiniciar con el reloj correcto |

## 11. Limpieza

```bash
make clean
rm -rf ~/.ros/log
```

## 12. Referencias

- [F-06] ROS 2 Jazzy Installation.
- [F-07] Nav2 Quickstart.
- [F-09] Gazebo + ROS.
- [`entorno-desarrollo.md`](entorno-desarrollo.md).
