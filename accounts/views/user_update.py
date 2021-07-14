from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from accounts.forms import UserUpdateForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()

        if user_form.is_valid():
            return self.form_valid(user_form)

        return self.form_invalid(user_form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': self.object.pk})