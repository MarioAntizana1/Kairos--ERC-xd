# Trazabilidad requisito → diseño → prueba → evidencia

> Estado: Vivo · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA
>
> La evidencia de hardware está pendiente. Ninguna fila debe marcarse “Aprobada”
> sin una carpeta sellada en `docs/08-evidencia/`.

| ID | Diseño | Prueba | Evidencia | Estado |
|---|---|---|---|---|
| RF-01 | `diseno-vision.md` §6.1 | TC-01, TC-02 | Pendiente | Pendiente |
| RF-02 | `diseno-vision.md` §6.2 | TC-05, TC-06 | Pendiente | Pendiente |
| RF-03 | `diseno-vision.md` §6.3 | TC-08, TC-14 | Pendiente | Pendiente |
| RF-04 | `diseno-vision.md` §6.4 | TC-07 | Pendiente | Pendiente |
| RF-05 | `diseno-vision.md` §6.6 | TC-09, TC-14 | Pendiente | Pendiente |
| RF-06 | `diseno-vision.md` §6.7 | TC-10 | Pendiente | Pendiente |
| RF-07 | `diseno-vision.md` §5 | TC-03, TC-04 | Pendiente | Pendiente |
| RF-08 | `diseno-vision.md` §6.3 | TC-08 | Pendiente | Pendiente |
| RF-09 | `diseno-vision.md` §6.6–6.7 | TC-14 | Pendiente | Pendiente |
| RF-10 | `diseno-vision.md` §6.4 | TC-07 | Pendiente | Pendiente |
| RF-11 | `diseno-vision.md` §6.7 | TC-10 | Pendiente | Pendiente |
| RF-12 | `diseno-vision.md` §6.5 | TC-02 | Pendiente | Pendiente |
| RNF-01 | `diseno-vision.md` §8 | TC-12 | Pendiente | Pendiente |
| RNF-02 | `diseno-vision.md` §7 | TC-11 | Pendiente | Pendiente |
| RNF-03 | `diseno-vision.md` §4.3 | TC-06 | Pendiente | Pendiente |
| RNF-04 | `diseno-vision.md` §4.2 | TC-06 | Pendiente | Pendiente |
| RNF-05 | `diseno-vision.md` §9 | TC-01, TC-05 | Pendiente | Pendiente |
| RNF-06 | `diseno-vision.md` §6.6 | TC-09 | Pendiente | Pendiente |
| RNF-07 | `diseno-vision.md` §7 | TC-11 | Pendiente | Pendiente |
| RNF-08 | `diseno-vision.md` §6.7 | TC-10 | Pendiente | Pendiente |
| RNF-09 | `diseno-vision.md` §5 | TC-03, TC-04 | Pendiente | Pendiente |
| RNF-10 | `diseno-vision.md` §6.5 | TC-02 | Pendiente | Pendiente |
| RNF-11 | `diseno-vision.md` §6.1, §7 | TC-13 | Pendiente | Pendiente |
| RNF-12 | `bom-peru.md` §5 | TC-15 | Pendiente | Pendiente |
| RNF-13 | `metodologia.md` §6 | TC-15 | Pendiente | Pendiente |
| RNF-14 | `seguridad.md` §3–4 | TC-10, TC-14 | Pendiente | Pendiente |

## Cómo actualizar

1. Crear o actualizar el caso de prueba en `casos-prueba.md`.
2. Ejecutar y sellar la evidencia en `docs/08-evidencia/`.
3. Actualizar la columna `Evidencia` con el ID `EV-...`.
4. Cambiar `Estado` a `Aprobada`, `Fallida` o `Obsoleta`.
5. Ejecutar `make check`.

## Cobertura

| Tipo | Definidos | Con prueba | Con evidencia |
|---|---:|---:|---:|
| RF | 12 | 12 | 0 |
| RNF | 14 | 14 | 0 |
| **Total** | **26** | **26** | **0** |

> La cobertura de prueba es 100 % a nivel de diseño; la cobertura de evidencia es
> 0 % porque no hay hardware. No confundir ambas.
