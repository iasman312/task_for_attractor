from django.urls import path
from articles.views import ArticleCreate

app_name = 'article'

urlpatterns = [
    path('articles/create', ArticleCreate.as_view(), name='create'),
]