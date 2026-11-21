# Runbook de demo

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Comunicación
> Objetivo: ejecutar una demo de 10 minutos, segura y reproducible, ante público o jurado.

## 1. Resumen

| Campo | Valor |
|---|---|
| Duración | 10 min (versión corta: 5 min) |
| Público | Jurado, universidad, patrocinadores |
| Mensaje clave | “Navegación autónoma fiable, segura y medible, con evidencia reproducible” |
| Riesgo principal | Fallo técnico en directo |
| Plan B | Vídeo pregrabado + bag + explicación |

## 2. Preparación

### T-60 min

- [ ] Cargar batería al 100%.
- [ ] Encender el rover y comprobar temperatura.
- [ ] Ejecutar preflight.
- [ ] Probar la e-stop.
- [ ] Verificar WiFi/Ethernet.
- [ ] Abrir RViz y el terminal con el runbook.
- [ ] Comprobar que el bag se graba.
- [ ] Ensayar la misión una vez.

### T-15 min

- [ ] Delimitar la zona.
- [ ] Retirar obstáculos no previstos.
- [ ] Colocar el rover en la pose inicial.
- [ ] Verificar TF y topics.
- [ ] Silenciar notificaciones.
- [ ] Confirmar que el vídeo de respaldo está accesible.

### T-5 min

- [ ] E-stop en mano del observador.
- [ ] Público fuera de la zona.
- [ ] Cronómetro listo.
- [ ] Guion a la vista.
- [ ] Respiración.

## 3. Guion de 10 minutos

| Tiempo | Bloque | Qué se dice / hace |
|---|---|---|
| 0:00–1:00 | Gancho | “Un rover que debe navegar solo en un terreno marciano. Hoy demostramos la base: autonomía, seguridad y evidencia.” |
| 1:00–2:30 | Problema | ERC, Marsyard, prueba de navegación, cinco checkpoints, autonomía sin vídeo. |
| 2:30–4:00 | Solución | ROS 2 + Nav2 + LiDAR + Raspberry Pi 4 8 GB. Diagrama simple. |
| 4:00–5:00 | Seguridad | E-stop, watchdog, límites, zona. |
| 5:00–8:00 | Demo | Lanzar misión. Mostrar RViz, progreso, rover. Narrar lo que ocurre. |
| 8:00–9:00 | Evidencia | Bag, métricas, 10 ensayos, error final. |
| 9:00–9:45 | Lecciones | Qué falló, qué aprendimos, qué sigue. |
| 9:45–10:00 | Cierre | “Buscamos llevar esta base al rover completo del ERC 2027.” |

## 4. Guion de 5 minutos

| Tiempo | Bloque |
|---|---|
| 0:00–0:45 | Gancho y problema |
| 0:45–1:45 | Solución y arquitectura |
| 1:45–3:30 | Demo en vivo |
| 3:30–4:30 | Evidencia y métricas |
| 4:30–5:00 | Cierre y siguiente paso |

## 5. Demo en vivo

### Antes de empezar

```bash
ros2 topic echo /rover/mission/status
```

Debe decir `IDLE`.

### Lanzar

```bash
ros2 launch rover_bringup mission.launch.py
```

O:

```bash
ros2 service call /rover/mission/start std_srvs/srv/Trigger
```

### Narrar

- “El rover ya tiene la misión cargada; no lo estoy teleoperando.”
- “Está planificando la ruta y evitando obstáculos.”
- “El progreso se publica en tiempo real.”
- “Si algo va mal, esta es la e-stop.”

### Terminar

- Esperar `COMPLETED`.
- Mostrar el resumen.
- Enseñar el bag y el registro de evidencias.
- No improvisar comandos nuevos.

## 6. Contingencias

| Fallo | Señal | Acción | Qué decir |
|---|---|---|---|
| Gazebo no arranca | Error en consola | Pasar al vídeo pregrabado | “La simulación no ha arrancado; veamos la ejecución grabada.” |
| El rover no se mueve | Sin `/cmd_vel` | Revisar Nav2; si no, abortar y vídeo | “Vamos a revisar la pila; mientras tanto, la ejecución grabada.” |
| Se pierde la localización | Robot salta en RViz | Abortar; re-localizar o vídeo | “El sistema ha detectado una pérdida de localización y se ha detenido.” |
| Batería baja | Estado `BATTERY_LOW` | Cambiar batería o vídeo | “La batería ha llegado al umbral de seguridad.” |
| WiFi cae | RViz congelado | El rover sigue; recuperar red o abortar | “La telemetría se ha interrumpido; el rover sigue su misión local.” |
| Público invade la zona | Persona dentro | E-stop inmediato | “Parada de seguridad.” |
| Pregunta inesperada | — | “Lo comprobamos y te respondemos con la evidencia.” | No inventar |

## 7. Plan B: vídeo

- Tener un vídeo de 2–3 min con la misión completa.
- Incluir RViz, Gazebo y el rover físico.
- Mostrar el resumen y los métricas.
- No presentar el vídeo como si fuera en vivo.

## 8. Post-demo

- [ ] Guardar bag y logs.
- [ ] Sellar evidencia.
- [ ] Anotar incidencias.
- [ ] Agradecer y recoger contacto.
- [ ] Actualizar FAQ con preguntas nuevas.

## 9. Frases que evitar

- “Funciona siempre.” (No es cierto; di la tasa medida.)
- “Es totalmente autónomo.” (Define el nivel N2.)
- “No puede fallar.” (Ningún sistema es infalible.)
- “Lo arreglamos en un momento.” (No improvises en directo.)

## 10. Checklist final

- [ ] Guion ensayado.
- [ ] Demo ejecutada al menos 3 veces.
- [ ] Vídeo de respaldo.
- [ ] Evidencia accesible.
- [ ] E-stop probada.
- [ ] Equipo asignado.
- [ ] Preguntas frecuentes repasadas.
