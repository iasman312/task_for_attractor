from rest_framework import serializers
from api_v1.serializers import ArticlesSerializer
from categories.models import Category


class CategoriesSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(many=True)

    class Meta:
        fields = (
            'title',
            'articles',
        )
        model = Category
