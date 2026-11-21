# Bitácora de implementación

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Software

## 2026-11-21 — Kickoff documental y cotización

**Hecho:**

- Se creó la estructura SDLC del proyecto de visión del dron, basada en la
  metodología del rover.
- Se definió el alcance: Pi 5 8 GB, 2 × Camera Module 3 Standard, ToF
  VL53L1X/VL53L5CX, pipeline estéreo y nube de puntos.
- Se investigaron precios y stock en The Pi Box, Electromanía, Naylamp,
  Falabella, Adafruit y ZoneFPV.
- Se escribió la BOM en soles y el CSV verificable.
- Se implementaron `check_docs.py` y `check_bom.py`.
- Se creó la evidencia documental de la validación local.

**No hecho / pendiente:**

- No se compró hardware.
- No se conectó ninguna Pi 5, cámara o ToF de piso.
- No se ejecutó captura, calibración, profundidad ni vuelo.
- No se validó ROS 2 ni MAVLink en hardware.

**Decisiones:**

- Pi 5 8 GB (ADR-0001).
- 2 × CM3 Standard, baseline 150 mm (ADR-0002).
- ToF VL53L5CX propuesto; VL53L1X base local (ADR-0003).
- Pipeline Picamera2 + OpenCV + ROS 2 propuesto (ADR-0004).
- Evidencia con hash (ADR-0005).

> **Actualización posterior (misma fecha):** la altura de 6 m cambia la base a
> **TFmini Plus 12 m**; ver la entrada “Ajuste por altura de 6 m y jaula”.

**Riesgos abiertos:**

- Stock del HAT+ M.2.
- Importación del VL53L5CX.
- UBEC 5 V/5 A no verificado localmente.
- Rolling shutter y autofoco en vuelo.
- Interferencia WiFi/BT.

**Siguiente:**

1. Aprobar G0.
2. Confirmar stock.
3. Comprar el núcleo operativo de banco.
4. Montar y validar captura dual.

---

## 2026-11-21 — Ajuste por altura de 6 m y jaula

**Contexto:** la competencia es en un entorno cerrado/jaula, con altura máxima de
**6 m** y sin GPS.

**Cambios:**

- ToF base: **TFmini Plus 12 m** (S/ 330, Electromanía). El VL53L1X y el
  VL53L5CX son de 4 m y quedan solo como alternativas de banco/vuelo ≤4 m.
- BOM base: **S/ 2.229,60** + 5 % = **S/ 2.341,08**. Con VL53L1X: S/ 2.073,33;
  con 8×8: S/ 2.194,08.
- ADR-0003 aceptada; OQ-02 cerrada (TFmini Plus para 6 m).
- Runbook: jaula, altura máxima 6 m, sin GPS, anti-flicker 50 Hz, WiFi/BT
  apagados, posicionamiento local de la FC.
- Evidencia: `EV-2026-11-21-04`.

**No hecho / pendiente:**

- No hay hardware; no se midió el TFmini a 6 m ni se voló.
- Falta confirmar la orientación de las cámaras (OQ-11) y el posicionamiento
  local de la jaula (OQ-12).

---

## Plantilla para nuevas entradas

```markdown
## YYYY-MM-DD — Título

**Hecho:**

- ...

**No hecho / pendiente:**

- ...

**Decisiones:**

- ...

**Riesgos/incidencias:**

- ...

**Evidencia:**

- `EV-...`

**Siguiente:**

1. ...
```
