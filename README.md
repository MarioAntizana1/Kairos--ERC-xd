# Kairos — ERC

Repositorio del equipo **Kairos** para el European Rover Challenge.

## Secciones

- [`mini-rover/`](mini-rover/) — producto mínimo verificable de navegación
  autónoma sobre Raspberry Pi 4 8 GB + Argon ONE, ROS 2 Jazzy, Nav2, LiDAR 2D
  y Gazebo Harmonic.
- [`drone/`](drone/) — payload de visión estéreo + ToF de piso para el dron:
  Raspberry Pi 5, 2 × Camera Module 3, TFmini Plus 12 m, calibración,
  profundidad, nube de puntos y cotización en Perú.
- [`rover-principal/`](rover-principal/) — visión del rover grande: investigación
  de sensores en Perú (Elgato Facecam 4K, TFmini Plus/S, LIDAR-Lite v3HP),
  arquitectura de percepción, requisitos, BOM y evidencia.

La documentación del drone se puede validar con:

```bash
cd drone
make check
```

La sección `rover-principal` es documental por ahora; hereda la metodología del
mini demo de navegación y aún no tiene pruebas de runtime.

## Mini Rover

El subproyecto de **navegación autónoma** está en
[`mini-rover/`](mini-rover/). Incluye la documentación SDLC, el workspace ROS 2
(`rover_description`, `rover_bringup`, `rover_mission`), los scripts de
validación y la evidencia local.

- Guía de inicio: [`mini-rover/README.md`](mini-rover/README.md).
- Documentación: [`mini-rover/docs/`](mini-rover/docs/).
- Estado: documentación y simulación en borrador; runtime ROS 2/Nav2 pendiente
  de validación en Ubuntu 24.04.
- Hardware base: Raspberry Pi 4 Model B 8 GB + Argon ONE, LiDAR 2D, ROS 2
  Jazzy, Nav2 y Gazebo Harmonic.

```bash
cd mini-rover
make check
```

## Cómo trabajar en el repositorio

El repositorio se organiza en tres carpetas de trabajo independientes:

| Carpeta | Proyecto |
|---|---|
| [`mini-rover/`](mini-rover/) | **Mini-rover** — navegación autónoma |
| [`drone/`](drone/) | **Drone** — payload de visión estéreo + ToF de piso |
| [`rover-principal/`](rover-principal/) | **Rover-principal** — visión del rover grande |

Las reglas comunes para personas y agentes están en [`AGENTS.md`](AGENTS.md), y
las reglas propias de cada subproyecto, en su propio `AGENTS.md`. Las skills
compartidas viven en [`.dsh/skills/`](.dsh/skills/) (ver
[`.dsh/README.md`](.dsh/README.md) y [`.dsh/SOURCES.md`](.dsh/SOURCES.md)).

El BOM de los tres subproyectos, consolidado por proveedor con cantidades totales
y precios para pedir cotizaciones, está en [`cotizaciones/`](cotizaciones/).

## Cotización general

La **cotización general** reúne el BOM de los tres subproyectos agrupado por
proveedor, con cantidades totales, precios, stock al 2026-11-21 y enlaces, lista
para enviar la solicitud a cada empresa:

| Documento | Para qué sirve |
|---|---|
| [`cotizaciones/bom-consolidado.md`](cotizaciones/bom-consolidado.md) | Documento principal: 43 líneas, 55 unidades y ~S/ 7.135,68 repartidos en 11 proveedores |
| [`cotizaciones/bom-consolidado.csv`](cotizaciones/bom-consolidado.csv) | La misma información en tabla, para filtrar o adjuntar |
| [`cotizaciones/solicitud-plantilla.md`](cotizaciones/solicitud-plantilla.md) | Correo y WhatsApp listos, más la tabla de seguimiento de respuestas |

Los precios son de catálogo web consultado el 2026-11-21 y **no autorizan compra**;
el alcance, las exclusiones y la copia de BOM que no se suma están en
[`cotizaciones/README.md`](cotizaciones/README.md).

## Enlaces rápidos

- [Investigación de sensores del rover en Perú](rover-principal/docs/01-investigacion/sensores-peru-2026-11-21.md)
- [Visión del rover grande](rover-principal/docs/01-investigacion/vision-rover-grande.md)
- [BOM de visión](rover-principal/docs/04-diseno/bom-vision.md)
- [Registro de decisiones](rover-principal/docs/00-gobierno/registro-decisiones.md)
