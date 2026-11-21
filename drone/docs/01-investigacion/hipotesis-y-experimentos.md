# Hipótesis y experimentos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Visión

## 1. Principio

Cada hipótesis se formula antes de medir, con una métrica y un umbral. Un
resultado negativo es un resultado: se documenta y se ajusta el diseño. **No se
presenta una hipótesis como hecho.**

## 2. Hipótesis

| ID | Hipótesis | Métrica | Umbral | Experimento |
|---|---|---|---|---|
| H-01 | La Pi 5 captura dos CM3 a 2304 × 1296 y ≥ 10 fps | FPS, frames perdidos | ≥ 10 fps, < 1 % perdidos | EXP-01 |
| H-02 | SGBM a 640 × 360 corre a ≥ 15 fps en la Pi 5 | FPS de profundidad | ≥ 15 fps | EXP-02 |
| H-03 | El error de profundidad a 5 m es ≤ 10 cm | Error absoluto | ≤ 10 cm | EXP-03 |
| H-04 | La calibración estéreo logra RMS < 0,5 px | RMS de reproyección | < 0,5 px | EXP-04 |
| H-05 | La baseline se mantiene ±1 mm en banco | Medición física | ±1 mm | EXP-04 |
| H-06 | El foco bloqueado no deriva en 20 min | Nitidez/rectificación | < 0,3 px de cambio | EXP-05 |
| H-07 | El ToF de piso da una referencia de altura/escala con error ≤2 % a 6 m | Error de altura/escala | ≤2 % (≤12 cm a 6 m) | EXP-06 |
| H-08 | El payload consume < 20 W y no throttlea en 20 min | Potencia/temperatura | < 20 W; < 80 °C; `0x0` | EXP-07 |
| H-09 | La latencia de obstáculo es ≤ 200 ms | Captura → salida | ≤ 200 ms | EXP-08 |
| H-10 | La pose MAVLink se sincroniza con ≤ 20 ms de error | Diferencia de timestamp | ≤ 20 ms | EXP-09 |
| H-11 | La vibración con hélices no arruina el estéreo en banco | Cambio de baseline/rectificación | < 0,5 mm; < 0,5 px | EXP-10 |
| H-12 | La nube de puntos tiene escala correcta | Error de distancia entre puntos | ≤ 2 % | EXP-11 |

## 3. Variables

| Tipo | Ejemplo |
|---|---|
| Independiente | Baseline, resolución, exposición, foco, iluminación, textura, vibración |
| Dependiente | Error de profundidad, FPS, latencia, cobertura, temperatura, potencia |
| Controlada | Misma calibración, mismo tablero, misma distancia, mismo hardware |
| Extraña | Temperatura ambiente, carga de CPU, viento, vibración del banco |

## 4. Protocolo general

1. **Preparar** el hardware y la calibración; registrar versiones.
2. **Fijar** exposición, ganancia, balance de blancos y foco.
3. **Medir** el ground truth con cinta métrica o tablero de distancia conocida.
4. **Repetir** al menos 10 veces por condición (ver
   [`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md)).
5. **Registrar** datos crudos, logs y temperatura.
6. **Analizar** media, desviación, percentiles y outliers.
7. **Concluir** si se cumple el umbral; si no, explicar la causa.
8. **Sellar** la evidencia con hash.

## 5. Validez

- **Interna:** mismas condiciones para todas las repeticiones; calibrar antes de
  cada sesión.
- **Externa:** probar al menos dos escenas (tablero y estructura real) y dos
  iluminaciones (interior y exterior).
- **Constructo:** la métrica mide lo que dice medir (error de profundidad, no
  “se ve bien”).
- **Conclusión:** no generalizar de 3 ensayos; usar 10 y reportar dispersión.

## 6. Resultados

| ID | Estado | Evidencia | Conclusión |
|---|---|---|---|
| H-01 | Pendiente | — | — |
| H-02 | Pendiente | — | — |
| H-03 | Pendiente | — | — |
| H-04 | Pendiente | — | — |
| H-05 | Pendiente | — | — |
| H-06 | Pendiente | — | — |
| H-07 | Pendiente | — | — |
| H-08 | Pendiente | — | — |
| H-09 | Pendiente | — | — |
| H-10 | Pendiente | — | — |
| H-11 | Pendiente | — | — |
| H-12 | Pendiente | — | — |

> No hay resultados de hardware. Cualquier número en este documento es un
> umbral de diseño, no una medición.
