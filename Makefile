PYTHON := python3
PYTHONPATH := src

.PHONY: help compile test check

help:
	@echo "Crypto-Tractatus commands"
	@echo ""
	@echo "  make compile   Compile all Python files"
	@echo "  make test      Run unit tests"
	@echo "  make check     Run compile + tests"

compile:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m compileall -q src

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -v

check: compile test
