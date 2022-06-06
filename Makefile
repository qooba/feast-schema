MAKE_HELP_LEFT_COLUMN_WIDTH:=14
.PHONY: help build
help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-$(MAKE_HELP_LEFT_COLUMN_WIDTH)s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

format: ## Format all the code using isort and black
	isort feast_schema/
	black --target-version py37 feast_schema

lint: ## Run mypy, isort, flake8, and black
	mypy feast_schema/
	isort feast_schema/ --check-only
	flake8 feast_schema/
	black --check feast_schema

test:
	pytest tests

build: ## Build the wheel
	rm -rf dist/*
	python setup.py sdist
#	python -m build

publish-testpypi: ## Publish to testpipy
	twine upload --repository testpypi dist/*

publish-pypi: ## Publish to pipy
	twine upload --repository pypi dist/*

