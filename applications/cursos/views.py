from applications.alumnos.models import Alumno,Alumno_antecedente
from applications.antecedentes.models import Antecedente
from django.urls import reverse_lazy, reverse
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from .models import Curso, Curso_Alumno , Fecha, PlanEstudio, Profesor
from .logicas import cursos_base , get_curso_anterior_pk, check_cursos
from datetime import datetime
import math
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
        context['alumnos_cuarto'] =Curso.objects.alumnos_cuarto(current_año,current_semestre)
        if cursos:
            context['current_año'] = int(current_año)
            context['current_año_new'] = int(current_año)+1
            context['current_semestre'] = int(current_semestre)
        return context
class CursosDetalle(LoginRequiredMixin,DetailView):
    template_name = 'cursos/curso.html'
    model = Curso
    def get_context_data(self, **kwargs):
        context = super(CursosDetalle, self).get_context_data(**kwargs)
        cursos, current_año, current_semestre = Curso.objects.get_all_data()
        current_curso = Curso.objects.get(id_curso= self.kwargs['pk'])
        if current_curso.cod_fecha.fecha_termino != None:
            result = current_curso.cod_fecha.fecha_inicio - current_curso.cod_fecha.fecha_termino
            result= str(result)
            result = result.split(" ",1)
            days = result[0]        
            context['total_dias'] =math.floor(int(days))
        context['semestre'] =current_semestre
        context['year'] =current_año
        context['alumnos'] =Alumno.objects.get_alumno_sin_curso()
        context['profs'] =Profesor.objects.all()
        return context

class CursosAll(LoginRequiredMixin,ListView):
    template_name = 'cursos/all_cursos.html'
    model = Curso
    paginate_by = 9
    context_object_name = 'cursos'

    def get_queryset(self):
        todo = True
        if len(self.request.GET) == 0:
            pass
        elif 'id' in self.request.get_full_path():
            values=[]
            values.append(self.request.GET['id'])
            values.append(self.request.GET['year'])
            values.append(self.request.GET['semestre'])
            values.append(self.request.GET['jefe'])
            vacio = 0
            for value in values:
                if value == '': 
                    vacio+=1
            if not  vacio == 4:
                todo = False
        if todo:
            query = Curso.objects.all()
            return query
        else:
            return Curso.objects.get_cursos_filter(values)
    def get_context_data(self, **kwargs):
        context = super(CursosAll, self).get_context_data(**kwargs)
        context['fechas'] =Fecha.objects.get_years()
        context['profes'] =Profesor.objects.get_jefes()
        return context

def set_asistencia(request):
    if request.method == 'POST':
        alumno_curso = Curso_Alumno.objects.get(id=request.POST['alumno'])
        alumno_curso.dias_asistencia = request.POST['asistencia']
        alumno_curso.save()
        messages.success(request,'!!Asistencia ingresada correctamente!!.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def init_cursos(request):
    if request.method == 'POST':
        check_exists_cursos = Curso.objects.all()
        check_exists_planes = PlanEstudio.objects.all().count()
        if check_exists_cursos.count() ==0 and check_exists_planes >0:
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
                        numero=base[2],
                        plan_estudio = PlanEstudio.objects.get(nombre='Educación General')                        
                    )
                else:
                    Curso.objects.create(
                        id_curso=key_curso,
                        cod_fecha=Fecha.objects.get(cod_fecha=key_fecha),
                        nombre=base[1],
                        numero=base[2],
                        electivo=base[3],
                        plan_estudio = PlanEstudio.objects.get(nombre='Técnico Profesional')                        
                    )
                this_curso = Curso.objects.get(id_curso = key_curso)
                linked_asignaturas_to_curso(this_curso)
            messages.success(request,'!!Cursos generados con exito!!.')
        else:
            messages.error(request,'No hay planes de estudio disponibles.')
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
        if curso.numero > 1.0 :
            pk = get_curso_anterior_pk(curso.numero) + str(año) + str(semestre)
            c_anterior = Curso.objects.get(id_curso=pk)
        if data[0] == 'repitente':
            c_anterior.alumnos.add(data[1])
            for al in c_anterior.curso_alumno_set.all():
                if al.alumno.rut == data[1]:
                    al.is_current = True
                    al.save()
            curso.alumnos.remove(data[1])
            # Aqui deberia escribir que es repitente en ANTECEDENTES
            antecedente_repitente(data[1],curso )

        elif data[0] == 'abandono':
            print(data)
            alumno = Alumno.objects.get(rut = data[1])
            alumno.estado= '1'
            alumno.save()
            for al in curso.curso_alumno_set.all():
                if al.alumno.rut == alumno.rut:
                    al.abandono= True
                    al.save()
        elif data[0] == 'error':
            curso.alumnos.remove(data[1])
        messages.success(request,'!!La accion ha sido ejecutada sin problemas!!.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def finalizar_semestre(request):
    if request.method == 'POST':
        rol = str(request.user.rol)
        fecha_inicio_old = request.POST['semestre_old']
        fecha_inicio_new = request.POST['semestre_new']
        if rol == 'Administrador' or rol == 'Director':
            cursos, current_año, current_semestre = Curso.objects.get_all_data()
            proceder, errors = validate_cursos(cursos=cursos)
            if proceder:
                #aqui retorna el mismo año
                new_year = create_new_fecha(
                current_año=current_año,
                current_semestre=current_semestre,
                fecha_inicio_new=fecha_inicio_new,
                fecha_inicio_old=fecha_inicio_old,
                what='fsemestre'
                )
                for i in range(0, len(cursos_base)):
                    #creamos el curso del segundo semestre
                    base = cursos_base[i]
                    key = base[0]+str(new_year)+'2'
                    #Aqui obtenemos el curso pasado (el del 1°er semestre)
                    curso_semestre_pasado = Curso.objects.get(id_curso=base[0]+str(current_año)+str(current_semestre))
                    if i in [10,11,12,13,14,15]:
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'2'),
                            nombre=base[1],
                            numero=base[2],
                            electivo=base[3],
                            plan_estudio = curso_semestre_pasado.plan_estudio
                        )
                    else:
                        Curso.objects.create(
                            id_curso=key,
                            cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'2'),
                            nombre=base[1],
                            numero=base[2],
                            plan_estudio = PlanEstudio.objects.get(nombre = 'Educación General')
                        )
                    #Aqui copiamos los alumnos del antiguo curso al nuevo curso
                    this_curso = Curso.objects.get(id_curso=key)
                    for alumno in curso_semestre_pasado.curso_alumno_set.all():
                        alumno.is_current = False
                        alumno.save()
                        if not alumno.abandono:
                            this_curso.alumnos.add(alumno.alumno.rut)
                            
                    linked_asignaturas_to_curso(this_curso)
                    #Finalmente fijamos como el curso actual a los alumnos
                    for current_al in this_curso.curso_alumno_set.all():
                        current_al.is_current = True
                        current_al.save()
                messages.success(request,'!!Semestre finalizado con exito!!.')
            else:
                errores=''
                for e in errors:
                    errores+=e+'<br />'
                messages.error(request, 'No se cumplen todas las condiciones para cerrar este periodo')
                messages.info(request, mark_safe(errores)) 
        else:
            messages.error(request,'No tienes los permisos de usuario para realizar esta acción.')
        
    return HttpResponseRedirect(reverse('cursos_app:all'))

def finalizar_año(request,):
    if request.method == 'POST':
        rol = str(request.user.rol)
        fecha_inicio_old = request.POST['semestre_old']
        fecha_inicio_new = request.POST['semestre_new']
        if rol == 'Administrador' or rol == 'Director':
            cursos, current_año, current_semestre = Curso.objects.get_all_data()
            proceder, errors = validate_cursos(cursos=cursos)
            if proceder:
                repitentes = request.POST.getlist('repitentes')
                new_year = create_new_fecha(
                    current_año=current_año,
                    current_semestre=current_semestre,
                    fecha_inicio_new=fecha_inicio_new,
                    fecha_inicio_old=fecha_inicio_old,
                    what='faño'
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
                            numero=base[2],
                            plan_estudio = PlanEstudio.objects.get(nombre='Educación General')                        
                        )
                        this_curso = Curso.objects.get(id_curso = key)
                        linked_asignaturas_to_curso(this_curso)
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
                                plan_estudio = PlanEstudio.objects.get(nombre='Técnico Profesional')
                            )
                            #Añade los alumnos del curso anterior al nuevo
                            this_curso = Curso.objects.get(id_curso=key)
                            for alumno in curso_anterior.curso_alumno_set.all():
                                alumno.is_current=False
                                alumno.save() 
                                if not alumno.abandono:
                                    this_curso.alumnos.add(alumno.alumno.rut)
                            linked_asignaturas_to_curso(this_curso)
                            #Cambia el estado a Finalizado de los alumnos que salen de 4to
                            cuarto_actual = Curso.objects.get(id_curso = base[0]+str(current_año)+str(current_semestre))
                            for alumno in cuarto_actual.curso_alumno_set.all():
                                if not alumno.alumno.rut in repitentes:
                                    alumno.alumno.estado = '2'
                                    alumno.alumno.save()
                                for repitente in repitentes:
                                    if repitente == alumno.alumno.rut:
                                        this_curso.alumnos.add(repitente)
                                        antecedente_repitente(repitente,cuarto_actual)
                                alumno.is_current= False
                                alumno.save()          
                            #Este curso es el actual de los alumnos
                            for a in this_curso.curso_alumno_set.all():
                                a.is_current=True
                                a.save()
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
                                plan_estudio = PlanEstudio.objects.get(nombre='Técnico Profesional')
                            )
                            this_curso = Curso.objects.get(id_curso = key)
                            linked_asignaturas_to_curso(this_curso)
                        #Acciones de Segundo medio hasta segundo basico
                        else:
                            #Crea el nuevo curso
                            key = base[0]+str(new_year)+'1'
                            Curso.objects.create(
                                id_curso=key,
                                cod_fecha=Fecha.objects.get(cod_fecha=str(new_year)+'1'),
                                nombre=base[1],
                                numero=base[2],
                                plan_estudio = PlanEstudio.objects.get(nombre='Educación General')
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
                                    if not alumno.abandono:
                                        this_curso.alumnos.add(alumno.alumno.rut)
                                #Este curso es el actual de los alumnos
                                for a in this_curso.curso_alumno_set.all():
                                    a.is_current=True
                                    a.save()
                                # Accion unica para segundo medio
                                if i == 9 :
                                    check = Curso.objects.get_cursos_by_id(base[0],current_año,current_semestre)
                                    if check.count() > 0:
                                        curso_Actual = Curso.objects.get(id_curso = base[0]+str(current_año)+str(current_semestre))
                                        for alumno in curso_Actual.curso_alumno_set.all():
                                            alumno.is_current=False
                                            alumno.save()
                                linked_asignaturas_to_curso(this_curso)
                messages.success(request,'!!Año finalizado con exito!!.')                   
            else:
                errores=''
                for e in errors:
                    errores+=e+'<br />'
                messages.error(request, 'No se cumplen todas las condiciones para cerrar este periodo')
                messages.info(request, mark_safe(errores))
        else:
            messages.error(request,'No tienes los permisos de usuario para realizar esta acción.')
    
    return HttpResponseRedirect(reverse('cursos_app:all'))

def linked_asignaturas_to_curso(curso):
    if curso.numero > 10:
        curso.asignaturas.add('MA')
        curso.asignaturas.add('ING')
    for asig in curso.plan_estudio.asignaturas.all():
        if asig.nombre == 'Inglés' and curso.numero < 5 :
            pass # Solamente para saltarse la asignatura y no Añadirla                                                    
        elif asig.nombre == 'Lengua indígena':
            if curso.numero < 3 or curso.numero > 8:
                pass # Solamente para saltarse la asignatura y no Añadirla
            else:
                curso.asignaturas.add(asig.cod_asign)
        elif  asig.cod_asign == 'LCP' and curso.numero > 6 :
            pass # Solamente para saltarse la asignatura y no Añadirla
        else:
            curso.asignaturas.add(asig.cod_asign)

def profe_to_curso(request,):
    if request.method == 'POST':
        print(request.POST)
        key_profe = request.POST['prof_jefe']
        key_curso = request.POST['curso']
        curso = Curso.objects.get(id_curso = key_curso)
        if key_profe == '':
            curso.id_prof_jefe =None
            curso.save()
        else:
            curso.id_prof_jefe = Profesor.objects.get(rut = key_profe)
            curso.save()
        messages.success(request,'!!Profesor Jefe actualizado con exito!!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def antecedente_repitente(rut,curso):
    alumno = Alumno.objects.get(rut=rut)
    cant = Antecedente.objects.filter(nombre_antecedente = 'Repitente').count()
    if cant == 0:
        Antecedente.objects.create(
            nombre_antecedente = 'Repitente'
        )
    Alumno_antecedente.objects.create(
        alumno = alumno,
        fecha = datetime.now(),
        detalle='Alumno repitente del curso ' + curso.nombre + ' del año ' + str(curso.cod_fecha.year),
        antecedente =Antecedente.objects.get(nombre_antecedente = 'Repitente')
    )

def validate_cursos(cursos):
    proceder = True
    errors=[]
    for curso in cursos:
        errors = check_cursos(curso)
        if len(errors) > 0:
            proceder= False
            break
    
    return proceder, errors
def create_new_fecha(current_año, current_semestre, fecha_inicio_old, fecha_inicio_new, what):
    #Seteamos la fecha de termino a traves de la busqueda get
    print(current_año, current_semestre)
    pk = str(current_año)+str(current_semestre)
    semestre_old= Fecha.objects.get(cod_fecha=pk)
    semestre_old.fecha_termino = fecha_inicio_old
    semestre_old.save()

    #Creamos la nueva fecha con el año siguiente
    if what == 'faño':
        new_year = int(current_año) +1
        Fecha.objects.create(
            cod_fecha = str(new_year)+'1',
            fecha_inicio = fecha_inicio_new,
            semestres = 1,
            year = new_year
        )
        return new_year
     #Creamos la nueva fecha con el mismo año 
    else:
        Fecha.objects.create(
            cod_fecha = str(current_año)+'2',
            fecha_inicio = fecha_inicio_new,
            semestres = 2,
            year = current_año
        )
        return current_año


    
   