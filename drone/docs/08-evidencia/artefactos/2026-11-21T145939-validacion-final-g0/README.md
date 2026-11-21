# Validación final G0 — 2026-11-21

> Estado: Aprobada con limitación · Fecha: 2026-11-21T14:59:39-05:00 · Responsable: QA

## Objetivo

Repetir la validación documental y de BOM después de los ajustes de cierre de G0:

- Enlaces locales, requisitos, fuentes, casos y ADRs.
- Totales de la BOM y contingencias.
- Coherencia de la cotización con el README y el plan.

## Entorno

| Campo | Valor |
|---|---|
| Host | Mario-laptop |
| SO | Linux 7.3.3-100.fc43.x86_64 (Fedora 43) |
| Python | 3.14.10 |
| Raspberry Pi | No conectada |
| Cámaras / ToF | No conectados |
| ROS 2 | No instalado |

## Comando

```bash
make check
```

## Resultado

```text
Docs scanned: 49
Local links checked: 123
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

**Aprobada con limitación.** La documentación y la BOM están cerradas para G0.
No hay evidencia de hardware: no se ejecutó captura, calibración, profundidad,
ToF ni vuelo.

## Limitaciones

- No hay Raspberry Pi, cámaras ni ToF.
- No se validó el pipeline en runtime.
- Los precios son un estudio web del 2026-11-21, no facturas.
- Esta evidencia no demuestra funcionamiento; demuestra consistencia documental.

## Reproducibilidad

`make check` en la raíz del repositorio, con Python 3.11+.

## Integridad

Ver [`MANIFEST.sha256`](MANIFEST.sha256).
