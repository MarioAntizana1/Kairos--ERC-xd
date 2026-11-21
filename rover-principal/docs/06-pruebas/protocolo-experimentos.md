# Protocolo de experimentos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
> Este documento es el procedimiento operativo. Las hipótesis están en [`../01-investigacion/hipotesis-y-experimentos.md`](../01-investigacion/hipotesis-y-experimentos.md).

## 1. Preparación del entorno

### 1.1 Simulación

```bash
source /opt/ros/jazzy/setup.bash
cd ros_ws
colcon build --symlink-install
source install/setup.bash
make assets-check
ros2 launch rover_bringup sim.launch.py
```

Verificar:

- [ ] Gazebo abre el mundo `mini_marsyard`.
- [ ] RViz muestra mapa, robot, LiDAR y TF.
- [ ] `/clock` avanza.
- [ ] `/scan` a ~10 Hz.
- [ ] `/odom` a ≥ 20 Hz.
- [ ] `map → base_footprint` disponible.
- [ ] Nav2 activo (`ros2 lifecycle get /bt_navigator`).
- [ ] Nodo de misión en `IDLE`.

### 1.2 Hardware

- [ ] Batería cargada (≥ 12.8 V en reposo).
- [ ] E-stop probada.
- [ ] LiDAR y IMU detectados.
- [ ] Odometría calibrada.
- [ ] Pista delimitada y barrida.
- [ ] Estación de operación conectada.
- [ ] Preflight en verde.

## 2. Ejecución de un ensayo

### 2.1 Crear la evidencia

```bash
bash scripts/evidence/new_evidence.sh "E1-run-01"
```

Anotar la ruta devuelta.

### 2.2 Iniciar la grabación

```bash
bash scripts/evidence/record_bag.sh <ruta-evidencia> 600
```

El segundo argumento es el tiempo máximo en segundos. Si se omite, graba hasta `Ctrl-C`.

### 2.3 Lanzar la misión

```bash
ros2 launch rover_bringup mission.launch.py \
  waypoints:=$PWD/ros_ws/src/rover_mission/config/waypoints_demo.yaml
```

O:

```bash
ros2 service call /rover/mission/start std_srvs/srv/Trigger
```

### 2.4 Observar

- Estado en `/rover/mission/status`.
- Progreso en `/rover/mission/progress`.
- Tiempo, waypoint actual, reintentos.
- Comportamiento anómalo.

### 2.5 Terminar

1. Esperar `COMPLETED`, `FAILED` o `ABORTED`.
2. Detener la grabación con `Ctrl-C`.
3. Guardar logs.
4. Medir la pose final.
5. Rellenar la fila del CSV.
6. Sellar la evidencia.

## 3. Medición de la pose final

### Simulación

```bash
ros2 run tf2_ros tf2_echo map base_footprint
```

O consultar el estado del modelo en Gazebo. Anotar `x`, `y`, `yaw`.

### Hardware

1. Marcar el waypoint objetivo en el suelo.
2. Detener el rover al terminar.
3. Medir la distancia desde el centro del rover hasta la marca con cinta métrica.
4. Medir la orientación con una brújula o referencia.
5. Anotar con precisión de ± 1 cm.

## 4. Registro de datos

Usar [`resultados/plantilla-datos.csv`](resultados/plantilla-datos.csv). Una fila por ensayo.

| Campo | Cómo obtenerlo |
|---|---|
| `run_id` | `E1-01`, `E2-01`, etc. |
| `environment` | `sim` o `hw` |
| `date` | ISO 8601 |
| `commit` | `git rev-parse --short HEAD` |
| `controller` | `rpp`, `dwb`, `mppi` |
| `max_speed` | m/s |
| `success` | 1/0 |
| `waypoints_reached` | 0–5 |
| `final_error_m` | Medición |
| `final_yaw_error_rad` | Medición |
| `duration_s` | Logs |
| `collisions` | Conteo |
| `interventions` | Conteo |
| `cpu_mean_pct` | `psutil` |
| `cpu_peak_pct` | `psutil` |
| `ram_peak_mb` | `psutil` |
| `temp_peak_c` | `vcgencmd` |
| `battery_start_v` | Multímetro/INA219 |
| `battery_end_v` | Multímetro/INA219 |
| `notes` | Observaciones |

## 5. Análisis

```bash
python3 scripts/analysis/analyze_runs.py docs/06-pruebas/resultados/datos.csv
```

El script genera:

- Número de ensayos.
- Tasa de éxito e intervalo de Wilson.
- Media, mediana, desviación y p95 del error final.
- Tiempo medio y desviación.
- Colisiones e intervenciones.
- Comparación sim vs hardware si hay ambos.

## 6. Criterios de parada

Detener la campaña si:

- Hay una colisión con daño o riesgo.
- La batería baja del umbral de seguridad.
- La temperatura supera el límite.
- Se pierde la localización de forma irrecuperable 2 veces seguidas.
- El operador o el observador consideran insegura la situación.

## 7. Informe

Cada campaña genera:

- `README.md` con objetivo, método, resultados y conclusión.
- `datos.csv`.
- `analisis.md` generado por el script.
- Bags y logs.
- `MANIFEST.sha256`.

El informe debe incluir:

- Hipótesis evaluada.
- Número de ensayos y exclusiones.
- Resultados con incertidumbre.
- Desviaciones y causas.
- Conclusión y siguiente acción.

## 8. Checklist de cierre

- [ ] Todos los ensayos registrados, incluidos los fallidos.
- [ ] CSV completo.
- [ ] Bag y logs guardados.
- [ ] Hashes generados.
- [ ] Entrada en el registro de evidencias.
- [ ] Trazabilidad actualizada.
- [ ] Bitácora actualizada.
- [ ] Riesgos revisados si hubo incidente.
