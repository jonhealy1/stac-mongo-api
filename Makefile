run-local: 
	uvicorn api.main:app --reload

run-mongo:
	docker-compose up mongo

test-local:
	python3 -m pytest tests/