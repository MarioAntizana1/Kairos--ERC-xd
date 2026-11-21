# Visión y alcance

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Producto

## 1. Problema

El equipo quiere competir en el European Rover Challenge (ERC) 2027, pero el rover completo (navegación, brazo, ciencia, perforación, dron) es un sistema grande, caro y de alto riesgo. Abordarlo todo a la vez impide aprender, medir y demostrar progreso.

**Problema concreto:** no existe todavía una base validada de navegación autónoma, segura y reproducible sobre la que construir el rover grande.

## 2. Solución propuesta

Un **rover mini demo** que:

- Navega de forma autónoma entre cinco waypoints en una arena reducida.
- Evita obstáculos con un LiDAR 2D.
- Se localiza con AMCL sobre un mapa conocido.
- Registra telemetría, logs y bags para demostrar lo ocurrido.
- Se detiene de forma segura ante fallo o emergencia.
- Funciona primero en simulación y luego en hardware con la misma pila.

## 3. Objetivos

| ID | Objetivo | Métrica de éxito |
|---|---|---|
| OBJ-01 | Demostrar navegación autónoma | Misión de 5 waypoints completada |
| OBJ-02 | Demostrar seguridad | E-stop y watchdog verificados |
| OBJ-03 | Demostrar reproducibilidad | Cualquiera puede repetir la demo con el runbook |
| OBJ-04 | Generar evidencia | Bag, logs, vídeo y métricas por ensayo |
| OBJ-05 | Preparar el escalado | Arquitectura modular documentada |

## 4. Alcance

### Dentro del alcance (v0.1)

- Navegación por waypoints con Nav2.
- Localización AMCL con mapa estático.
- Evitación de obstáculos con LiDAR 2D.
- Misión pregrabada en YAML.
- Telemetría de estado y progreso.
- Parada de emergencia y watchdog.
- Simulación Gazebo Harmonic.
- Documentación SDLC y evidencia.
- Operación en Raspberry Pi 4 Model B de 8 GB (ADR-0010).

### Fuera del alcance (fase rover grande)

- Brazo manipulador y pinza.
- Perforación y análisis científico.
- Dron.
- Visión estereoscópica y SLAM visual.
- Navegación GPS de largo alcance.
- Autonomía de exploración (N3).
- Operación remota BVLOS.
- Competir oficialmente en 2027 con este demo.

> El mini demo **no sustituye** al rover del ERC. Es un peldaño verificable.

## 5. Stakeholders

| Stakeholder | Interés | Influencia |
|---|---|---|
| Equipo del rover | Aprender, validar tecnología, competir | Alta |
| Universidad | Visibilidad, docencia, cumplimiento | Alta |
| Jurado del ERC | Rigor, autonomía, seguridad, presentación | Media |
| Patrocinadores | Resultados visibles, retorno | Media |
| Público | Demo atractiva y segura | Baja |

## 6. Supuestos

- Hay acceso a un taller y a una pista de pruebas.
- Se dispone de presupuesto para el hardware del BOM.
- Al menos una persona tiene experiencia en Linux/Python.
- El ERC 2027 se celebrará en una fecha compatible con el plan.
- La universidad permite publicar documentación y vídeo.

## 7. Restricciones

- ROS 2 Jazzy requiere Ubuntu 24.04.
- El host de desarrollo actual es Fedora 43, sin ROS; se usará VM/contenedor/Pi.
- El rover debe ser transportable y operable por una sola persona.
- La demo debe poder ejecutarse sin conexión a internet.
- El presupuesto es limitado (ver BOM).

## 8. Criterios de éxito

| Criterio | Umbral | Verificación |
|---|---|---|
| Misión nominal | 5/5 waypoints | TC-10 |
| Fiabilidad | ≥ 80% en 10 ensayos | TC-15 |
| Precisión final | ≤ 0.30 m | TC-16 |
| Evitación | 0 colisiones en 10 ensayos | TC-11, TC-15 |
| Seguridad | E-stop detiene motores | TC-17 |
| Reproducibilidad | Runbook ejecutable por tercera persona | TC-19 |
| Documentación | Trazabilidad 100% | TC-21 |

## 9. Entregables

| ID | Entregable | Fase |
|---|---|---|
| E-01 | Documentación SDLC | Transversal |
| E-02 | Workspace ROS 2 compilable | G3 |
| E-03 | Simulación con mundo y mapa | G3 |
| E-04 | Misión autónoma de 5 waypoints | G4 |
| E-05 | Rover físico operativo | G4 |
| E-06 | Evidencia de ensayos | G4 |
| E-07 | Runbook y guion de demo | G5 |
| E-08 | Vídeo de presentación | G5 |

## 10. Aprobación

| Rol | Nombre | Fecha | Estado |
|---|---|---|---|
| Product Owner | | | Pendiente |
| Tech Lead | | | Pendiente |

> Sin aprobación de G0, el alcance se considera propuesta y puede cambiar.
