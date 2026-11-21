# Política de evidencia

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Principio

La evidencia no es un adorno: es la prueba de que el sistema cumple lo que
decimos. Debe ser **trazable, reproducible, íntegra y verificable**.

## 2. Qué cuenta como evidencia

| Tipo | Ejemplo | Válido |
|---|---|---|
| Ejecución de prueba | Log de calibración, CSV de profundidad | Sí |
| Captura o vídeo | Nube, demo, vuelo | Sí, con contexto |
| Medición | 10 ensayos, error, FPS, temperatura | Sí, con método |
| Documento firmado | Checklist de seguridad | Sí |
| “Funciona en mi máquina” | Sin log ni entorno | **No** |
| Captura sin fecha ni commit | — | **No** |
| Vídeo editado sin datos | — | **No** |

## 3. Formato

```text
docs/08-evidencia/artefactos/YYYY-MM-DDTHHMMSS-<slug>/
├── README.md          # objetivo, resultado, conclusión, reproducibilidad
├── metadata.json      # fecha, host, SO, versiones, commit, comando, operador
├── MANIFEST.sha256    # hashes
├── logs/              # salidas de consola
├── media/             # fotos, vídeos, capturas
└── bags/              # rosbag2 o datos crudos (o enlace + hash)
```

## 4. Metadatos mínimos

| Campo | Ejemplo |
|---|---|
| `id` | `EV-2026-11-21-01` |
| `date` | `2026-11-21T15:00:00Z` |
| `operator` | `QA` |
| `host` | `drone-vision-bench` |
| `os` | `Raspberry Pi OS 64-bit` |
| `kernel` | `6.6.x` |
| `python` | `3.11` |
| `opencv` | `4.x` |
| `ros_distro` | `jazzy` |
| `commit` | `abc1234` |
| `dirty` | `false` |
| `command` | `make check` |
| `requirements` | `RNF-13` |
| `tests` | `TC-15` |
| `result` | `passed` |

## 5. Integridad

- Generar `MANIFEST.sha256` con `sha256sum` al cerrar.
- No modificar archivos después de sellar.
- Si hay que corregir, crear una nueva carpeta y marcar la anterior como
  `Obsoleta`.
- Los datos > 50 MB se guardan fuera del repo; registrar URL y hash.

## 6. Retención

| Tipo | Retención | Dónde |
|---|---|---|
| Logs y CSV | Todo el proyecto | Git |
| Datos pequeños (< 50 MB) | Todo el proyecto | Git |
| Datos grandes | Hasta 1 año | Almacenamiento externo |
| Vídeos | Todo el proyecto | Git LFS o externo |
| Evidencia de demo | Permanente | Git + copia |

## 7. Privacidad

- No grabar rostros sin consentimiento.
- Anonimizar nombres, matrículas y ubicaciones sensibles.
- No publicar datos personales.
- Respetar la licencia de imágenes y software.

## 8. Registro

Cada carpeta se anota en
[`registro-evidencias.md`](registro-evidencias.md) con ID, fecha, tipo,
requisitos, casos, resultado, ruta, hash y estado.

## 9. Ejemplo

```bash
make evidence SLUG=validacion-documental
# ... ejecutar ...
make seal DIR=docs/08-evidencia/artefactos/2026-11-21T150000-validacion-documental
```

## 10. Buenas prácticas

- Ejecutar en el entorno objetivo, no en uno aproximado.
- Incluir el comando exacto, no un resumen.
- Guardar logs completos, no solo el “OK”.
- Si algo falla, guardarlo también.
- Verificar que el manifiesto no esté vacío.
- Enlazar desde la matriz de trazabilidad.
