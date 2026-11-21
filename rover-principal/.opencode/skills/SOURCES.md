# Skills del proyecto — fuentes y alcance

Creadas el **2026-11-21** para la sección `rover-principal`. No son código de
terceros: son instrucciones propias, adaptadas del método de documentación que
el equipo ya usaba en otros proyectos.

| Skill | Propósito | Origen |
|---|---|---|
| `rover-vision` | Contexto, alcance, decisiones y reglas de la visión del rover grande | Propia |
| `documentacion-trazabilidad` | Citas `F-xx`, supuestos, ADR, `OQ-Vxx`, bitácora y evidencia | Adaptada del método de documentación del equipo (proyecto Ares Atlas) |
| `investigacion-proveedores-peru` | Precios, stock, marketplace e importación en tiendas peruanas | Propia, a partir de la investigación del 2026-11-21 |

## Reglas

- Cada skill vive en `.opencode/skills/<id>/SKILL.md`.
- El frontmatter debe tener `name` y `description`.
- No se copian skills de terceros sin licencia verificable.
- Si se adapta una skill externa, se anota aquí la fuente y la licencia.

## Cómo mantenerlas

1. Si cambia una convención del proyecto, actualiza la skill correspondiente.
2. Si una skill deja de aplicar, márcala como obsoleta en este archivo antes de
   borrarla.
3. No dupliques reglas: la fuente de verdad es `AGENTS.md` y
   `docs/00-gobierno/`.
