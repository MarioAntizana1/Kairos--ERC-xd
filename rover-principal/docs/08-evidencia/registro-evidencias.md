# Registro de evidencias — Visión

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Verificación

Índice de ejecuciones y artefactos de la sección. La política de integridad,
formato y retención está en [`README.md`](README.md).

## Convención

- `EV-V01`, `EV-V02`, … secuencial.
- Cada evidencia tiene una carpeta en `artefactos/FECHA-HORA-slug/` con:
  `README.md`, `metadata.json`, `logs/`, `bags/` y `media/`.
- `metadata.json` incluye fecha, entorno, comando, resultado, hash y
  responsable.
- `MANIFEST.sha256` sella los archivos.

## Evidencias

| ID | Fecha | Experimento | Estado | Artefacto | Responsable |
|---|---|---|---|---|---|
| — | — | Aún no hay evidencias de runtime | — | — | — |

## Evidencia heredada del mini demo (referencia)

Las carpetas `2026-11-21T123009-validacion-local`, `2026-11-21T123309-validacion-estatica-urdf`,
`2026-11-21T123448-validacion-final-pre-runtime` y `2026-11-21T123636-integracion-final`
se copiaron del mini demo como **referencia de formato y trazabilidad**. No son
evidencia de esta sección ni demuestran el funcionamiento de la visión del rover
grande. Se conservan porque los documentos heredados de requisitos y pruebas las
enlazan.

## Evidencias de investigación

La investigación de sensores del 2026-11-21 **no es una evidencia de
experimento**: es un registro de fuentes. Sus URLs, fechas y precios están en
[`../01-investigacion/fuentes.md`](../01-investigacion/fuentes.md) y en
[`../01-investigacion/sensores-peru-2026-11-21.md`](../01-investigacion/sensores-peru-2026-11-21.md).

## Plantilla de metadata

```json
{
  "id": "EV-V01",
  "fecha": "YYYY-MM-DDTHH:MM:SS-05:00",
  "experimento": "E-V1",
  "objetivo": "Medir error de profundidad del par estéreo",
  "entorno": "Ubuntu 24.04, ROS 2 Jazzy, ...",
  "hardware": "2 x Elgato Facecam 4K, base 15 cm, ...",
  "comando": "ros2 launch ...",
  "resultado": "Pendiente",
  "responsable": "Nombre",
  "hash_manifest": "sha256:..."
}
```

## Referencias

- [`README.md`](README.md) — política de evidencia.
- [`../06-pruebas/protocolo-experimentos.md`](../06-pruebas/protocolo-experimentos.md) — protocolo.
- Plantilla: [`../00-gobierno/plantillas/informe-evidencia.md`](../00-gobierno/plantillas/informe-evidencia.md).
