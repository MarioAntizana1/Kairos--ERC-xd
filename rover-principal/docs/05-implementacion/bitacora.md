# Bitácora — Visión del rover grande

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Documentación

Registro cronológico de trabajo. Cada entrada indica fecha, qué se hizo, qué se
aprendió y qué queda pendiente. No se borran entradas; se corrigen con una nota.

## 2026-11-21 — Creación de la sección e investigación de sensores

**Hecho:**

- Se creó `rover-principal` como sección de visión del rover grande.
- Se copió del mini demo (`../../../rover`) la base metodológica: `metodologia.md`,
  plantillas, `marco-metodologico.md`, `percepcion-3d.md`, `fuentes.md`,
  `protocolo-experimentos.md`, `glosario.md` y política de evidencia.
- Se adaptó `AGENTS.md` para la sección, con decisiones heredadas y preguntas
  propias.
- Se investigaron precios y stock en Memory Kings, Electromanía, Ripley,
  Promart y Naylamp.
- Se documentó la investigación en
  [`../01-investigacion/sensores-peru-2026-11-21.md`](../01-investigacion/sensores-peru-2026-11-21.md).

**Hallazgos:**

- Memory Kings vende un solo modelo de cámara Elgato: Facecam 4K, S/ 828,
  stock > 10. Dos unidades para estéreo: S/ 1 656.
- El “ToF potente” de Electromanía es el TFmini Plus (S/ 330, stock 8), con
  el TFmini-S (S/ 299, stock 3) como alternativa. También hay LIDAR-Lite v3HP
  (S/ 850, stock 11), que es un telémetro de 40 m, no una cámara ToF.
- No hay VL53L8CX ni VL53L5CX en las tiendas peruanas consultadas; hay que
  importarlos.
- La Facecam 4K a 4K solo enfoca 30–120 cm; a 1080p llega a infinito. Es el
  dato que cambia la decisión de modo de trabajo.

**Pendiente:**

- Cerrar OQ-V01 (plataforma de cómputo) y OQ-V02 (3D denso).
- Aprobar presupuesto de la combinación V-A (S/ 1 986).
- Ejecutar E-V2 (sincronía) antes de E-V1 (profundidad).
- Cotizar montaje, cables y envío.
