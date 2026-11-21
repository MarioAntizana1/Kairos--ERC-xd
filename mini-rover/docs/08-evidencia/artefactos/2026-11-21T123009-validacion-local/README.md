# Evidencia EV-2026-11-21-01 — validación local

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01, TC-02, TC-03, TC-04, TC-05, TC-21

## 1. Objetivo

Demostrar que, en el host de desarrollo actual, son válidos:

- La estructura y los enlaces de la documentación.
- La coherencia entre `arena.json`, el mundo SDF y el mapa PGM/YAML.
- La lógica pura de misión mediante pruebas unitarias.
- La sintaxis de todos los archivos Python, Bash, YAML, XML/URDF/SDF y JSON.
- El comportamiento seguro del instalador al ejecutarse en un sistema no soportado.

## 2. Requisitos y casos

| Requisito | Caso | Qué se comprueba |
|---|---|---|
| RNF-09 | TC-01..05 | Calidad y pruebas de la lógica de misión |
| RNF-11 | TC-21 | Trazabilidad y documentación |
| — | TC-05 | Carga del YAML de demostración |
| — | Guard | El instalador rechaza Fedora y no modifica el sistema |

## 3. Entorno

| Elemento | Valor |
|---|---|
| Host | Fedora Linux 43 (x86_64) |
| Kernel | 7.3.3-100.fc43.x86_64 |
| Python | 3.14.10 |
| ROS 2 | No instalado |
| Gazebo | No instalado |
| Docker | No instalado |
| Podman | Instalado (no usado) |
| Commit | Sin repositorio Git inicializado en el momento de la ejecución |

> Limitación principal: **no se ejecutó** la pila ROS 2/Nav2/Gazebo. Esta evidencia cubre documentación, assets, lógica pura y sintaxis, no integración.

## 4. Comandos ejecutados

```bash
make check
bash scripts/check_env.sh
python3 scripts/analysis/analyze_runs.py logs/ejemplo-datos-sinteticos.csv \
  --output logs/analisis-ejemplo.md
bash scripts/setup/install_ros_jazzy.sh --dry-run   # debe rechazar Fedora
```

## 5. Resultado

| Comprobación | Resultado | Detalle |
|---|---|---|
| Documentación | OK | 59 documentos, 151 enlaces locales, 0 errores |
| IDs y trazabilidad | OK | 13 RF, 14 RNF, 21 casos de prueba, 7 ADRs |
| Assets | OK | Mapa 260 × 180 px, 0.05 m/px, waypoints validados |
| Pruebas unitarias | OK | 32/32 pruebas |
| Sintaxis | OK | Python 15, Bash 11, YAML 4, XML/URDF/SDF 5, JSON 1 |
| Instalador en Fedora | OK (rechazo esperado) | Exit code 1, sin cambios en el sistema |
| Integración ROS 2 | No ejecutada | Requiere Ubuntu 24.04 + ROS 2 Jazzy |
| Simulación Gazebo | No ejecutada | Requiere Gazebo Harmonic |
| Hardware | No ejecutado | Sin rover físico |

### Salida resumida de `make check`

```text
Docs scanned: 59
Local links checked: 151
Functional/NFR IDs: 13/14
Test cases: 21
ADRs: 7

OK: 0 error(s), 0 warning(s)
OK: mini_marsyard — map 260x180 px, origin (-6.5, -4.5), waypoints validated
Ran 32 tests in 0.008s
OK
Python: 15 file(s), 0 error(s)
Bash: 11 file(s), 0 error(s)
YAML: 4 file(s), 0 error(s)
XML/URDF/SDF: 5 file(s), 0 error(s)
JSON: 1 file(s), 0 error(s)
OK: validación completa
```

## 6. Artefactos

| Archivo | Descripción |
|---|---|
| `logs/make-check.log` | Salida completa de `make check` |
| `logs/check-env.log` | Informe del entorno |
| `logs/install-guard.log` | Rechazo esperado del instalador en Fedora |
| `logs/ejemplo-datos-sinteticos.csv` | Datos **sintéticos** para probar el analizador |
| `logs/analisis-ejemplo.md` | Análisis generado a partir de los datos sintéticos |
| `metadata.json` | Metadatos de la ejecución |
| `MANIFEST.sha256` | Hash de integridad |

> Los datos sintéticos **no** son resultados de la misión. Sirven únicamente para verificar que `analyze_runs.py` calcula métricas e intervalos de confianza correctamente. No deben citarse como evidencia de rendimiento.

## 7. Conclusión

**Aprobada con limitación.** La documentación, los assets, la lógica de misión y la sintaxis son coherentes y pasan las comprobaciones locales. La validación de integración con ROS 2, Nav2 y Gazebo queda pendiente y debe registrarse como una evidencia separada (G3/G4).

## 8. Reproducibilidad

```bash
cd /home/mario/Documentos/rover
make check
bash scripts/check_env.sh
bash scripts/setup/install_ros_jazzy.sh --dry-run || echo "rechazo esperado"
```

Para repetir en un entorno válido:

```bash
# Ubuntu 24.04
bash scripts/setup/install_ros_jazzy.sh
bash scripts/sim/build.sh
ros2 launch rover_bringup sim.launch.py
```

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh \
  docs/08-evidencia/artefactos/2026-11-21T123009-validacion-local
```
