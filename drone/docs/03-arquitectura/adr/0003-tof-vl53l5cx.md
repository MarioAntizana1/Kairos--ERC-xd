# ADR-0003 — ToF de piso: VL53L1X, TFmini Plus o VL53L5CX

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: rol de Visión
>
> **No confundir:** el ToF va mirando al piso y da una referencia de
> altura/escala. **No** calcula geometría epipolar; eso lo hace el par estéreo.

## Contexto

El payload necesita medir la **distancia cámara–suelo** para:

- tener una referencia métrica de altura;
- escalar/validar la calibración y el plano del suelo;
- comparar la altura del ToF con la profundidad del estéreo en el centro;
- apoyar la estimación de la extrínseca ToF–cámara.

El ToF no sustituye la calibración con tablero. La altura de vuelo y el tipo de
piso determinan el alcance y el haz necesarios.

## Alternativas

| Alternativa | Zonas | Alcance | FoV/haz | Peso | Precio | Disponibilidad | Uso |
|---|---|---:|---|---:|---|---|---|
| **VL53L1X** | 1 | 4 m | 27° | 1,8 g | S/ 75 | **Sí** | Banco y vuelo bajo (≤4 m) |
| **TFmini Plus** | 1 | 12 m | ~2° | ~11 g | S/ 330 | Sí | **Vuelo >4 m**; spot preciso |
| **VL53L5CX** | 8×8 | 4 m | 63° | 0,5 g | US$ 19,95 | Importar | Plano del suelo ≤4 m |
| VL53L4CX | 1 | 6 m | 18° | ~2 g | US$ 14,95 | Importar | Intermedio |
| DFRobot 4 m IP67 | 1 | 4 m | ancho | ~10 g | S/ 115 | Sí | Robustez ≤4 m |

## Decisión

**Aceptada para la competencia (altura de vuelo 6 m, entorno cerrado):**

1. **Base:** **TFmini Plus 12 m**, haz estrecho, IP65, local en Electromanía. A
   6 m el piso está dentro de rango y el spot es ~21 cm.
2. **Alternativa de banco / vuelo ≤4 m:** VL53L1X 4 m. No sirve para 6 m.
3. **Alternativa 8×8 ≤4 m:** VL53L5CX para ajustar un plano del suelo y rechazar
   outliers; no sirve para 6 m.

La altura de 6 m y el entorno de jaula hacen que el TFmini Plus sea la opción
principal; los ToF de 4 m quedan solo para banco o pruebas de baja altura.

## Consecuencias

- **Positivas:** referencia métrica de altura; validación independiente de la
  calibración; bajo peso; la Pi 5 puede leerlo.
- **Negativas:** hay que montarlo en la base con ventana y calibrar su
  extrínseca; el VL53L1X tiene un cono de 27° y promedia una zona; el TFmini
  Plus es más pesado y caro; el VL53L5CX es de 4 m y se importa.
- **Riesgos:** vuelo >4 m sin TFmini; piso inclinado/irregular; sol/reflectancia;
  polvo de la hélice; deriva térmica.
- **Requisitos afectados:** RF-04, RF-10, RNF-03.

## Evidencia

- F-14, F-15, F-16, F-17, F-18.
- Diseño y procedimiento: [`../../04-diseno/diseno-vision.md`](../../04-diseno/diseno-vision.md) §6.4.
- Cotización: [`../../04-diseno/bom-peru.md`](../../04-diseno/bom-peru.md) §9.2.

## Revisión

| Fecha | Revisor | Resultado |
|---|---|---|
| 2026-11-21 | Visión | Aceptada para 6 m y entorno cerrado; validar TFmini Plus a 6 m en EXP-06 |
