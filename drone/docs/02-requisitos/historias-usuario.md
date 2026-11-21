# Historias de usuario

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto

## HU-01 — Captura dual

**Como** ingeniero de visión, **quiero** capturar las dos cámaras con timestamp
**para** construir un par estéreo confiable.

- **Dado** que la Pi 5 tiene dos CM3 conectadas,
- **cuando** inicio la captura,
- **entonces** obtengo dos frames de 2304 × 1296 con timestamps y <1 % de
  pérdidas en 60 s.

Requisitos: RF-01, RNF-05.

## HU-02 — Calibración

**Como** ingeniero de visión, **quiero** calibrar intrínseca y estéreo y guardar
el YAML **para** que la profundidad sea métrica y reproducible.

- **Dado** un tablero ChArUco y el par montado,
- **cuando** ejecuto la calibración,
- **entonces** obtengo RMS <0,5 px, baseline ±1 mm y un YAML con hash.

Requisitos: RF-07, RNF-09.

## HU-03 — Profundidad y nube

**Como** operador, **quiero** ver una nube de puntos 3D **para** inspeccionar la
estructura y medir distancias.

- **Dado** un par calibrado,
- **cuando** apunto a una escena con textura,
- **entonces** obtengo una nube PCD/PLY con escala verificada y error ≤10 cm a
  5 m.

Requisitos: RF-02, RF-03, RF-08, RNF-04.

## HU-04 — ToF de piso y referencia de calibración

**Como** ingeniero de visión, **quiero** que el ToF mida la distancia al piso
**para** tener una referencia métrica y validar la calibración.

- **Dado** un piso plano y el ToF montado en la base,
- **cuando** el dron está a 0,5–4 m,
- **entonces** el ToF reporta la altura con error ≤2 % o 5 cm y la comparo con
  \(Z_{stereo}\) en el centro.

Requisitos: RF-04, RF-10, RNF-03.

## HU-05 — Registro y evidencia

**Como** QA, **quiero** que cada sesión guarde datos y metadatos **para** repetir
el experimento y demostrar el resultado.

- **Dado** una sesión de 30 min,
- **cuando** la detengo de forma ordenada,
- **entonces** tengo frames, profundidad, ToF de piso, pose, calibración y logs
  en NVMe, con hash y sin corrupción.

Requisitos: RF-06, RF-11, RNF-08, RNF-13.

## HU-06 — Integración con el dron

**Como** equipo del dron, **quiero** recibir la pose y los obstáculos por MAVLink
**para** integrar la visión sin acoplar el código de vuelo.

- **Dado** la FC conectada,
- **cuando** el payload arranca,
- **entonces** sincroniza timestamps ≤20 ms y publica obstáculos en un topic o
  mensaje documentado, sin enviar comandos de motor.

Requisitos: RF-05, RF-09, RF-12, RNF-10, RNF-14.
