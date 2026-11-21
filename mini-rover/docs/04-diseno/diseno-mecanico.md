# Diseño mecánico (conceptual)

> Estado: Conceptual · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Hardware
> **Aviso:** no hay CAD ni prototipo físico todavía. Las dimensiones y cálculos son una base de diseño, no un plano de fabricación.

> **Nota de coherencia (2026-11-21):** este documento describe el rover **4x4
> base** (rueda de 90 mm, dos motores). La variante **6x6** con seis ruedas
> motrices y seis servos de dirección aún no tiene diseño mecánico. El cálculo
> de par de dirección y energía para esa variante está en
> [`energia/calculo-energetico.md`](energia/calculo-energetico.md); la geometría
> (radio de rueda, `scrub radius`, masa) debe validarse antes de fabricar.
>
> **Impacto de la cotización en Perú:** [`bom-peru.md`](bom-peru.md) sustituye
> el perfil V-Slot 2020 (agotado) por 2040 y las ruedas de 90 mm por impresión
> 3D con buje a medida. Revisar masa, cotas y rigidez antes de cortar o
> imprimir; no mezclar las cotas del diseño original con las del sustituto.

## 1. Concepto

Rover de cuatro ruedas, tracción diferencial trasera (o 4WD en la versión final), chasis de aluminio y placas de PETG/Aluminio, con el LiDAR en la parte delantera elevada y la electrónica protegida en el centro.

```text
        LiDAR
          │
   ┌──────┴──────┐
   │   Electrónica │
   │   Batería     │
   └──┬────────┬───┘
  rueda       rueda
  del.        del.
  rueda       rueda
  tras.       tras.
```

## 2. Dimensiones objetivo

| Parámetro | Valor | Nota |
|---|---|---|
| Largo total | 0.55 m | Sin LiDAR |
| Ancho total | 0.45 m | Sin ruedas |
| Alto del chasis | 0.20 m | Caja de electrónica |
| Altura total | 0.40 m | Con LiDAR |
| Distancia entre ejes | 0.36 m | Wheelbase |
| Vía (track) | 0.51 m | Centro a centro de ruedas |
| Diámetro de rueda | 0.18 m | Radio 0.09 m |
| Anchura de rueda | 0.05 m | Goma o TPU |
| Altura libre | 0.03 m | Ground clearance |
| Masa objetivo | 7–8 kg | Con batería |

## 3. Cálculo de tracción

### Supuestos

- Masa total: 8 kg.
- Velocidad máxima: 0.45 m/s.
- Pendiente máxima: 10°.
- Aceleración: 0.5 m/s².
- Coeficiente de rodadura: 0.05.
- Radio de rueda: 0.09 m.

### Fuerza necesaria

\[
F = mg\sin\theta + \mu_r mg\cos\theta + ma
\]

\[
F = 8 \cdot 9.81 \cdot 0.174 + 0.05 \cdot 8 \cdot 9.81 \cdot 0.985 + 8 \cdot 0.5
\]

\[
F \approx 13.6 + 3.9 + 4.0 = 21.5\ \text{N}
\]

### Par por rueda

Con 2 ruedas motrices:

\[
\tau = \frac{F \cdot r}{2} = \frac{21.5 \cdot 0.09}{2} \approx 0.97\ \text{N·m}
\]

Con factor de seguridad 2:

\[
\tau_{diseño} \approx 1.94\ \text{N·m}
\]

**Selección:** motorreductor de 12 V con **≥ 2.5 N·m de par de salida** y **≈ 50 rpm** a velocidad nominal.

### Velocidad

\[
n = \frac{v}{\pi d} \cdot 60 = \frac{0.45}{\pi \cdot 0.18} \cdot 60 \approx 47.8\ \text{rpm}
\]

Un motor de 3.000 rpm con reductor 1:60 da 50 rpm. Encoder de 11 PPR × 60 = 660 cuentas/vuelta; con cuadratura, 2.640 cuentas/vuelta, ≈ 0.21 mm por cuenta. Suficiente.

## 4. Estabilidad

\[
\theta_{vuelco} = \arctan\left(\frac{track}{2 h_{cg}}\right)
\]

Con `track = 0.51 m` y `h_cg = 0.15 m`:

\[
\theta_{vuelco} \approx \arctan(1.7) \approx 59^\circ
\]

Margen amplio para una pendiente de 10°. La batería se coloca baja y centrada para mantener el CG.

## 5. Materiales

| Elemento | Material | Proceso | Nota |
|---|---|---|---|
| Chasis | Perfil aluminio 2020 | Corte y escuadras | Rigidez y modularidad |
| Placas | PETG 3 mm o aluminio 2 mm | Impresión 3D / corte láser | Prototipo |
| Soportes de motor | Aluminio 3 mm | Corte láser | Evitar flexión |
| Ruedas | Goma o TPU | COTS | 90 mm |
| Caja de electrónica | PETG | Impresión 3D | Con ventilación |
| Soporte LiDAR | PETG | Impresión 3D | Aislado de vibración |
| Batería | Soporte impreso + correa | — | No velcro solo |

## 6. Montaje

1. Montar el chasis y comprobar escuadra.
2. Fijar los motores y las ruedas.
3. Comprobar que las ruedas giran libremente y no rozan.
4. Montar la bandeja de electrónica con amortiguación.
5. Fijar la batería con correa y separador ignífugo.
6. Montar el LiDAR a 0.35 m, con línea de visión despejada.
7. Montar la IMU cerca del centro y lejos de vibraciones.
8. Pasar el cableado por canaletas y fijarlo.
9. Colocar la e-stop en un lugar accesible.
10. Verificar el CG y el peso.

## 7. Verificaciones

| Verificación | Criterio |
|---|---|
| Peso | ≤ 9 kg |
| CG | Altura ≤ 0.18 m, centrado |
| Ruedas | Giro libre, sin roce |
| Ground clearance | ≥ 25 mm |
| Rigidez | Sin flexión visible al levantar |
| Vibración | LiDAR sin oscilación |
| Acceso | Batería y fusibles accesibles sin desmontar |

## 8. Pendiente

- CAD detallado (FreeCAD/SOLIDWORKS).
- Simulación estructural básica.
- Diseño de soportes definitivos.
- Protecciones de piñones y correas.
- Prueba de vuelco.
- Integración del brazo en la fase grande.

## 9. Referencias

- [`bom.md`](bom.md).
- [`diseno-electrico.md`](diseno-electrico.md).
- [`../01-investigacion/benchmarking-plataformas.md`](../01-investigacion/benchmarking-plataformas.md).
