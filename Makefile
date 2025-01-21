# Django Commands
dj-make:
	python3 manage.py makemigrations
dj-mig:
	python3 manage.py migrate
dj-run:
	python3 manage.py runserver
dj-collect:
	python3 manage.py collectstatic
dj-superuser:
	python3 manage.py createsuperuser

# Virtual environment commands
venv310:
	python3.10 -m venv .venv
	@echo "Virtual environment created for Python 3.10"
venv39:
	python3.9 -m venv .venv
	@echo "Virtual environment created for Python 3.9"

# Poetry commands
install:
	poetry install
shell:
	poetry shell

# Dev utils
dev-pep8:
	isort .
	black .
dev-lint:
	flake8 .
	mypy .
dev-full:
	dev-pep8 dev-lint
tree:
	tree -a -I ".venv|.git|.vscode|.idea|node_modules|__pycache__"
