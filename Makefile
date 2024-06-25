.PHONY: help install lint test start image push docker-compose-start deploy-k8s doc pypi clean

tag ?= v0.1.0
releaseName = toolbox
dockerhubUser = tyvek2zhang
sourceDir = src
deployDir = deploy

help:
	@echo "Available make targets:"
	@echo "  install               Install project dependencies using poetry."
	@echo "  lint                  Perform static code analysis."
	@echo "  test                  Run unit tests."
	@echo "  start                 Start the project."
	@echo "  image                 Build the Docker image for the project."
	@echo "  push                  Push Docker image to dockerHub."
	@echo "  docker-compose-start  Start the project using Docker Compose."
	@echo "  deploy-k8s            Deploy the project to Kubernetes."
	@echo "  doc                   Make doc for this project."
	@echo "  pypi                  Build and publish to pypi."
	@echo "  clean                 Remove temporary files."
	@echo "Use 'make <target>' to run a specific command."

install:
	cd $(sourceDir) && \
	poetry shell && \
	poetry install

lint:
	python -m pip install pre-commit && \
	pre-commit run --all-files --verbose --show-diff-on-failure

test:
	cd $(sourceDir); \
	rm -rf migrations/db/fss.db; \
	rm -rf htmlcov; \
	alembic upgrade head; \
	coverage run -m pytest; \
	coverage html

start:
	cd $(sourceDir) && \
	alembic upgrade head && \
	python apiserver.py

clean:
	find . -type f -name '*.pyc' -delete; \
	find . -type d -name __pycache__ -delete; \
	rm -rf .pytest_cache; \
	rm -rf .ruff_cache; \
	rm -rf dist; \
	rm -rf log; \
	rm -rf poetry.lock; \
	rm -rf docs/build; \
	rm -rf $(sourceDir)/htmlcov; \
	rm -rf $(sourceDir)/migrations/db/fss.db; \
	rm -rf $(sourceDir)/.env_fss; \
	rm -rf $(sourceDir)/.coverage; \

image: clean
	docker build -t $(dockerhubUser)/$(releaseName):$(tag) .

push: image
	docker push $(dockerhubUser)/$(releaseName):$(tag)

docker-compose-start:
	cd ${deployDir} && \
	docker-compose up -d

deploy-k8s:
	kubectl apply -f ${deployDir}/k8s

doc:
	pip install -r docs/requirements.txt; \
	sphinx-build -M html docs/source/ docs/build/

pypi:
	poetry build; \
	poetry publish
