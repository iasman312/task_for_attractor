from django.urls import path
from articles.views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'article'

urlpatterns = [
    path('articles/create/', ArticleCreateView.as_view(), name='create'),
    path('articles/update/', ArticleUpdateView.as_view(), name='update'),
    path('articles/delete/', ArticleDeleteView.as_view(), name='delete'),
]