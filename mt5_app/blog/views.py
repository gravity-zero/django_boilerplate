from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from blog.models import Post
import json


class ArticleView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticleView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            slug = data.get('slug')
            content = data.get('content')
            author_id = data.get('author_id')
            new_blog_post = Post(title=title, slug=slug, content=content, author_id=author_id)
            new_blog_post.save()
            return JsonResponse({'message': 'Article created successfully'}, status=201)
            pass
        except Exception as e:
            return JsonResponse({'error': 'An exception occurred, ' + str(e)}, status=400)
    def get(self, request, article_id):
        try:
            article = get_object_or_404(Post, id=article_id)
            serialized_article = {
                'id': article.id,
                'title': article.title,
                'slug': article.slug,
                'content': article.content,
                'author_id': article.author_id,

            }

            return JsonResponse(serialized_article)
            pass
        except Exception as e:
            return JsonResponse({'error': 'An exception occurred, ' + str(e)}, status=400)


class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UserView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            is_staff = data.get('is_staff')
            is_active = data.get('is_active')
            new_user = User(username=username, password=password,
                            first_name=first_name, last_name=last_name,
                            email=email, is_staff=is_staff, is_active=is_active)
            new_user.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
            pass
        except Exception as e:
            return JsonResponse({'error': 'An exception occurred, ' + str(e)}, status=400)

    def get(self, request, user_id):
        try:
            user = get_object_or_404(User, id=user_id)
            serialized_user = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined
            }
            return JsonResponse(serialized_user)
            pass
        except Exception as e:
            return JsonResponse({'error': 'An exception occurred, ' + str(e)}, status=400)
