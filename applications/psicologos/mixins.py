
from applications.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse, reverse_lazy
from django.contrib import messages



class PsicologosPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('home_app:login')
    
    def dispatch(self,request,*arg,**kwargs):
        # print(request.user.rol)
        if not request.user.is_authenticated:
            
            return self.handle_no_permission()
        elif not(request.user.rol.nombre == 'Psicologo' or (request.user.rol.nombre == 'Administrador')):
            messages.error(self.request,"No tienes permiso para entrar a esta pestaña.")
            return HttpResponseRedirect(
                reverse('home_app:home')
            )
        
        return super().dispatch(request,*arg,**kwargs)