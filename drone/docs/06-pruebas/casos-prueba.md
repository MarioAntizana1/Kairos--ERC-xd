# Casos de prueba

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
>
> Todos los casos están **Pendientes**. No escribir “Aprobado” sin evidencia
> sellada.

### TC-01 — Detección y captura dual

- **Requisitos:** RF-01, RNF-05.
- **Precondiciones:** Pi 5, 2 CM3, cables 22→15, OS instalado.
- **Procedimiento:**
  1. `rpicam-hello --list-cameras`.
  2. Capturar 60 s con ambas cámaras a 2304 × 1296.
  3. Contar frames y pérdidas.
- **Esperado:** 2 cámaras, ≥10 fps, <1 % de frames perdidos.
- **Evidencia:** log, CSV de FPS, captura de cada cámara.

### TC-02 — Timestamps y sincronización

- **Requisitos:** RF-01, RF-12, RNF-10.
- **Precondiciones:** captura dual; FC conectada o simulador MAVLink.
- **Procedimiento:**
  1. Registrar `SensorTimestamp` y host time por frame.
  2. Ejecutar `TIMESYNC`.
  3. Calcular offset y deriva en 5 min.
- **Esperado:** offset ≤20 ms; deriva documentada.
- **Evidencia:** CSV de timestamps y offset.

### TC-03 — Calibración intrínseca

- **Requisitos:** RF-07, RNF-09.
- **Precondiciones:** tablero ChArUco, foco bloqueado.
- **Procedimiento:**
  1. Capturar 15–25 imágenes por cámara.
  2. Ejecutar `calibrateCamera`.
  3. Revisar RMS y mapas de error.
- **Esperado:** RMS <0,5 px por cámara.
- **Evidencia:** YAML, imágenes, log, hash.

### TC-04 — Calibración estéreo y baseline

- **Requisitos:** RF-07, RNF-09.
- **Precondiciones:** TC-03 aprobado; barra montada.
- **Procedimiento:**
  1. Capturar 20–30 pares del tablero.
  2. Ejecutar `stereoCalibrate` con `CALIB_FIX_INTRINSIC`.
  3. Medir baseline física con calibrador.
  4. Verificar error epipolar.
- **Esperado:** RMS <0,5 px; baseline ±1 mm; vertical <0,3 px.
- **Evidencia:** YAML, log, foto de la medición.

### TC-05 — Rectificación y disparidad

- **Requisitos:** RF-02, RNF-05.
- **Precondiciones:** TC-04 aprobado.
- **Procedimiento:**
  1. Rectificar un par con textura.
  2. Ejecutar SGBM a 640 × 360 y 1152 × 648.
  3. Medir FPS y % de píxeles válidos.
- **Esperado:** 640 × 360 ≥15 fps; 1152 × 648 ≥5 fps; máscara coherente.
- **Evidencia:** mapas, CSV de FPS, log.

### TC-06 — Exactitud de profundidad

- **Requisitos:** RF-02, RNF-03, RNF-04.
- **Precondiciones:** TC-04/TC-05 aprobados; ground truth.
- **Procedimiento:**
  1. Colocar un tablero a 1, 2, 3, 5, 8 y 10 m.
  2. Medir la distancia con cinta y con el estéreo.
  3. Repetir 10 veces por distancia.
- **Esperado:** error ≤10 cm a 5 m; ≤25 cm a 10 m; dispersión documentada.
- **Evidencia:** CSV, nube, fotos, análisis.

### TC-07 — ToF de piso: altitud y referencia de calibración

- **Requisitos:** RF-04, RF-10, RNF-03.
- **Precondiciones:** ToF montado en la base, mirando al piso; offset medido;
  superficie plana y mate.
- **Procedimiento:**
  1. Medir 0,5, 1, 2, 3, 4 y **6 m** con cinta y con el ToF; 10 repeticiones.
  2. Comparar el ToF con la altura conocida y con \(Z_{stereo}\) en el centro.
  3. Estimar la homografía del piso y la normal; usar el ToF para fijar la
     escala.
  4. Resolver \(T_{tof}^{cam}\) y proyectar el spot del ToF; medir el residual.
- **Esperado:** ≥10 Hz; error ≤2 % (≤12 cm a 6 m); residual de proyección
  <5 px; plano RMS <2 cm.
- **Evidencia:** CSV, YAML, imagen de proyección, log.

### TC-08 — Nube de puntos y exportación

- **Requisitos:** RF-03, RF-08.
- **Precondiciones:** TC-06 aprobado.
- **Procedimiento:**
  1. Escanear una maqueta con textura.
  2. Generar PCD/PLY.
  3. Medir dos puntos conocidos en la nube.
- **Esperado:** escala ≤2 %; nube legible en Open3D/PCL.
- **Evidencia:** PCD/PLY, captura, medición.

### TC-09 — Detección de obstáculos y latencia

- **Requisitos:** RF-05, RNF-06.
- **Precondiciones:** pipeline en modo SCAN; obstáculo controlado.
- **Procedimiento:**
  1. Acercar un obstáculo a 0,5–4 m.
  2. Registrar timestamp de captura y de salida.
  3. Repetir 20 veces.
- **Esperado:** detección correcta; latencia ≤200 ms; sin falsos positivos
  graves.
- **Evidencia:** CSV de latencia, log, vídeo.

### TC-10 — Registro, apagado y recuperación

- **Requisitos:** RF-06, RF-11, RNF-08, RNF-14.
- **Precondiciones:** NVMe con espacio; sesión de 30 min.
- **Procedimiento:**
  1. Grabar 30 min.
  2. Apagar de forma ordenada.
  3. Verificar archivos, hashes y montaje.
  4. Simular corte y comprobar recuperación.
- **Esperado:** ≥30 min; archivos íntegros; sin corrupción del sistema.
- **Evidencia:** logs, `fsck`, manifiesto.

### TC-11 — Térmica y potencia

- **Requisitos:** RNF-02, RNF-07.
- **Precondiciones:** caja cerrada; carga de CPU; fuente/UBEC.
- **Procedimiento:**
  1. Ejecutar pipeline 20 min.
  2. Medir temperatura, throttling, tensión y corriente.
- **Esperado:** <80 °C; `get_throttled=0x0`; >4,9 V; ≤20 W.
- **Evidencia:** CSV, `vcgencmd`, foto térmica.

### TC-12 — Vibración y estabilidad del montaje

- **Requisitos:** RNF-01, RNF-09, RF-02.
- **Precondiciones:** dron armado sin hélices; luego hélices y amarrado.
- **Procedimiento:**
  1. Medir baseline y calibración antes.
  2. Encender motores a rpm creciente.
  3. Medir cambio de baseline, rectificación y nitidez.
- **Esperado:** <0,5 mm; <0,5 px; sin blur grave.
- **Evidencia:** mediciones, imágenes, log.

### TC-13 — Interferencia WiFi/BT

- **Requisitos:** RNF-11.
- **Precondiciones:** RC encendida; dron armado sin hélices.
- **Procedimiento:**
  1. Encender WiFi/BT de la Pi.
  2. Verificar RSSI/pérdida de RC a 1, 10 y 50 m.
  3. Repetir con WiFi/BT apagados.
- **Esperado:** sin pérdida crítica; si hay interferencia, volar apagado.
- **Evidencia:** log de RSSI, vídeo, configuración.

### TC-14 — Vuelo cautivo end-to-end

- **Requisitos:** RF-03, RF-05, RF-09, RNF-14.
- **Precondiciones:** TC-01 a TC-13 aprobados; permiso; geofence; spotter.
- **Procedimiento:**
  1. Preflight completo.
  2. Vuelo cautivo a baja altura.
  3. Escanear una maqueta; registrar nube y obstáculos.
  4. Aterrizar y verificar datos.
- **Esperado:** sin incidentes; nube y telemetría coherentes; failsafe probado.
- **Evidencia:** logs, vídeo, nube, checklist firmado.

### TC-15 — Auditoría de BOM y reproducibilidad

- **Requisitos:** RNF-12, RNF-13.
- **Precondiciones:** BOM y CSV actualizados.
- **Procedimiento:**
  1. Ejecutar `make bom`.
  2. Verificar precios, cantidades y totales.
  3. Revisar que la evidencia tenga hash y comando.
- **Esperado:** total consistente; documentación reproducible.
- **Evidencia:** log de `make check`, CSV, facturas (si existen).
