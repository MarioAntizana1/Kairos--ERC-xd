# Evidencia EV-2026-11-21-03 — validación final previa a runtime

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09, RNF-11 · Casos: TC-01..05, TC-21

## 1. Objetivo

Consolidar el estado del proyecto antes de pasar a Ubuntu 24.04 + ROS 2:

- Documentación, enlaces, IDs y trazabilidad.
- Coherencia de la arena, el mundo SDF y el mapa.
- Pruebas unitarias de la lógica de misión.
- Sintaxis de Python, Bash, YAML, XML/URDF/SDF y JSON.
- Xacro → URDF y estructura del robot.
- Ruff (errores estáticos).
- Modelo energético preliminar.
- Comportamiento seguro del instalador en un SO no soportado.

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
| Herramientas | Ruff 0.17.6, Xacro (pip), PyYAML 6.0.2 |
| Commit | Sin repositorio Git inicializado en la ejecución |

> La validación de runtime (Gazebo, Nav2, hardware) **no** forma parte de esta evidencia. Debe ejecutarse en Ubuntu 24.04 y registrarse como EV posterior.

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
| Documentación | 63 Markdown (incluye este informe), 174 enlaces, 0 errores |
| IDs y trazabilidad | 13 RF, 14 RNF, 21 casos, 7 ADRs |
| Assets | Mapa 260 × 180 px, 0.05 m/px, waypoints válidos |
| Pruebas unitarias | **34/34 OK** |
| Python | 16 archivos, 0 errores |
| Bash | 11 archivos, 0 errores |
| YAML | 5 archivos, 0 errores |
| XML/URDF/SDF | 6 archivos, 0 errores |
| JSON | 3 archivos, 0 errores |
| Ruff (E9/F) | 0 errores |
| Xacro → URDF | 291 líneas |
| Estructura URDF | 8 links, 7 joints, 2 sensores, 2 plugins |
| Modelo energético | OK (crucero 20,4 W; pack 2S2P 50,4 Wh) |
| Instalador en Fedora | Rechazo esperado (exit 1) |
| Runtime ROS 2 / Gazebo | No ejecutado |
| Hardware | No ejecutado |

### Salida clave

```text
Docs scanned: 63
Local links checked: 174
OK: 0 error(s), 0 warning(s)

Ran 34 tests in 0.009s
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

**Aprobada con limitación.** El proyecto es coherente a nivel documental, estático y de lógica pura. La pila ROS 2/Nav2/Gazebo sigue sin validarse en runtime; esa es la siguiente puerta (G3/G4).

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
  docs/08-evidencia/artefactos/2026-11-21T123448-validacion-final-pre-runtime
```
