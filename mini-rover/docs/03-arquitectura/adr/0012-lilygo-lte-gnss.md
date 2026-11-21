# ADR-0012 — LilyGO T-SIM7600X como enlace LTE y GNSS (propuesta)

> Estado: Propuesta · Fecha: 2026-11-21 · Responsable: Navegación/Comunicaciones · Reemplaza a: —

## Contexto

El inventario de facultad (F-52) incluye un **LilyGO ESP32 7600X**. La
documentación del fabricante (F-53) identifica la familia **T-SIM7600X**:

- ESP32-WROVER-B (4 MB flash, 8 MB PSRAM), Wi-Fi 2.4 GHz y Bluetooth 4.2.
- Módem **SIM7600 LTE Cat-4** (hasta 150 Mbps de bajada, 50 Mbps de subida)
  con **GNSS multi-constelación**.
- Ranura **Nano SIM**, lector TF, soporte de **batería 18650** y 2 × 16 pines
  de expansión.
- **Un solo USB-C perteneciente al ESP32**; el SIM7600 se controla por **UART**
  (GPIO26/27). No es un módem USB directo.
- Variantes **E** (Europa/África), **G** (global) y **SA-H** (Sudamérica/
  Australia/NZ) con bandas LTE distintas. Hay que confirmar la variante y las
  bandas del operador peruano.

El proyecto ya tiene Wi-Fi/Ethernet para la estación de operación. La red móvil
puede aportar:

- Telemetría remota fuera del alcance del Wi-Fi.
- Posición GNSS para operación exterior (no para el demo indoor).
- Un enlace de respaldo para diagnóstico, nunca para el lazo de control.

No se propone usar el LilyGO como controlador de motores: no es un ESP32-S3,
tiene GPIO reservados para el módem y su prioridad es la conectividad. El
[ADR-0008](0008-esp32-interfaz-tiempo-real.md) sigue siendo la propuesta para el
control de tiempo real.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste | Madurez |
|---|---|---|---|---|
| **LilyGO T-SIM7600X como gateway LTE/GNSS** | Ya disponible; LTE + GNSS + 18650; 2 × 16 pines | No es módem USB directo; hay que programar el ESP32; bandas/variante por confirmar; consumo y antena | 0 (reutilizado) + SIM/datos | Media |
| Solo Wi-Fi/Ethernet | Simple; sin coste recurrente; DDS local | Sin telemetría fuera del alcance; sin GNSS | 0 | Alta |
| Dongle USB LTE | El Pi 4 lo ve como módem; menos firmware | Comprar; antena; consumo; otro dispositivo | ~30–60 EUR | Alta |
| Router LTE industrial | Robusto; Ethernet/Wi-Fi; varias SIM | Peso, coste, alimentación | ~100–200 EUR | Alta |
| Satélite | Cobertura total | Coste y latencia prohibitivos para el demo | Muy alto | Baja |

## Decisión propuesta

Usar el **LilyGO T-SIM7600X como gateway LTE/GNSS opcional** para telemetría y
diagnóstico, **fuera del lazo de control y de la cadena de seguridad**:

1. La Pi 4 se conecta al ESP32 por **USB serie (puente USB-UART)** o UART
   directa; el ESP32 habla con el SIM7600 por UART.
2. El ESP32 puede: (a) hacer de puente PPP/RNDIS para dar salida a Internet a
   la Pi 4, o (b) publicar directamente telemetría por MQTT/HTTPS. La opción se
   decide en el spike; no se asume que el firmware exista.
3. El tráfico de ROS 2 **no se expone directamente a Internet**. Se usa VPN o
   un broker MQTT con TLS y credenciales; DDS queda en la red local.
4. La alimentación es dedicada: 18650 protegida en el portapilas, o 5 V desde
   un riel con condensadores de reserva. No se alimenta del pin 3.3 V de la Pi.
5. Se confirma la variante (**SA-H** o **G**) y las bandas del operador antes de
   comprar la SIM. La variante E no cubre Sudamérica.
6. GNSS se usa para logs y operación exterior; no sustituye a AMCL en el demo
   indoor.

El enlace LTE **no se usa para e-stop, watchdog, `cmd_vel` ni navegación** en
tiempo real. Si falla, el rover sigue su misión local y pierde telemetría.

## Plan de validación (spike)

| Paso | Medición | Criterio |
|---|---|---|
| 1 | Identificar variante y bandas | SA-H o G compatible con el operador |
| 2 | SIM y registro en red | `AT+COPS?`, RSSI/RSRP estables |
| 3 | Datos | Ping, descarga y latencia durante 10 min |
| 4 | GNSS | Fix con antena activa en exterior |
| 5 | Puente o MQTT | La Pi 4 obtiene salida o publica telemetría |
| 6 | Consumo | Medir picos con transmisión; fuente estable |
| 7 | Reconexión | Recuperar tras pérdida de cobertura/SIM |
| 8 | Seguridad | Sin puertos ROS/DDS expuestos; TLS/VPN |

> El plazo y los umbrales se confirman antes de empezar. No se presentan como
> resultados hasta que exista evidencia.

## Consecuencias

### Positivas

- Telemetría remota y GNSS sin comprar un módem adicional.
- El tablero tiene 18650 y expansión; sirve para un nodo de comunicaciones.
- Se mantiene Wi-Fi/Ethernet como enlace primario.
- No contamina el lazo de control ni la seguridad.

### Negativas / deuda asumida

- No es un módem USB plug-and-play: hay que programar el ESP32 y validar el
  puente o el cliente MQTT.
- Variante y bandas por confirmar; la E no sirve para Perú.
- Consumo y picos LTE; antena exterior y ubicación.
- Coste recurrente de SIM/datos y gestión de credenciales.
- Latencia y cobertura variables; no apto para tiempo real.
- Seguridad: VPN/TLS, firewall y rotación de credenciales.
- Un 18650 adicional introduce otra química y otra carga supervisada.

### Neutrales

- El ADR-0008 (ESP32-S3) no cambia: el LilyGO no es el controlador de motores.
- El demo puede seguir siendo 100% local; LTE es opcional.
- La antena GNSS no aporta al demo indoor.

## Impacto documental

| Documento | Cambio |
|---|---|
| `03-arquitectura/arquitectura-sistema.md` | Nodo de comunicaciones opcional |
| `03-arquitectura/interfaces.md` | Interfaz Pi 4 ↔ LilyGO y telemetría LTE (propuesta) |
| `04-diseno/bom.md` | SIM, antena, 18650 protegida y soporte (si se acepta) |
| `04-diseno/inventario-facultad.md` | LilyGO como gateway LTE/GNSS, no como MCU |
| `06-pruebas/` | Caso de enlace LTE (si se acepta) |
| `00-gobierno/registro-decisiones.md` | OQ-16 y OQ-17 |

## Criterios de revisión

- La variante no cubre las bandas del operador o no hay SIM disponible.
- El consumo/picos desestabilizan el riel de 5 V.
- El puente PPP/RNDIS no es estable o la latencia no sirve ni para telemetría.
- Se requiere LTE en la demo oficial como requisito, no como extra.
- Aparece un dongle/router LTE más simple y barato.

## Referencias

- F-52: inventario de facultad (LilyGO 7600X).
- F-53: LilyGO T-SIM7600X — documentación (variantes, UART, USB-C, GNSS).
- [ADR-0008](0008-esp32-interfaz-tiempo-real.md) — ESP32-S3 para tiempo real.
- [ADR-0010](0010-raspberry-pi-4.md) — plataforma Pi 4.
