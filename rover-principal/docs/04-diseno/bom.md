# Lista de materiales y presupuesto

> Estado: Estimado · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
> **Aviso:** precios orientativos en EUR a 2026-11-21, sin IVA, envío ni aduanas. Cotizar antes de comprar.
>
> **Cotización en Perú (2026-11-21):** precios en PEN, stock y alternativas
> locales en [`bom-peru.md`](bom-peru.md). Es un estudio de abastecimiento; no
> autoriza compra ni sustituye la estimación en EUR.
>
> **Propuesta de interfaz (ADR-0008):** añadir un ESP32-S3 para PWM, encoders,
> IMU, batería y expansión I²C, dejando la Pi 5 como cerebro. No está incluido
> en esta BOM; el add-on y sus costes están en
> [`bom-peru.md`](bom-peru.md), sección 4.6, y en
> [`../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md`](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md).
>
> **Variante 6×6 (estudio paralelo):** esta BOM corresponde al mini demo
> (2 motores, LiFePO4 12,8 V). La variante 6×6 con Li-ion, 6 servos y solar tiene
> **BOM separada** en [`energia/bom-6x6.md`](energia/bom-6x6.md) y diseño
> eléctrico en [`energia/diseno-electrico-6x6.md`](energia/diseno-electrico-6x6.md).
> Requiere OQ-09 antes de comprar. **No mezclar ambas BOM.**
>
> **Spike de percepción 3D (ADR-0009):** la BOM de 2 × Camera Module 3 + ToF
> está en la **sección 9**. No está incluida en el total y su compra requiere
> confirmación de presupuesto.

## 1. Escenario recomendado

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. | Total | Nota |
|---|---|---|---|---|---|---|---|
| 1 | Cómputo | Raspberry Pi 5 8 GB | — | 1 | 90 | 90 | Ubuntu 24.04 |
| 2 | Cómputo | HAT NVMe + SSD 128 GB | — | 1 | 60 | 60 | Evita corrupción de SD |
| 3 | Cómputo | Refrigeración activa | Oficial o equivalente | 1 | 10 | 10 | Necesaria en caja |
| 4 | Cómputo | microSD 64 GB A2 | — | 1 | 12 | 12 | Respaldo |
| 5 | Cómputo | Fuente de banco 5 V 5 A | — | 1 | 15 | 15 | Pruebas |
| 6 | Sensor | LiDAR 2D 360° | RPLIDAR A1M8 / LD19 | 1 | 100 | 100 | 12 m, 10 Hz |
| 7 | Sensor | IMU 9-DOF | BNO085 | 1 | 25 | 25 | Fusión opcional |
| 8 | Sensor | Monitor de batería | INA219 | 1 | 8 | 8 | I2C |
| 9 | Tracción | Motorreductor 12 V con encoder | 50 rpm, ≥ 2.5 N·m | 2 | 35 | 70 | 2 ruedas motrices |
| 10 | Tracción | Driver doble | Cytron MDD10A | 1 | 45 | 45 | 10 A/canal |
| 11 | Tracción | Ruedas 90 mm | Goma/TPU | 4 | 8 | 32 | — |
| 12 | Chasis | Perfil aluminio 2020 + escuadras | — | 1 | 40 | 40 | Corte |
| 13 | Chasis | Placas PETG/aluminio | — | 1 | 20 | 20 | Impresión/corte |
| 14 | Energía | Batería LiFePO4 12.8 V 6 Ah | Con BMS | 1 | 70 | 70 | Segura |
| 15 | Energía | DC-DC 5 V 5 A | — | 1 | 15 | 15 | Pi |
| 16 | Energía | DC-DC 5 V 3 A | — | 1 | 8 | 8 | Sensores |
| 17 | Energía | Fusibles y portafusibles | — | 1 | 15 | 15 | 10 A + 3 A + 2 A |
| 18 | Energía | E-stop seta NC | — | 1 | 12 | 12 | Enclavamiento |
| 19 | Energía | Interruptor general | 12 V 20 A | 1 | 8 | 8 | — |
| 20 | Cableado | Cable, conectores, termorretráctil | — | 1 | 30 | 30 | XT60/XT30/JST |
| 21 | Tornillería | Tornillos, tuercas, separadores | — | 1 | 20 | 20 | M3/M4 |
| 22 | Varios | Ventilador, rejilla, espuma | — | 1 | 10 | 10 | — |
| 23 | Repuestos | Fusibles, cable, conector | — | 1 | 25 | 25 | Crítico |
| | | | | | **Subtotal** | **705** | |
| | | | | | **Envío estimado (10%)** | **70** | |
| | | | | | **Total estimado** | **775** | |

> **Revisión 2026-11-21:** al sumar las 23 líneas de la tabla se obtienen
> **740 EUR**, no 705 EUR. La diferencia es de 35 EUR y afecta al total
> (810 EUR con el envío estimado). Se mantiene el total publicado hasta que el
> PO y el responsable de Hardware aprueben la corrección; no se cambia el
> presupuesto de forma unilateral. Ver la comparación en
> [`bom-peru.md`](bom-peru.md).

## 2. Escenario mínimo

Recortes posibles:

| Cambio | Ahorro | Riesgo |
|---|---|---|
| Raspberry Pi 4B 8 GB en lugar de Pi 5 | ~5 EUR | Menos CPU, mismo software |
| SD A2 en lugar de NVMe | ~60 EUR | Corrupción, lentitud |
| LiDAR LD19 en lugar de RPLIDAR | ~20 EUR | Menos soporte |
| Chasis impreso 100% PETG | ~30 EUR | Menos rigidez |
| Sin IMU | ~25 EUR | Odometría menos robusta |
| **Total mínimo aproximado** | **~635 EUR** | Mayor riesgo |

## 3. Escenario ampliado

| Añadido | Coste | Beneficio |
|---|---|---|
| Cámara RGB-D | 150–300 EUR | Percepción 3D |
| GNSS RTK | 150–400 EUR | Navegación exterior |
| Segundo LiDAR | 100 EUR | Redundancia |
| Jetson Orin Nano | 250 EUR | Visión/IA |
| **Total ampliado** | **+650–1.050 EUR** | Futuro |

## 4. Herramientas

Si el equipo no las tiene, añadir:

| Herramienta | Coste est. |
|---|---|
| Multímetro | 25 EUR |
| Soldador + estaño | 30 EUR |
| Crimpadora | 25 EUR |
| Destornilladores y llaves | 30 EUR |
| Fuente de laboratorio | 60 EUR |
| **Total** | **170 EUR** |

> Muchas universidades tienen taller; comprobar antes de comprar.

## 5. Licencias y software

| Elemento | Coste | Nota |
|---|---|---|
| Ubuntu 24.04 | 0 | Open source |
| ROS 2 Jazzy | 0 | Apache-2.0 |
| Nav2 | 0 | Apache-2.0 |
| Gazebo Harmonic | 0 | Apache-2.0 |
| FreeCAD / KiCad | 0 | Open source |
| SOLIDWORKS | 0 (licencia ERC) | Solo finalistas |

## 6. Plan de compra

| Prioridad | Componentes | Cuándo |
|---|---|---|
| 1 | Pi 5, NVMe, refrigeración, fuente | Semana 1 |
| 2 | LiDAR, IMU, driver, motores | Semana 2–3 |
| 3 | Batería, DC-DC, fusibles, e-stop | Semana 3–4 |
| 4 | Chasis, ruedas, cableado | Semana 4–5 |
| 5 | Repuestos y herramientas | Semana 5 |

## 7. Riesgos de suministro

- Plazo de LiDAR y motores: pedir con 4–6 semanas de margen.
- Baterías: restricciones de envío; comprar proveedor local.
- Compatibilidad de conectores: estandarizar XT60/XT30.
- Aduanas: presupuestar 10–20% adicional si se importa.

## 8. Control de cambios

Cualquier cambio de BOM debe:

1. Registrarse en este documento.
2. Actualizar el presupuesto.
3. Revisar el impacto en el diseño eléctrico/mecánico.
4. Aprobarse por el PO y el HW.

## 9. BOM del spike de percepción 3D (no incluida en el total)

> **Estado:** propuesta para el spike del
> [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md). **No está
> incluida** en el subtotal ni en el total de la sección 1. La compra requiere
> confirmación de presupuesto del PO y del responsable de Hardware.

Objetivo: probar dos Camera Module 3 y un ToF VL53L8CX durante **10 semanas
efectivas (2,5 meses), con hitos de 2 semanas**, después de un plazo de compra
estimado de **10 días laborables**. Los 10 días son de suministro, no de
desarrollo; el proyecto tiene ~10 meses de calendario hasta el ERC 2027.

| # | Categoría | Componente | Modelo propuesto | Cant. | Precio unit. (USD) | Total (USD) | Nota |
|---|---|---|---|---|---|---|---|
| 1 | Visión | Camera Module 3 estándar | IMX708, 66° H, 4,74 mm | 2 | 25,00 | 50,00 | F-41; no wide, para no perder profundidad |
| 2 | Visión | Cable CSI 22 pines a 15 pines | 200 mm, FPC | 2 | 5,00 | 10,00 | Estimación; la Pi 5 usa 22 pines y la CM3 15 |
| 3 | Visión | ToF 8 × 8 | Pololu VL53L8CX (3419) | 1 | 24,95 | 24,95 | F-45; incluye reguladores y level shifter |
| 4 | Mecánica | Base rígida de 70 mm | Perfil 2020 + escuadras | 1 | 15,00 | 15,00 | Estimación; no imprimir en flexible |
| 5 | Calibración | Tablero de ajedrez rígido | Impresión + foam board | 1 | 5,00 | 5,00 | Estimación; 20–30 pares |
| | | | | | **Subtotal** | **104,95** | |
| | | | | | **Envío/importación (25%)** | **26,24** | Estimación; cotizar en Perú |
| | | | | | **Total** | **~131,19** | ~130 USD puesto en el país |

### 9.1 Impacto eléctrico y térmico

| Carga | Potencia añadida | Nota |
|---|---:|---|
| Segunda CM3 | +1,25 W | 250 mA a 5 V, F-001 |
| VL53L8CX | +0,50 W | 100 mA a 5 V típicos, F-45 |
| Cómputo estéreo | +3,00 W | Estimación; medir en el spike |
| **Total en 5 V** | **+4,75 W** | 13,1 W, 2,6 A; dentro del DC-DC de 5 A |
| **Visto por la batería** | **+5,3 W** | 90% de rendimiento |

No se añade DC-DC ni batería. El *active cooler* de la Pi 5 ya está en la BOM
base; hay que verificar la temperatura en caja cerrada. Si el cable de I²C del
ToF supera los 8 cm, probar a 100 kHz o mover el sensor al ESP32-S3
(ADR-0008, aún propuesto).

### 9.2 Condiciones de compra

- El plazo de 10 días laborables es una **estimación de suministro**; no se
  confunde con las 10 semanas de ejecución del spike.
- Los precios son de lista, sin IVA, aduanas ni envío; el 25% es una
  estimación conservadora.
- Si el spike falla, los componentes siguen siendo útiles: una CM3 y el ToF
  pasan a la opción A; la segunda CM3 queda para teleoperación o repuesto.
- Cualquier compra debe registrarse aquí y aprobarse según la sección 8.

