# Seguridad del sistema

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Seguridad
> Este documento acompaña a [`../01-investigacion/normativa-y-seguridad.md`](../01-investigacion/normativa-y-seguridad.md). No certifica cumplimiento normativo.

## 1. Objetivos de seguridad

| ID | Objetivo | Medida |
|---|---|---|
| SG-01 | Evitar daño a personas | Zona delimitada, e-stop, límites de velocidad |
| SG-02 | Evitar daño al rover | Watchdog, límites, parada segura |
| SG-03 | Evitar daño al entorno | Geofence, evitación de obstáculos |
| SG-04 | Detener ante fallo | Fallo seguro por diseño |
| SG-05 | Poder auditar | Logs, bag, registro de incidentes |

## 2. Análisis de peligros (preliminar)

| ID | Peligro | Causa | Consecuencia | Severidad | Probabilidad | Medida |
|---|---|---|---|---|---|---|
| H-01 | Colisión con persona | Pérdida de control, velocidad excesiva | Lesión | Alta | Media | E-stop, zona, límite 0.45 m/s |
| H-02 | Atropello en giro | Punto ciego | Lesión | Alta | Baja | Observador, giro lento |
| H-03 | Quemadura de batería | Cortocircuito, sobrecarga | Incendio | Alta | Baja | BMS, fusible, carga supervisada |
| H-04 | Corte de dedos | Piñón/correa expuesta | Lesión | Media | Media | Protectores |
| H-05 | Caída del rover | Levantamiento incorrecto | Daño | Media | Media | Asas, procedimiento |
| H-06 | Vuelco | CG alto, giro brusco | Daño | Media | Baja | CG bajo, límite de giro |
| H-07 | Descarga eléctrica | Cable pelado | Lesión | Media | Baja | Aislamiento, fusibles |
| H-08 | Emisión RF no permitida | Módulo sin certificar | Interferencia | Baja | Baja | Equipos certificados |
| H-09 | Pérdida de control por software | Bug, timeout | Colisión | Alta | Media | Watchdog, tests |
| H-10 | Arranque inesperado | Estado no inicializado | Movimiento no deseado | Alta | Baja | Motores deshabilitados al arrancar |

## 3. FMEA (resumen)

| Componente | Modo de fallo | Efecto | Detección | Mitigación |
|---|---|---|---|---|
| E-stop | Contacto pegado | No detiene | Prueba antes de cada sesión | Relé normalmente cerrado, doble canal |
| Driver | Sobrecorriente | Motores descontrolados | Fusible, sensor de corriente | Fusible, límite de corriente |
| Encoder | Pérdida de pulsos | Odometría mala | Comparación con IMU/LiDAR | Detección de inconsistencia, parada |
| LiDAR | Datos congelados | Colisión | Timeout, comparación de frames | Parada, watchdog |
| Pi | Cuelgue | Rover sigue o se para | Heartbeat externo | Watchdog hardware, corte de motores |
| Batería | Baja tensión | Parada inesperada | Monitor de voltaje | Umbral, aviso, retorno |
| WiFi | Pérdida | Sin telemetría | Heartbeat | Misión local continúa, parada segura |
| Software | Excepción | Misión colgada | Timeout de goal | Cancelar, estado FAILED |

## 4. Arquitectura de parada

```mermaid
flowchart TD
    A[E-stop física] -->|corta| B[Relé de potencia]
    B --> C[Driver de motores]
    D[Watchdog de software] -->|señal| B
    E[Botón de aborto] -->|servicio| F[Nodo de misión]
    F -->|cancelar| G[Nav2]
    G -->|cero| H[/cmd_vel]
    H --> C
    I[Batería baja] --> F
```

### Capas de parada

1. **Física:** e-stop corta potencia de motores.
2. **Watchdog de hardware:** si el Pi no late, corta motores.
3. **Watchdog de software:** si no llega `/cmd_vel`, el driver para.
4. **Aborto lógico:** el nodo de misión cancela el objetivo y publica cero.
5. **Límites de Nav2:** velocidad y aceleración acotadas.

Una sola capa no es suficiente. La e-stop es la última línea y debe funcionar sin software.

> **Propuesta ADR-0008:** el watchdog de software y el corte por pérdida de
> `/cmd_vel` se implementan en el ESP32-S3; la e-stop sigue cortando potencia en
> hardware y el relé de potencia no se sustituye por el MCU. Ver
> [`adr/0008-esp32-interfaz-tiempo-real.md`](adr/0008-esp32-interfaz-tiempo-real.md).

## 5. Reglas de operación

- La velocidad máxima en presencia de público es **0.30 m/s**.
- La e-stop debe estar a menos de 2 m del rover y accesible.
- Nadie entra en la zona mientras los motores estén habilitados.
- El operador no usa el teléfono ni atiende distracciones durante la misión.
- Si hay duda, se aborta.
- No se opera con batería por debajo del 20% o con temperatura ambiente > 35 °C.
- No se opera con lluvia ni humedad en el rover.

## 6. Verificación de seguridad

| Prueba | Qué se comprueba | Criterio |
|---|---|---|
| TC-17 | E-stop a 0.3 m/s | Detención ≤ 0.30 m |
| TC-17 | E-stop con rover parado | No hay movimiento al rearmar |
| TC-14 | Arranque | Motores deshabilitados hasta `start` |
| TC-13 | Aborto software | `/cmd_vel` a cero en ≤ 0.5 s |
| TC-12 | Fallo de waypoint | No se queda acelerando |
| TC-18 | Batería baja | Aborto y aviso |
| Inspección | Fusibles y cableado | Sin errores |

## 7. Incidentes

Todo incidente, incluso sin daños, se registra en `docs/08-evidencia/` con:

- Fecha, hora y lugar.
- Personas presentes.
- Descripción objetiva.
- Bag y logs.
- Causa raíz (si se conoce).
- Acción correctiva.
- Riesgo actualizado.

## 8. Revisión

- Antes de cada campaña de pruebas.
- Tras cualquier incidente.
- Antes de la demo con público.
- Si cambia el hardware, la batería o el firmware del driver.

## 9. Limitaciones conocidas

- El análisis es preliminar y no sustituye a una evaluación de riesgos formal.
- No hay redundancia de LiDAR ni de IMU en esta fase.
- El watchdog de hardware está especificado, no implementado.
- La certificación eléctrica y RF no está confirmada.
- La operación con público requiere revisión de un responsable de seguridad.
