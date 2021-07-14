from rest_framework import serializers

from articles.models import Article


class ArticlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'user',
            'category',
            'image',
        )
        model = Article