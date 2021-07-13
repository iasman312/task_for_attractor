from django.views.generic import DetailView

from categories.models import Category


class CategoryView(DetailView):
    model = Category
    template_name = 'categories/view.html'