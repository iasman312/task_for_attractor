from rest_framework import generics

from api_v1.serializers import CategoriesSerializer
from categories.models import Category


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Category.objects.all()