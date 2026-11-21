# Visión y alcance — Percepción visual del rover grande

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: PO / Visión
>
> Documento de alcance de la sección. No sustituye la visión del proyecto
> completo; acota qué se va a investigar, construir y demostrar en materia de
> visión.

## 1. Problema

El rover grande necesita percibir su entorno para navegar, operar el brazo,
identificar objetivos científicos y generar evidencia. El LiDAR ya cubre la
navegación 2D, pero no los obstáculos bajos, los negativos, las superficies sin
textura ni la semántica. La visión debe cerrar esas brechas con un coste y una
complejidad razonables.

## 2. Objetivo

Diseñar, justificar y validar un **subsistema de percepción visual** para el
rover grande que:

1. Complemente al LiDAR con profundidad y semántica.
2. Use hardware disponible en Perú cuando sea posible.
3. Tenga una arquitectura ROS 2 integrable y medible.
4. Genere evidencia reproducible para el jurado y para el equipo.

## 3. Alcance

### Incluido

- Estudio de cámaras (UVC, CSI, estéreo, RGB-D) y ToF (punto único y multizona).
- Selección de hardware con precio, stock y proveedor local.
- Arquitectura de percepción y fusión con LiDAR.
- Calibración, sincronía y pruebas de profundidad.
- Integración ROS 2 y publicación de `image_raw`, `camera_info`, `PointCloud2`
  y `LaserScan`/`Range` según corresponda.
- Evidencia: bags, CSV, logs, fotos y informes.

### Excluido

- Diseño mecánico definitivo del mástil o del brazo.
- Control del brazo y agarre.
- Ciencia del suelo, perforación y análisis de muestras.
- Navegación autónoma completa del rover grande.
- Operación BVLOS y autonomía de largo alcance.
- Compra de hardware sin aprobación de presupuesto.

> **LiDAR:** se hereda como sensor primario. Esta sección no elige el modelo;
> solo define cómo se fusiona con la visión.

## 4. Stakeholders

| Rol | Interés | Responsabilidad |
|---|---|---|
| PO | Presupuesto, prioridad, alcance | Aprobar compras y cierre de OQ |
| Tech Lead | Arquitectura, integración ROS 2 | ADRs, interfaces, revisión |
| Hardware | Cámaras, ToF, montaje, energía | Selección, compra, calibración |
| Navegación | Costmap, localización, fusión | Consumir la percepción |
| Ciencia | Objetivos, muestras, marcadores | Requisitos de CU-V3/CU-V4 |
| Documentación | Evidencia y trazabilidad | Registro y revisión |

## 5. Supuestos

> **Supuesto 1:** el rover grande usará ROS 2 Jazzy o compatible. Si cambia la
> distro, la integración se revisa.
>
> **Supuesto 2:** el LiDAR entrega `LaserScan` o `PointCloud2` en `base_link` o
> en un frame conectado por `tf2`.
>
> **Supuesto 3:** hay espacio físico y energía para dos cámaras y un ToF.
>
> **Supuesto 4:** la misión permite una latencia de 100–200 ms en la imagen de
> teleoperación.
>
> **Supuesto 5:** el presupuesto de visión está entre S/ 2 000 y S/ 3 000 para
> el prototipo; la importación se decide aparte.

## 6. Criterios de éxito

| ID | Criterio | Métrica | Prioridad |
|---|---|---|---|
| CE-V1 | Profundidad útil a corto alcance | Error ≤ 10% a 1 m y ≤ 20% a 3 m | Must |
| CE-V2 | Frecuencia suficiente | ≥ 5 Hz en el pipeline | Must |
| CE-V3 | Integración ROS 2 | Topics y `tf` estables; `rosbag2` reproducible | Must |
| CE-V4 | Robustez exterior | Funciona con sol y polvo en prueba controlada | Should |
| CE-V5 | Evidencia | Bag + CSV + logs + fotos con hash | Must |
| CE-V6 | Coste | Dentro del presupuesto aprobado | Must |
| CE-V7 | Mantenibilidad | Calibración repetible por otra persona | Should |

## 7. Entregables

1. Investigación de sensores en Perú con precios, stock y fuentes.
2. Documento de arquitectura y ADR de selección.
3. BOM de visión con cotización local e importación.
4. Protocolo de calibración y pruebas.
5. Evidencia de los experimentos E-V1 a E-V5.
6. Informe de resultados y recomendación para el rover grande.

## 8. Hitos

| Hito | Fecha objetivo | Criterio |
|---|---|---|
| M-V0 | 2026-11-21 | Base documental e investigación de campo |
| M-V1 | Por definir | OQ-V01 y OQ-V02 cerradas |
| M-V2 | Por definir | Presupuesto aprobado y hardware comprado |
| M-V3 | Por definir | Calibración y E-V2 ejecutados |
| M-V4 | Por definir | E-V1/E-V3/E-V4 ejecutados |
| M-V5 | Por definir | Informe y recomendación |

Las fechas se fijan cuando el PO cierre el presupuesto y la plataforma.

## 9. Riesgos principales

Ver [`../00-gobierno/gestion-riesgos.md`](../00-gobierno/gestion-riesgos.md).
Los más relevantes para el alcance son RSK-V01 (estéreo sin sincronía),
RSK-V02 (enfoque 4K), RSK-V07 (importación del VL53L8CX) y RSK-V08 (cómputo
sin definir).

## 10. Preguntas abiertas

Ver [`../00-gobierno/registro-decisiones.md`](../00-gobierno/registro-decisiones.md).
Las que bloquean este alcance son OQ-V01, OQ-V02, OQ-V03 y OQ-V05.
