# Runbook de vuelo

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Seguridad
>
> **No volar** sin autorización, permiso/seguro, geofence, failsafe, spotter y
> preflight completo. La visión es advisory; el piloto y la FC tienen la
> autoridad.

## 1. Roles

| Rol | Responsabilidad |
|---|---|
| Piloto | RC, actitud, aterrizaje |
| Spotter | Espacio aéreo, personas, obstáculos |
| Operador de visión | Payload, calibración, registro |
| Seguridad | Checklist, geofence, contingencia |

Una persona puede cubrir varios roles en banco, pero **no** en vuelo.

## 2. Preflight (30 min antes)

- [ ] Permiso, seguro y zona autorizada.
- [ ] **Jaula/entorno cerrado:** red y puertas en buen estado; nadie dentro;
      salida de emergencia libre; altura máxima **6 m**.
- [ ] Batería del dron cargada y en buen estado.
- [ ] Batería/UBEC del payload con tensión correcta.
- [ ] Hélices y payload asegurados; tornillería revisada.
- [ ] Cámaras limpias; foco bloqueado; calibración cargada; **anti-flicker
      50 Hz** si hay luz artificial.
- [ ] **TFmini Plus** leyendo; comparar con cinta/altitud hasta **6 m**; rango
      válido.
- [ ] NVMe con espacio; reloj sincronizado.
- [ ] WiFi/BT deshabilitados; probar interferencia con la RC.
- [ ] Geofence, altura máxima y failsafe verificados en la FC.
- [ ] Posicionamiento local/optical flow de la FC verificado (sin GPS).
- [ ] Spotter y zona despejada.
- [ ] Extintor y kit de batería cerca.

## 3. Secuencia de encendido

1. Encender la RC.
2. Encender la FC; esperar el modo de posicionamiento local/armado según el
   procedimiento del dron (sin GPS en jaula).
3. Encender el payload (UBEC).
4. Esperar el autodiagnóstico (`BOOT → IDLE`).
5. Verificar:

```bash
rpicam-hello --list-cameras
i2cdetect -y 1
vcgencmd measure_temp
vcgencmd get_throttled
```

6. Verificar topics/telemetría:

```bash
ros2 topic hz /vision/left/image_raw
ros2 topic hz /vision/depth
ros2 topic echo /vision/status
```

7. Iniciar el registro y el modo `CAPTURE`/`SCAN`.
8. Confirmar en la estación que la nube y los obstáculos se actualizan.

## 4. Antes de armar

- [ ] Payload estable, sin cables sueltos.
- [ ] Cámaras con baseline y foco correctos.
- [ ] TFmini Plus con lectura coherente a 0,5–6 m (comparar con cinta/FC).
- [ ] Altura máxima de 6 m y geofence horizontal configurados.
- [ ] Temperatura < 60 °C en reposo.
- [ ] Tensión > 4,9 V.
- [ ] Registro activo y NVMe con espacio.
- [ ] Spotter listo; zona despejada.

## 5. Vuelo

1. Armar y despegar según el procedimiento del dron.
2. Mantener VLOS, altura máxima **6 m** y distancias de geofence.
3. Volar lento y evitar giros bruscos (rolling shutter).
4. Mantener distancia de seguridad a la estructura.
5. Monitorizar:
   - FPS y latencia.
   - Temperatura y throttling.
   - Tensión del payload.
   - Altura del ToF de piso vs barómetro/FC.
   - Calidad de la nube/obstáculos.
6. Si hay duda, **aterrizar**.

## 6. Contingencias

| Evento | Acción |
|---|---|
| Una cámara falla | Aterrizar; no confiar en la profundidad; revisar cable |
| ToF de piso falla | Usar barómetro/altitud de la FC; seguir con estéreo; aterrizar si es crítico |
| Sobrecalentamiento | Bajar carga/resolución; aterrizar si > 85 °C |
| Tensión baja | Apagar payload; aterrizar |
| Pérdida de enlace de red | Seguir registrando local; recuperar enlace o aterrizar |
| Pérdida de RC | Failsafe de la FC (RTL/aterrizaje); no intervenir desde la Pi |
| Pérdida de posicionamiento local | Aterrizar; no confiar en la nube |
| Contacto con la red/jaula | Aterrizar; revisar hélices y estructura |
| Vibración/blur | Reducir velocidad; aterrizar y revisar montaje |
| Persona en la zona | Aterrizar o alejarse; priorizar seguridad |
| Batería inflada/humo | Aterrizar, desarmar, alejar, extinguir |

## 7. Aterrizaje y apagado

1. Aterrizar y desarmar.
2. Detener el registro y el modo `SCAN`.
3. Apagar el payload de forma ordenada (`SHUTDOWN`).
4. Esperar el sync del NVMe; no cortar la alimentación antes.
5. Apagar la FC y la RC.
6. Retirar la batería y revisarla.

## 8. Postflight

- [ ] Descargar logs y verificar hashes.
- [ ] Revisar temperatura, throttling y errores.
- [ ] Inspeccionar lentes, cables y montaje.
- [ ] Guardar evidencia y anonimizar.
- [ ] Registrar incidencias en la bitácora.
- [ ] Cargar baterías en superficie ignífuga.

## 9. Criterios de aborto

- Viento fuera de límites o jaula dañada.
- Personas o aeronaves en la zona.
- Pérdida de geofence/failsafe o de posicionamiento local.
- Temperatura > 85 °C o tensión < 4,8 V.
- Cámara/ToF de piso crítico caído.
- Cualquier duda del piloto o del spotter.

## 10. Referencias

- [`../03-arquitectura/seguridad.md`](../03-arquitectura/seguridad.md).
- [`../01-investigacion/normativa-y-seguridad.md`](../01-investigacion/normativa-y-seguridad.md).
- [`mantenimiento.md`](mantenimiento.md).
