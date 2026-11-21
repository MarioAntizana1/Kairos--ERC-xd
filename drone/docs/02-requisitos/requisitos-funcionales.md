# Requisitos funcionales

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto
>
> Prioridad MoSCoW. Cada requisito tiene un criterio de aceptación medible.

| ID | Requisito | Prioridad | Criterio de aceptación |
|---|---|---|---|
| RF-01 | Capturar de forma casi simultánea imágenes de las dos Camera Module 3 | Must | 2 cámaras detectadas; 2304 × 1296 a ≥10 fps; diferencia de timestamp registrada; <1 % de frames perdidos en 60 s |
| RF-02 | Rectificar el par estéreo y calcular disparidad/profundidad | Must | Mapa de disparidad y profundidad en metros; rectificación con error vertical <0,5 px; máscara de validez |
| RF-03 | Generar una nube de puntos 3D | Must | PCD/PLY con color; frame de cámara; si hay pose, transformada a NED/local; voxel ≤5 cm |
| RF-04 | Medir la distancia cámara–suelo con el ToF de piso | Must | ≥10 Hz; 0,1–12 m (TFmini Plus; misión a 6 m); timestamp; estado de validez |
| RF-05 | Detectar obstáculos cercanos | Must | Rejilla de profundidad; distancia mínima por celda; salida a ≤200 ms; rango 0,3–4 m |
| RF-06 | Registrar datos de la sesión | Must | Frames, profundidad, ToF de piso, pose, calibración y logs en NVMe; ≥30 min; cierre ordenado |
| RF-07 | Calibrar intrínseca y estéreo | Must | YAML con K, D, R, T, R1, R2, P1, P2, Q, RMS, baseline, foco y fecha; RMS <0,5 px |
| RF-08 | Exportar la nube para análisis offline | Should | PCD y PLY legibles por Open3D/PCL; escala verificada ≤2 % |
| RF-09 | Publicar preview/telemetría al operador | Should | Stream o topic con FPS y estado; latencia de red ≤1 s en banco |
| RF-10 | Usar el ToF de piso como referencia de escala y validación de calibración | Should | Comparar con distancia conocida y con \(Z_{stereo}\) en el centro; error ≤2 % o 5 cm; flag de deriva; log |
| RF-11 | Iniciar/detener el payload de forma segura | Must | Servicio o comando; apagado ordenado; watchdog; no deja el NVMe corrupto |
| RF-12 | Sincronizar timestamps con la FC | Should | MAVLink `TIMESYNC`; error ≤20 ms; registro de offset |

## Notas

- RF-01 a RF-07 son el **MVP** para G3/G4.
- RF-08 a RF-10 son necesarios para la demo de escaneo 3D.
- RF-11 y RF-12 son necesarios para volar y para la evidencia.
- La visión es advisory: RF-05 no implica control de motores.
