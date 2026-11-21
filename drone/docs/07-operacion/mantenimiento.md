# Mantenimiento

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware

## 1. Frecuencia

| Tarea | Antes de cada vuelo | Cada 10 vuelos | Mensual | Notas |
|---|---|---|---|---|
| Limpiar lentes | ✓ | | | Paño de microfibra; sin solventes |
| Revisar cables FPC | ✓ | | | Sin pliegues ni contactos sucios |
| Revisar tornillería | ✓ | | | M2.5/M3; par suave |
| Revisar aisladores | ✓ | | | Silicona sin grietas |
| Medir baseline | | ✓ | | Calibrador; ±1 mm |
| Recalibrar estéreo | | ✓ | | Después de golpe o cambio |
| Revisar ventilador | | ✓ | | Polvo; giro libre |
| Revisar NVMe | | | ✓ | `smartctl`, espacio |
| Actualizar firmware/OS | | | ✓ | Con backup y evidencia |
| Revisar batería/UBEC | ✓ | | | Tensión, hinchazón, conectores |
| Revisar hélices | ✓ | | | Grietas, balance |
| Backup de datos | | | ✓ | Dos copias; hash |

## 2. Lentes y cámaras

- Usar paño de microfibra y aire; no líquidos agresivos.
- No tocar el sensor ni el voice-coil.
- Verificar que el foco esté bloqueado y en la posición esperada.
- Revisar que las cámaras estén paralelas y firmes.
- Si hay polvo interno, no abrir; contactar al proveedor.

## 3. Cables

- FPC: sin pliegues de 90°, sin polvo, bien insertado.
- Alimentación: 20 AWG, sin empalmes flojos, fusible correcto.
- I²C: 3,3 V, GND común, longitud corta.
- Reemplazar cables con marcas o conductores expuestos.

## 4. Térmica

- Limpiar el disipador y el ventilador.
- Verificar que la caja tenga ventilación.
- Medir temperatura en banco después de 20 min.
- Si hay throttling, reducir carga o mejorar el flujo.

## 5. Almacenamiento

- `smartctl -a` si está disponible.
- Mantener >20 % libre.
- Rotar/borrar sesiones antiguas después de respaldar.
- Verificar hashes de las sesiones importantes.
- No extraer el NVMe con la Pi encendida.

## 6. Calibración

- Recalibrar después de:
  - golpe o caída;
  - cambio de baseline o soporte;
  - cambio de foco;
  - cambio de temperatura >10 °C;
  - resultados de profundidad fuera de tolerancia.
- Guardar el YAML nuevo; no sobrescribir el anterior.
- Registrar fecha, temperatura, RMS y baseline.

## 7. Baterías y energía

- Inspeccionar hinchazón, cables y conectores.
- Cargar con balanceador; no dejar sin supervisión.
- Almacenar a voltaje de almacenamiento.
- No volar con batería dañada.
- Revisar el UBEC y el fusible; medir tensión en carga.

## 8. Repuestos

| Repuesto | Cantidad | Nota |
|---|---|---|
| Cable FPC 22→15 | 2 | Crítico |
| Fusible 5 A | 4 | Crítico |
| Tornillería M2.5/M3 | Surtido | — |
| Aisladores | 4 | — |
| microSD | 1 | Rescate |
| Ventilador | 1 | — |
| Cable USB-C | 1 | — |

## 9. Registro de mantenimiento

| Fecha | Equipo | Tarea | Resultado | Responsable |
|---|---|---|---|---|
| | | | | |

## 10. Referencias

- [`runbook-vuelo.md`](runbook-vuelo.md).
- [`../03-arquitectura/seguridad.md`](../03-arquitectura/seguridad.md).
- [`../05-implementacion/guia-instalacion.md`](../05-implementacion/guia-instalacion.md).
