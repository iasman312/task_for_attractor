from rest_framework import serializers

from articles.models import Article


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title',
            'description',
            'user',
            'category',
        )
        model = Article