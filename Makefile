.DEFAULT_GOAL := help

VENV :=.venv

folder = notebooks

.PHONY: venv
venv: ## Create the virtual environment
	python -m venv ${VENV}

.PHONY: install
install:  venv ## Install a virtual environment
	${VENV}/bin/pip install --upgrade pip
	# No dependencies for this project!
	# ${VENV}/bin/pip install -r requirements.txt

.PHONY: fmt
fmt: venv ## Run autoformatting and linting
	${VENV}/bin/pip install pre-commit
	${VENV}/bin/pre-commit install
	${VENV}/bin/pre-commit run --all-files

.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

.PHONY: jupyter
jupyter: install ## Start jupyter lab
	${VENV}/bin/pip install jupyterlab
	${VENV}/bin/jupyter lab

.PHONY: test
test: ## Run the import test across all notebooks, use make test folder="notebooks"
	${VENV}/bin/pip install --no-cache-dir pytest nbmake==1.4.6
	${VENV}/bin/pytest --nbmake --nbmake-find-import-errors --nbmake-timeout=2 $(folder)
