# Hipótesis y diseño de experimentos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Principio

Ninguna afirmación de rendimiento se publica sin un experimento que la respalde. Este documento define **qué se mide, cómo, cuántas veces y con qué criterio se acepta**. El protocolo operativo está en [`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md).

## 2. Hipótesis

| ID | Hipótesis | Predicción | Métrica | Umbral |
|---|---|---|---|---|
| H1 | La pila Nav2 completa misiones de 5 waypoints con fiabilidad suficiente | ≥ 8 de 10 | Tasa de éxito | ≥ 80% |
| H2 | La precisión final es adecuada para un demo | Error medio ≤ 0.30 m | Error euclídeo final | ≤ 0.30 m |
| H3 | El Pi 5 puede con la pila sin degradarse | CPU media < 80% | CPU, temperatura | < 80%, < 80 °C |
| H4 | La brecha sim-real es manejable | Δ éxito ≤ 20 pp | Tasa de éxito sim vs real | ≤ 20 pp |
| H5 | RPP es suficiente y más eficiente que MPPI en Pi 5 | RPP ≥ MPPI en éxito y CPU | Éxito, CPU | RPP mejor o igual |
| H6 | Dos CM3 + ToF pueden dar profundidad 3D útil para navegación en la Pi 5 sin agotar CPU ni térmica | 640 × 480 a ≥ 5 Hz; error ≤ 10 % a 1 m y ≤ 20 % a 3 m; CPU < 60 %; T < 80 °C; +6 W | fps, error de profundidad, CPU, temperatura, potencia | Pasa/no pasa (ADR-0009) |

H5 es opcional; si no hay tiempo, se documenta como no evaluada.

## 3. Experimento E1 — Línea base en simulación

| Campo | Valor |
|---|---|
| Objetivo | Medir H1, H2, H3 en condiciones controladas |
| Entorno | Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Harmonic |
| Mundo | `mini_marsyard.sdf` |
| Mapa | `mini_marsyard.pgm` (12 × 8 m, 0.05 m/px) |
| Robot | URDF del repo, diferencial, LiDAR 360° |
| Misión | 5 waypoints (`waypoints_demo.yaml`) |
| Controlador | RPP |
| Velocidad máxima | 0.40 m/s |
| Repeticiones | 10 |
| Ground truth | Pose del modelo en Gazebo |
| Evidencia | Rosbag2 + logs + CSV + vídeo de pantalla |

### Procedimiento

1. Compilar y lanzar `sim.launch.py`.
2. Verificar TF `map → odom → base_footprint` y `/scan` a 10 Hz.
3. Confirmar pose inicial (0, 0, 0).
4. Lanzar la misión y cronometrar.
5. Al terminar, extraer la pose final y calcular el error contra el waypoint.
6. Guardar bag, logs y captura.
7. Repetir 10 veces, reiniciando la simulación entre ensayos.

### Criterio de éxito por ensayo

Un ensayo es exitoso si:

- Se alcanzan los 5 waypoints dentro de tolerancia (0.25 m).
- No hay colisiones.
- No hay intervenciones humanas.
- El tiempo total es ≤ 10 min.
- El rover termina en estado `COMPLETED` (no `FAILED`/`ABORTED`).

## 4. Experimento E2 — Línea base en hardware

| Campo | Valor |
|---|---|
| Objetivo | Medir H1, H2, H3, H4 en el rover físico |
| Entorno | Pista de 8 × 6 m, superficie lisa, iluminación constante |
| Robot | Rover montado y calibrado |
| Misión | La misma lista de waypoints, escalada a la pista |
| Repeticiones | 10 |
| Ground truth | Cinta métrica y marcas en el suelo (± 1 cm) |
| Evidencia | Rosbag2 + logs + CSV + vídeo externo |

### Diferencias con E1

- La pista física puede ser más pequeña; se usa una lista de waypoints equivalente y se documenta la escala.
- La pose final se mide con cinta métrica desde el centro del rover hasta la marca del waypoint.
- Se registra el voltaje de batería al inicio y al final.
- Se registra la temperatura del Pi y del driver.

## 5. Experimento E3 — Sensibilidad a la velocidad (opcional)

| Campo | Valor |
|---|---|
| Objetivo | Evaluar el compromiso velocidad/fiabilidad |
| Velocidades | 0.20, 0.30, 0.40 m/s |
| Repeticiones | 5 por velocidad |
| Entorno | Simulación |
| Métricas | Éxito, tiempo, error final, CPU |

Análisis: comparar medias y dispersión. Si 0.40 m/s reduce el éxito de forma significativa, se baja la velocidad de operación.

## 6. Experimento E4 — Comparación de controladores (opcional)

| Campo | Valor |
|---|---|
| Objetivo | Contrastar RPP vs DWB (y MPPI si el CPU lo permite) |
| Configuraciones | RPP, DWB, MPPI |
| Repeticiones | 5 por configuración |
| Entorno | Simulación |
| Métricas | Éxito, tiempo, suavidad, CPU, temperatura |

> MPPI puede no ser viable en Pi 5. Si no se puede ejecutar, se documenta la limitación y no se inventan resultados.

## 7. Variables y datos

### Variables independientes

- Entorno (sim/real).
- Controlador.
- Velocidad máxima.
- Calidad de odometría.
- Resolución del mapa.

### Variables dependientes

- `success` (0/1).
- `waypoints_reached` (0–5).
- `final_error_m`.
- `final_yaw_error_rad`.
- `duration_s`.
- `collisions` (conteo).
- `interventions` (conteo).
- `cpu_mean_pct`, `cpu_peak_pct`.
- `ram_peak_mb`.
- `temp_peak_c`.
- `battery_start_v`, `battery_end_v`.

### Esquema CSV

```csv
run_id,environment,date,commit,controller,max_speed,success,waypoints_reached,total_waypoints,final_error_m,final_yaw_error_rad,duration_s,collisions,interventions,cpu_mean_pct,cpu_peak_pct,ram_peak_mb,temp_peak_c,battery_start_v,battery_end_v,notes
```

Plantilla vacía: [`../06-pruebas/resultados/plantilla-datos.csv`](../06-pruebas/resultados/plantilla-datos.csv).

## 8. Análisis

### Estadística descriptiva

- Media, desviación estándar, mediana, mínimo, máximo y percentil 95 para variables continuas.
- Conteo y porcentaje para variables categóricas.

### Intervalo de confianza

Para la tasa de éxito se usa el intervalo de Wilson al 95%:

\[
\frac{\hat{p} + \frac{z^2}{2n} \pm z\sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^2}{4n^2}}}{1 + \frac{z^2}{n}}
\]

Con n = 10 y 8 éxitos, el intervalo es aproximadamente [49%, 94%]. Es una estimación exploratoria; no se presenta como una garantía.

### Comparación sim vs real

- Diferencia absoluta de tasa de éxito en puntos porcentuales.
- Diferencia de error medio final.
- Identificación de causas por observación y logs.

### Herramienta

`scripts/analysis/analyze_runs.py` lee el CSV y genera un resumen en Markdown. No requiere dependencias externas.

## 9. Experimento E5 — Spike de percepción 3D (ADR-0009)

| Campo | Valor |
|---|---|
| Objetivo | Medir H6: viabilidad de 2 × CM3 + ToF en la Pi 5 |
| Entorno | Laboratorio con luz controlada (300–1 000 lx) y una prueba a la intemperie |
| Hardware | Pi 5 8 GB, 2 × CM3 estándar, base rígida de 70 mm, VL53L8CX |
| Software | Ubuntu 24.04, Jazzy, fork de `libcamera`, `camera_ros` o nodo propio, `stereo_image_proc` |
| Captura | Estática y en movimiento lento; una pasada con Nav2 para CPU y temperatura |
| Repeticiones | 30 por distancia (0,5, 1, 2 y 3 m) |
| Ground truth | Cinta métrica y tablero rígido; error ≤ 1 cm |
| Evidencia | Bag, CSV, logs, fotos, mapa de disparidad y `MANIFEST.sha256` |
| Compra | 10 días laborables de plazo de suministro; **no** es tiempo de desarrollo |
| Horizonte | ~10 meses hasta el ERC 2027 (fecha por confirmar) |
| Ejecución | 10 semanas (2,5 meses) de trabajo efectivo, con hitos de 2 semanas |

### Procedimiento

1. Verificar que la Pi 5 detecta las dos cámaras (`rpicam-hello --list-cameras`)
   y el ToF responde por I²C.
2. Montar las dos CM3 en la base rígida de 70 mm, con los ejes paralelos y a la
   misma altura; fijar el ToF inclinado 20–30° hacia el suelo.
3. Compilar el fork de `libcamera` y `camera_ros`; bloquear enfoque,
   exposición y ganancia.
4. Calibrar con checkerboard a la resolución de trabajo; aceptar solo si el
   error de reproyección es < 0,5 px.
5. Medir profundidad a 0,5, 1, 2 y 3 m, 30 repeticiones por distancia, con
   luz de laboratorio.
6. Ejecutar Nav2 con el estéreo y el ToF publicando; medir CPU, RAM,
   temperatura y potencia durante 10 min.
7. Repetir una captura a la intemperie y registrar el alcance del ToF y la
   tasa de frames válidos.
8. Guardar bag, CSV, logs y fotos; sellar la evidencia.

### Criterio de éxito

- ≥ 5 Hz a 640 × 480.
- Error ≤ 10 % a 1 m y ≤ 20 % a 3 m.
- CPU media < 60 % con Nav2.
- Temperatura < 80 °C.
- Potencia añadida < 6 W.
- ≥ 90 % de frames válidos en laboratorio.

La prueba exterior se registra, pero no bloquea el paso si el alcance baja por
sol directo; se documenta como limitación.

### Si falla

Se vuelve a la opción A (1 CM3 + ToF), se marca el ADR-0009 como
«Rechazada para arquitectura final» y se conserva la evidencia del fallo. Los
componentes del spike se reutilizan en A o como repuesto.

## 10. Criterios de parada

Un experimento se detiene si:

- Hay una colisión con daño o riesgo para personas.
- La batería baja de 3.0 V por celda (LiFePO4: 2.8 V) o el BMS corta.
- La temperatura del Pi supera 80 °C o la del driver supera el límite del fabricante.
- La localización se pierde de forma irrecuperable más de 2 veces en un ensayo.
- El operador pierde la visión directa o la zona se vuelve insegura.

## 11. Ética y comunicación

- Se publican todos los ensayos, no solo los exitosos.
- Los resultados negativos se documentan con la misma calidad.
- No se comparan métricas de simulación con métricas de hardware sin indicarlo.
- No se atribuye causalidad sin diseño experimental.

## 12. Referencias

- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *JASA*, 22(158), 209–212.
- Montgomery, D. C. (2017). *Design and Analysis of Experiments* (9th ed.). Wiley.
- Protocolo operativo: [`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md).
