# Normativa y seguridad

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Seguridad

## 1. Advertencia

Este documento es una guía de trabajo, **no un permiso aeronáutico ni asesoría
legal**. Antes de volar, el equipo debe verificar la normativa vigente de su
país, la zona de operación, el seguro y los permisos institucionales. En Perú, la
autoridad aeronáutica es la **DGAC** (Dirección General de Aeronáutica Civil) y
las reglas de RPAS pueden cambiar; confirmar con la autoridad y con la
universidad.

## 2. Reglas de operación

- **VLOS:** vuelo en línea de vista, con spotter.
- **Geofence:** límite de altura (**6 m** en la competencia) y distancia
  configurado en la FC; verificar en tierra.
- **Jaula/entorno cerrado:** revisar red, puertas, anclajes y que no haya
  personas dentro; dejar salida de emergencia libre.
- **Zonas prohibidas:** aeropuertos, instalaciones militares, áreas pobladas,
  espacios con restricción temporal.
- **Personas:** no volar sobre personas; mantener distancia de seguridad.
- **Clima:** no volar con viento fuerte, lluvia, niebla o baja visibilidad.
- **Batería:** respetar el mínimo de la FC; aterrizar con margen.
- **Failsafe:** RTL o aterrizaje automático configurado y probado. Sin GPS,
  verificar el failsafe de posicionamiento local/optical flow.
- **Autorización:** piloto responsable, spotter, permiso y seguro antes de volar.

## 3. Seguridad del payload

| Riesgo | Control |
|---|---|
| Brownout de la Pi 5 | UBEC 5 A, fusible, capacitor, medir tensión |
| Sobrecalentamiento | Active Cooler, caja ventilada, límite de CPU |
| Vibración | Aisladores, barra rígida, balance de hélices |
| Interferencia WiFi/BT | Deshabilitar en vuelo; probar en tierra |
| Cable suelto | Fijar FPC y alimentación; tirón suave |
| Peso/CG | Pesar, montar cerca del CG, verificar autonomía |
| Caída | Hélices y payload asegurados; no volar sobre personas |
| Incendio de batería | Cargadores balanceadores, superficie ignífuga, extintor |

## 4. Seguridad de la visión

- La visión es **advisory**: no controla motores ni sustituye la FC.
- Si el pipeline falla, la FC debe seguir volando con su failsafe.
- No usar el ToF de piso como sensor de evitación; mide altura, no obstáculos
  frontales. El estéreo es la fuente para la escena y puede fallar con poca
  textura, luz artificial o movimiento.
- Para 6 m, usar **TFmini Plus 12 m**; el VL53L1X/VL53L5CX de 4 m no alcanzan.
- No confiar en una nube de puntos no georreferenciada para navegación.
- Marcar como inválidos los píxeles sin textura o con baja confianza.

## 5. Privacidad y datos

- No grabar rostros, matrículas o interiores privados sin consentimiento.
- Anonimizar la evidencia publicada.
- No publicar coordenadas exactas de infraestructuras sensibles.
- Guardar los datos en el NVMe y borrar lo que no sea necesario.
- Respetar la licencia de imágenes, mapas y software.

## 6. Checklist de preflight

- [ ] Permiso/seguro vigente y zona autorizada.
- [ ] Piloto y spotter presentes.
- [ ] Jaula/entorno cerrado revisado; nadie dentro; salida libre; altura 6 m.
- [ ] Batería del dron y del payload cargadas.
- [ ] Geofence, altura máxima y failsafe verificados.
- [ ] Posicionamiento local/optical flow de la FC verificado (sin GPS).
- [ ] Hélices y payload asegurados.
- [ ] Cámaras limpias, foco bloqueado, calibración cargada, anti-flicker 50 Hz.
- [ ] TFmini Plus leyendo y con rango válido hasta 6 m.
- [ ] NVMe con espacio y reloj sincronizado.
- [ ] WiFi/BT deshabilitados si interfieren.
- [ ] Temperatura y tensión dentro de rango.
- [ ] Plan de contingencia y aterrizaje definido.

## 7. Checklist de postflight

- [ ] Apagar la Pi de forma ordenada.
- [ ] Descargar logs y verificar hashes.
- [ ] Revisar temperatura, throttling y errores.
- [ ] Inspeccionar cables, lentes y montaje.
- [ ] Registrar incidencias en la bitácora.
- [ ] Guardar evidencia y anonimizar.

## 8. Referencias

- Normativa local de RPAS: verificar DGAC/MTC y la universidad.
- Seguridad de baterías de litio: protocolo del equipo y del fabricante.
- Privacidad: consentimiento y minimización de datos.
- No se cita una norma específica no verificada; registrar la fuente antes de
  afirmar un requisito legal.
