# ADR-0002 — Par estéreo con 2 × Camera Module 3 Standard

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: rol de Visión

## Contexto

Se necesita un par estéreo métrico, con color, resolución suficiente para
inspección a 1–10 m y precio local. La baseline debe caber en el payload
(150 mm nominal). El autofoco es útil en banco, pero riesgoso en vuelo.

## Alternativas

| Alternativa | Ventajas | Desventajas | Coste (2 uds.) |
|---|---|---|---|
| **2 × CM3 Standard** | 12 MP, 66° H, autofoco, precio | Rolling shutter; sin genlock; lente móvil | S/ 280 |
| 2 × CM3 Wide | 102° H, más cobertura | Menos resolución angular; más distorsión | S/ 390 |
| 2 × Global Shutter OV9281 | Sin rolling shutter | Monocroma, 1 MP; sync a verificar | S/ 400 |
| 2 × HQ Camera | Lente intercambiable, 12 MP | Peso, tamaño, foco manual, precio | S/ 620+ |
| Cámara estéreo USB | Sincronización de fábrica | Menos control, USB, precio | US$ 100+ |
| Arducam stereo HAT | Sincronía, integración | Disponibilidad, precio, rigidez | US$ 100+ |

## Decisión

**2 × Camera Module 3 Standard**, baseline **150 mm**, foco **bloqueado** en
vuelo.

Motivos:

1. 12 MP y 66° H dan buena resolución angular para profundidad.
2. El autofoco permite enfocar en banco; se bloquea para volar.
3. Precio local y stock.
4. La baseline de 150 mm equilibra rango cercano y lejano.
5. El color es útil para la nube y la inspección.

## Consecuencias

- **Positivas:** resolución, color, coste, disponibilidad.
- **Negativas:** rolling shutter; no hay genlock; el voice-coil puede vibrar.
- **Riesgos:** skew en giros, foco variable, deriva de baseline.
- **Mitigaciones:** vuelo lento, exposición corta, foco manual, barra rígida,
  aisladores; GS como plan B.
- **Requisitos afectados:** RF-01, RF-02, RF-07, RNF-04, RNF-09.

## Evidencia

- F-02, F-03, F-07, F-08, F-13.
- Cálculo de profundidad: [`../04-diseno/diseno-vision.md`](../../04-diseno/diseno-vision.md) §4.
- Cotización: [`../04-diseno/bom-peru.md`](../../04-diseno/bom-peru.md).

## Revisión

| Fecha | Revisor | Resultado |
|---|---|---|
| 2026-11-21 | Visión | Aceptada; revisar si TC-06/TC-12 muestran skew o blur excesivo |
