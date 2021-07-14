from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from articles.forms import ArticleForm
from articles.models import Article
from categories.models import Category


class ArticleCreate(CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    model = Article

    def get_success_url(self):
        return reverse(
            'category:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        article = form.instance
        article.category = category
        article.user = self.request.user
        return super().form_valid(form)
