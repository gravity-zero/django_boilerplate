dev:
	docker compose --env-file .env.dev up -d --build && \
	if [ -d ./mt5_app ]; then \
		sudo chown -R $(USER) ./mt5_app; \
	else \
  		sleep 20 && sudo chown -R $(USER) ./mt5_app; \
	fi

migrations:
	docker exec django_app python ./mt5_app/manage.py makemigrations && \
	docker exec django_app python ./mt5_app/manage.py migrate