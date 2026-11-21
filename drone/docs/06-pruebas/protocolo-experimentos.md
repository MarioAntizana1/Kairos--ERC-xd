# Protocolo de experimentos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Objetivo

Definir cómo se mide, repite y reporta cada hipótesis para que el resultado sea
comparable y reproducible. **No hay resultados en este documento.**

## 2. Reglas

1. **10 repeticiones** por condición, salvo que se justifique otra cosa.
2. **Misma calibración** dentro de una serie; registrar el `calibration_id`.
3. **Ground truth** con cinta métrica, tablero o distancia conocida.
4. **Datos crudos** guardados; no solo el promedio.
5. **Outliers:** reportar todos; excluir solo con causa documentada.
6. **Incertidumbre:** media, desviación estándar, mínimo, máximo y percentil 95.
7. **Condiciones:** luz, temperatura, viento y textura registradas.
8. **Seguridad:** banco primero; vuelo solo con autorización.

## 3. Experimentos

| ID | Hipótesis | Condición | Métrica | Repeticiones |
|---|---|---|---|---:|
| EXP-01 | H-01 captura dual | 2304 × 1296, 60 s | FPS, pérdidas | 10 |
| EXP-02 | H-02 SGBM | 640 × 360 y 1152 × 648 | FPS, CPU | 10 |
| EXP-03 | H-03 profundidad | 1, 2, 3, 5, 8, 10 m | Error absoluto | 10 por distancia |
| EXP-04 | H-04/H-05 calibración | Tablero, 20 pares | RMS, baseline | 10 |
| EXP-05 | H-06 foco | 20 min, temperatura | Cambio de nitidez | 5 |
| EXP-06 | H-07 ToF de piso | Piso plano 0,5–6 m | Error de altura/escala | 10 |
| EXP-07 | H-08 térmica | Carga máxima 20 min | °C, W, throttling | 5 |
| EXP-08 | H-09 latencia | Obstáculo 0,5–4 m | ms | 20 |
| EXP-09 | H-10 sync | MAVLink `TIMESYNC` | Offset ms | 10 |
| EXP-10 | H-11 vibración | Motores a rpm creciente | mm, px | 10 |
| EXP-11 | H-12 escala | Maqueta con cotas | % error | 10 |
| EXP-12 | ToF de piso vs estéreo | 0,5–6 m | Diferencia en el centro | 10 |

## 4. Procedimiento general

1. **Preparar:** hardware, calibración, ground truth, formulario.
2. **Verificar:** temperatura, tensión, NVMe, foco, exposición.
3. **Registrar:** `metadata.json` con versiones, lugar, clima, operador.
4. **Ejecutar:** una condición por serie; no mezclar.
5. **Guardar:** datos crudos, logs, fotos/vídeos.
6. **Analizar:** calcular métricas y gráficos.
7. **Concluir:** cumple/no cumple; causa; acción.
8. **Sellar:** hash y registro.

## 5. Datos mínimos

| Campo | Ejemplo |
|---|---|
| `session_id` | `2026-11-21T150000Z_scan-01` |
| `experiment_id` | `EXP-03` |
| `calibration_id` | `2026-11-21T140000Z-b150` |
| `distance_m` | `5.0` |
| `depth_m` | `5.04` |
| `error_m` | `0.04` |
| `fps` | `14.8` |
| `temperature_c` | `62.5` |
| `voltage_v` | `5.08` |
| `notes` | `pared con textura` |

## 6. Análisis

- Error absoluto medio (MAE) y error cuadrático medio (RMSE).
- Percentil 95 para latencia.
- Gráfico error vs distancia.
- Gráfico FPS vs resolución.
- Comparación ToF de piso vs estéreo en el centro.
- Test de repetibilidad (desviación entre sesiones).

## 7. Criterios de aceptación

| Experimento | Criterio |
|---|---|
| EXP-01 | ≥10 fps, <1 % pérdidas |
| EXP-02 | ≥15 fps a 640 × 360; ≥5 fps a 1152 × 648 |
| EXP-03 | ≤10 cm a 5 m; ≤25 cm a 10 m |
| EXP-04 | RMS <0,5 px; baseline ±1 mm |
| EXP-05 | Cambio <0,3 px |
| EXP-06 | Error de altura/escala ≤2 % a 6 m |
| EXP-07 | <80 °C; ≤20 W; `0x0` |
| EXP-08 | ≤200 ms p95 |
| EXP-09 | ≤20 ms |
| EXP-10 | <0,5 mm; <0,5 px |
| EXP-11 | ≤2 % |
| EXP-12 | Diferencia documentada; sin sesgo grave |

## 8. Reporte

Cada experimento produce:

- `README.md` con objetivo, método, resultado, conclusión y limitaciones.
- `datos.csv` con las columnas mínimas.
- Gráficos en `media/`.
- `MANIFEST.sha256`.
- Enlace en la matriz y el registro de evidencias.

## 9. Repetibilidad

- Misma versión de software y calibración.
- Mismo hardware y montaje.
- Misma iluminación y distancia.
- Si algo cambia, se registra y se marca como nueva serie.

## 10. Ética

- No grabar personas sin consentimiento.
- No manipular datos ni excluir outliers sin justificar.
- Reportar resultados negativos.
- No presentar una simulación como vuelo real.
