# Mantenimiento

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware

## 1. Inspección

| Frecuencia | Qué revisar | Criterio |
|---|---|---|
| Antes de cada sesión | Tornillos, cables, ruedas, e-stop | Sin holguras ni daños |
| Semanal | Limpieza de LiDAR y ventilación | Sin polvo |
| Mensual | Batería, conectores, calibración | Voltaje equilibrado, sin hinchazón |
| Trimestral | Desgaste de ruedas, rodamientos | Sin juego excesivo |
| Anual | Revisión completa y actualización | Documentada |

## 2. Calibración

### Odometría

1. Marcar una línea recta de 2 m.
2. Comandar velocidad constante durante 10 s.
3. Medir la distancia real.
4. Ajustar `wheel_separation` y `wheel_diameter` en el URDF/driver.
5. Repetir hasta que el error sea < 2%.

### Giro

1. Comandar un giro de 360°.
2. Medir el ángulo real.
3. Ajustar el factor de escala.
4. Repetir.

### LiDAR

- Verificar que el scan coincide con el entorno.
- Comprobar el ángulo de montaje y el frame.
- Limpiar la lente.

### IMU

- Calibrar sesgos en reposo.
- Verificar ejes y orientación.
- Comprobar que el frame coincide.

## 3. Batería

- Cargar con el cargador adecuado.
- No descargar por debajo del umbral del BMS.
- Almacenar a ~50% si no se usa.
- Revisar hinchazón, olor o calor.
- Registrar ciclos y capacidad.
- Sustituir si la autonomía cae > 30%.

## 4. Software

- Actualizar solo con pruebas y evidencia.
- Registrar versiones en `entorno-desarrollo.md`.
- No actualizar la semana de la demo.
- Mantener un snapshot de la VM y una imagen del Pi.
- Revisar logs de errores.

## 5. Repuestos

| Repuesto | Cantidad | Crítico |
|---|---|---|
| Fusibles | 5 | Sí |
| Cable y conectores | 1 set | Sí |
| Rueda | 1 | Sí |
| Rodamiento | 2 | No |
| LiDAR | 0 (caro) | No |
| SD/NVMe | 1 | Sí |
| E-stop | 1 | Sí |

## 6. Almacenamiento

- Lugar seco, sin polvo.
- Batería desconectada y a ~50%.
- Rover sobre soportes para no deformar ruedas.
- Cables enrollados sin tensión.
- Funda o caja rígida.

## 7. Registro

| Fecha | Acción | Responsable | Notas |
|---|---|---|---|
| — | — | — | — |

## 8. Fin de vida

- Reciclar baterías en punto autorizado.
- Reutilizar electrónica y perfiles.
- Documentar el desmontaje.
- No tirar residuos electrónicos a la basura.
