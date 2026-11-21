# Gestión de riesgos — Visión del rover grande

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Gestión de Proyecto

Registro de riesgos del subsistema de visión. Escala de probabilidad e impacto: 1 (bajo) a 5 (alto). Exposición = probabilidad × impacto.

## Matriz de riesgos

| ID | Riesgo | Tipo | P | I | Exp. | Mitigación | Plan de contingencia | Responsable | Estado |
|---|---|---|---|---|---|---|---|---|---|
| RSK-V01 | Comprar dos webcams sin sincronía hardware y esperar estéreo denso de calidad | Técnico | 4 | 4 | 16 | Prueba de sincronía y profundidad antes de comprar el segundo par; usar 1080p y exposición fija; calibrar | Aceptar estéreo de corto alcance o migrar a OAK-D / global shutter | TL / Visión | Abierto |
| RSK-V02 | El enfoque fijo de la Facecam 4K limita el 4K a 30–120 cm y arruina la profundidad a distancia | Técnico | 4 | 4 | 16 | Usar 1080p (25 cm–infinito); verificar en pista antes de fijar la decisión | Cambiar de cámara o usar solo RGB a corta distancia | HW | Abierto |
| RSK-V03 | Dos cámaras 4K saturan el ancho de banda USB y bajan fps o resolución | Técnico | 4 | 3 | 12 | Usar MJPG/NV12, 1080p, controladores USB separados; medir con las dos cámaras a la vez | Bajar a 720p o una sola cámara + ToF | TL | Abierto |
| RSK-V04 | Un ToF de punto único no cubre el campo de visión y deja huecos | Técnico | 4 | 3 | 12 | Usar varios ToF o un ToF multizona; complementar con LiDAR y estéreo | Importar VL53L8CX o añadir segundo TFmini | HW | Abierto |
| RSK-V05 | El sol directo reduce el alcance del ToF y degrada el estéreo | Ambiental | 3 | 4 | 12 | Medir a 70 klx; usar capucha/sombra; no confiar en el alcance de laboratorio | Operar en horarios de baja irradiancia o añadir iluminación activa | Visión | Abierto |
| RSK-V06 | Stock local insuficiente o precio que cambia entre la cotización y la compra | Suministro | 4 | 3 | 12 | Verificar stock el día de la compra; pedir cotización formal; tener alternativa | Importar o comprar el modelo superior/inferior | Logística | Abierto |
| RSK-V07 | No hay VL53L8CX en Perú; la importación tarda o cuesta más de lo previsto | Suministro | 4 | 3 | 12 | Cotizar Mouser/Pololu/RobotShop con envío e impuestos; considerar VL53L1X local como puente | Usar TFmini Plus local y posponer el 3D multizona | Logística | Abierto |
| RSK-V08 | La plataforma de cómputo del rover grande no está definida y bloquea la arquitectura | Gestión | 4 | 4 | 16 | Cerrar OQ-V01 antes de comprar; diseñar el pipeline independiente del hardware | Prototipar en x86 y portar después | PO / TL | Abierto |
| RSK-V09 | La calibración se pierde por vibración o por un montaje flexible | Técnico | 3 | 3 | 9 | Base rígida de aluminio, tornillos, calibración periódica y verificación con tablero | Recalibrar antes de cada misión; montaje redundante | HW | Abierto |
| RSK-V10 | Lesión ocular por uso indebido del láser clase 1 o del ToF | Seguridad | 1 | 5 | 5 | No apuntar a ojos; no abrir carcasas; señalizar pruebas | Detener la prueba y evaluar | Seguridad | Abierto |
| RSK-V11 | El polvo o el agua degradan la óptica en exteriores | Ambiental | 3 | 3 | 9 | IP65/IP67 en ToF; ventana limpia; funda para cámaras | Limpiar y repetir la medición | HW | Abierto |
| RSK-V12 | Se compra hardware antes de aprobar requisitos y luego no encaja | Gestión | 3 | 4 | 12 | Comprar solo después de G1/G2 y de la prueba de concepto | Revender o reasignar a otro proyecto | PO | Abierto |

> **Nota:** la exposición no es una medida de probabilidad real; es una priorización cualitativa. Se revisa mensualmente.

## Riesgos cerrados

| ID | Riesgo | Cómo se cerró | Fecha |
|---|---|---|---|
| — | — | — | — |

## Referencias

- Metodología: [`metodologia.md`](metodologia.md).
- Decisiones abiertas: [`registro-decisiones.md`](registro-decisiones.md).
- Investigación de sensores: [`../01-investigacion/sensores-peru-2026-11-21.md`](../01-investigacion/sensores-peru-2026-11-21.md).
