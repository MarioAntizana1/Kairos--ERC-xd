# Visión y alcance

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto

## 1. Problema

El dron necesita percibir profundidad y obstáculos para inspeccionar estructuras
y generar un mapa 3D, con un payload ligero y de bajo coste. La solución debe ser
reproducible, calibrable y segura; no se acepta una “caja negra” sin métricas.

## 2. Objetivo

Construir un payload de visión con dos Camera Module 3 y un **ToF de piso**
sobre Raspberry Pi 5 que entregue:

1. Profundidad métrica a partir del par estéreo.
2. Nube de puntos 3D con color.
3. Distancia cámara–suelo y referencia de escala/calibración con el ToF.
4. Detección de obstáculos con el estéreo.
5. Registro de datos para evidencia y reconstrucción offline.

## 3. Alcance

### Incluido

- Cómputo, cámaras, ToF de piso, almacenamiento y energía del payload.
- Captura dual, calibración, rectificación, disparidad y nube.
- Altitud/distancia al piso y referencia de escala/calibración.
- Detección de obstáculos con el estéreo y telemetría.
- Documentación SDLC, BOM y evidencia.

### Excluido

- Control de vuelo, autonomía, planificación y evitación activa.
- Frame, motores, ESCs, batería, radio y estación de tierra.
- RTK, fotogrametría profesional y operación BVLOS.
- Certificación aeronáutica.

## 4. Stakeholders

| Stakeholder | Necesidad |
|---|---|
| Equipo de visión | Hardware, calibración, métricas |
| Equipo del dron | Peso, potencia, integración, seguridad |
| PO / universidad | Presupuesto, alcance, evidencia |
| Piloto / seguridad | Vuelo seguro, failsafes, geofence |
| Jurado | Rigor y demo reproducible |

## 5. Criterios de aceptación de la fase

| Criterio | Métrica | Evidencia |
|---|---|---|
| Captura dual | 2 cámaras, ≥10 fps, timestamps | TC-01/TC-02 |
| Calibración | RMS <0,5 px; baseline ±1 mm | TC-03/TC-04 |
| Profundidad | ≤10 cm a 5 m | TC-06 |
| Nube | PCD/PLY con escala ≤2 % | TC-08 |
| ToF de piso | ≥10 Hz; error ≤2 % a 6 m | TC-07 |
| Obstáculos | ≤200 ms | TC-09 |
| Térmica | <80 °C, sin throttling 20 min | TC-11 |
| Registro | ≥30 min | TC-10 |

## 6. Supuestos

- La FC entrega actitud por MAVLink; la posición local es deseable.
- El dron puede cargar 250–350 g.
- Hay espacio para baseline de 150 mm.
- La operación es diurna, VLOS y autorizada.
- El equipo tiene acceso a banco de pruebas.

## 7. Fuera de alcance / no objetivos

- No se promete precisión milimétrica ni densidad LiDAR.
- No se promete vuelo autónomo ni evitación activa.
- No se promete funcionar con lluvia, niebla o sol directo extremo.
- No se promete georreferencia absoluta sin GPS/RTK.

## 8. Entregables

- Payload montado y calibrado.
- Pipeline de captura, profundidad y nube.
- BOM y cotización.
- Casos de prueba y evidencia.
- Runbook de vuelo y guion de demo.

## 9. Aprobación

| Rol | Nombre | Fecha | Firma |
|---|---|---|---|
| PO | | | |
| Visión | | | |
| Seguridad | | | |
