django_manage_file = ./FeatureFlag/manage.py
wsgi_file_dir = ./FeatureFlag
wsgi_file_realpath = $(realpath $(wsgi_file_dir))
requirement_file = ./requirement.txt
env_file_location = ./.env
app_name = simplefeature
app_host = ${host}
app_port = ${port}

export_env_file:
	export $(xargs < $(env_file_location) )

install_requirement:
	pip install --upgrade pip
	pip install -r $(requirement_file)

migrate_db:
	$(django_manage_file) migrate

DB:
	$(django_manage_file) makemigrations
	$(django_manage_file) migrate

debug_mode: export_env_file DB
	$(django_manage_file) runserver

run_server:
	#gunicorn --bind localhost:$(app_port) $(app_name).wsgi --chdir $(wsgi_file_realpath)
	$(django_manage_file) runserver

production: export_env_file install_requirement migrate_db run_server

