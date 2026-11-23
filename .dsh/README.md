# `.dsh/` — capa central (madre) de skills del workspace

Este directorio es la **fuente canónica de skills** de todo el workspace Kairos
ERC. No es código del proyecto ni estado de ejecución: son instrucciones
versionadas.

## Por qué está aquí

El proveedor local de skills de DeepSeek Harness escanea, en orden de prioridad:

| Rango | Origen | Ruta |
|---|---|---|
| 100 | `project-dsh` | `<raíz-del-repo>/.dsh/skills` |
| 200 | `project-agents` | `<raíz-del-repo>/.agents/skills` |
| 300 | `custom` | `Config.customSkillDirs` |
| 400 | `user-dsh` | `<dshHome>/skills` |

La raíz del proyecto es el ancestro más cercano que contiene `.git`. Como el
workspace es un checkout del repositorio, la raíz es `D:\ERC-UNMSM-Rover` y todo
lo que viva en `.dsh/skills/` lo ven **todos** los agentes y subagentes que
trabajen dentro de `mini-rover/`, `drone/` o `rover-principal/`.

## Estructura

```text
.dsh/
├── README.md                       Este documento (no es una skill)
├── SOURCES.md                      Procedencia y reglas de mantenimiento
└── skills/
    ├── documentacion-trazabilidad/SKILL.md
    ├── investigacion-proveedores-peru/SKILL.md
    └── rover-vision/SKILL.md
```

## Reglas de formato

- Una skill es una **carpeta** `skills/<nombre>/SKILL.md`; el nombre debe ser
  kebab-case y coincidir con el `name` del frontmatter.
- El frontmatter necesita `name` y `description`. La `description` es lo único
  que ve el agente en el catálogo (límite práctico 500 caracteres): debe decir
  **cuándo** usar la skill, no cómo implementarla.
- No pongas archivos `.md` sueltos en `.dsh/skills/`: el proveedor los trata
  como skills planas y un nombre inválido ensucia el catálogo.
- Referencias a scripts, plantillas o datos: guarda los recursos dentro de la
  carpeta de la skill y cítalos con ruta relativa.

## Cómo se heredan

1. `AGENTS.md` de la raíz da las reglas globales del workspace.
2. `AGENTS.md` de cada subproyecto da las reglas específicas y **prevalece**
   sobre el de la raíz para los archivos de su carpeta.
3. Las skills de `.dsh/skills/` están disponibles para los tres subproyectos;
   cada skill declara en su primera sección a qué subproyecto aplica y cómo se
   resuelven sus rutas.

## Relación con `rover-principal/.opencode/skills/`

Las tres skills nacieron en `rover-principal/.opencode/skills/` (cliente
opencode). Esa copia se conserva para no romper ese flujo, pero la **madre es
esta**: aquí están adaptadas para el workspace completo (rutas calificadas por
subproyecto y convenciones de IDs de los tres proyectos).

Si cambias una convención compartida:

1. Actualiza la skill en `.dsh/skills/` (la que leen los agentes de este
   workspace).
2. Si el equipo sigue usando opencode, actualiza también la copia en
   `rover-principal/.opencode/skills/`.
3. Anota el cambio en `.dsh/SOURCES.md` y en la bitácora del subproyecto.

## Añadir una skill nueva

1. Comprueba que no exista ya una regla en el `AGENTS.md` del subproyecto: si la
   regla es corta, va en `AGENTS.md`; si es un procedimiento con pasos, va en
   una skill.
2. Crea `skills/<nombre>/SKILL.md` con frontmatter `name` + `description`.
3. Abre el archivo con la sección **Ámbito**, indicando a qué subproyecto aplica
   y las rutas relativas que usa.
4. Registra el origen y la licencia en `.dsh/SOURCES.md`.
5. Verifica que aparece en el catálogo de la sesión (el proveedor tiene un
   watcher: no hace falta reiniciar).
