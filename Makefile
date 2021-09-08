run-local: 
	uvicorn api.main:app --reload

run-mongo:
	docker-compose up mongo