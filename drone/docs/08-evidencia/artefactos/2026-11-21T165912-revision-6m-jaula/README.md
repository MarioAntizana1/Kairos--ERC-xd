# Revisión: vuelo a 6 m en jaula — 2026-11-21

> Estado: Aprobada con limitación · Fecha: 2026-11-21T16:59:12-05:00 · Responsable: QA

## Objetivo

Registrar el ajuste de la cotización y el diseño para la competencia:
**vuelo hasta 6 m en un entorno cerrado/jaula, sin GPS**.

## Cambios

- ToF base: **TFmini Plus 12 m** (S/ 330, Electromanía). A 6 m el VL53L1X y el
  VL53L5CX de 4 m no alcanzan.
- BOM base: **S/ 2.229,60** + 5 % = **S/ 2.341,08**.
- Alternativas de banco: VL53L1X (total S/ 2.073,33) y VL53L5CX 8×8 (total
  S/ 2.194,08), solo ≤4 m.
- ADR-0003 aceptada; OQ-02 cerrada.
- Runbook y seguridad: jaula, 6 m, sin GPS, anti-flicker 50 Hz, WiFi/BT
  apagados, posicionamiento local.
- Se añadió OQ-12 (posición local en jaula).

## Entorno

| Campo | Valor |
|---|---|
| Host | Mario-laptop |
| SO | Linux 7.3.3-100.fc43.x86_64 |
| Python | 3.14.10 |
| Raspberry Pi | No conectada |
| Cámaras / ToF | No conectados |

## Comando

```bash
make check
```

## Resultado

```text
Docs scanned: 51
Local links checked: 127
Functional/NFR IDs: 12/14
Test cases: 15
Sources: 28
ADRs: 5

OK: 0 error(s), 0 warning(s)
Base (incluir=si): S/ 2,229.60
Contingencia 5%:   S/ 111.48
Total:             S/ 2.341,08

OK: BOM consistente
```

Salida completa en [`logs/check.log`](logs/check.log).

## Conclusión

**Aprobada con limitación.** La cotización y el diseño reflejan el vuelo a 6 m
en jaula. No hay evidencia de hardware: no se midió el TFmini a 6 m, no se
calibró el ToF–cámara y no se voló.

## Limitaciones

- No se validó el TFmini Plus a 6 m en hardware.
- No se confirmó el posicionamiento local de la jaula (OQ-12).
- La orientación de las cámaras sigue abierta (OQ-11).
- Los precios son un estudio web del 2026-11-21, no facturas.

## Integridad

Ver [`MANIFEST.sha256`](MANIFEST.sha256).
