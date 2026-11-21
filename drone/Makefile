SHELL := /bin/bash
PYTHON ?= python3
SLUG ?= validacion
DIR ?=

.PHONY: help check docs bom test evidence seal clean

help:
	@echo "Comandos disponibles:"
	@echo "  make check     Valida documentación y totales de la BOM"
	@echo "  make docs      Valida enlaces, IDs, ADRs y evidencia"
	@echo "  make bom       Valida el CSV de cotización"
	@echo "  make test      Alias de make check"
	@echo "  make evidence  Crea una carpeta de evidencia: make evidence SLUG=mi-prueba"
	@echo "  make seal      Sella una evidencia: make seal DIR=docs/08-evidencia/artefactos/..."
	@echo "  make clean     Limpia cachés temporales"

check: docs bom

docs:
	$(PYTHON) scripts/docs/check_docs.py

bom:
	$(PYTHON) scripts/docs/check_bom.py

test: check

evidence:
	@bash scripts/evidence/new_evidence.sh "$(SLUG)"

seal:
	@if [ -z "$(DIR)" ]; then echo "Uso: make seal DIR=<carpeta>"; exit 2; fi
	@bash scripts/evidence/seal_evidence.sh "$(DIR)"

clean:
	rm -rf .pytest_cache __pycache__ scripts/docs/__pycache__
