from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso
# Create your views here.
class CursosHome(LoginRequiredMixin,ListView):
    template_name = 'cursos/cursos.html'
    model = Curso
    context_object_name = 'cursos'
    paginate_by=5
    login_url = reverse_lazy('home_app:login')
    def get_context_data(self, **kwargs):
        context = super(CursosHome, self).get_context_data(**kwargs)
        context['current_cursos'] = Curso.objects.get_current_cursos()
        return context
class CursosDetalle(DetailView):
    template_name = 'cursos/curso.html'
    model = Curso

    
   