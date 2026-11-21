SHELL := /bin/bash
.DEFAULT_GOAL := help
PYTHON ?= python3

.PHONY: help check docs assets assets-check test lint urdf-check energy evidence sim mission clean

help: ## Muestra esta ayuda
	@echo "Rover Mini Demo — comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

check: docs assets-check test lint ## Validación completa sin ROS (docs, assets, tests, sintaxis)
	@echo "OK: validación completa"

docs: ## Valida enlaces internos, IDs y trazabilidad
	$(PYTHON) scripts/docs/check_docs.py

assets: ## Regenera mundo SDF y mapa PGM desde arena.json
	$(PYTHON) scripts/docs/generate_arena.py --all

assets-check: ## Comprueba que mundo y mapa coinciden con arena.json
	$(PYTHON) scripts/docs/generate_arena.py --check

test: ## Ejecuta las pruebas unitarias de la lógica de misión
	bash scripts/test/run_tests.sh

energy: ## Calcula el presupuesto energético preliminar
	$(PYTHON) scripts/energy/calculo_energia.py

lint: ## Comprueba sintaxis de Python, Bash, YAML, XML y JSON
	bash scripts/test/lint.sh

urdf-check: ## Genera el URDF desde Xacro y valida su estructura (requiere xacro)
	@command -v xacro >/dev/null 2>&1 || { echo "ERROR: xacro no está instalado (ros-jazzy-xacro)."; exit 1; }
	xacro ros_ws/src/rover_description/urdf/rover.urdf.xacro > /tmp/rover_demo.urdf
	python3 scripts/test/check_urdf.py /tmp/rover_demo.urdf

evidence: ## Crea una carpeta de evidencia con metadatos
	bash scripts/evidence/new_evidence.sh "manual"

sim: ## Lanza Gazebo + Nav2 + RViz (requiere ROS 2 Jazzy)
	bash scripts/sim/run_sim.sh

mission: ## Lanza la misión sobre la simulación (requiere ROS 2 Jazzy)
	bash scripts/sim/run_mission.sh

clean: ## Limpia artefactos de build de colcon
	rm -rf ros_ws/build ros_ws/install ros_ws/log
