from applications.users.mixins import UsersPermisoMixin
from applications.cursos.models import Profesor
from applications.psicologos.models import Psicologo
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .models import User, Rol
from .forms import RolRegisterForm, UserRegisterForm
from datetime import date
from django.core.files.storage import FileSystemStorage
from TrabajoTitulo.settings.base import BASE_DIR
from django.core.files.storage import default_storage
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "usuarios/profile.html"
    login_url = reverse_lazy('home_app:login')

class UserMainView(UsersPermisoMixin,TemplateView):
    template_name = "usuarios/inicio.html"
    login_url = reverse_lazy('home_app:login')

    def get_context_data(self, **kwargs):
        context = super(UserMainView, self).get_context_data(**kwargs)
        context['userform'] = UserRegisterForm
        context['rolform'] = RolRegisterForm
        context['users'] = User.objects.all()
        context['roles'] = Rol.objects.all()
        return context
   
class CreateUser(LoginRequiredMixin,CreateView):
    form_class= UserRegisterForm
    success_url = '.'
    login_url = reverse_lazy('home_app:login')
    def render_to_response(self, context, **response_kwargs):
        context['users'] = User.objects.all()
        context['roles'] = Rol.objects.all()
        context['rolform'] = RolRegisterForm
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template='usuarios/inicio.html',
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(userform=form))

    def form_valid(self, form):   
        print(form.cleaned_data['rol'])
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['rut'],
            form.cleaned_data['password1'],
            rol=form.cleaned_data['rol'],        
        ) 
        if str(form.cleaned_data['rol']).strip() == 'Psicologo':
            Psicologo.objects.create(
            rut= form.cleaned_data['rut'],
            nombre=form.cleaned_data['username'],
            apellido_paterno="",
            apellido_materno="",
            correo=None,
            telefono="",
            fecha_ingreso=date.today()
            )
        elif str(form.cleaned_data['rol']).strip() == 'Profesor':
            Profesor.objects.create(
            rut=form.cleaned_data['rut'],
            nombres=form.cleaned_data['username'],
            apellido_paterno="",
            apellido_materno="",
            asig_impartir=None,
            )
            
        return HttpResponseRedirect(reverse('user_app:registrar'),)
        
def edit_profile(request):
    if request.method == 'POST':
        user = User.objects.get(rut=request.user.rut)
        if request.FILES:
            myfile = request.FILES['image']
            fs = FileSystemStorage(location='media/usuarios', base_url='/usuarios')
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            user.image = url
            user.username = request.POST['username']
            user.save()
        else:
            if request.POST['borrar']:
                default_storage.delete(BASE_DIR+user.image.url)
                user.image=None
            user.username = request.POST['username']
            user.save()
    return HttpResponseRedirect(reverse('user_app:profile'))