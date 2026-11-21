# Bitácora del proyecto

> Estado: Vivo · Responsable: todo el equipo
> Registro cronológico de trabajo, decisiones y evidencias. Añadir una entrada por sesión.

## Formato

```markdown
### YYYY-MM-DD — Título

**Objetivo:** …
**Hecho:** …
**Comandos:** …
**Resultado:** …
**Evidencia:** enlace
**Siguiente:** …
```

---

## 2026-11-21 — Arranque del proyecto

**Objetivo:** crear la base documental y técnica del rover mini demo para el ERC 2027.

**Hecho:**

- Investigación del contexto ERC: edición 2026 (4–6 septiembre, Cracovia), pruebas y prueba de navegación.
- Confirmación de que el ERC 2027 no tiene fechas publicadas a esta fecha.
- Selección de stack: Ubuntu 24.04 + ROS 2 Jazzy + Nav2 + Gazebo Harmonic + Raspberry Pi 5.
- Creación de la estructura SDLC: gobierno, investigación, requisitos, arquitectura, diseño, implementación, pruebas, operación, evidencia y presentación.
- Redacción de 7 ADRs.
- Definición de 13 requisitos funcionales y 14 no funcionales.
- Diseño de la arena y de la misión de 5 waypoints.
- Creación del workspace ROS 2 con `rover_description`, `rover_bringup` y `rover_mission`.
- Implementación de la lógica de misión pura y sus pruebas unitarias.
- Creación de scripts de validación documental, generación de arena, pruebas, lint y evidencia.

**Comandos previstos:**

```bash
make assets
make check
```

**Resultado:** documentación y código en estado borrador. La integración con ROS 2/Gazebo **no se ha validado** porque el host Fedora 43 no tiene ROS 2.

**Evidencia:** [`EV-2026-11-21-01`](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md) (validación local; runtime ROS 2 pendiente).

**Siguiente:**

1. Crear VM Ubuntu 24.04.
2. Instalar ROS 2 Jazzy y compilar.
3. Ejecutar la simulación y corregir errores.
4. Registrar la evidencia de G3.

---

## 2026-11-21 — Cálculo energético preliminar del rover 6x6

**Objetivo:** dimensionar la batería y revisar los servos MG90S para un rover de
6 ruedas con tracción y dirección independientes.

**Hecho:**

- Modelo paramétrico `scripts/energy/calculo_energia.py`, sin dependencias.
- Documento `docs/04-diseno/energia/calculo-energetico.md` con supuestos,
  presupuesto de potencia, pack, solar y par de dirección.
- Diseño eléctrico de la variante 6×6 en
  `docs/04-diseno/energia/diseno-electrico-6x6.md` y BOM separada en
  `docs/04-diseno/energia/bom-6x6.md`.
- Objetivo `make energy`.
- Fuentes F-001 a F-008 en `docs/01-investigacion/fuentes.md`.
- OQ-09 actualizada con enlaces al cálculo, diseño y BOM de la variante.

**Comandos:**

```bash
make energy
python3 scripts/energy/calculo_energia.py --json
```

**Resultado:** consumo medio 18,4 W (0,31 Wh/min); pack elegido 2S4P de 8
celdas (100,8 Wh) para la variante 6×6; 2S2P de 4 celdas queda como mínimo para
demos cortas. Los paneles de 17,3 Wp no sostienen el consumo; los MG90S no son
suficientes (mínimo 10 kg·cm, recomendado 20 kg·cm).

**Evidencia:** cálculo reproducible; autonomía real `Pendiente` de TC-18.

**Siguiente:** elegir motor, pesar el prototipo y medir el par de dirección.

---

## 2026-11-21 — Validación local y primera evidencia

**Objetivo:** comprobar la coherencia de la documentación, los assets, la lógica
de misión y la sintaxis antes de pasar a un entorno con ROS 2.

**Hecho:**

- `make check`: 59 documentos, 151 enlaces, 13 RF, 14 RNF, 21 casos, 7 ADRs.
- Assets regenerados y verificados: mapa 260 × 180 px, 0.05 m/px.
- 34 pruebas unitarias de la lógica de misión en verde.
- Sintaxis validada en Python, Bash, YAML, XML/URDF/SDF y JSON.
- El instalador rechaza correctamente Fedora y no modifica el sistema.
- Xacro genera un URDF de 291 líneas con 8 links, 7 joints, 2 sensores y 2 plugins.
- Ruff no encuentra errores estáticos y el modelo energético se ejecuta.
- Dos evidencias selladas con SHA-256 y registradas.

**Comandos:**

```bash
make check
bash scripts/check_env.sh
bash scripts/setup/install_ros_jazzy.sh --dry-run   # rechazo esperado
bash scripts/evidence/seal_evidence.sh \
  docs/08-evidencia/artefactos/2026-11-21T123009-validacion-local
```

**Resultado:** validación local aprobada con limitación. No se ejecutaron ROS 2,
Nav2, Gazebo ni hardware. La integración sigue pendiente (G3/G4).

**Evidencia:** [`EV-2026-11-21-01`](../08-evidencia/artefactos/2026-11-21T123009-validacion-local/README.md),
hash del manifiesto `bcec912b938625108291b7cc7684074a7d6fa87bc3505b6601cd2e6d508724c3`;
[`EV-2026-11-21-02`](../08-evidencia/artefactos/2026-11-21T123309-validacion-estatica-urdf/README.md),
hash `4662cff7b37d59904bba3537f9570b1f64dca281db3c1494b49800141fe45fc9`;
[`EV-2026-11-21-03`](../08-evidencia/artefactos/2026-11-21T123448-validacion-final-pre-runtime/README.md),
hash `2b7b07c64af7edaccc954f28a57edf195b99466a358cd90927981b725e65af3f`;
[`EV-2026-11-21-04`](../08-evidencia/artefactos/2026-11-21T123636-integracion-final/README.md),
hash `ce4c99496374ae241ee969a2100fd06de952762736b052d397c3b7e6c6448271`.

**Siguiente:** crear una VM Ubuntu 24.04, instalar ROS 2 Jazzy, compilar y
registrar la evidencia de simulación.

---

## 2026-11-21 — Abastecimiento de electrónica en Perú

**Objetivo:** comprobar si la BOM base del mini demo se puede comprar en Perú,
incluidas provincias, y documentar alternativas para lo que no tenga stock.

**Hecho:**

- Búsqueda en tiendas peruanas con envío nacional y marketplaces: The Pi Box,
  Electromanía, Naylamp, Electronics Peru (Ica), Falabella, Autosolar y
  Print3D.pe (Trujillo).
- Verificación de precio y stock de Pi 5 8 GB, LiDAR, IMU, motores, drivers,
  batería, DC-DC, e-stop, interruptor, fusibles, perfil y almacenamiento.
- Documento `docs/04-diseno/bom-peru.md` con BOM en PEN, ruta 100 % Perú,
  alternativas locales, importación y riesgos.
- Datos crudos en `docs/04-diseno/bom-peru.csv`.
- Fuentes F-19 a F-29 en `docs/01-investigacion/fuentes.md`.
- Enlace desde `docs/04-diseno/bom.md`, `docs/README.md` y `README.md`.

**Comandos:**

```bash
# Consultas web documentadas; no se ejecutaron compras ni pruebas de hardware.
make docs
```

**Resultado:** la mayor parte de la BOM se consigue en Perú. Quedan sin stock
exacto la LiFePO4 de 6 Ah, el motor de 50 rpm con encoder, el Cytron MDD10A, el
perfil V-Slot 2020 y el HAT NVMe. La ruta recomendada cuesta ~S/ 3.250–3.750 y
usa sustitutos locales verificados (FIT0185, 2 × BTS7960, Goldenmate 10 Ah,
SSD USB, perfil 2040, ruedas impresas). No se compró nada.
Además se detectó que la suma de las 23 líneas de `bom.md` da 740 EUR, no los
705 EUR publicados; la diferencia de 35 EUR queda anotada y pendiente de
aprobación.

**Evidencia:** [`docs/04-diseno/bom-peru.md`](../04-diseno/bom-peru.md) y
[`docs/04-diseno/bom-peru.csv`](../04-diseno/bom-peru.csv). Precios y stock
consultados el 2026-11-21; no son una reserva.

**Siguiente:** confirmar stock por WhatsApp/correo, decidir batería de 10 Ah vs
20 Ah y almacenamiento USB vs NVMe, cotizar impresión 3D y cargador, y emitir
la orden de compra solo con aprobación del PO.

---

## 2026-11-21 — Propuesta de ESP32-S3 y pack Li-ion a medida

**Objetivo:** evaluar un ESP32-C6/S3 como interfaz de tiempo real entre la Pi 5
y los actuadores/sensores, y comprobar si la celda EVE INR18650/35V de Bracsan
sirve para fabricar un pack 3S.

**Hecho:**

- Revisión de la celda EVE INR18650/35V: 3500 mAh, 3,6 V, 50 g, descarga máxima
  10,2 A “not for cycle life”; S/ 19 en Bracsan.
- Diseño de pack 3S2P (~7 Ah, 75,6 Wh) y 3S3P (~10,5 Ah, 113,4 Wh), con BMS
  3S 25A, cargador 12,6 V 3 A, nickel, espaciadores, XT60 y fusibles.
- Comparación C6 vs S3 vs XIAO C6 vs ESP32 clásico vs RP2040/Teensy.
- ADR-0008 propuesto: Pi 5 como cerebro; ESP32-S3 como interfaz de tiempo real
  con micro-ROS sobre USB.
- Actualización de arquitectura, interfaces y diseño eléctrico con la propuesta.
- BOM add-on: ESP32-S3 ~S/ 195; pack 3S2P ~S/ 218; 3S3P ~S/ 306.
- Revisión de Hifisac: catálogo con precios más bajos (ESP32-S3 S/ 49, BMS 3S 25A S/ 9,90, INA219 S/ 8,20, level shifter S/ 2,70), pero **todas las fichas probadas marcan “Sin existencias”**; la venta es por WhatsApp. No se contabiliza como stock.
- Fuentes F-30 a F-38.

**Comandos:**

```bash
make docs
```

**Resultado:** la celda es apta para un pack 3S2P/3S3P, pero es **Li-ion**, no
LiFePO4: exige BMS con balanceo, carga supervisada, fusibles y carcasa. Para el
demo de 2 motores, 3S2P iguala la energía de la BOM (75,6 Wh vs 76,8 Wh) y pesa
mucho menos que la Goldenmate; 3S3P da más margen de corriente. El ESP32-S3 es
la opción recomendada por GPIO/PWM/PCNT y escalabilidad a 6×6; el C6 basta para
la base. Ninguna de las dos propuestas está aprobada ni comprada. Hifisac sirve como referencia de precio, no como stock confirmado.

**Evidencia:** [ADR-0008](../03-arquitectura/adr/0008-esp32-interfaz-tiempo-real.md),
[`bom-peru.md`](../04-diseno/bom-peru.md) secciones 4.6–4.7,
[`bom-peru-addons.csv`](../04-diseno/bom-peru-addons.csv) y
[`fuentes.md`](../01-investigacion/fuentes.md) F-30–F-38.

**Siguiente:** decidir OQ-10 (S3/C6/RP2040), confirmar que el BMS balancea,
validar el pinout del S3 y medir latencia de micro-ROS antes de comprar.

---

## 2026-11-21 — Investigación de percepción 3D (2 × Camera Module 3 + ToF)

**Objetivo:** evaluar la propuesta de dos cámaras CM3 y un ToF multizona para
profundidad 3D en tiempo real sin disparar el consumo.

**Hecho:**

- Verificado que la Pi 5 tiene dos transceptores MIPI de 4 carriles y 1,5 Gbps,
  y que admite dos CM3 simultáneas (F-39, F-42).
- Verificado que `libcamera` no tiene estéreo nativo: dos procesos, 3A manual y
  sincronía software de decenas de microsegundos; solo la Global Shutter tiene
  disparo externo XTR (F-42, F-43).
- Verificado que la CM3 en Ubuntu 24.04 + Jazzy requiere el fork de `libcamera`
  de Raspberry Pi y `camera_ros` compilado (F-44).
- Caracterizado el VL53L8CX: 8 × 8 zonas, 65° diagonal, 4 m en oscuridad,
  ~2,8 m a 5 000 lx, 60 Hz, 100 mA típicos, 24,95 USD (F-45).
- Comparadas cuatro alternativas: 1 CM3 + ToF, 2 CM3 + ToF, OAK-D Lite y
  2 Global Shutter con sincronía hardware (F-46, F-47).
- Estimado el coste energético: +4,75 W en 5 V para 2 CM3 + ToF + estéreo;
  la batería de 76,8 Wh sigue dando > 2,5 h teóricas.
- Estimado el error de profundidad: ~14 cm/px a 3 m con 70 mm de base y
  1280 × 720; ~7,6 cm/px a 3 m a resolución completa.
- Documentadas las preguntas abiertas OQ-11 a OQ-15.

**Comandos:**

```bash
make docs
```

**Resultado:** la propuesta es viable, pero el estéreo de dos CM3 no es
«enchufar y listo»: exige sincronía, calibración, montaje rígido y CPU. Para el
demo se recomienda 1 CM3 + ToF; el estéreo queda como spike con fecha límite.
No se modifican requisitos, BOM ni arquitectura.

**Evidencia:** [`percepcion-3d.md`](../01-investigacion/percepcion-3d.md),
[`fuentes.md`](../01-investigacion/fuentes.md) F-39–F-51,
[`registro-decisiones.md`](../00-gobierno/registro-decisiones.md) OQ-11–OQ-15.

**Siguiente:** decidir OQ-11 (A/B/C/D) y, si se aprueba, redactar ADR-0009,
actualizar la BOM y definir el caso de prueba del ToF.

---

## 2026-11-21 — Decisión: spike de percepción 3D (B)

**Objetivo:** formalizar la opción B (2 CM3 + ToF) como spike y separar el
plazo de compra del tiempo de desarrollo.

**Hecho:**

- ADR-0009 aceptado con alcance de spike: 2 CM3 + ToF, A como fallback, 10
  semanas efectivas de ejecución y 10 días laborables de compra.
- BOM del spike (sección 9 de `bom.md`): ~105 USD en materiales, ~130 USD con
  importación; no incluida en el total base.
- H6 y E5 añadidos a `hipotesis-y-experimentos.md`.
- OQ-11 resuelta; OQ-12 a OQ-15 siguen abiertas.

**Comandos:**

```bash
make check
```

**Resultado:** el spike queda aprobado, pero la compra requiere confirmación de
presupuesto. Los 10 días son de suministro; la ejecución es de 10 semanas
efectivas, con hitos de 2 semanas, dentro del horizonte de ~10 meses.

**Evidencia:** [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md),
[`bom.md`](../04-diseno/bom.md) sección 9,
[`hipotesis-y-experimentos.md`](../01-investigacion/hipotesis-y-experimentos.md)
H6/E5.

**Siguiente:** confirmar presupuesto y proveedor, comprar, montar y ejecutar E5;
si falla, volver a A.

---

## 2026-11-21 — Inventario de materiales de facultad

**Objetivo:** registrar el material disponible en facultad y contrastarlo con la
BOM vigente, la variante 6×6 y los requisitos.

**Hecho:**

- Documento [`inventario-facultad.md`](../04-diseno/inventario-facultad.md) con
  17 líneas de inventario, mapeo a la BOM base y a la variante 6×6, brechas,
  datos pendientes y notas de seguridad.
- Brechas críticas identificadas: LiDAR 2D, encoders, fusibles/e-stop/BMS,
  DC-DC de 5 V/5 A, chasis/ruedas y cargador LiPo.
- El Pi 4 queda como *fallback* de ADR-0002; no se cambia la decisión.
- OQ-09 y ADR-0008 siguen abiertas; no se mezclan BOM ni se autoriza compra.
- RSK-19 añadido al registro de riesgos.
- Fuentes F-52 y F-53 registradas.

**Comandos:**

```bash
make check
```

**Resultado:** validación estática en verde: 73 documentos, 61 fuentes, 34
pruebas unitarias y lint sin errores. El inventario no se ha verificado
físicamente y no se ejecutaron ROS 2, Nav2, Gazebo ni hardware.

**Evidencia:** [`EV-2026-11-21-05`](../08-evidencia/artefactos/2026-11-21T171912-inventario-facultad/README.md).

**Siguiente:** confirmar RAM del Pi 4, datos de los motores 10F125, modelo del
LilyGO, estado/cargador de la LiPo y Vmp/Imp de los paneles; después decidir si
se compra LiDAR + encoders o se limita el alcance a un *spike* de banco.

---

## 2026-11-21 — Cambio a Raspberry Pi 4 y propuestas de cámara/LTE

**Objetivo:** formalizar la decisión del usuario de usar la Raspberry Pi 4 Model
B de 8 GB con carcasa Argon ONE, y evaluar la Camera V2.1 + USB y el LilyGO
T-SIM7600X como propuestas.

**Hecho:**

- [ADR-0010](../03-arquitectura/adr/0010-raspberry-pi-4.md) aceptado: Pi 4
  8 GB + Argon ONE, SSD USB 3.0, 5 V/3 A y un solo CSI. Reemplaza a ADR-0002.
- RNF-07, TC-20, arquitectura, diseño eléctrico, instalación, operación y
  presentación actualizados a Pi 4.
- BOM revisada: Pi 4 y Argon reutilizadas; SSD USB en lugar de HAT NVMe.
  Subtotal 610 EUR y total 671 EUR, pendiente de aprobación del PO/HW.
- [ADR-0009](../03-arquitectura/adr/0009-spike-percepcion-3d.md) marcado
  obsoleto: la Pi 4 no tiene dos CSI.
- [ADR-0011](../03-arquitectura/adr/0011-estereo-csi-usb.md) propuesto: spike
  de 2 semanas con Camera V2.1 + USB. No es estéreo sincronizado; no sustituye
  al LiDAR/ToF ni se usa para seguridad.
- [ADR-0012](../03-arquitectura/adr/0012-lilygo-lte-gnss.md) propuesto:
  LilyGO T-SIM7600X como gateway LTE/GNSS opcional, fuera del lazo de control.
  El SIM7600 va por UART al ESP32; no es un módem USB directo. Confirmar
  variante (SA-H/G), SIM, antena y consumo.
- OQ-16 a OQ-18 abiertas; riesgos RSK-20 a RSK-22 añadidos.

**Comandos:**

```bash
make check
```

**Resultado:** validación estática en verde. No se ejecutaron ROS 2, Nav2,
Gazebo ni hardware; las propuestas de cámara y LTE son spikes, no resultados.

**Evidencia:** [`EV-2026-11-21-06`](../08-evidencia/artefactos/2026-11-21T180549-cambio-pi4-camera-lte/README.md).

**Siguiente:** aprobar la BOM revisada, verificar el acceso al CSI con la
carcasa Argon y ejecutar los spikes de cámara y LTE con criterios medibles.

---

## 2026-11-21 — BOM base en soles (Perú)

**Objetivo:** expresar la BOM base en PEN con precios de Perú y dejar una única
referencia de compra.

**Hecho:**

- [`bom.md`](../04-diseno/bom.md) reescrito en PEN: 25 líneas, subtotal
  **S/ 2.520,08** y total **S/ 2.646,08** con 5 % de imprevistos.
- Pi 4 y Argon a S/ 0 por reutilización; SSD USB 256 GB + caja, fuente 27 W,
  cargador LiFePO4 y sustitutos locales (FIT0185, BTS7960, Goldenmate 10 Ah).
- [`bom-peru.md`](../04-diseno/bom-peru.md): ruta vigente 5.2 en PEN; tablas
  4.1/5.1 marcadas como históricas con Pi 5.
- [`bom-peru.csv`](../04-diseno/bom-peru.csv) actualizado a Pi 4/Argon y total
  S/ 2.520,08.
- La BOM 6×6 sigue en EUR como estudio hasta resolver OQ-09.

**Comandos:**

```bash
make check
```

**Resultado:** validación estática en verde. Los precios son una fotografía a
2026-11-21, no una compra; falta confirmar stock y aprobar el total.

**Evidencia:** [`EV-2026-11-21-07`](../08-evidencia/artefactos/2026-11-21T183000-bom-pen/README.md).

**Siguiente:** aprobar el total de S/ 2.646,08, confirmar stock y emitir la
orden de compra por prioridades.

---

## Plantilla para nuevas entradas

### YYYY-MM-DD — Título

**Objetivo:**

**Hecho:**

- …

**Comandos:**

```bash
…
```

**Resultado:**

**Evidencia:**

**Siguiente:**
