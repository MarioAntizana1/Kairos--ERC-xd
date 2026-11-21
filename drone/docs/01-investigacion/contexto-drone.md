# Contexto del proyecto

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Visión

## 1. Problema

Un dron de inspección necesita **percibir profundidad** y **detectar obstáculos**
sin añadir un LiDAR 3D pesado ni un sensor industrial caro. La misión de la
competencia es **volar hasta 6 m dentro de una jaula/entorno cerrado** y producir
una nube de puntos utilizable, con un presupuesto y un peso acotados. Sin GPS, el
posicionamiento local depende de la FC o de un sistema de la organización.

La visión es la parte que este equipo controla. El dron —frame, controladora de
vuelo, ESCs, motores, batería, radio— lo desarrolla otro equipo o se adquiere
como plataforma. La integración se hace por MAVLink y por un riel de 5 V.

## 2. Por qué estéreo + ToF

| Necesidad | Estéreo | ToF de piso | Combinación |
|---|---|---|---|
| Mapa denso de profundidad | Sí, pasivo | No | Estéreo denso |
| Altitud / plano del suelo | No | Sí | ToF fija escala y plano |
| Validación de calibración | Parcial | Sí, referencia | ToF vs \(Z_{stereo}\) |
| Obstáculos frontales | Sí, con textura | No | Estéreo; ToF frontal opcional |
| Color | Sí | No | Estéreo aporta color |
| Peso | Bajo | Muy bajo | ~250–350 g con Pi 5 |
| Coste | Medio | Bajo | Ruta local viable |

El estéreo es la fuente principal de densidad y color; el **ToF de piso** da
altitud y una referencia métrica para escalar/validar la calibración. **El ToF
no sustituye la geometría epipolar del par estéreo.**

## 3. Stakeholders

| Stakeholder | Interés | Influencia |
|---|---|---|
| Equipo de visión | Pipeline, calibración, métricas | Alta |
| Equipo del dron | Peso, potencia, integración, seguridad | Alta |
| PO / universidad | Presupuesto, alcance, evidencia | Alta |
| Piloto / seguridad | Vuelo seguro, failsafes, geofence | Alta |
| Jurado / evaluadores | Rigor, demo, reproducibilidad | Media |
| Terceros filmados | Privacidad y consentimiento | Media |

## 4. Alcance de esta fase

**Incluido:**

- Pi 5 8 GB, 2 × Camera Module 3 Standard, **TFmini Plus 12 m** (base para 6 m);
  VL53L1X/VL53L5CX solo como alternativas de banco (≤4 m).
- Captura dual, calibración, rectificación, profundidad y nube de puntos.
- Detección de obstáculos y registro en NVMe.
- Documentación SDLC y evidencia.

**Excluido:**

- Control de vuelo, planificación de trayectoria, autonomía.
- Frame, motores, ESCs, batería, radio, estación de tierra.
- Certificación aeronáutica y operación BVLOS.
- RTK/GNSS de precisión y fotogrametría profesional.

## 5. Criterios de éxito

| Criterio | Métrica | Fase |
|---|---|---|
| Captura dual | 2 cámaras, frames con timestamp | G3 |
| Calibración | RMS < 0,5 px; baseline ±1 mm | G4 |
| Profundidad | ≤ 10 cm a 5 m | G4 |
| Nube | PCD/PLY con escala verificada | G4 |
| ToF de piso | Altura/referencia ≥ 10 Hz; error ≤2 % a 6 m | G4 |
| Obstáculos | Latencia ≤ 200 ms en banco | G4 |
| Térmica | < 80 °C sin throttling 20 min | G4 |
| Vuelo | Demo estable con spotter y geofence | G5 |

## 6. Supuestos

- La controladora de vuelo entrega actitud por MAVLink; la posición local es
  deseable pero no obligatoria.
- El dron puede cargar 250–350 g adicionales.
- Hay espacio físico para una baseline de 150 mm.
- La altura máxima es **6 m** y el entorno es **cerrado/jaula**, sin GPS.
- El equipo tiene acceso a un banco de pruebas y a una Pi 5 para calibrar.
- La operación será diurna (o con luz artificial controlada), VLOS y autorizada.

## 7. Contexto del proyecto rover

Este proyecto reutiliza la metodología del rover (SDLC + DSR, puertas G0–G5,
requisitos IEEE 29148, riesgos ISO 31000, evidencia con hash). El rover prioriza
navegación terrestre; el dron prioriza percepción aérea. Comparten disciplina
documental, no hardware.

## 8. Fuentes

- Raspberry Pi 5 y Camera Module 3: `F-01`–`F-04`.
- ToF: `F-14`–`F-18`.
- Precios: `F-06`–`F-22`.
- OpenCV/MAVLink/ROS 2: `F-23`–`F-26`.
