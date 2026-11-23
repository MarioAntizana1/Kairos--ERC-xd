# Changelog

Todos los cambios visibles del proyecto se registran aquí. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y versionado semántico adaptado a documentación.

## [No publicado]

### Cambiado

- BOM de Perú revisada el **2026-11-23**: base **S/ 1.719,39** y total con 5 %
  de contingencia **S/ 1.805,36**.
- Fuera el HAT+ M.2, la fuente de 27 W, el SSD NVMe y la impresión 3D de
  proveedor (ahora se imprime en local). El dron arranca desde **microSD**.
- El UBEC importado (~S/ 120) se reemplaza por un **XL4005** local de S/ 6,59,
  con capacitor de 1000 µF y derrateo a 3 A.
- `check_bom.py` actualizado a la nueva base y total; `check_docs.py` sigue en
  verde (52 documentos, 129 enlaces).

## [0.1.0] — 2026-11-21

### Añadido

- Estructura SDLC del proyecto de visión del dron: gobierno, investigación, requisitos, arquitectura, diseño, pruebas, operación, evidencia y presentación.
- Metodología adaptada del proyecto rover: SDLC + DSR, puertas G0–G5, sprints de 2 semanas y control de cambios.
- Cotización en Perú del payload de visión: Raspberry Pi 5 8 GB, 2 × Camera Module 3, ToF de piso, almacenamiento, energía y montaje.
- Referencia internacional en USD y CSV de cotización verificable.
- Requisitos funcionales y no funcionales con trazabilidad inicial.
- ADRs de cómputo, par estéreo, ToF de piso, pipeline y evidencia.
- Validadores `check_docs.py` y `check_bom.py`, y scripts de evidencia.
- Evidencia documental de la validación local.

### Notas

- No se adquirió hardware.
- No se ejecutaron pruebas de cámara, calibración ni vuelo.
- Los precios son un estudio de abastecimiento y deben revalidarse antes de comprar.
