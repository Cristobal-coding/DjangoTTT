from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Curso , Fecha
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
            cursos_base = [['1erobasico','Primero básico',1.0], ['2dobasico','Segundo básico',2.0],['3robasico','Tercero básico',3.0],
            ['4tobasico', 'Cuarto básico',4.0],['5tobasico','Quinto básico',5.0],['6tobasico', 'Sexto básico',6.0],
            ['7tobasico', 'Septimo básico',7.0],['8vobasico', 'Octavo básico',8.0],['1eromedio','Primero medio',9.0],['2domedio','Segundo medio',10.0],
            ['3romedioCON','Tercero medio Construccion', 11.0],
            ['3romedioEL','Tercero medio Electricidad', 11.1],
            ['3romedioMET','Tercero medio Construnccion Metalicas', 11.2],
            ['4tomedioCON','Cuarto medio Construccion',12.0] ,
            ['4tomedioEL','Cuarto medio Electricidad',12.1] ,
            ['4tomedioMET','Cuarto medio Construnccion Metalicas',12.2] ,
            ]
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
                        anteriores = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                        base = cursos_base[i]
                        for c in anteriores:
                            #Crea el nuevo curso, traspasando
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
                                print(alumno.alumno.nombre)  
                                this_curso.alumnos.add(alumno.alumno.rut)
                            #Este curso es el actual de los alumnos
                            for a in this_curso.curso_alumno_set.all():
                                a.is_current=True
                                a.save()
                        #Finalizar estado de los alumnos del cuarto medio actual
                        cuarto_actual = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                        for c in cuarto_actual:
                            for alumno in c.curso_alumno_set.all():
                                a.alumno.rut = 2
                                a.alumno.save()
                    #Acciones para Tercero medio
                    elif i in [10,11,12]:
                        base = cursos_base[i]
                        key = base[0]+str(new_year)+'1'
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                            nombre=base[1],
                            numero=base[2]
                        )
                    #Acciones de Segundo medio hasta segundo basico
                    else:
                        base = cursos_base[i-1]
                        anteriores = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                        base = cursos_base[i]
                        for c in anteriores:
                            #Crea el nuevo curso, traspasando
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

    
   