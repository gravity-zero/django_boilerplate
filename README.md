# django_boilerplate

### Dépendances à installer

- Docker et docker-compose
```bash
curl -L https://get.docker.com | sh
sudo usermod -aG docker $USER 
```
- Makefile
```bash
#Mac
brew install make

#Ubuntu/Debian
sudo apt install build-essential && sudo apt install make

# Pour Windows il est temps de vous pencher sur WSL (windows subsystem for linux)
```


## Lancement du projet
### Avec le Makefile

```bash
# Lancement du projet et installation des dépendances
make dev
# Lancement des migrations (attendez que toutes les dépendances soit bien installé avant de lancer les migrations)
make migrations
```

### Sans Makefile
```bash
# Lancement du projet et installation des dépendances
docker compose up -d --build && \
sudo chown -R $(USER) ./mt5_app;
# Lancement des migrations (attendez que toutes les dépendances soit bien installé avant de lancer les migrations)
docker exec django_app python ./mt5_app/manage.py makemigrations && \
docker exec django_app python ./mt5_app/manage.py migrate
```

### Variable d'environnement
- Actuellement les variables d'environnement sont stocké dans un .env.dev pour une mise en production, il faudrait modifier l'import du .Env