format:
	isort . &&\
		black .

covg:
	pytest --cov-report term-missing --cov=. -s &&\
		coverage-badge -o coverage.svg