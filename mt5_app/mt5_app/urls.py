from django.contrib import admin
from django.urls import path
from blog.views import ArticleView, UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article',  ArticleView.as_view()),
    path('article/<int:article_id>', ArticleView.as_view()),
    path('user',  UserView.as_view()),
    path('user/<int:user_id>', UserView.as_view())
]