---
name: investigacion-proveedores-peru
description: Método para buscar y verificar precios, stock y disponibilidad de hardware en tiendas peruanas (Memory Kings, Electromanía, Naylamp, The Pi Box, Ripley, Promart, Falabella, Mouser Perú) y registrar la evidencia. Úsala al cotizar cámaras, sensores, placas o componentes para cualquier subproyecto del workspace.
---

# Investigación de proveedores en Perú

## Ámbito

Aplica a los tres subproyectos. Cada uno tiene su propio registro de fuentes:

| Subproyecto | Registro de fuentes | BOM |
|---|---|---|
| `mini-rover/` | `mini-rover/docs/01-investigacion/fuentes.md` | `mini-rover/docs/04-diseno/bom*.md` y `.csv` |
| `drone/` | `drone/docs/01-investigacion/fuentes.md` | `drone/docs/04-diseno/bom*.md` y `.csv` |
| `rover-principal/` | `rover-principal/docs/01-investigacion/fuentes.md` | `rover-principal/docs/04-diseno/bom*.md` y `.csv` |

Registra la fuente en el proyecto que va a comprar el componente, no en otro.

El consolidado transversal por proveedor —cantidades totales de los tres BOM,
totales y paquete de solicitud— está en `cotizaciones/` (ver
`cotizaciones/README.md`).

## Cuándo usarla

- Necesitas precio, stock o plazo de un componente en Perú.
- Debes comparar tienda local vs. marketplace vs. importación.
- Vas a actualizar un `fuentes.md`, una BOM o su `.csv`.

## Regla de oro

**Especificaciones: fabricante. Precio y stock: tienda.** No uses la tienda
para afirmar una especificación que el fabricante no respalda.

## Procedimiento

1. **Define la pregunta y el criterio.**
   - Ejemplo: “¿Cuánto cuestan dos Facecam 4K con stock online hoy?”
2. **Busca en la tienda y abre la ficha del producto.**
   - No te quedes con el resultado del buscador: el precio puede estar en la
     ficha y el stock puede cambiar.
3. **Copia textualmente:**
   - nombre exacto del producto;
   - SKU / código interno / número de parte;
   - precio y moneda;
   - texto de stock (“> 10”, “Solo quedan 3”, “Agotado”, “Consultar stock”);
   - vendedor (tienda o marketplace);
   - condición (nuevo, reacondicionado, bundle);
   - fecha y URL.
4. **Verifica la ficha del fabricante** para el modelo exacto. Si hay
   discrepancia, anótala.
5. **Busca una alternativa local** (otra tienda o modelo equivalente).
6. **Calcula el coste total:** hardware + montaje + cables + envío + impuestos.
7. **Registra la fuente** en el `fuentes.md` del subproyecto con su ID, URL,
   fecha, qué se extrajo y confianza.
8. **Actualiza** el documento de investigación, la bitácora y el changelog.
9. **No ejecutes el validador en esta fase.** Deja la BOM lista y anota en el
   documento que la validación con `drone/scripts/docs/check_bom.py` (o el
   equivalente `make bom`) queda para la fase de ejecución. `mini-rover` no tiene
   validador de BOM.

## Notas por tienda

### Memory Kings (`memorykings.pe`)

- Muestra precio en USD y PEN: `$ 238.00 ó S/ 828.00`.
- Indica `Stock: > 10`, `Stock: 2`, etc.
- El precio incluye IGV; el flete no está incluido.
- Tiene código interno y número de parte en la ficha.
- El filtro de marca (`/filtros/280/elgato`) lista todos los productos de la
  marca; úsalo para confirmar si hay más de un modelo.
- Cuidado: “productos relacionados” puede mezclar marcas (Genius Facecam).

### Electromanía (`electromania.pe`)

- WooCommerce. La ficha muestra `Solo quedan N disponibles` o `Agotado`.
- El SKU aparece como `J006-SEN0309`, `C010A-SEN0259`, etc.
- La categoría “Distancia y proximidad” tiene 41 productos; usa
  `?per_page=36&orderby=price-desc` para ver los más caros primero.
- Algunas fichas tienen imágenes inconsistentes (por ejemplo, el DFRobot 4 m
  muestra una imagen de sensor de vibración). Pide foto real antes de comprar.
- Venta por WhatsApp; el número está en la web.

### Naylamp (`naylampmechatronics.com`)

- PrestaShop. Indica `En Stock` o agotado.
- Envío gratis a todo el Perú por compras > S/ 200 (condiciones de la tienda).
- Precios en soles.

### The Pi Box (`thepibox.pe`)

- Especializada en Raspberry Pi y accesorios (Pi 5, Camera Module 3, HAT+,
  fuentes, coolers).
- Precios en soles con IGV; envío nacional por Olva.
- Verifica el stock real: varios accesorios aparecen agotados o “por confirmar”.

### Ripley / Promart / Falabella (marketplace)

- Distingue **precio normal**, **precio internet** y **precio con tarjeta**.
- Verifica si el vendedor es la tienda o un marketplace.
- “Producto agotado”, “0 unidades” o “solo tiendas” no es stock online.
- El precio puede incluir una promo temporal; anota la fecha.
- En Falabella muchos productos importados llegan desde EE. UU.: revisa plazo.

### Mouser Perú / Pololu / RobotShop (importación)

- El precio de lista no incluye envío, aduana ni IGV.
- Verifica si el sitio tiene inventario Perú o si envía desde EE. UU.
- Para el VL53L8CX, el carrier de Pololu es la referencia más clara.
- No compares un precio local con un precio de importación sin sumar costes.

## Señales de alerta

- Fotos que no corresponden al producto.
- “Consultar stock” sin precio.
- Marketplace con vendedor desconocido y garantía dudosa.
- Precio muy por debajo del resto sin explicación.
- Bundle que mezcla cámara + accesorios y oculta el precio unitario.
- Especificaciones copiadas de otra versión del producto.
- “Envío gratis” solo para Lima o solo con compra mínima.

## Plantilla de registro

```markdown
| Tienda | Producto | SKU | Precio | Stock | Vendedor | Fecha | URL | Nota |
|---|---|---|---|---|---:|---|---|---|---|
| Memory Kings | Elgato Facecam 4K | 040866 | S/ 828 | > 10 | Memory Kings | 2026-11-21 | ... | IGV incluido; flete no |
```

## Checklist

- [ ] ¿Abrí la ficha del producto, no solo el buscador?
- [ ] ¿Copié el stock textual?
- [ ] ¿Distinguí tienda de marketplace?
- [ ] ¿Verifiqué el modelo en la ficha del fabricante?
- [ ] ¿Busqué una alternativa local?
- [ ] ¿Calculé el coste total?
- [ ] ¿Registré la fuente con fecha y URL en el `fuentes.md` del subproyecto?
- [ ] ¿Actualicé bitácora y changelog?
