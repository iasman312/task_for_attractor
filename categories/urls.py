from django.urls import path, include

from categories.views import (
    IndexView,
    CategoryView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

app_name = 'category'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/', CategoryView.as_view(), name='view'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),
    path('<int:pk>/', include('articles.urls')),
]