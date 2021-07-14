from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from articles.forms import ArticleForm
from articles.models import Article


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'articles/update.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('category:view', kwargs={'pk': self.kwargs.get('pk')})