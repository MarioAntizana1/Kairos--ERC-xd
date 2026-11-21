# Revisión: ToF de piso y calibración — 2026-11-21

> Estado: Aprobada con limitación · Fecha: 2026-11-21T15:39:38-05:00 · Responsable: QA

## Objetivo

Registrar la revisión del diseño después de aclarar que el **ToF va mirando al
piso** y se usa como referencia de altura/escala para calibrar/validar la
cámara, no como sensor frontal de obstáculos.

## Cambios

- ToF de piso en README, arquitectura, interfaces, requisitos, diseño, BOM y
  pruebas.
- RF-04 y RF-10 reescritos para distancia al piso y referencia de calibración.
- TC-07 reescrito para altitud, homografía del piso y extrínseca ToF–cámara.
- ADR-0003 actualizado: VL53L1X ≤4 m; TFmini Plus >4 m; VL53L5CX 8×8 ≤4 m.
- BOM: se mantiene el VL53L1X base; TFmini Plus +S/ 255; VL53L5CX +S/ 115.
- Se añadió la configuración A (cámaras al piso) y B (cámaras al frente).

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
Docs scanned: 50
Local links checked: 125
Functional/NFR IDs: 12/14
Test cases: 15
Sources: 28
ADRs: 5

OK: 0 error(s), 0 warning(s)
Base (incluir=si): S/ 1,974.60
Contingencia 5%:   S/ 98.73
Total:             S/ 2,073.33

OK: BOM consistente
```

Salida completa en [`logs/check.log`](logs/check.log).

## Conclusión

**Aprobada con limitación.** La documentación refleja el ToF de piso y la
referencia de calibración. No hay evidencia de hardware: no se midió el piso, no
se calibró el ToF–cámara y no se voló.

## Limitaciones

- La altura de vuelo no está confirmada; decide VL53L1X (≤4 m) vs TFmini Plus
  (>4 m).
- La orientación de las cámaras (piso vs frente) sigue abierta (OQ-11).
- Los precios son un estudio web del 2026-11-21, no facturas.
- No se validó el método de homografía/extrínseca en hardware.

## Integridad

Ver [`MANIFEST.sha256`](MANIFEST.sha256).
