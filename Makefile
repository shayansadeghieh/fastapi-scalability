.PHONY: api
api:
	@poetry run python -m uvicorn main:app --reload --port 9000

.PHONY: install
install:
	@poetry config virtualenvs.in-project true
	@poetry install
