# Gestión de riesgos

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Seguridad

## 1. Método

Inspirado en ISO 31000. Cada riesgo se identifica, se evalúa (probabilidad × impacto), se trata y se sigue. La escala es 1–5.

| Probabilidad | Valor | Impacto | Valor |
|---|---|---|---|
| Muy baja | 1 | Insignificante | 1 |
| Baja | 2 | Menor | 2 |
| Media | 3 | Moderado | 3 |
| Alta | 4 | Grave | 4 |
| Muy alta | 5 | Crítico | 5 |

**Exposición = Probabilidad × Impacto.**

| Exposición | Nivel | Acción |
|---|---|---|
| 1–4 | Bajo | Aceptar y observar |
| 5–9 | Medio | Mitigar y revisar mensualmente |
| 10–14 | Alto | Mitigar antes de la siguiente puerta |
| 15–25 | Crítico | Detener el trabajo hasta reducir |

## 2. Registro de riesgos

| ID | Riesgo | Categoría | P | I | Exp. | Mitigación | Contingencia | Responsable | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RSK-01 | No validar ROS 2/Nav2 en runtime y llegar a la demo con fallos de integración | Técnico | 4 | 5 | 20 | Validar en VM Ubuntu 24.04 antes de comprar hardware; hitos M3/M4 | Usar simulación como demo principal y hardware como complemento | TL | Abierto |
| RSK-02 | Compatibilidad Raspberry Pi 4 8 GB + Ubuntu 24.04 + ROS 2 Jazzy | Técnico | 3 | 4 | 12 | Prueba temprana con imagen oficial; documentar kernel/firmware; medir CPU/temperatura | Usar Pi 5 o mini PC x86 | HW | Abierto |
| RSK-03 | Autonomía insuficiente de batería durante la demo | Hardware | 3 | 4 | 12 | Cálculo de potencia, batería con margen 2×, medición en banco | Batería de repuesto y demo corta | HW | Abierto |
| RSK-04 | Colisión o daño por fallo de control | Seguridad | 3 | 5 | 15 | E-stop hardware, watchdog, límites de velocidad, zona de prueba | Apagar motores, revisar FMEA | SAFE | Abierto |
| RSK-05 | Localización pobre por odometría mal calibrada | Técnico | 4 | 3 | 12 | Calibrar ruedas, encoder, IMU; AMCL con láser; validar error | Re-localizar con pose manual | NAV | Abierto |
| RSK-06 | LiDAR con ruido, sombras o rango insuficiente | Hardware | 3 | 3 | 9 | Elegir LiDAR 360° ≥ 8 m; filtros; validar en exterior | Añadir segundo sensor o cámara | HW | Abierto |
| RSK-07 | Cambio de reglas o fechas del ERC 2027 | Externo | 3 | 4 | 12 | Seguir la web oficial; diseñar módulos flexibles | Replanificar alcance | PO | Abierto |
| RSK-08 | Presupuesto insuficiente o retraso de proveedores | Gestión | 3 | 3 | 9 | Cotizar 2 proveedores; priorizar COTS; comprar repuestos críticos | Préstamo de laboratorio o versión mínima | PO | Abierto |
| RSK-09 | Pérdida de datos o evidencia no reproducible | Gestión | 2 | 4 | 8 | Git + evidencia con hash + copia externa | Reejecutar prueba y documentar | QA | Abierto |
| RSK-10 | Personas con poca disponibilidad | Equipo | 4 | 3 | 12 | Backlog pequeño, documentación, roles cruzados | Reducir alcance a simulación | PO | Abierto |
| RSK-11 | Fallo de red WiFi durante operación | Operación | 3 | 3 | 9 | Operación local en el Pi; no depender de la nube | Modo autónomo preprogramado | NAV | Abierto |
| RSK-12 | Sobrecalentamiento del Pi o del driver | Hardware | 2 | 3 | 6 | Ventilación, disipador, límites térmicos, monitorización | Pausa y refrigeración | HW | Abierto |
| RSK-13 | Incendio o daño de batería LiPo/Li-ion | Seguridad | 2 | 5 | 10 | BMS, fusible, carga supervisada, bolsa ignífuga | Desconectar y usar extintor adecuado | SAFE | Abierto |
| RSK-14 | Documentación desactualizada | Gestión | 4 | 2 | 8 | `make check` en CI local, revisión en cada puerta | Auditoría antes de la demo | DOC | Abierto |
| RSK-15 | Dependencia de una sola persona para la demo | Equipo | 3 | 4 | 12 | Runbook paso a paso, ensayo cruzado | Guion en vídeo pregrabado | PO | Abierto |
| RSK-16 | Dos arquitecturas energéticas sin unificar: mini demo 2 motores/LiFePO4 vs variante 6×6/Li-ion/solar | Gestión | 3 | 4 | 12 | Resolver OQ-09 antes de comprar; mantener BOM separadas | Congelar compras y usar la base del mini demo | PO | Abierto |
| RSK-17 | El estéreo 3D con dos CM3 consume CPU y tiempo de integración y retrasa el demo | Técnico | 3 | 4 | 12 | LiDAR como sensor primario; estéreo como spike con fecha límite; presupuesto de CPU y térmico | Volver a 1 CM3 + ToF y documentar el resultado | NAV | Abierto |
| RSK-18 | La CM3 en Ubuntu 24.04 + Jazzy depende del fork de `libcamera` y puede romperse con actualizaciones | Técnico | 4 | 3 | 12 | Fijar versiones, compilar en el workspace, registrar el commit y probar tras cada actualización | Usar cámara USB o Raspberry Pi OS para la captura | HW | Abierto |
| RSK-19 | El inventario de facultad no cubre LiDAR, encoders ni seguridad eléctrica; el demo puede retrasarse o comprarse dos veces | Hardware/Gestión | 4 | 3 | 12 | Usar el inventario para banco de pruebas; comprar solo LiDAR, encoders y protecciones tras verificar modelos | Limitar el alcance a simulación + banco y registrar la desviación | HW | Abierto |
| RSK-20 | El estéreo CSI + USB no está sincronizado y la profundidad no es fiable | Técnico | 4 | 3 | 12 | Spike ADR-0011 con criterios medibles; LiDAR/ToF como sensores primarios; no usar para seguridad | Volver a CSI + ToF y documentar el resultado | NAV | Abierto |
| RSK-21 | LTE: variante/bandas incompatibles, SIM/antena, consumo o exposición de red | Técnico/Seguridad | 3 | 3 | 9 | Spike ADR-0012; confirmar SA-H/G; VPN/TLS; sin DDS expuesto; medir picos | Operar solo Wi-Fi/Ethernet | NAV | Abierto |
| RSK-22 | La carcasa Argon ONE no deja salir el cable CSI | Hardware | 3 | 2 | 6 | Verificar el acceso antes de montar; probar cable FPC y ruta | Usar cámara USB o carcasa abierta para el banco | HW | Abierto |

## 3. Top 5 y tratamiento

### RSK-01 — Integración no validada (crítico)

**Tratamiento:** crear una VM Ubuntu 24.04 esta semana, instalar ROS 2 Jazzy + Nav2 + Gazebo Harmonic y ejecutar el launch de simulación. La evidencia de esa ejecución es la puerta G3. Mientras no exista, todo el software se marca como “borrador”.

**Señal de alerta:** el launch falla más de 3 veces por errores de configuración no relacionados con el entorno.

### RSK-04 — Colisión (alto)

**Tratamiento:** e-stop físico que corta la alimentación de motores, watchdog de 500 ms, límite de velocidad 0.45 m/s, geofence en el costmap y zona de pruebas despejada. Antes de cada ensayo se hace el preflight.

**Señal de alerta:** cualquier colisión, por leve que sea, abre un incidente y bloquea nuevos ensayos hasta el análisis.

### RSK-02 / RSK-05 / RSK-15 — Riesgos medios-altos

- **RSK-02:** probar la imagen Ubuntu 24.04 + Jazzy en la Pi 4 antes de diseñar la electrónica definitiva; medir CPU y temperatura.
- **RSK-05:** dedicar una sesión específica a calibrar odometría y medir error en línea recta y giro.
- **RSK-15:** el runbook debe poder seguirlo alguien que no programó el sistema.

## 4. Riesgos aceptados

| ID | Motivo de aceptación | Revisión |
|---|---|---|
| RSK-11 | La operación autónoma no depende de red; el riesgo residual es bajo | Mensual |
| RSK-12 | El Pi 4 con la carcasa Argon ONE es suficiente para la carga prevista | Tras 30 min de carga |

## 5. Revisión

- **Mensual:** actualizar P, I y estado.
- **Antes de cada puerta:** revisar los riesgos altos y críticos.
- **Tras un incidente:** añadir o actualizar el riesgo y registrar la lección.
- **Cierre:** un riesgo solo se cierra con evidencia de que la mitigación funciona.
