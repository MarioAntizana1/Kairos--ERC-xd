# ADR-0007 — Evidencia reproducible y auditable

> Estado: Aceptada · Fecha: 2026-11-21 · Responsable: QA · Reemplaza a: —

## Contexto

El proyecto necesita demostrar resultados ante el equipo, la universidad y un jurado. Un vídeo o una captura no bastan: hay que poder reproducir la ejecución, verificar el entorno y detectar manipulación o errores. Además, el equipo es pequeño y no puede permitirse un sistema de gestión documental pesado.

## Alternativas consideradas

| Alternativa | Ventajas | Desventajas | Coste | Veredicto |
|---|---|---|---|---|
| **Carpeta de evidencia + metadatos + SHA-256** | Simple, portable, auditable, sin servicios | Disciplina manual; almacenamiento | Bajo | **Elegida** |
| Solo vídeo | Atractivo | No verificable; no reproducible | Bajo | Insuficiente |
| Plataforma externa (Drive, Notion) | Cómoda | Dependencia, privacidad, enlaces rotos | Medio | Complemento |
| CI/CD con artefactos | Automático | Requiere infraestructura; no cubre hardware | Alto | Futuro |

## Decisión

Cada ejecución relevante genera una carpeta:

```
docs/08-evidencia/artefactos/<fecha>-<slug>/
├── README.md
├── metadata.json
├── MANIFEST.sha256
├── logs/
├── media/
└── bags/
```

Con:

- **metadata.json:** fecha, host, SO, versiones, commit, comando, operador.
- **MANIFEST.sha256:** hash de cada archivo.
- **README.md:** objetivo, resultado, conclusión y reproducibilidad.
- **Registro:** entrada en `registro-evidencias.md`.

Los bags grandes se guardan fuera del repo y se registra URL + hash.

## Consecuencias

### Positivas

- Cualquiera puede verificar la integridad y repetir la ejecución.
- No depende de un servicio externo.
- Funciona offline y en el campo.
- Es fácil de revisar en una presentación.

### Negativas

- Requiere disciplina y tiempo.
- El almacenamiento crece con los vídeos y bags.
- Los hashes no impiden que alguien modifique el repo; solo detectan cambios.

### Neutrales

- Se puede automatizar en CI en el futuro.

## Reglas

1. No se edita un artefacto después de sellarlo.
2. Si hay que corregir, se crea una nueva ejecución y se marca la anterior como `Obsoleta`.
3. Los datos personales se anonimizan.
4. Los bags > 50 MB no se versionan.
5. Toda evidencia enlaza requisito y caso de prueba.

## Criterios de revisión

- Si el volumen de evidencia se vuelve inmanejable.
- Si se implanta CI/CD con artefactos firmados.
- Si el jurado exige un formato específico.

## Referencias

- [`../../08-evidencia/README.md`](../../08-evidencia/README.md).
- [`../../06-pruebas/plan-pruebas.md`](../../06-pruebas/plan-pruebas.md).
- `scripts/evidence/new_evidence.sh`.
