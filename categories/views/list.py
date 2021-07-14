from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from categories.models import Category


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'categories/index.html'
    model = Category
    context_object_name = 'categories'