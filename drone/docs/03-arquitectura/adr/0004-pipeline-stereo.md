# ADR-0004 — Pipeline Picamera2 + OpenCV + ROS 2

> Estado: Propuesta · Fecha: 2026-11-21 · Responsable: rol de Software

## Contexto

El payload necesita capturar dos cámaras, calibrar, rectificar, calcular
disparidad, generar nube, leer ToF, recibir pose y registrar. El equipo viene del
proyecto rover, que usa ROS 2 Jazzy. La Pi 5 no tiene CUDA; el pipeline debe
correr en CPU.

## Alternativas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| **ROS 2 Jazzy + Picamera2 + OpenCV** | Reutiliza stack, topics, tf2, rosbag2; integración | Más dependencias; overhead; OS |
| Python puro + MAVLink | Simple, menos overhead | Sin ecosistema; interfaces a mano |
| C++ + libcamera + OpenCV | Máximo rendimiento | Más desarrollo; menos flexible |
| ROS 1 + cv_bridge | Maduro | EOL; no alineado con rover |
| GStreamer + OpenCV | Bajo nivel | Complejo de calibrar y depurar |

## Decisión

**Propuesta:** ROS 2 Jazzy + Picamera2 + OpenCV SGBM, con **fallback** a Python
puro + MAVLink si el overhead o la estabilidad del stack de cámara en Ubuntu
24.04 no convencen.

Motivos:

1. Reutiliza la metodología y el stack del rover.
2. `sensor_msgs/Image`, `PointCloud2`, `tf2` y `rosbag2` ya resuelven interfaces.
3. Permite integrar `mavros` o un nodo MAVLink propio.
4. OpenCV es estándar para calibración y SGBM.

## Consecuencias

- **Positivas:** integración, trazabilidad, ecosistema.
- **Negativas:** ROS 2 + OpenCV + doble cámara consumen CPU/RAM; la instalación
  en Pi 5 requiere cuidado; Ubuntu 24.04 vs Raspberry Pi OS es una decisión
  abierta.
- **Riesgos:** latencia, dependencias, soporte de cámara en Ubuntu.
- **Mitigaciones:** perfilar; usar 640×360 para tiempo real; contenedor/entorno
  fijado; fallback Python.
- **Requisitos afectados:** RF-01, RF-02, RF-03, RF-09, RNF-05, RNF-13.

## Evidencia

- F-04, F-23, F-25, F-26.
- Interfaces: [`../interfaces.md`](../interfaces.md).
- Entorno: [`../../05-implementacion/entorno-desarrollo.md`](../../05-implementacion/entorno-desarrollo.md).

## Revisión

| Fecha | Revisor | Resultado |
|---|---|---|
| 2026-11-21 | Software | Propuesta; validar en banco antes de G3 |
