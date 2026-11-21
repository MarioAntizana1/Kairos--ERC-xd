# Política de evidencia

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
>
> **Nota de esta sección:** esta política se heredó del mini demo. Los scripts
> `scripts/evidence/*.sh` viven en `../../../rover/scripts/evidence/` y todavía
> no se copiaron a `rover-principal`. La sección usará su propia carpeta cuando
> ejecute el primer experimento de visión.

## 1. Principio

La evidencia no es un adorno: es la prueba de que el sistema cumple lo que decimos. Debe ser **trazable, reproducible, íntegra y verificable**.

## 2. Qué cuenta como evidencia

| Tipo | Ejemplo | Válido |
|---|---|---|
| Ejecución de prueba | Log de `unittest`, salida de `colcon test` | Sí |
| Bag de ROS 2 | `/scan`, `/odom`, `/cmd_vel`, estado | Sí |
| Captura o vídeo | Demo, RViz, rover en pista | Sí, con contexto |
| Medición | CSV de 10 ensayos, error final | Sí, con método |
| Documento firmado | Checklist de seguridad | Sí |
| “Funciona en mi máquina” | Sin log ni entorno | **No** |
| Captura sin fecha ni commit | — | **No** |
| Vídeo editado sin datos | — | **No** |

## 3. Formato de carpeta

```text
docs/08-evidencia/artefactos/YYYY-MM-DDTHHMMSS-<slug>/
├── README.md          # objetivo, resultado, conclusión, reproducibilidad
├── metadata.json      # fecha, host, SO, versiones, commit, comando, operador
├── MANIFEST.sha256    # hashes
├── logs/              # salidas de consola
├── media/             # fotos, vídeos, capturas
└── bags/              # rosbag2 (o enlace + hash)
```

## 4. Metadatos mínimos

| Campo | Ejemplo |
|---|---|
| `id` | `EV-2026-11-21-01` |
| `date` | `2026-11-21T12:00:00Z` |
| `operator` | `QA` |
| `host` | `rover-dev-vm` |
| `os` | `Ubuntu 24.04.5` |
| `kernel` | `6.8.0-...` |
| `ros_distro` | `jazzy` |
| `gazebo` | `harmonic` |
| `commit` | `abc1234` |
| `dirty` | `false` |
| `command` | `make check` |
| `requirements` | `RNF-09, RNF-11` |
| `tests` | `TC-01..05, TC-21` |
| `result` | `passed` |

## 5. Integridad

- Generar `MANIFEST.sha256` con `sha256sum` al cerrar.
- No modificar archivos después de sellar.
- Si hay que corregir, crear una nueva carpeta y marcar la anterior como `Obsoleta`.
- Los bags grandes se guardan fuera del repo; registrar URL y hash.

## 6. Retención

| Tipo | Retención | Dónde |
|---|---|---|
| Logs y CSV | Todo el proyecto | Git |
| Bags pequeños (< 50 MB) | Todo el proyecto | Git |
| Bags grandes | Hasta 1 año | Almacenamiento externo |
| Vídeos | Todo el proyecto | Git LFS o externo |
| Evidencia de demo | Permanente | Git + copia |

## 7. Privacidad

- No grabar rostros sin consentimiento.
- Anonimizar nombres si es necesario.
- No publicar datos personales.
- Respetar la licencia de imágenes y música.

## 8. Registro

Cada carpeta se anota en [`registro-evidencias.md`](registro-evidencias.md):

| Campo | Descripción |
|---|---|
| ID | `EV-YYYY-MM-DD-NN` |
| Fecha | ISO 8601 |
| Tipo | test, sim, hardware, demo, docs |
| Requisitos | IDs |
| Casos | IDs |
| Resultado | passed/failed/inconclusive |
| Ruta | Relativa |
| Hash | SHA-256 del manifiesto |
| Estado | Ejecutada/Aprobada/Obsoleta |

## 9. Ejemplo

```bash
bash scripts/evidence/new_evidence.sh "validacion-local"
# ... ejecutar ...
bash scripts/evidence/seal_evidence.sh docs/08-evidencia/artefactos/2026-11-21T120000-validacion-local
```

## 10. Buenas prácticas

- Ejecuta la evidencia en el entorno objetivo, no en uno aproximado.
- Incluye el comando exacto, no un resumen.
- Guarda los logs completos, no solo el “OK”.
- Si algo falla, guárdalo también: los fallos son evidencia.
- Revisa que el manifiesto no esté vacío.
- Enlaza la evidencia desde la matriz de trazabilidad.
