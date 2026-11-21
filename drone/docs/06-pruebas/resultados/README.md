# Resultados de pruebas

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## Contenido

Cada campaña se guarda en una subcarpeta con:

```text
resultados/<fecha>-<slug>/
├── README.md          # objetivo, método, resultado, conclusión
├── datos.csv          # métricas crudas
├── media/             # gráficos, capturas, vídeos
├── logs/              # salidas de consola
└── MANIFEST.sha256    # hashes
```

## Estado

**No hay resultados de hardware.** La única evidencia actual es la validación
documental (`EV-2026-11-21-01`). No se deben inventar métricas de FPS, error de
profundidad, temperatura ni vuelo.

## Plantilla de datos

Usar [`plantilla-datos.csv`](plantilla-datos.csv) con las columnas mínimas:

- `session_id`
- `experiment_id`
- `test_case`
- `timestamp`
- `distance_m`
- `depth_m`
- `error_m`
- `fps`
- `latency_ms`
- `temperature_c`
- `voltage_v`
- `notes`

## Cómo publicar un resultado

1. Ejecutar el caso según [`casos-prueba.md`](../casos-prueba.md).
2. Guardar datos crudos y logs.
3. Calcular métricas y gráficos.
4. Escribir el `README.md` con limitaciones.
5. Sellar con `make seal`.
6. Registrar en [`../../08-evidencia/registro-evidencias.md`](../../08-evidencia/registro-evidencias.md).
7. Actualizar la matriz.

## Reglas

- No editar un resultado después de sellarlo.
- Reportar resultados negativos.
- Anonimizar personas y ubicaciones sensibles.
- No presentar una simulación como vuelo real.
