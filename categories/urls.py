from django.urls import path, include

from categories.views import IndexView, ArticleView

urlpatterns = [
    path('', IndexView.as_view(), name='category-list'),
    path('<int:pk>/', ArticleView.as_view(), name='category-view'),
]