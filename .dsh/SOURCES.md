# Skills madre del workspace — fuentes, alcance y mantenimiento

Actualizado el **2026-11-23** para la capa central `.dsh/skills/` del workspace
Kairos ERC.

## Origen

Las tres skills nacieron el 2026-11-21 en
`rover-principal/.opencode/skills/` y se promovieron a la raíz del workspace el
2026-11-23 para que los tres subproyectos las compartan. No son código de
terceros: son instrucciones propias, adaptadas del método de documentación que el
equipo ya usaba en otros proyectos.

| Skill | Propósito | Origen | Adaptación en la capa madre |
|---|---|---|---|
| `rover-vision` | Contexto, alcance, decisiones y reglas de la visión del rover grande | Propia | Rutas calificadas con `rover-principal/`; nota explícita de ámbito |
| `documentacion-trazabilidad` | Citas `F-xx`, supuestos, ADR, `OQ`, matriz, bitácora y evidencia | Adaptada del método del equipo (proyecto Ares Atlas) | Generalizada a los tres subproyectos; tabla de IDs por proyecto |
| `investigacion-proveedores-peru` | Precios, stock, marketplace e importación en tiendas peruanas | Propia, a partir de la investigación del 2026-11-21 | Generalizada; se añadió The Pi Box y Falabella al mapa de tiendas |

## Licencia y terceros

- Las skills son material propio del equipo Kairos; su licencia es la del
  repositorio.
- No se copian skills de terceros sin licencia verificable.
- Si se adapta una skill externa, se anota aquí la fuente, la versión y la
  licencia, y el texto no debe implicar respaldo del autor original.

## Reglas de mantenimiento

1. La fuente de verdad de las reglas del proyecto es el `AGENTS.md` de cada
   subproyecto. Una skill es un **procedimiento**, no un reglamento paralelo: si
   la regla ya está en `AGENTS.md` y cabe en tres líneas, no la dupliques aquí.
2. Cada skill declara su ámbito en la primera sección y califica sus rutas con el
   subproyecto (`mini-rover/`, `drone/`, `rover-principal/`).
3. Si una skill deja de aplicar, se marca como obsoleta en este archivo antes de
   borrarla.
4. Si cambia una convención compartida, se actualizan en el mismo commit la skill
   de `.dsh/skills/` y, cuando el equipo use opencode, la copia de
   `rover-principal/.opencode/skills/`.
5. Los cambios que afecten a los tres subproyectos se anotan también en el
   `CHANGELOG.md` del subproyecto donde se originaron y en la bitácora
   correspondiente.

## Estado

| Skill | Estado | Última revisión |
|---|---|---|
| `rover-vision` | Vigente | 2026-11-23 |
| `documentacion-trazabilidad` | Vigente | 2026-11-23 |
| `investigacion-proveedores-peru` | Vigente | 2026-11-23 |

## Huecos conocidos

- `mini-rover/` y `drone/` **no tienen skills propias**: sus reglas viven solo en
  su `AGENTS.md`. Si aparece un procedimiento repetitivo (por ejemplo validar
  URDF/Xacro o generar evidencia de simulación), conviene crear la skill aquí.
- No hay todavía una skill de operación segura de hardware (preflight, E-stop,
  failsafes) aunque la regla existe en los tres `AGENTS.md`. Candidata natural
  para la próxima iteración.
