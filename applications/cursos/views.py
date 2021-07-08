from applications.alumnos.models import Alumno
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Curso , Fecha, PlanEstudio
from .logicas import cursos_base , get_curso_anterior_pk
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
        if cursos:
            context['current_año'] = int(current_año)
            context['current_año_new'] = int(current_año)+1
            context['current_semestre'] = int(current_semestre)
        return context
class CursosDetalle(DetailView):
    template_name = 'cursos/curso.html'
    model = Curso
    def get_context_data(self, **kwargs):
        context = super(CursosDetalle, self).get_context_data(**kwargs)
        context['alumnos'] =Alumno.objects.get_alumno_sin_curso()
        return context

def init_cursos(request):
    if request.method == 'POST':
        check_exists_cursos = Curso.objects.all()
        if check_exists_cursos.count() ==0:
            semestre = request.POST['semestre']
            año = request.POST['año']
            inicio = request.POST['inicio']
            key_fecha = str(año)+str(semestre)
            Fecha.objects.create(
                cod_fecha = key_fecha,
                fecha_inicio = inicio,
                semestres = semestre,
                year = año
            )
            
            for i in range(0, len(cursos_base)):
                base = cursos_base[i]
                key_curso = base[0]+str(año)+str(semestre)
                if i<10:
                    Curso.objects.create(
                        id_curso=key_curso,
                        cod_fecha=Fecha.objects.get(cod_fecha=key_fecha),
                        nombre=base[1],
                        numero=base[2]                        
                    )
                else:
                    Curso.objects.create(
                        id_curso=key_curso,
                        cod_fecha=Fecha.objects.get(cod_fecha=key_fecha),
                        nombre=base[1],
                        numero=base[2],
                        electivo=base[3],
                        plan_estudio = PlanEstudio.objects.get(id=3)                        
                    )
    messages.info(request,'!!Cursos generados con exito!!.')
    return HttpResponseRedirect(reverse('cursos_app:all'))
    # return HttpResponseRedirect(reverse('cursos_app:all'))

def gestionar_alumnos(request,):
    if request.method == 'POST':
        alumnos = list(request.POST.getlist('alumnos'))
        curso = Curso.objects.get(id_curso=request.POST['curso'])
        if len(alumnos) > 0 :
            for alumno in alumnos:
                curso.alumnos.add(alumno)
            for c in curso.curso_alumno_set.all():
                c.is_current = True
                c.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
def remove_alumno(request,):
    if request.method == 'POST':
        data = request.POST['razon']
        data = data.split('_')
        curso = Curso.objects.get(id_curso=request.POST['curso'])
        año, semestre = Curso.objects.get_año_semestre()
        pk = get_curso_anterior_pk(curso.numero) + str(año) + str(semestre)
        c_anterior = Curso.objects.get(id_curso=pk)
        if data[0] == 'repitente':
            c_anterior.alumnos.add(data[1])
            for al in c_anterior.curso_alumno_set.all():
                if al.alumno.rut == data[1]:
                    al.is_current = True;
                    al.save()
            curso.alumnos.remove(data[1])
            # Aqui deberia escribir que es repitente en ANTECEDENTES

        elif data[0] == 'abandono':
            alumno = Alumno.objects.get(rut = data[1])
            alumno.estado= '1'
            alumno.save()
            curso.alumnos.remove(data[1])
        elif data[0] == 'error':
            curso.alumnos.remove(data[1])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

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
                        #Crea el nuevo curso
                        key = base[0]+str(new_year)+'1'
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                            nombre=base[1],
                            numero=base[2]
                        )
                        base = cursos_base[i-1]
                        anteriores = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                        
                        if anteriores.count() > 0 :
                            curso_anterior = Curso.objects.get(id_curso = base[0]+str(current_año)+str(current_semestre))
                            base = cursos_base[i]            
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
                            if i == 9 :
                                check = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                                if check.count() > 0:
                                    curso_Actual = Curso.objects.get(id_curso = base[0]+str(current_año)+str(current_semestre))
                                    for alumno in curso_Actual.curso_alumno_set.all():
                                        alumno.is_current=False
                                        alumno.save()
                            
             
    messages.info(request,'Año finalizado con exito!!.')
    return HttpResponseRedirect(reverse('cursos_app:all'))

    
   