# Roles y matriz RACI

> Estado: Borrador · Versión: 0.1 · Revisión: 2026-11-21 · Responsable: rol de Gestión de Proyecto

## 1. Principio

Un equipo pequeño puede cubrir varios roles, pero **cada responsabilidad debe tener un nombre**. Si una persona cubre dos roles incompatibles (por ejemplo, quien implementa y quien aprueba seguridad), se documenta la excepción y se busca una revisión externa.

## 2. Roles

| Rol | Código | Responsabilidad principal | Perfil |
|---|---|---|---|
| Product Owner | PO | Alcance, prioridades, aceptación, relación con el jurado | Gestión / liderazgo |
| Tech Lead | TL | Arquitectura, decisiones técnicas, revisión de código | Software/robótica |
| Navegación y percepción | NAV | Nav2, localización, costmaps, tuning | ROS 2 / algoritmos |
| Embedded y hardware | HW | Chasis, motores, electrónica, energía, e-stop | Electrónica/mecánica |
| QA y evidencia | QA | Plan de pruebas, ejecución, métricas, integridad | Testing / análisis |
| Seguridad | SAFE | Análisis de riesgos, FMEA, procedimientos | Seguridad / sistemas |
| Documentación y comunicación | DOC | Documentación, guion, vídeo, FAQ | Comunicación técnica |

## 3. Matriz RACI

**R** = Responsable de hacerlo · **A** = Aprueba · **C** = Consultado · **I** = Informado

| Actividad | PO | TL | NAV | HW | QA | SAFE | DOC |
|---|---|---|---|---|---|---|---|
| Visión y alcance | A/R | C | C | C | C | C | I |
| Roadmap y plan | A/R | C | I | I | C | C | I |
| Requisitos funcionales | A | R | C | C | C | C | I |
| Requisitos no funcionales | A | R | C | C | R | C | I |
| Arquitectura | A | R | C | C | C | C | I |
| ADRs | A | R | C | C | I | C | I |
| URDF y simulación | I | A | R | C | C | I | I |
| Nav2 y tuning | I | A | R | I | C | C | I |
| Nodo de misión | I | A | R | I | C | I | I |
| Chasis y mecánica | I | C | I | A/R | C | C | I |
| Electrónica y energía | I | C | I | A/R | C | C | I |
| E-stop y watchdog | I | C | C | R | C | A | I |
| Plan de pruebas | I | C | C | C | A/R | C | I |
| Ejecución de pruebas | I | I | C | C | A/R | C | I |
| Evidencia | I | C | C | C | A/R | C | C |
| Seguridad de la demo | A | C | C | C | C | R | C |
| Documentación | I | C | C | C | C | C | A/R |
| Guion y vídeo | A | I | I | I | I | C | R |
| Presupuesto | A/R | C | I | R | I | I | I |
| Licencia y publicación | A | C | I | I | I | I | R |

## 4. Reuniones y decisiones

| Decisión | Quién decide | Quién consulta | Quién se entera |
|---|---|---|---|
| Cambio de alcance | PO | TL, QA, HW | Todos |
| Cambio de arquitectura | TL | NAV, HW, QA | Todos |
| Compra de hardware | PO | HW, TL | Todos |
| Aprobación de seguridad | SAFE | HW, TL | Todos |
| Publicación de vídeo/documentos | PO | DOC, SAFE | Todos |
| Aceptación de un incremento | PO | QA | Todos |

## 5. Escalado

1. El responsable del rol intenta resolver en 24 h.
2. Si hay impacto en alcance, presupuesto o seguridad, escala a PO + TL.
3. Si hay desacuerdo técnico, se escribe un ADR con alternativas y se decide en revisión.
4. Si hay riesgo para personas o hardware, SAFE tiene veto hasta que se mitigue.

## 6. Cobertura mínima

Con 2 personas:

- Persona A: PO + DOC + QA (con revisión externa de seguridad).
- Persona B: TL + NAV + HW.

Con 1 persona:

- Se documenta la ausencia de revisión por pares y se busca un mentor o profesor para revisar seguridad y arquitectura.
- Ninguna demo con público se hace sin una segunda persona que controle la e-stop.
