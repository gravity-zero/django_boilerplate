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

### Routing

La première partie de la configuration des routes ce situe dans le fichier mt5_app/urls.py

Le but est de déclarer les routes et les paramètres + la classe à appeler.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article',  ArticleView.as_view()),
    path('article/<int:article_id>', ArticleView.as_view()),
    path('user',  UserView.as_view()),
    path('user/<int:user_id>', UserView.as_view())
]
```

Dans le fichier blog/views.py, vous trouverez 2 classes avec des méthodes post et get (C'est un des moyens de "respecter" les principes de REST et surtout d'être sûr de la méthode utilisé pour appeler la route)

```python
 class ArticleView(View):

 ## ....
 
    def post(self, request):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            slug = data.get('slug')
            content = data.get('content')
            author_id = data.get('author_id')
            new_blog_article = Article(title=title, slug=slug, content=content, author_id=author_id)
            new_blog_article.save()
            return JsonResponse({'message': 'Article created successfully'}, status=201)
            pass
        except Exception as e:
            return JsonResponse({'error': 'An exception occurred, ' + str(e)}, status=500)
 ```

