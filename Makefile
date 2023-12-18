dev:
	docker compose up -d --build && \
	if [ -d ./blog ]; then \
		sudo chown -R $(USER) ./blog; \
	else \
  		sleep 20 && sudo chown -R $(USER) ./blog; \
	fi