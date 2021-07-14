from rest_framework import generics

from api_v1.serializers import ArticlesSerializer
from articles.models import Article


class ArticleListAPIView(generics.ListAPIView):
    serializer_class = ArticlesSerializer

    def get_queryset(self):
        return Article.objects.all()