.PHONY: test api

test:
	pytest

api:
	uvicorn pi_brain.api_main:app --host 0.0.0.0 --port 8000
