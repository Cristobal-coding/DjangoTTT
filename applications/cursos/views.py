from django.urls import reverse_lazy, reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Curso , Fecha
# Create your views here.
class CursosHome(LoginRequiredMixin,ListView):
    template_name = 'cursos/cursos.html'
    model = Curso
    context_object_name = 'cursos'
    paginate_by=5
    login_url = reverse_lazy('home_app:login')
    def get_context_data(self, **kwargs):
        context = super(CursosHome, self).get_context_data(**kwargs)
        cursos, current_año, current_semestre = Curso.objects.get_all_data()
        context['current_cursos'] =cursos
        context['current_año'] = int(current_año)
        context['current_año_new'] = int(current_año)+1
        context['current_semestre'] = int(current_semestre)
        return context
class CursosDetalle(DetailView):
    template_name = 'cursos/curso.html'
    model = Curso


def finalizar_semestre(request):
    if request.method == 'POST':
        rol = str(request.user.rol)
        if rol == 'Administrador' or rol == 'Director':
            cursos, current_año, current_semestre = Curso.objects.get_all_data()
            if current_semestre == 2 :
                new_year = int(current_año) +1
                Fecha.objects.create(
                    cod_fecha = str(new_year)+'1',
                    fecha_inicio = datetime.now(),
                    semestres = 1,
                    year = new_year
                )
            

    return HttpResponseRedirect(reverse('cursos_app:all'))

    
   