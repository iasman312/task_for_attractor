from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from categories.models import Category


class CategoryView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'categories/view.html'