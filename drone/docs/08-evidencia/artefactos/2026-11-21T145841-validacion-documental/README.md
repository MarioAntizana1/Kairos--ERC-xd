# Validación documental y de BOM — 2026-11-21

> Estado: Aprobada con limitación · Fecha: 2026-11-21T14:58:41-05:00 · Responsable: QA

## Objetivo

Verificar que la documentación del payload de visión es coherente antes de
aprobar G0:

- Enlaces locales válidos.
- Requisitos `RF`/`RNF` definidos y trazados.
- Fuentes `F` registradas.
- Casos de prueba `TC` definidos.
- ADRs listados y con estado.
- Totales de la BOM consistentes con el CSV.
- Sin rutas absolutas del equipo.

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
Docs scanned: 48
Local links checked: 121
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

**Aprobada con limitación.** La documentación, la trazabilidad y los totales de
la BOM son consistentes. No hay evidencia de hardware: no se ejecutó captura,
calibración, profundidad, ToF ni vuelo.

## Limitaciones

- No se probó la Raspberry Pi 5 ni las cámaras.
- No se validó ROS 2, Picamera2 ni OpenCV en el hardware objetivo.
- Los precios son un estudio de abastecimiento del 2026-11-21; no hay facturas.
- La evidencia demuestra consistencia documental, **no** funcionamiento del
  sistema.

## Reproducibilidad

Cualquier persona con Python 3.11+ puede ejecutar `make check` en la raíz del
repositorio. El resultado esperado es `0 error(s), 0 warning(s)` y los totales
indicados.

## Integridad

Ver [`MANIFEST.sha256`](MANIFEST.sha256).
