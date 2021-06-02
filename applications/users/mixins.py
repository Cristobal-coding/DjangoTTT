from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

# from django.views.generic import View
#
# from .models import User
# class IsActivePermisoMixin(LoginRequiredMixin):
#     login_url = reverse_lazy('users_app:user-login')

#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#         #
        
#         if not request.user.activo:
#             messages.add_message(request, messages.INFO, 'Usuario Bloqueado.')
#             return HttpResponseRedirect(
#                 reverse(
#                     'home_app:login'
#                 )
#             )

#         return super().dispatch(request, *args, **kwargs)