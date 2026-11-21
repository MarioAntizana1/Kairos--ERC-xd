# Resultados de pruebas

> Estado: Vivo · Responsable: rol de QA

Este directorio contiene los resultados de cada campaña. Una campaña = un conjunto de ensayos con el mismo objetivo y entorno.

## Estructura

```text
resultados/
├── README.md
├── plantilla-datos.csv
├── 2026-11-21-validacion-local/
│   ├── README.md
│   ├── datos.csv
│   └── analisis.md
└── ...
```

## Convención de nombres

`YYYY-MM-DD-<entorno>-<objetivo>/`

Ejemplos:

- `2026-11-21-local-unitarias/`
- `2026-12-05-sim-mision-nominal/`
- `2027-01-20-hw-pista/`

## Reglas

- Los datos crudos no se editan.
- Los ensayos fallidos se incluyen.
- Cada campaña enlaza su evidencia sellada.
- El análisis se genera con `scripts/analysis/analyze_runs.py`.
- Si se repite una campaña, se crea una carpeta nueva.

## Plantilla de datos

Ver [`plantilla-datos.csv`](plantilla-datos.csv). Cabecera:

```csv
run_id,environment,date,commit,controller,max_speed,success,waypoints_reached,total_waypoints,final_error_m,final_yaw_error_rad,duration_s,collisions,interventions,cpu_mean_pct,cpu_peak_pct,ram_peak_mb,temp_peak_c,battery_start_v,battery_end_v,notes
```

## Plantilla de informe

Ver [`../../00-gobierno/plantillas/informe-evidencia.md`](../../00-gobierno/plantillas/informe-evidencia.md).
