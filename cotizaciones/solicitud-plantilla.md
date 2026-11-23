# Plantilla de solicitud de cotización

> Estado: Borrador de planificación · Fecha: 2026-11-23
> **No autoriza compra.** Enviar la solicitud no es comprar: no se reserva, no se
> paga y no se compromete presupuesto.

## 1. Antes de enviar

- [ ] Elegir el proveedor en [`bom-consolidado.md`](bom-consolidado.md).
- [ ] Copiar su tabla de líneas (modelo, cantidad y enlace) al cuerpo del mensaje.
- [ ] Completar los datos del comprador (nombre, cargo, teléfono, correo, RUC de la
      universidad). **No inventar el RUC ni el nombre del contacto.**
- [ ] Confirmar que las cantidades son las del consolidado (no las de un solo
      subproyecto).
- [ ] Dejar claro que es una **consulta de cotización**, no una orden de compra.

## 2. Asunto del correo

```text
Solicitud de cotización — Equipo Kairos ERC (UNMSM) — componentes de robótica
```

Variante por proveedor:

```text
Solicitud de cotización — Equipo Kairos ERC (UNMSM) — [Proveedor] — [N] ítems
```

## 3. Cuerpo del correo

```text
Estimados señores de [PROVEEDOR]:

Somos el equipo Kairos de la Universidad Nacional Mayor de San Marcos (Lima),
participantes del European Rover Challenge. Estamos preparando el abastecimiento
de tres subproyectos (rover de navegación, dron y rover principal) y quisiéramos
solicitar su cotización formal para los siguientes ítems:

[PEGAR AQUÍ LA TABLA DE LÍNEAS]

Para poder evaluar la compra, le agradeceremos confirmar:

1. Disponibilidad real (stock) para la cantidad total solicitada.
2. Precio unitario con IGV y, si aplica, precio sin IGV.
3. Posibilidad de descuento por volumen: es una compra única de equipo
   universitario.
4. Costo y plazo de envío a Lima (y a la ciudad indicada si el despacho es
   distinto).
5. Emisión de factura o boleta con RUC a nombre de la universidad.
6. Garantía y política de devolución.
7. Forma de pago aceptada (transferencia, depósito, pasarela).
8. Vigencia de la cotización (días) y nombre del vendedor responsable.

Si algún modelo exacto no está disponible, agradeceremos proponer un sustituto
con especificación equivalente e indicar la diferencia técnica.

Quedamos atentos a su respuesta.

Saludos cordiales,
[NOMBRE Y APELLIDO] — [ROL]
Equipo Kairos — European Rover Challenge
Universidad Nacional Mayor de San Marcos (UNMSM), Lima
Tel.: [TELÉFONO] · Correo: [CORREO]
```

## 4. Versión corta para WhatsApp

```text
Buenas tardes, soy [NOMBRE] del equipo Kairos (UNMSM, Lima), participamos en el
European Rover Challenge. Quisiera cotizar estos componentes, con precio con IGV,
stock real y costo de envío a Lima:

1) [MODELO] — [CANT.] — [ENLACE]
2) [MODELO] — [CANT.] — [ENLACE]
3) ...

¿Me pueden confirmar disponibilidad, precio final y plazo? Es una compra única de
equipo universitario, con factura a nombre de la UNMSM. Gracias.
```

## 5. Tabla de líneas (para pegar)

| # | Modelo / SKU | Cantidad | Enlace | Observación |
|---:|---|---:|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

> Copiar las filas desde la sección del proveedor en
> [`bom-consolidado.md`](bom-consolidado.md). Si el proveedor no abre enlaces,
> borrar esa columna y dejar modelo + cantidad.

## 6. Seguimiento de respuestas

| Proveedor | Fecha envío | Fecha respuesta | N.° cotización | Total con IGV | Stock | Envío | Plazo | Validez | Contacto |
|---|---|---|---|---|---|---|---|---|---|
| Electromanía | | | | | | | | | |
| The Pi Box | | | | | | | | | |
| Memory Kings | | | | | | | | | |
| Falabella | | | | | | | | | |
| Naylamp | | | | | | | | | |
| Electronics Peru | | | | | | | | | |
| Print3D.pe | | | | | | | | | |
| ZoneFPV | | | | | | | | | |
| Taller / tienda local | | | | | | | | | |

## 7. Cuándo se convierte en evidencia

La cotización recibida es evidencia **de la fase de compras**. Cuando esa fase se
abra:

1. Se crea la carpeta `docs/08-evidencia/artefactos/<fecha>-<slug>/` en el
   subproyecto que compra.
2. Se guardan el PDF o correo de la cotización y un `README.md` con el resumen.
3. Se sella con `SHA-256` y se registra en `registro-evidencias.md`.

Mientras siga la fase de planificación, estas respuestas se anotan en la tabla de
§6 y no se crean carpetas de evidencia.

## 8. Reglas

- **No reservar** productos por teléfono ni por la web.
- **No pagar** nada con esta cotización.
- No prometer al proveedor fechas de pago ni volúmenes futuros.
- No compartir datos personales de terceros ni credenciales.
- Si un proveedor insiste en una compra inmediata, responder que la decisión
  depende del presupuesto del equipo.
