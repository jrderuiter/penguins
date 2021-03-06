.PHONY: docker-build
docker-build:
	docker build -t europe-west1-docker.pkg.dev/gdd-vertex/vertex/penguin_model -f docker/Dockerfile .


.PHONY: docker-push
docker-push: docker-build
	docker push europe-west1-docker.pkg.dev/gdd-vertex/vertex/penguin_model


.PHONY: lint
lint:
	find src -type f -name "*.py" | xargs pylint

.PHONY: format
	black .
