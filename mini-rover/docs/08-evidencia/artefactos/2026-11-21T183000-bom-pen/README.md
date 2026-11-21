# Evidencia EV-2026-11-21-07 — BOM base en soles

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01..05, TC-21

## 1. Objetivo

Validar la conversión de la BOM base a soles peruanos (PEN) con precios locales
de Perú, y comprobar que la documentación asociada (`bom.md`, `bom-peru.md`,
`bom-peru.csv` y la bitácora) es coherente.

La BOM vigente usa Pi 4 8 GB + Argon ONE reutilizadas, SSD USB 256 GB, fuente
27 W, cargador LiFePO4 y sustitutos locales para motor, driver y batería.

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
| Precios | Catálogos de Perú consultados el 2026-11-21 |

## 4. Comando ejecutado

```bash
make check
```

## 5. Resultado

| Comprobación | Resultado |
|---|---|
| Documentación | 78 Markdown (incluye este informe), 355 enlaces, 0 errores |
| IDs y trazabilidad | 13 RF, 14 RNF, 21 casos, 12 ADRs |
| Fuentes | 64 registradas y referenciadas |
| Assets | Mapa 260 × 180 px, 0.05 m/px, waypoints válidos |
| Pruebas unitarias | **34/34 OK** |
| Python | 16 archivos, 0 errores |
| Bash | 11 archivos, 0 errores |
| YAML | 5 archivos, 0 errores |
| XML/URDF/SDF | 6 archivos, 0 errores |
| JSON | 5 archivos, 0 errores |
| BOM | 25 líneas; subtotal S/ 2.520,08; total S/ 2.646,08 |
| Runtime ROS 2 / Gazebo | **No ejecutado** |
| Stock / compra | **No confirmado** |

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

La validación estática pasa y la suma de la BOM coincide con el total
(S/ 2.520,08 + 5 % = S/ 2.646,08). Limitaciones: los precios son una fotografía
al 2026-11-21, el stock no está reservado, la compra no está aprobada y no se
ejecutó runtime ROS 2/Gazebo ni verificación física del hardware.

## 8. Reproducibilidad

```bash
cd <raíz-del-repositorio>
make check
python3 - <<'PY'
# Suma de la tabla de bom.md
# (ver el informe; el total debe dar S/ 2.520,08)
PY
```

El resultado de `make check` debe ser 0 errores y 0 advertencias. Las
herramientas opcionales (`ruff`, `xacro`, `shellcheck`) no están instaladas en
este host y se omiten.

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh "docs/08-evidencia/artefactos/2026-11-21T183000-bom-pen"
```
