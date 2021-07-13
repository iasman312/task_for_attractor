from django.urls import reverse_lazy
from django.views.generic import CreateView

from categories.forms import CategoryForm
from categories.models import Category


class CreateCategoryView(CreateView):
    template_name = 'categories/create.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('category:list')