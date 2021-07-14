from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from categories.forms import CategoryForm
from categories.models import Category


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'categories/update.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('category:view', kwargs={'pk': self.kwargs.get('pk')})