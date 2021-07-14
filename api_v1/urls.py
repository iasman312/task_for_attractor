from django.urls import path
from api_v1.views import CategoryListAPIView, ArticleListAPIView

app_name = 'api_v1'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('articles/', ArticleListAPIView.as_view(), name='articles'),
]
