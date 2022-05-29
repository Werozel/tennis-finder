all: compile-babel

build-dist:
	python -m build --sdist

build-wheel:
	python -m build --wheel

create-migrations:
	alembic revision --autogenerate

upgrade:
	alembic upgrade head

compile-babel:
	pybabel compile -f -d tennis_finder/translations

up:
	docker-compose up
rebuild:
	docker-compose up --build --force-recreate
