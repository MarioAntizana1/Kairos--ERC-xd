# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y versionado semántico.

## [No publicado]

### Añadido

- Sección **Rover Principal — Percepción y Visión** con base documental y metodológica copiada del mini demo.
- `AGENTS.md` adaptado a la visión del rover grande, con decisiones heredadas y preguntas abiertas propias.
- Metodología SDLC + Design Science Research y plantillas de gobierno.
- Investigación heredada de percepción 3D: estéreo, sincronía, calibración, CPU y alternativas.
- **Investigación de sensores en Perú (2026-11-21):**
  - Elgato Facecam 4K en Memory Kings (S/ 828, stock > 10), Ripley (S/ 1,069) y Promart (S/ 1,199, sin stock online).
  - ToF en Electromanía: TFmini Plus (S/ 330), TFmini-S (S/ 299), LIDAR-Lite v3HP (S/ 850), DFRobot 4 m (S/ 115) y VL53L0X (S/ 16).
  - Alternativas en Naylamp: VL53L1X (S/ 75) y VL53L0X (S/ 69).
  - Brecha identificada: no hay VL53L8CX (ToF 8×8) en las tiendas peruanas consultadas; requiere importación.
- Documento de visión del rover grande: casos de uso, arquitecturas candidatas, hipótesis y criterios de evaluación.
- Alcance de la sección en `docs/02-requisitos/vision-alcance.md`.
- Registro de decisiones y preguntas abiertas `OQ-Vxx`.
- Registro de riesgos `RSK-Vxx`.
- Bitácora y registro de evidencias de la sección.
- BOM de visión `docs/04-diseno/bom-vision.md` y CSV con la combinación recomendada y alternativas.
- Fuentes F-52 a F-71 con URL y fecha de acceso.
- Skills del proyecto: `rover-vision`, `documentacion-trazabilidad` e `investigacion-proveedores-peru`.

### Notas

- No se compró hardware. Los precios y el stock son una fotografía del 2026-11-21.
- La plataforma de cómputo del rover grande sigue sin decidirse; no se asume Raspberry Pi 5.
- El LiDAR se mantiene como sensor primario de navegación y no se re-evalúa en esta sección.
