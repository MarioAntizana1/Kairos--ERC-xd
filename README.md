# Kairos — ERC

Repositorio del equipo **Kairos** para el European Rover Challenge.

## Secciones

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

## Enlaces rápidos

- [Investigación de sensores del rover en Perú](rover-principal/docs/01-investigacion/sensores-peru-2026-11-21.md)
- [Visión del rover grande](rover-principal/docs/01-investigacion/vision-rover-grande.md)
- [BOM de visión](rover-principal/docs/04-diseno/bom-vision.md)
- [Registro de decisiones](rover-principal/docs/00-gobierno/registro-decisiones.md)
