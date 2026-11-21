# Requisitos no funcionales

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto
>
> Cada RNF tiene métrica, umbral y método de verificación.

| ID | Requisito | Prioridad | Métrica / umbral | Verificación |
|---|---|---|---|---|
| RNF-01 | Peso del payload | Must | ≤350 g; objetivo 250–300 g | Báscula; suma de masas |
| RNF-02 | Consumo eléctrico | Must | ≤20 W típico; entrada 5 V/5 A; riel >4,9 V | Fuente de banco / medidor USB-C |
| RNF-03 | Rango de operación | Must | Estéreo 1–10 m; ToF de piso 0,1–12 m (TFmini Plus; misión a 6 m) | Tablero y piso a 0,5–6 m |
| RNF-04 | Exactitud de profundidad | Must | ≤10 cm a 5 m; ≤25 cm a 10 m | Ground truth con cinta/tablero |
| RNF-05 | Rendimiento | Must | Captura ≥10 fps; 640×360 ≥15 fps; 1152×648 ≥5 fps | Medición de FPS y CPU |
| RNF-06 | Latencia de obstáculo | Must | ≤200 ms captura → salida | Timestamps |
| RNF-07 | Térmica | Must | <80 °C; `get_throttled=0x0` en 20 min | `vcgencmd` + carga |
| RNF-08 | Registro | Must | ≥30 min; 128 GB; sin corrupción | Sesión de 30 min + verificación |
| RNF-09 | Calibración | Must | RMS <0,5 px; baseline ±1 mm; vertical <0,3 px | OpenCV + calibrador |
| RNF-10 | Sincronización con FC | Must | ≤20 ms | `TIMESYNC` / timestamps |
| RNF-11 | Compatibilidad electromagnética | Must | WiFi/BT deshabilitados o sin interferencia | Prueba en tierra con RC |
| RNF-12 | Coste | Must | ≤S/ 2.300 del payload, sin dron | BOM + facturas |
| RNF-13 | Reproducibilidad | Must | Versiones fijadas; YAML; hash; comando | `make check` + evidencia |
| RNF-14 | Seguridad | Must | Visión advisory; failsafe; watchdog; apagado ordenado | Revisión + TC-10/TC-14 |

## Notas

- RNF-04 se calcula con baseline 150 mm, \(f_{px}=1693\) y \(\sigma_d=0,5\) px;
  ver [`../04-diseno/diseno-vision.md`](../04-diseno/diseno-vision.md).
- RNF-05 es una hipótesis hasta medir en la Pi 5; si no se cumple, se reduce
  resolución o se cambia SGBM por BM.
- RNF-12 incluye la reserva del 10 % sobre la BOM base; no incluye herramientas,
  dron ni permisos.
- RNF-14 no convierte la visión en sistema de seguridad: la FC conserva la
  autoridad.
