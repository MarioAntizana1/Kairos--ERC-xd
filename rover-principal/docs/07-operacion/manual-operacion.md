# Manual de operación

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Operación

## 1. Alcance

Procedimientos para arrancar, operar, abortar y apagar el rover en simulación y en hardware. Para la demo, usar además el [`runbook-demo.md`](runbook-demo.md).

## 2. Roles

| Rol | Responsabilidad |
|---|---|
| Operador principal | Inicia, observa y aborta la misión |
| Observador de seguridad | Vigila la zona y controla la e-stop |
| Técnico | Preflight, calibración y resolución de problemas |

En demos con público, el operador y el observador son personas distintas.

## 3. Antes de arrancar

- [ ] Zona despejada y delimitada.
- [ ] E-stop accesible y probada.
- [ ] Batería cargada y sujeta.
- [ ] Cables y conectores revisados.
- [ ] LiDAR limpio y con visión libre.
- [ ] Runbook a mano.
- [ ] Preflight ejecutado.

## 4. Arranque en simulación

```bash
source /opt/ros/jazzy/setup.bash
source ros_ws/install/setup.bash
ros2 launch rover_bringup sim.launch.py
```

Esperar a que:

- Gazebo muestre la arena.
- RViz muestre mapa, robot y LiDAR.
- Nav2 esté activo.
- `/rover/mission/status` publique `IDLE`.

## 5. Arranque en hardware

```bash
source /opt/ros/jazzy/setup.bash
source ros_ws/install/setup.bash
ros2 launch rover_bringup bringup.launch.py
```

> El launch de hardware es un esqueleto. Los drivers concretos (LiDAR, IMU, base) deben estar instalados y configurados. Verificar los topics antes de mover.

### Secuencia física

1. Colocar el rover en la pose inicial.
2. Encender la estación de operación.
3. Encender el rover (interruptor general).
4. Esperar el arranque de ROS 2 (≤ 60 s).
5. Verificar TF y topics.
6. Ejecutar el preflight.
7. Confirmar que la e-stop está liberada.
8. Iniciar la misión.

## 6. Ejecutar una misión

```bash
ros2 launch rover_bringup mission.launch.py
```

O manualmente:

```bash
ros2 service call /rover/mission/start std_srvs/srv/Trigger
```

### Monitorizar

```bash
ros2 topic echo /rover/mission/status
ros2 topic echo /rover/mission/progress
ros2 topic hz /scan
ros2 topic hz /odom
```

En RViz: mapa, robot, LiDAR, ruta y objetivo.

## 7. Pausar, reanudar y abortar

```bash
# Pausar tras el waypoint actual
ros2 service call /rover/mission/pause std_srvs/srv/Trigger

# Reanudar
ros2 service call /rover/mission/resume std_srvs/srv/Trigger

# Abortar
ros2 service call /rover/mission/abort std_srvs/srv/Trigger
```

### Aborto de emergencia

1. Pulsar la **e-stop física**.
2. Confirmar que el rover se detiene.
3. No rearmar hasta que la zona esté segura.
4. Registrar el incidente.

> El aborto por software es para situaciones controladas. La e-stop es la última línea.

## 8. Estados

| Estado | Significado | Acción |
|---|---|---|
| `IDLE` | Cargado, sin empezar | Puede iniciarse |
| `RUNNING` | Navegando | Observar |
| `PAUSED` | Pausado | Reanudar o abortar |
| `COMPLETED` | Terminado | Guardar evidencia |
| `COMPLETED_WITH_WARNING` | Terminado con fallo en retorno | Revisar logs |
| `FAILED` | Fallo | Revisar causa |
| `ABORTED` | Cancelado | Revisar motivo |
| `BATTERY_LOW` | Batería baja | Cargar |

## 9. Apagado

### Simulación

```bash
# Ctrl-C en la terminal del launch
```

### Hardware

1. Abortar o esperar a `COMPLETED`.
2. Detener la misión.
3. Apagar ROS 2 (`Ctrl-C`).
4. Apagar el rover con el interruptor general.
5. Desconectar la batería.
6. Guardar logs y bag.
7. Inspección visual.

> No apagar bruscamente con la batería conectada si el sistema está escribiendo en disco.

## 10. Carga de batería

- Usar el cargador del fabricante.
- Cargar en superficie ignífuga.
- No dejar sin supervisión.
- No cargar dentro del rover.
- Comprobar temperatura y hinchazón.
- Almacenar a ~50% si no se usa.

## 11. Problemas frecuentes

| Síntoma | Causa | Acción |
|---|---|---|
| No arranca | Sin `source` | `source /opt/ros/jazzy/setup.bash` |
| No hay TF | Nodo caído | `ros2 node list`, revisar logs |
| No hay `/scan` | LiDAR desconectado | Revisar USB y permisos |
| La misión no inicia | Action server ausente | Esperar a Nav2 |
| Se desvía | Odometría mal calibrada | Recalibrar |
| Se pierde | AMCL sin convergencia | Re-localizar |
| Batería baja | Consumo alto | Cargar y revisar |
| Sobrecalienta | Ventilación | Pausar y ventilar |

## 12. Registro

Al terminar cada sesión:

- Guardar bag y logs.
- Rellenar el CSV de resultados.
- Sellar la evidencia.
- Anotar en la bitácora.
- Registrar incidentes.

## 13. Contactos

| Rol | Nombre | Contacto |
|---|---|---|
| Operador | | |
| Seguridad | | |
| Soporte técnico | | |
| Emergencias | 112 | — |
