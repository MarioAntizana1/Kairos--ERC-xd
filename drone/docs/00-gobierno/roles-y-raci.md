# Roles, responsabilidades y RACI

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Gestión de Proyecto

## 1. Principios

- El equipo es pequeño; una persona puede cubrir varios roles, pero **cada
  decisión tiene un responsable nombrado**.
- La visión es un payload **advisory**: el responsable de seguridad y el piloto
  tienen la última palabra en vuelo.
- Ningún rol puede aprobar su propio cambio crítico sin revisión de otro rol.

## 2. Roles

| Rol | Responsabilidad principal | Puede combinar con |
|---|---|---|
| **PO / Producto** | Alcance, prioridades, presupuesto, aceptación | Gestión |
| **Visión Lead** | Arquitectura de percepción, calibración, métricas | Software |
| **Software** | Captura, pipeline, ROS 2/MAVLink, registro | Visión |
| **Hardware** | BOM, compra, montaje, energía, térmica | Seguridad |
| **QA** | Casos, ejecución, evidencia, trazabilidad | Documentación |
| **Seguridad / Piloto** | FMEA, preflight, geofence, failsafes, vuelo | Hardware |
| **Documentación** | SDLC, enlaces, plantillas, presentación | QA |

> En un equipo de 2–3 personas, lo mínimo es: **Visión/Software**, **Hardware** y
> **QA/Seguridad**. El PO puede ser el director del proyecto o el profesor.

## 3. Matriz RACI

R = responsable de hacer; A = aprueba; C = consultado; I = informado.

| Actividad | PO | Visión | Software | Hardware | QA | Seguridad |
|---|---|---|---|---|---|---|
| Alcance y presupuesto | A | C | I | C | C | I |
| Requisitos RF/RNF | A | R | C | C | C | C |
| Arquitectura de visión | I | A/R | C | C | C | I |
| BOM y compra | A | C | I | R | I | C |
| Montaje y cableado | I | C | I | R | C | A |
| Captura y calibración | I | A/R | R | C | C | I |
| Pipeline de profundidad | I | A | R | I | C | I |
| Integración MAVLink | I | C | R | C | C | A |
| Casos de prueba | I | C | C | C | R | C |
| Evidencia | I | C | C | C | R | I |
| Preflight y vuelo | I | I | C | C | C | A/R |
| Demo y presentación | A | C | C | C | C | C |

## 4. Reglas de decisión

1. **Cambio de alcance:** PO aprueba; Visión evalúa impacto técnico.
2. **Cambio de hardware:** Hardware propone; Visión y QA evalúan impacto;
   PO aprueba si cambia el presupuesto.
3. **Vuelo:** Seguridad/Piloto autoriza; no se vuela por consenso informal.
4. **Publicación de evidencia:** QA verifica anonimización; PO aprueba.
5. **Licencia:** PO y universidad; nadie publica bajo una licencia no acordada.

## 5. Disponibilidad y relevo

- Documentar las decisiones en el repositorio, no en chats privados.
- Cada rol deja un “estado” en la bitácora antes de ausentarse.
- Las credenciales y calibraciones locales no se comparten por el repo; usar
  `~/.config/drone/` y un gestor de secretos.
