.PHONY: api
api:
	@poetry run python -m uvicorn main:hungry --reload --port 9000
