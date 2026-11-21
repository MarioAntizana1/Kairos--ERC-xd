# Guion de demo y presentación

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Comunicación

## 1. Mensaje central

> “Construimos una base de navegación autónoma fiable, segura y medible sobre la que escalar el rover del ERC 2027. No es un vídeo: es un sistema con evidencia reproducible.”

Tres ideas que el jurado debe recordar:

1. **Autonomía real (N2):** la misión se carga antes; el rover decide ruta y evita obstáculos.
2. **Seguridad por diseño:** e-stop física, watchdog, límites y zona delimitada.
3. **Rigor:** requisitos, pruebas, bags, métricas y lecciones aprendidas.

## 2. Estructura de 10 minutos

| Min | Bloque | Contenido | Soporte |
|---|---|---|---|
| 0:00 | Gancho | “Imagina un rover a 200 millones de km; no puedes teleoperarlo.” | Imagen del Marsyard |
| 0:45 | Problema | ERC, navegación, 5 checkpoints, autonomía sin vídeo | Slide 2 |
| 1:45 | Solución | Rover mini demo: ROS 2 + Nav2 + LiDAR + Pi 5 | Slide 3 |
| 3:00 | Arquitectura | Diagrama de componentes y flujo de misión | Slide 4 |
| 4:00 | Seguridad | E-stop, watchdog, límites, FMEA | Slide 5 |
| 4:45 | Demo | Misión en vivo o vídeo | RViz / rover |
| 7:30 | Evidencia | 10 ensayos, éxito, error, tiempos | Slide 6 |
| 8:30 | Lecciones | Fallos, correcciones, qué aprendimos | Slide 7 |
| 9:15 | Siguiente | Escalado al rover grande y ERC 2027 | Slide 8 |
| 9:45 | Cierre | Gracias + pregunta | — |

## 3. Guion de 5 minutos

| Min | Bloque |
|---|---|
| 0:00 | Gancho y problema |
| 0:45 | Solución y arquitectura |
| 1:45 | Demo |
| 3:30 | Evidencia y seguridad |
| 4:30 | Lecciones y siguiente paso |
| 4:50 | Cierre |

## 4. Storytelling

### Acto 1 — El problema

“En Marte no hay un mando a distancia. El rover tiene que decidir. El ERC lo prueba con cinco checkpoints, obstáculos y puntuación extra si eres autónomo y no usas vídeo.”

### Acto 2 — La solución

“No intentamos construir el rover completo de golpe. Construimos la base: percepción, localización, planificación, control y seguridad. Y lo hacemos con estándares abiertos: ROS 2, Nav2, Gazebo.”

### Acto 3 — La prueba

“Aquí está el rover. La misión ya está cargada. No lo estoy teleoperando. Mirad el progreso y la ruta. Si algo va mal, esta e-stop corta la potencia.”

### Acto 4 — La evidencia

“No os pedimos que confiéis: aquí está el bag, el CSV, el informe y el hash. Cualquiera puede repetirlo.”

### Acto 5 — El siguiente paso

“Esta base escala al rover grande: brazo, ciencia, perforación. El ERC 2027 es el objetivo.”

## 5. Slides

1. Portada: nombre, equipo, ERC 2027.
2. Problema: Marsyard, navegación, autonomía.
3. Solución: rover mini demo.
4. Arquitectura: diagrama de componentes.
5. Seguridad: capas de parada.
6. Evidencia: métricas y trazabilidad.
7. Lecciones: qué falló y qué aprendimos.
8. Roadmap: del demo al rover completo.
9. Cierre: gracias y contacto.

### Consejos de diseño

- Una idea por slide.
- Texto grande, poco texto.
- Diagramas propios, no capturas borrosas.
- Mostrar números reales, no promesas.
- Incluir el estado “borrador” si algo no está validado.

## 6. Demo en vivo

### Antes

- Ensayar 3 veces.
- Tener el vídeo de respaldo.
- E-stop en mano del observador.
- Zona despejada.
- Bag grabando.

### Durante

- Narrar lo que se ve.
- No tocar comandos no ensayados.
- Si algo falla, abortar con calma y pasar al vídeo.
- No decir “funciona siempre”.

### Después

- Mostrar el resumen y la evidencia.
- Guardar todo.
- Anotar incidencias.

## 7. Preguntas y respuestas

Ver [`faq-jurado.md`](faq-jurado.md). Reglas:

- Si no sabes, di “no lo hemos medido; lo comprobamos”.
- No inventes cifras.
- Apoya cada afirmación en un documento o evidencia.
- Reconoce las limitaciones.

## 8. Material de apoyo

| Material | Dónde |
|---|---|
| Vídeo de demo | `docs/08-evidencia/artefactos/` |
| Bag | `docs/08-evidencia/artefactos/` |
| Métricas | `docs/06-pruebas/resultados/` |
| Arquitectura | `docs/03-arquitectura/` |
| Requisitos | `docs/02-requisitos/` |
| Runbook | `docs/07-operacion/runbook-demo.md` |

## 9. Ensayo

| Fecha | Duración | Observaciones | Estado |
|---|---|---|---|
| — | — | — | Pendiente |

## 10. Checklist de presentación

- [ ] Guion memorizado.
- [ ] Slides revisadas.
- [ ] Demo ensayada.
- [ ] Vídeo de respaldo.
- [ ] Evidencia accesible.
- [ ] FAQ repasado.
- [ ] Contacto y QR al repo.
- [ ] Llegada con margen.
