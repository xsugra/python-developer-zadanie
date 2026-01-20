# Makefile for the Flyer Scraper project

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: all help venv install run clean

# Default target
all: help

# Help: Show available commands
help:
	@echo "Available commands:"
	@echo "  make venv      - Create a Python virtual environment"
	@echo "  make install   - Install project dependencies into the venv"
	@echo "  make run       - Run the scraper using the venv"
	@echo "  make clean     - Remove generated files and the venv"
	@echo "To activate the venv, run: source $(VENV)/bin/activate"

# Venv: Create the virtual environment
venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV); \
	fi

# Install: Install dependencies
install: venv
	$(PIP) install -r requirements.txt

# Run: Run the scraper
run: venv
	$(PYTHON) main.py

# Clean: Remove generated files and venv
clean:
	rm -f hyperia_letaky.json
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -name ".DS_Store" -delete
	rm -rf $(VENV)