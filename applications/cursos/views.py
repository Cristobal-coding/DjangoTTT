from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Curso , Fecha, PlanEstudio
from .logicas import cursos_base
# Create your views here.
class CursosHome(LoginRequiredMixin,TemplateView):
    template_name = 'cursos/cursos.html'
    model = Curso
    context_object_name = 'cursos'
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


def finalizar_año(request,):
    if request.method == 'POST':
        rol = str(request.user.rol)
        fecha_inicio_old = request.POST['semestre_old']
        fecha_inicio_new = request.POST['semestre_new']
        if rol == 'Administrador' or rol == 'Director':
            cursos, current_año, current_semestre = Curso.objects.get_all_data()
            new_year = int(current_año) +1
            #Seteamos la fecha de termino a traves de la busqueda get
            pk = str(current_año)+str(current_semestre)
            semestre_old= Fecha.objects.get(cod_fecha=pk)
            semestre_old.fecha_termino = fecha_inicio_old
            semestre_old.save()
            #Creamos la nueva fecha con el año siguiente
            Fecha.objects.create(
                cod_fecha = str(new_year)+'1',
                fecha_inicio = fecha_inicio_new,
                semestres = 1,
                year = new_year
            )
            
            for i in range(0, len(cursos_base)):
                base = cursos_base[i]
                #Acciones para Primero Basico
                if i == 0 :
                    key = base[0]+str(new_year)+'1'
                    Curso.objects.create(
                        id_curso=key,
                        cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                        nombre=base[1],
                        numero=base[2]                        
                    )
                else:
                    #Acciones para Cuarto medio
                    if i in [13,14,15]:
                        base = cursos_base[i-3]
                        curso_anterior = Curso.objects.get(id_curso=base[0]+str(current_año)+str(current_semestre))
                        base = cursos_base[i]
                        #Crea el nuevo curso
                        key = base[0]+str(new_year)+'1'
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                            nombre=base[1],
                            numero=base[2],
                            electivo=base[3],
                            plan_estudio = PlanEstudio.objects.get(id=3)
                        )
                        #Añade los alumnos del curso anterior al nuevo
                        this_curso = Curso.objects.get(id_curso=key)
                        for alumno in curso_anterior.curso_alumno_set.all():
                            alumno.is_current=False
                            alumno.save() 
                            
                            this_curso.alumnos.add(alumno.alumno.rut)
                        #Este curso es el actual de los alumnos
                        for a in this_curso.curso_alumno_set.all():
                            a.is_current=True
                            a.save()
                        #Cambia el estado a Finalizado de los alumnos que salen de 4to
                        cuarto_actual = Curso.objects.get(id_curso = base[0]+str(current_año)+str(current_semestre))
                        for alumno in cuarto_actual.curso_alumno_set.all():
                            alumno.alumno.estado = '2'
                            alumno.alumno.save()          
                    #Acciones para Tercero medio
                    elif i in [10,11,12]:
                        base = cursos_base[i]
                        key = base[0]+str(new_year)+'1'
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                            nombre=base[1],
                            numero=base[2],
                            electivo=base[3],
                            plan_estudio = PlanEstudio.objects.get(id=3)
                        )
                    #Acciones de Segundo medio hasta segundo basico
                    else:
                        base = cursos_base[i-1]
                        anteriores = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                        base = cursos_base[i]
                        for c in anteriores:
                            #Crea el nuevo curso
                            key = base[0]+str(new_year)+'1'
                            Curso.objects.create(
                                id_curso=key,
                                cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                                nombre=base[1],
                                numero=base[2]
                            )
                            #Añade los alumnos del curso anterior al nuevo
                            this_curso = Curso.objects.get(id_curso=key)  
                            for alumno in c.curso_alumno_set.all():
                                alumno.is_current=False
                                alumno.save()
                                this_curso.alumnos.add(alumno.alumno.rut)
                            #Este curso es el actual de los alumnos
                            for a in this_curso.curso_alumno_set.all():
                                a.is_current=True
                                a.save()
             
    messages.info(request,'Año finalizado con exito!!.')
    return HttpResponseRedirect(reverse('cursos_app:all'))

    
   