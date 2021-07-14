from django.contrib.auth import get_user_model
from django.views.generic import UpdateView

from accounts.forms import UserUpdateForm


class UserUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'user_update.html'
    context_object_name = 'user_obj'
    form_class = UserUpdateForm