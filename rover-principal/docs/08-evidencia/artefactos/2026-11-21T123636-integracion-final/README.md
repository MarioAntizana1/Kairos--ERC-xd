# Evidencia EV-2026-11-21-04 — integración final

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01..05, TC-21

## 1. Objetivo

Validar el repositorio completo una vez integrado el estudio 6×6 (cálculo
energético, diseño eléctrico y BOM) junto con la base del mini demo:

- Documentación, enlaces, IDs, fuentes y trazabilidad.
- Coherencia de arena, mundo y mapa.
- Pruebas unitarias de la lógica de misión.
- Sintaxis de todos los lenguajes y formatos.
- Xacro → URDF y estructura del robot.
- Ruff y modelo energético.
- Separación explícita entre la base del mini demo y la variante 6×6 (OQ-09).

## 2. Requisitos y casos

| Requisito | Caso | Cobertura |
|---|---|---|
| RNF-09 | TC-01..05 + lint | Calidad de código y lógica |
| RNF-11 | TC-21 | Documentación y trazabilidad |
| — | Estático | URDF, Xacro, Ruff y energía |

## 3. Entorno

| Elemento | Valor |
|---|---|
| Host | Fedora Linux 43 (x86_64) |
| Python | 3.14.10 |
| ROS 2 / Gazebo | No instalados |
| Venv aislado | `/tmp/opencode/rover-venv` |
| Herramientas | Ruff 0.17.6, Xacro 2.1.1, PyYAML 6.0.4 |
| Commit | Sin repositorio Git inicializado en la ejecución |

## 4. Comandos ejecutados

```bash
export PATH="/tmp/opencode/rover-venv/bin:$PATH"
make check
make urdf-check
make energy
make docs
bash scripts/check_env.sh
```

## 5. Resultado

| Comprobación | Resultado |
|---|---|
| Documentación | 67 Markdown (incluye este informe), 207 enlaces, 0 errores |
| IDs y trazabilidad | 13 RF, 14 RNF, 21 casos, 7 ADRs |
| Fuentes | 26 registradas y referenciadas |
| Assets | Mapa 260 × 180 px, 0.05 m/px, waypoints válidos |
| Pruebas unitarias | **34/34 OK** |
| Python | 16 archivos, 0 errores |
| Bash | 11 archivos, 0 errores |
| YAML | 5 archivos, 0 errores |
| XML/URDF/SDF | 6 archivos, 0 errores |
| JSON | 4 archivos, 0 errores |
| Ruff (E9/F) | 0 errores |
| Xacro → URDF | 291 líneas |
| Estructura URDF | 8 links, 7 joints, 2 sensores, 2 plugins |
| Modelo energético | OK (crucero 20,4 W; pack 2S2P 50,4 Wh) |
| Runtime ROS 2 / Gazebo | No ejecutado |
| Hardware | No ejecutado |

### Salida clave

```text
Docs scanned: 67
Local links checked: 207
Sources: 26
OK: 0 error(s), 0 warning(s)

Ran 34 tests in 0.008s
OK

URDF OK: 8 links, 7 joints, 2 sensors, 2 gazebo plugins
All checks passed!
OK: validación completa
```

## 6. Artefactos

| Archivo | Descripción |
|---|---|
| `logs/make-check.log` | Suite completa |
| `logs/urdf-check.log` | Generación y validación del URDF |
| `logs/energy.log` | Informe energético |
| `logs/docs.log` | Validación documental |
| `logs/check-env.log` | Entorno del host |
| `logs/tool-versions.txt` | Versiones de herramientas |
| `logs/pip-freeze.txt` | Dependencias del venv |
| `metadata.json` | Metadatos |
| `MANIFEST.sha256` | Integridad |

## 7. Conclusión

**Aprobada con limitación.** La base del mini demo y el estudio 6×6 están
documentados, separados y validados a nivel estático. La decisión de arquitectura
energética (OQ-09) sigue abierta y **no debe comprarse hardware de la variante**
hasta que se resuelva. La pila ROS 2/Nav2/Gazebo sigue pendiente de runtime.

## 8. Reproducibilidad

```bash
cd /home/mario/Documentos/rover
python3 -m venv /tmp/opencode/rover-venv
/tmp/opencode/rover-venv/bin/pip install PyYAML xacro ruff
export PATH="/tmp/opencode/rover-venv/bin:$PATH"
make check
make urdf-check
make energy
```

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh \
  docs/08-evidencia/artefactos/2026-11-21T123636-integracion-final
```
