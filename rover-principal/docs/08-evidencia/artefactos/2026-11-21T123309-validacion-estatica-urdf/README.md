# Evidencia EV-2026-11-21-02 — validación estática de URDF, lint y energía

> Fecha: 2026-11-21 · Estado: Aprobada con limitación · Responsable: QA
> Requisitos: RNF-09 · Casos: evidencia de soporte (no sustituye TC-06)

## 1. Objetivo

Validar sin ROS 2:

- Que el Xacro del rover se procesa y genera un URDF bien formado.
- Que el URDF tiene enlaces, joints, sensores y plugins coherentes.
- Que el código Python no tiene errores estáticos (nombres indefinidos, sintaxis).
- Que el modelo energético del estudio 6×6 se ejecuta y produce resultados.
- Que la suite documental y de pruebas unitarias sigue en verde.

## 2. Alcance y limitación

Esta evidencia es **estática**. No demuestra que Gazebo cargue el modelo, que Nav2
se active ni que el rover navegue. Esas pruebas requieren Ubuntu 24.04 + ROS 2
Jazzy + Gazebo Harmonic y se registrarán por separado (TC-06 y siguientes).

El estudio energético 6×6 es una **variante** documentada en
[`docs/04-diseno/energia/calculo-energetico.md`](../../../04-diseno/energia/calculo-energetico.md).
No es la base del mini demo hasta que se resuelva OQ-09.

## 3. Entorno

| Elemento | Valor |
|---|---|
| Host | Fedora Linux 43 (x86_64) |
| Python | 3.14.10 |
| ROS 2 / Gazebo | No instalados |
| Herramientas aisladas | `xacro`, `urdf-parser-py`, `ruff` en `/tmp/opencode/rover-venv` |
| Commit | Sin repositorio Git inicializado en el momento de la ejecución |

## 4. Comandos ejecutados

```bash
make check
bash scripts/test/lint.sh
/tmp/opencode/rover-venv/bin/ruff check --select E9,F --output-format concise .
/tmp/opencode/rover-venv/bin/xacro \
  ros_ws/src/rover_description/urdf/rover.urdf.xacro \
  > logs/rover.urdf
python3 scripts/test/check_urdf.py logs/rover.urdf
make energy
```

## 5. Resultado

| Comprobación | Resultado | Detalle |
|---|---|---|
| Xacro | OK | Genera un URDF de 291 líneas |
| Estructura URDF | OK | 8 links, 7 joints, 2 sensores, 2 plugins de Gazebo |
| Ruff (E9/F) | OK | 0 errores |
| `make check` | OK | 61 documentos, 170 enlaces, 32 pruebas unitarias |
| Modelo energético | OK | Consumo de crucero 20,4 W; pack 2S2P 50,4 Wh; fallo 187,2 W |
| Runtime ROS 2 | No ejecutado | Pendiente de Ubuntu 24.04 |

### Salida clave

```text
URDF OK: 8 links, 7 joints, 2 sensors, 2 gazebo plugins
All checks passed!
OK: validación completa
```

## 6. Artefactos

| Archivo | Descripción |
|---|---|
| `logs/rover.urdf` | URDF generado desde Xacro |
| `logs/xacro.log` | Salida de error de Xacro (vacía si no hay avisos) |
| `logs/urdf-check.log` | Resultado del validador estático |
| `logs/ruff.log` | Resultado de Ruff |
| `logs/lint.log` | Resultado de `scripts/test/lint.sh` |
| `logs/make-check.log` | Suite completa |
| `logs/energy.log` | Informe del modelo energético |
| `logs/check-env.log` | Entorno del host |
| `metadata.json` | Metadatos |
| `MANIFEST.sha256` | Integridad |

## 7. Conclusión

**Aprobada con limitación.** El URDF es sintácticamente válido y coherente, el
código no tiene errores estáticos y el modelo energético se ejecuta. Falta la
validación en Gazebo/Nav2 y en hardware.

## 8. Reproducibilidad

```bash
cd /home/mario/Documentos/rover
make check
bash scripts/test/lint.sh
xacro ros_ws/src/rover_description/urdf/rover.urdf.xacro > /tmp/rover.urdf
python3 scripts/test/check_urdf.py /tmp/rover.urdf
make energy
```

## 9. Sellar

```bash
bash scripts/evidence/seal_evidence.sh \
  docs/08-evidencia/artefactos/2026-11-21T123309-validacion-estatica-urdf
```
