.PHONY: docker-build
docker-build:
	docker build -t europe-west1-docker.pkg.dev/cde-ds-enablement-8k1r/cde-dse-test/penguin_model -f docker/Dockerfile .


.PHONY: docker-push
docker-push: docker-build
	docker push europe-west1-docker.pkg.dev/cde-ds-enablement-8k1r/cde-dse-test/penguin_model
