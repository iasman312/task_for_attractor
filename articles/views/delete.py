from django.urls import reverse
from django.views.generic import DeleteView

from articles.models import Article


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    context_object_name = 'article'

    def get_success_url(self):
        category = Article.objects.get(pk=self.kwargs.get('pk')).category
        return reverse('category:view', kwargs={'pk': category.id})
