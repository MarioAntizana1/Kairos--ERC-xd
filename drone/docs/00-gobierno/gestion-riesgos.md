# Gestión de riesgos

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Gestión de Proyecto

## 1. Método

Inspirado en ISO 31000. Cada riesgo tiene ID, causa, efecto, probabilidad (P),
impacto (I), exposición (P×I), mitigación, responsable y estado. La escala es
1–5; la exposición alta es ≥ 12.

| P \ I | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 | 10 | 15 | 20 | 25 |
| **4** | 4 | 8 | 12 | 16 | 20 |
| **3** | 3 | 6 | 9 | 12 | 15 |
| **2** | 2 | 4 | 6 | 8 | 10 |
| **1** | 1 | 2 | 3 | 4 | 5 |

## 2. Registro

| ID | Riesgo | Causa | Efecto | P | I | Exp. | Mitigación | Resp. | Estado |
|---|---|---|---|---:|---:|---:|---|---|---|
| RSK-01 | HAT/SSD sin stock | Cadena de suministro | No se puede registrar ni arrancar por NVMe | 4 | 3 | 12 | Confirmar stock; arrancar por microSD/USB; comprar después | Hardware | Abierto |
| RSK-02 | ToF de mayor alcance importado | Aduana/plazo | Retrasa la referencia de piso | 4 | 2 | 8 | VL53L1X local para ≤4 m; TFmini/8×8 según altura | Hardware | Abierto |
| RSK-03 | Rolling shutter / sin genlock | CM3 no tiene sync | Skew y errores en movimiento | 4 | 3 | 12 | Vuelo lento, exposición corta; GS como alternativa | Visión | Abierto |
| RSK-04 | Autofoco inestable | Voice-coil + vibración | Imágenes borrosas, calibración inválida | 3 | 4 | 12 | Bloquear foco; carta de resolución; aisladores | Visión | Abierto |
| RSK-05 | Vibración | Hélices/frame | Deriva de baseline y blur | 3 | 4 | 12 | Barra rígida, silicona, balance de hélices | Hardware | Abierto |
| RSK-06 | Throttling térmico | Caja cerrada | FPS bajos, reinicios | 3 | 3 | 9 | Active Cooler, ventilación, límite de CPU | Hardware | Abierto |
| RSK-07 | Brownout | UBEC insuficiente | Reinicio en vuelo, pérdida de datos | 2 | 5 | 10 | UBEC 5 A, fusible, capacitor, medir tensión | Hardware | Abierto |
| RSK-08 | Interferencia WiFi/BT | Pi 5 transmite | Pérdida de RC/telemetría | 3 | 5 | 15 | Deshabilitar en vuelo; probar en tierra; blindaje | Seguridad | Abierto |
| RSK-09 | Peso/CG | Payload 250–350 g | Autonomía y estabilidad | 3 | 3 | 9 | Pesar, montar cerca del CG, volar con margen | Hardware | Abierto |
| RSK-10 | Deriva de calibración | Temperatura/desgaste | Profundidad sesgada | 3 | 4 | 12 | Recalibrar; verificar baseline; registro | Visión | Abierto |
| RSK-11 | Pérdida de datos | Apagado brusco | Sesión irrecuperable | 3 | 3 | 9 | NVMe, cierre ordenado, respaldo, checksum | Software | Abierto |
| RSK-12 | Normativa/privacidad | Vuelo no autorizado | Sanción/daño reputacional | 2 | 5 | 10 | Permisos, geofence, VLOS, anonimización | Seguridad | Abierto |
| RSK-13 | Incompatibilidad HAT/SSD | M.2 2242 vs HAT | No arranca | 3 | 3 | 9 | Verificar especificación; comprar HAT+SSD juntos | Hardware | Abierto |
| RSK-14 | Dependencias de software | OpenCV/ROS 2 | Build roto | 3 | 2 | 6 | Versiones fijadas; contenedor; CI | Software | Abierto |
| RSK-15 | Textura escasa | Paredes lisas | Disparidad inválida | 4 | 3 | 12 | Luz/patrón; marcar inválido; el ToF de piso no rellena la escena | Visión | Abierto |
| RSK-16 | ToF de piso fuera de rango | Altura >4 m | No mide el piso | 3 | 3 | 9 | TFmini Plus 12 m; validar rango; barómetro/FC | Hardware | Abierto |

## 3. Riesgos altos (exposición ≥ 12)

- **RSK-01, RSK-03, RSK-04, RSK-05, RSK-08, RSK-10, RSK-15.** Todos requieren
  mitigación antes de G4 y verificación en evidencia.
- **RSK-08** (interferencia) es crítico para la seguridad: la Pi 5 debe volar
  con WiFi/BT deshabilitados o con un módulo externo probado.
- **RSK-03/04/05** afectan directamente la calidad del estéreo; sin ellos
  resueltos, no se promete precisión.

## 4. Revisión

- Revisión mensual del registro.
- Actualización al cerrar cada puerta.
- Un riesgo cerrado se marca `Cerrado` con la evidencia que lo demuestra; no se
  borra.
- Un riesgo aceptado se marca `Aceptado` con la firma del PO y la justificación.

## 5. Riesgos residuales

Aun con mitigación, quedan:

- Error de profundidad mayor en superficies sin textura o con reflexión.
- Deriva de calibración por temperatura en vuelos largos.
- Latencia variable por carga de CPU.
- Limitación de rango del ToF (4 m) y del estéreo (>10 m).
- Falta de georreferencia si la FC no entrega posición.

Estos riesgos se documentan en la nube de puntos y en el runbook; no se ocultan.
