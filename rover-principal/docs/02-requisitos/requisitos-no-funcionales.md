# Requisitos no funcionales

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Resumen

| ID | Requisito | Categoría | Prioridad | Umbral | Verificación |
|---|---|---|---|---|---|
| RNF-01 | Fiabilidad de misión | Fiabilidad | M | ≥ 80% en 10 ensayos | TC-15 |
| RNF-02 | Precisión de posición final | Precisión | M | ≤ 0.30 m (media) | TC-16 |
| RNF-03 | Límite de velocidad | Seguridad | M | ≤ 0.45 m/s | TC-08, inspección |
| RNF-04 | Distancia de parada | Seguridad | M | ≤ 0.30 m a 0.3 m/s | TC-17 |
| RNF-05 | Tiempo de arranque | Operación | S | ≤ 60 s | TC-14 |
| RNF-06 | Autonomía | Energía | S | ≥ 30 min | TC-18 |
| RNF-07 | Uso de CPU, RAM y temperatura | Rendimiento | S | CPU < 80%, RAM < 6 GB, T < 80 °C | TC-20 |
| RNF-08 | Reproducibilidad | Mantenibilidad | M | Un comando, versiones fijadas | TC-06, TC-14 |
| RNF-09 | Calidad de código | Mantenibilidad | S | Tests verdes + lint sin errores | TC-01..05, lint |
| RNF-10 | Seguridad eléctrica | Seguridad | M | Fusible, e-stop, BMS | TC-17, inspección |
| RNF-11 | Trazabilidad documental | Documentación | M | 100% RF/RNF con prueba | TC-21 |
| RNF-12 | Portabilidad sim/hardware | Mantenibilidad | S | Misma pila, solo cambia el launch | TC-10, TC-19 |
| RNF-13 | Latencia de telemetría | Rendimiento | S | ≤ 1 s | TC-08 |
| RNF-14 | Recuperabilidad | Operación | C | Rearranque ≤ 2 min | TC-14 |

## 2. Detalle

### RNF-01 — Fiabilidad

La pila debe completar al menos **8 de 10** misiones consecutivas de 5 waypoints sin colisiones ni intervenciones.

- **Métrica:** misiones completadas / misiones intentadas.
- **Umbral:** ≥ 0.80.
- **Confianza:** intervalo de Wilson al 95%; se reporta junto al valor puntual.
- **Contexto:** simulación y hardware por separado.

### RNF-02 — Precisión

El error euclídeo entre la pose final y el waypoint objetivo debe ser **≤ 0.30 m** en media, con percentil 95 ≤ 0.50 m.

- **Métrica:** distancia 2D al waypoint.
- **Ground truth:** pose de Gazebo (sim) o cinta métrica (hardware).
- **Exclusión:** ensayos fallidos se reportan, no se ocultan.

### RNF-03 — Velocidad

La velocidad lineal máxima comandada no debe superar **0.45 m/s**, y la angular **1.2 rad/s**, en operación normal.

- **Verificación:** parámetros de Nav2 + `ros2 topic echo /cmd_vel`.
- **Excepción:** recuperación manual, con operador y zona despejada.

### RNF-04 — Parada de emergencia

Al accionar la e-stop a 0.3 m/s, el rover debe detenerse en **≤ 0.30 m**.

- **Métrica:** distancia recorrida desde la activación hasta el reposo.
- **Verificación:** marca en el suelo + vídeo a 60 fps (precisión ± 5 cm).
- **Nota:** el umbral es conservador para un rover de 5–8 kg.

### RNF-05 — Arranque

Desde el encendido hasta que la misión puede iniciarse deben pasar **≤ 60 s**.

- **Métrica:** tiempo hasta que `/rover/mission/status` publica `IDLE` y Nav2 está activo.
- **Verificación:** cronómetro + logs.

### RNF-06 — Autonomía

El rover debe operar **≥ 30 min** con una carga completa en condiciones de demo.

- **Métrica:** tiempo hasta el corte del BMS o hasta el umbral de seguridad.
- **Verificación:** prueba de descarga controlada.
- **Nota:** se dimensiona la batería con margen 2×.

### RNF-07 — Rendimiento

En Raspberry Pi 5, con la misión en ejecución:

- CPU media < 80%, pico < 95%.
- RAM < 6 GB.
- Temperatura < 80 °C.
- Sin throttling térmico.

**Verificación:** `tegrastats` no aplica; usar `psutil`, `vcgencmd measure_temp`, `top`, logs de `ros2 topic hz`.

### RNF-08 — Reproducibilidad

Cualquier persona debe poder reconstruir el entorno y ejecutar la demo con:

1. Un comando de instalación documentado.
2. Un comando de build.
3. Un comando de simulación y otro de misión.
4. Versiones fijadas en la documentación.

**Verificación:** TC-06 y revisión por una persona ajena.

### RNF-09 — Calidad de código

- Pruebas unitarias de la lógica de misión en verde.
- Sin errores de sintaxis en Python, Bash, YAML, XML y JSON.
- Sin secretos ni credenciales.
- Cobertura de pruebas unitarias de las funciones críticas (validación, estados, reintentos).

### RNF-10 — Seguridad eléctrica

- Fusible principal y fusibles por rama.
- E-stop que corta potencia de motores.
- BMS en la batería.
- Cableado fijado y etiquetado.
- Sin partes metálicas accesibles a tensión.

### RNF-11 — Trazabilidad

El 100% de los RF y RNF debe tener al menos un caso de prueba asociado y una evidencia (o una excepción documentada).

- **Verificación:** `scripts/docs/check_docs.py` + revisión G4.

### RNF-12 — Portabilidad

La misma pila debe ejecutarse en simulación y hardware. Las diferencias se limitan a:

- Launch file (`sim.launch.py` vs `bringup.launch.py`).
- Drivers de hardware.
- Configuración de `use_sim_time`.

### RNF-13 — Latencia de telemetría

El estado de misión debe reflejar un cambio en **≤ 1 s**.

- **Verificación:** timestamp del mensaje vs reloj; prueba con un cambio de estado forzado.

### RNF-14 — Recuperabilidad

Tras un fallo de software, el sistema debe poder reiniciarse y volver a estado operativo en **≤ 2 min**, sin intervención manual en el código.

## 3. Requisitos de documentación

| ID | Requisito | Verificación |
|---|---|---|
| DOC-01 | Cada documento tiene estado, versión y responsable | Inspección |
| DOC-02 | Los enlaces internos son válidos | `make docs` |
| DOC-03 | Cada requisito tiene criterio de aceptación medible | Revisión G1 |
| DOC-04 | Cada ejecución de prueba tiene evidencia | Registro de evidencias |
| DOC-05 | Las fuentes tienen URL y fecha de acceso | `fuentes.md` |

## 4. Historial

| Fecha | Cambio | Autor |
|---|---|---|
| 2026-11-21 | Versión inicial | QA |
