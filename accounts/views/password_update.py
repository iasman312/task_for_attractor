from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from accounts.forms import UserChangePasswordForm


class UserChangePasswordView(LoginRequiredMixin, UpdateView):
    template_name = 'user_change_password.html'
    model = get_user_model()
    form_class = UserChangePasswordForm
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super(UserChangePasswordView, self).form_valid(form)

        # Перед тем, как вернуть пользователю ответ - обновляем его сессию,
        # чтобы пользователя не разлогинивало после смены пароля
        update_session_auth_hash(self.request, self.request.user)
        return response

    def get_success_url(self):
        return reverse('accounts:user-detail', kwargs={'pk': self.object.pk})