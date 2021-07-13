from django.urls import reverse_lazy
from django.views.generic import DeleteView

from categories.models import Category


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category:list')
