# Energía y variante 6×6

> Estado: Estudio · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: Diseño electrónico

Esta carpeta reúne el estudio energético y la variante 6×6 del rover. **No es la
base del mini demo** (2 motores, LiFePO4 de 12,8 V). La configuración elegida
para la variante es **2S4P de 8 celdas (7,2 V, 14 Ah, 100,8 Wh)**. Adoptarla
requiere resolver **OQ-09** y aprobar un ADR de energía. No mezclar las BOM ni
comprar hardware de la variante sin decisión.

| Documento | Contenido | Estado |
|---|---|---|
| [`calculo-energetico.md`](calculo-energetico.md) | Consumo, pack 2S4P de 8 celdas, solar, servos y conteo de componentes | Borrador |
| [`diseno-electrico-6x6.md`](diseno-electrico-6x6.md) | Arquitectura eléctrica de la variante: 6 motores, 6 servos, protecciones y control | Estudio |
| [`bom-6x6.md`](bom-6x6.md) | BOM separada de la variante, con precios orientativos y puerta de compra | Estudio |

## Decisión pendiente

- **OQ-09:** elegir entre la base de 2 motores + LiFePO4 y la variante 6×6 +
  Li-ion + solar.
- Si se adopta la variante, crear el ADR de energía y actualizar la BOM base.
- Mientras tanto, la BOM base sigue siendo
  [`../bom.md`](../bom.md) y el diseño eléctrico base
  [`../diseno-electrico.md`](../diseno-electrico.md).

## Reproducción del cálculo

```bash
make energy
python3 scripts/energy/calculo_energia.py --json
```

Los supuestos y las fuentes están en el documento de cálculo y en
[`../../01-investigacion/fuentes.md`](../../01-investigacion/fuentes.md).
