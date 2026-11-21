# Evidencia EV-2026-11-21-06 — cambio a Pi 4, cámara y LTE

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01..05, TC-21

## 1. Objetivo

Validar que la documentación del cambio de plataforma a **Raspberry Pi 4 Model B
de 8 GB + Argon ONE** (ADR-0010) es coherente y que las propuestas de cámara
CSI + USB (ADR-0011) y LTE/GNSS con LilyGO (ADR-0012) están correctamente
delimitadas.

El cambio afecta a RNF-07, TC-20, BOM, arquitectura, diseño eléctrico,
instalación, operación y presentación. La BOM revisada queda pendiente de
aprobación; las propuestas de cámara y LTE son spikes, no resultados.

## 2. Requisitos y casos

| Requisito | Caso | Cobertura |
|---|---|---|
| RNF-09 | TC-01..05 + lint | Calidad de código y lógica |
| RNF-11 | TC-21 | Documentación y trazabilidad |
| — | Estático | Enlaces, fuentes, IDs, assets y lint |

## 3. Entorno

| Elemento | Valor |
|---|---|
| Host | Fedora Linux 43 (x86_64) |
| Python | 3.14.10 |
| ROS 2 / Gazebo | No instalados |
| Commit | Sin repositorio Git inicializado en la ejecución |
| Hardware | Pi 4 8 GB + Argon ONE declarados, sin inspección física |

## 4. Comando ejecutado

```bash
make check
```

## 5. Resultado

| Comprobación | Resultado |
|---|---|
| Documentación | 77 Markdown (incluye este informe), 346 enlaces, 0 errores |
| IDs y trazabilidad | 13 RF, 14 RNF, 21 casos, 12 ADRs |
| Fuentes | 64 registradas y referenciadas |
| Assets | Mapa 260 × 180 px, 0.05 m/px, waypoints válidos |
| Pruebas unitarias | **34/34 OK** |
| Python | 16 archivos, 0 errores |
| Bash | 11 archivos, 0 errores |
| YAML | 5 archivos, 0 errores |
| XML/URDF/SDF | 6 archivos, 0 errores |
| JSON | 5 archivos, 0 errores |
| Runtime ROS 2 / Gazebo | **No ejecutado** |
| Hardware / CSI / LTE | **No verificado** |

## 6. Artefactos

| Archivo | Descripción |
|---|---|
| `logs/make-check.log` | Salida completa de `make check` |
| `metadata.json` | Metadatos de la ejecución |
| `MANIFEST.sha256` | Hashes de los archivos sellados |

## 7. Conclusión

- [ ] Aprobado
- [x] Aprobado con desviación
- [ ] Fallido
- [ ] Inconcluso

La validación estática pasa. Las limitaciones son: no se ejecutó ROS 2/Nav2/
Gazebo, el inventario no se ha inspeccionado, el acceso al CSI con la carcasa
Argon está por verificar y los spikes de cámara/LTE no se han ejecutado. La BOM
revisada (671 EUR) está pendiente de aprobación.

## 8. Reproducibilidad

```bash
cd <raíz-del-repositorio>
make check
```

El resultado debe ser 0 errores y 0 advertencias en documentación, assets,
pruebas unitarias y lint. Las herramientas opcionales (`ruff`, `xacro`,
`shellcheck`) no están instaladas en este host y se omiten.

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh "docs/08-evidencia/artefactos/2026-11-21T180549-cambio-pi4-camera-lte"
```
