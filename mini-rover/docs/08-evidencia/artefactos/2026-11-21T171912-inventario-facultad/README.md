# Evidencia EV-2026-11-21-05 — inventario de facultad

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01..05, TC-21

## 1. Objetivo

Registrar el inventario de materiales declarado por el responsable del proyecto
y validar que la documentación asociada (inventario, mapeo a la BOM base,
mapeo a la variante 6×6, brechas y riesgos) es coherente, enlaza correctamente
y no introduce identificadores sin definir.

El inventario **no se ha verificado físicamente** y no autoriza compras ni
cambios de alcance.

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
| Inventario | `inventario actual.txt`, declaración del usuario |

## 4. Comando ejecutado

```bash
make check
```

## 5. Resultado

| Comprobación | Resultado |
|---|---|
| Documentación | 73 Markdown (incluye este informe), 296 enlaces, 0 errores |
| IDs y trazabilidad | 13 RF, 14 RNF, 21 casos, 9 ADRs |
| Fuentes | 61 registradas y referenciadas |
| Assets | Mapa 260 × 180 px, 0.05 m/px, waypoints válidos |
| Pruebas unitarias | **34/34 OK** |
| Python | 16 archivos, 0 errores |
| Bash | 11 archivos, 0 errores |
| YAML | 5 archivos, 0 errores |
| XML/URDF/SDF | 6 archivos, 0 errores |
| JSON | 5 archivos, 0 errores |
| Runtime ROS 2 / Gazebo | **No ejecutado** |
| Inventario físico | **No verificado** |

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

La validación estática pasa. La limitación es doble: no se ejecutó la pila ROS
2/Nav2/Gazebo y el inventario es una declaración sin inspección física. Las
brechas de hardware siguen abiertas y se registran en
[`inventario-facultad.md`](../../../04-diseno/inventario-facultad.md).

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
bash scripts/evidence/seal_evidence.sh "docs/08-evidencia/artefactos/2026-11-21T171912-inventario-facultad"
```
