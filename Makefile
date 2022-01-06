SHELL := /bin/zsh
python_version = 3.9

.PHONY: all test docs

lint:
	@isort skit_auth
	@isort tests
	@black skit_auth
	@black tests

typecheck:
	@echo -e "Running type checker"
	@mypy -p skit_auth

test: ## Run the tests.conf
	@pytest --cov=skit_auth --cov-report html --cov-report term:skip-covered tests/

all: lint typecheck test
