from rest_framework import serializers

from api_v1.serializers import CategoriesSerializer
from articles.models import Article


class ArticlesSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()

    class Meta:
        fields = (
            'title',
            'description',
            'user',
            'category',
        )
        model = Article