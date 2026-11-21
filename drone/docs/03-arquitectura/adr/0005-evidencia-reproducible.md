# ADR-0005 — Evidencia reproducible con hash

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: rol de QA

## Contexto

El proyecto necesita demostrar que la calibración, la profundidad y el vuelo
funcionan. Una captura sin fecha, sin comando y sin entorno no es evidencia. El
jurado y el equipo deben poder repetir el experimento.

## Alternativas

| Alternativa | Ventajas | Desventajas |
|---|---|---|
| **Carpeta de evidencia + metadatos + SHA-256** | Trazable, reproducible, barata | Disciplina y tiempo |
| Solo logs en el repo | Simple | Sin contexto ni integridad |
| Capturas sueltas | Rápido | No reproducible |
| Vídeo editado | Atractivo | No verificable |
| Plataforma externa | Colaboración | Dependencia y privacidad |

## Decisión

Cada evidencia se guarda en:

```text
docs/08-evidencia/artefactos/YYYY-MM-DDTHHMMSS-<slug>/
├── README.md
├── metadata.json
├── MANIFEST.sha256
├── logs/
├── media/
└── bags/
```

Con:

- Comando exacto, versión, commit, host, OS y operador.
- Requisitos y casos de prueba asociados.
- Hash SHA-256 del manifiesto.
- Estado (`Pendiente`, `Ejecutada`, `Aprobada`, `Fallida`, `Obsoleta`).
- Registro en [`../../08-evidencia/registro-evidencias.md`](../../08-evidencia/registro-evidencias.md).

## Consecuencias

- **Positivas:** trazabilidad, integridad, reproducibilidad, defensa técnica.
- **Negativas:** overhead; los datos pesados no se versionan.
- **Mitigaciones:** scripts `new_evidence.sh` y `seal_evidence.sh`; enlaces
  externos para bags grandes.
- **Requisitos afectados:** RNF-13, RNF-14.

## Evidencia

- [`../../08-evidencia/README.md`](../../08-evidencia/README.md).
- [`../../../AGENTS.md`](../../../AGENTS.md) §7.
- `make evidence`, `make seal`.

## Revisión

| Fecha | Revisor | Resultado |
|---|---|---|
| 2026-11-21 | QA | Aceptada |
