from django.urls import path, include

from categories.views import IndexView, ArticleView, CreateCategoryView

app_name = 'category'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('create/', CreateCategoryView.as_view(), name='create'),
    path('<int:pk>/', ArticleView.as_view(), name='view'),
]