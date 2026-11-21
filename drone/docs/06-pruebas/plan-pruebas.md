# Plan de pruebas

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de QA

## 1. Objetivo

Demostrar, con evidencia, que el payload cumple los requisitos funcionales y no
funcionales en banco y, después, en el dron. La visión es advisory; las pruebas
de vuelo no sustituyen los failsafes de la FC.

## 2. Niveles

| Nivel | Alcance | Ejemplo | Responsable |
|---|---|---|---|
| Unitario | Funciones puras | Cálculo de disparidad, altitud/plano del suelo | Software |
| Integración | Nodos + hardware | Captura dual + calibración + profundidad | Visión |
| Sistema | Payload completo | Nube + ToF de piso + pose + registro | QA |
| Aceptación | Misión | Escaneo de una maqueta / vuelo cautivo | PO + Seguridad |

## 3. Estrategia

1. **Banco primero:** sin hélices, con fuente de laboratorio.
2. **Calibración antes de medir:** no se evalúa profundidad sin YAML válido.
3. **Ground truth:** cinta métrica, tablero de distancias conocidas y ToF de piso
   independiente.
4. **Repetición:** 10 ensayos por condición; reportar media y dispersión.
5. **Evidencia:** logs, frames, YAML, CSV y hash.
6. **Seguridad:** vuelo solo con preflight, geofence, spotter y autorización.

## 4. Entorno

| Fase | Entorno | Hardware |
|---|---|---|
| Unitario | Host / Pi | Sin cámara |
| Integración | Banco | Pi + 2 CM3 + ToF de piso + NVMe |
| Sistema | Banco | Payload completo + UBEC/fuente |
| Aceptación | Dron | Payload montado, hélices según fase |

## 5. Criterios de entrada

- [ ] Hardware recibido y sin daño.
- [ ] OS y dependencias instaladas.
- [ ] Cámaras detectadas.
- [ ] ToF de piso detectado y con lectura válida.
- [ ] Calibración YAML válida.
- [ ] NVMe con espacio.
- [ ] Preflight de seguridad (para vuelo).

## 6. Criterios de salida

- [ ] Todos los casos Must ejecutados.
- [ ] Métricas dentro de umbral o desviación aceptada.
- [ ] Evidencia sellada y registrada.
- [ ] Trazabilidad actualizada.
- [ ] Sin riesgos altos abiertos sin mitigación.
- [ ] Revisión de seguridad para vuelo.

## 7. Métricas

| Métrica | Umbral | Caso |
|---|---|---|
| FPS de captura | ≥10 fps | TC-01 |
| Error de timestamp | ≤20 ms | TC-02 |
| RMS intrínseco | <0,5 px | TC-03 |
| RMS estéreo / baseline | <0,5 px / ±1 mm | TC-04 |
| Error de profundidad a 5 m | ≤10 cm | TC-06 |
| ToF de piso | ≥10 Hz; error ≤2 % a 6 m | TC-07 |
| Latencia de obstáculo | ≤200 ms | TC-09 |
| Registro | ≥30 min | TC-10 |
| Temperatura | <80 °C; `0x0` | TC-11 |
| Peso | ≤350 g | TC-12 |
| Interferencia | Sin pérdida de RC | TC-13 |
| Vuelo end-to-end | Sin incidentes | TC-14 |

## 8. Seguridad

- No volar sin autorización, geofence, failsafe y spotter.
- Hélices quitadas en banco; dron amarrado en vibración.
- Batería en superficie ignífuga; extintor cerca.
- No tocar el payload con la batería conectada.
- Si algo huele a quemado, cortar potencia y alejarse.

## 9. Evidencia

Cada ejecución:

```bash
make evidence SLUG=tc-06-profundidad
# ejecutar y guardar logs/datos
make seal DIR=docs/08-evidencia/artefactos/<carpeta>
```

- `README.md` con objetivo, resultado, conclusión y limitaciones.
- `metadata.json` con versiones y comando.
- `MANIFEST.sha256`.
- Enlace desde la matriz y el registro.

## 10. Calendario

| Semana | Pruebas |
|---|---|
| T6–T7 | TC-01, TC-02, TC-03 |
| T8–T9 | TC-04, TC-05, TC-06 |
| T10 | TC-07, TC-08 |
| T11 | TC-09, TC-10, TC-11 |
| T12 | TC-12, TC-13, TC-15 |
| T14–T16 | TC-14 (tierra/vuelo cautivo) |

> Fechas relativas; dependen de la compra y del clima.

## 11. Referencias

- [`casos-prueba.md`](casos-prueba.md).
- [`protocolo-experimentos.md`](protocolo-experimentos.md).
- [`matriz-trazabilidad-pruebas.md`](matriz-trazabilidad-pruebas.md).
