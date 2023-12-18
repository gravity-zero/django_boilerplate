from datetime import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
 
# Vous pouvez rajouter les commentaires ici !
