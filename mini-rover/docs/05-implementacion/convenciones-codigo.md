# Convenciones de código y colaboración

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Tech Lead

## 1. Idioma

- **Documentación:** español.
- **Código:** inglés (nombres, docstrings, logs).
- **Commits:** inglés, Conventional Commits.
- **Mensajes al usuario:** español claro, sin jerga innecesaria.

## 2. Python

### Estilo

- PEP 8.
- 4 espacios.
- Líneas ≤ 100 caracteres.
- `snake_case` para funciones y variables; `PascalCase` para clases.
- Type hints en la lógica de dominio.
- Docstrings en inglés, formato Google o reST.
- Sin `print`; usar logging o `self.get_logger()`.

### Ejemplo

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Waypoint:
    """A single mission waypoint in the map frame."""

    id: str
    x: float
    y: float
    yaw: float = 0.0
    tolerance: float = 0.25
    timeout_s: float = 90.0

    def validate(self) -> None:
        """Raise ValueError if the waypoint is not usable."""
        if not self.id:
            raise ValueError("waypoint id must not be empty")
        if not all(math.isfinite(v) for v in (self.x, self.y, self.yaw)):
            raise ValueError(f"waypoint {self.id} has non-finite coordinates")
```

### Reglas

- La lógica de dominio no importa `rclpy`.
- Los nodos ROS son finos: traducen mensajes a llamadas de dominio.
- No usar `time.sleep()` en callbacks; usar timers.
- Manejar excepciones con contexto.
- No silenciar errores con `except Exception: pass`.

## 3. ROS 2

| Elemento | Convención | Ejemplo |
|---|---|---|
| Paquete | `snake_case` | `rover_mission` |
| Nodo | `snake_case` | `mission_node` |
| Topic | minúsculas, `/` | `/rover/mission/status` |
| Frame | `snake_case` | `base_footprint` |
| Parámetro | `snake_case` | `max_retries` |
| Acción | `snake_case` | `navigate_to_pose` |
| Servicio | `snake_case` | `/rover/mission/start` |
| Launch | `snake_case.launch.py` | `sim.launch.py` |
| Archivo de config | `snake_case.yaml` | `nav2_params.yaml` |

- Usar `use_sim_time` en simulación.
- Declarar todos los parámetros con `declare_parameter`.
- No hardcodear rutas; usar `get_package_share_directory`.
- Publicar estado con timestamp.
- Usar QoS adecuado: sensores `SensorDataQoS`, mapas `TransientLocal`.

## 4. YAML

- 2 espacios, sin tabs.
- Claves en `snake_case`.
- Comentarios solo para explicar decisiones, no obviedades.
- Validar con `yaml.safe_load` en los scripts.
- No usar anchors/aliases en configuración de ROS (dificultan la lectura).

## 5. XML/URDF/SDF

- 2 espacios.
- Un elemento por línea cuando sea largo.
- Comentar los plugins y parámetros no obvios.
- Validar XML con `xmllint` o `ElementTree`.
- No mezclar URDF y SDF sin documentar la fuente de verdad.

## 6. Bash

- `#!/usr/bin/env bash` y `set -euo pipefail`.
- Variables entre comillas: `"$VAR"`.
- Funciones con `snake_case`.
- `usage()` y `--help`.
- Comprobar dependencias antes de usarlas.
- No usar `sudo` dentro de scripts sin avisar y comprobar el SO.
- `shellcheck` recomendado (no instalado por defecto).

## 7. Git

### Ramas

| Rama | Uso |
|---|---|
| `main` | Estable, siempre compila |
| `feat/<tema>` | Nueva funcionalidad |
| `fix/<tema>` | Corrección |
| `docs/<tema>` | Documentación |
| `test/<tema>` | Pruebas |
| `chore/<tema>` | Mantenimiento |

### Commits

```text
feat(mission): add retry logic for failed waypoints
fix(bringup): correct map origin in YAML
docs(adr): record ROS 2 Jazzy decision
test(mission): cover duplicate waypoint ids
chore(ci): add docs validation
```

### Reglas

- Un commit = un cambio lógico.
- El mensaje explica **qué** y **por qué**, no solo “cambios”.
- No commitear `build/`, `install/`, `log/`, bags grandes ni secretos.
- Etiquetas semver: `v0.1.0`, `v0.2.0`, etc.
- Antes de merge: `make check`.

## 8. Documentación

- Encabezado de estado, versión, fecha y responsable.
- Enlaces relativos.
- IDs estables (`RF-01`, `TC-01`, `ADR-0001`).
- Diagramas Mermaid en el propio Markdown.
- Fuentes con URL y fecha de acceso.
- No duplicar información: enlazar a la fuente de verdad.

## 9. Pruebas

- Un archivo de test por módulo.
- Nombres descriptivos: `test_mark_failed_retries_once_then_fails`.
- Patrón Arrange-Act-Assert.
- Sin dependencias de red ni de ROS en tests unitarios.
- Cada test debe poder ejecutarse solo.
- Cobertura de casos límite: vacío, duplicado, NaN, timeout, reintento.

## 10. Revisión de código

- [ ] Cumple el requisito y su criterio de aceptación.
- [ ] Tiene tests.
- [ ] `make check` pasa.
- [ ] No hay secretos.
- [ ] La documentación está actualizada.
- [ ] Los nombres son claros.
- [ ] Los errores se manejan.
- [ ] La seguridad no se degrada.
