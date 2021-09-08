run-local: 
	uvicorn api.main:app --reload

run-mongo:
	docker-compose up mongo

test-local:
	pytest -v -p no:warnings