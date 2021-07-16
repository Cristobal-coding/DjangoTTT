from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView , ListView, UpdateView, DetailView
from django.http import HttpResponseRedirect
from django.views.generic.edit import  FormView
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.alumnos.models import Alumno, Apoderado, Alumno_antecedente
from applications.cursos.models import Curso, Parciales, Asignatura_Curso
from applications.antecedentes.models import Antecedente
from django.forms import formset_factory
#local
from .forms import AlumnosRegisterForm, ApoderadosRegisterForm, CertificadoForm, Alumno_AntecedenteForm

class AlumnosHome(LoginRequiredMixin,TemplateView):
    template_name = 'alumnos/inicio.html'
    login_url = reverse_lazy('home_app:login')
    
    def get_context_data(self, **kwargs):
        context = super(AlumnosHome, self).get_context_data(**kwargs)
        context['alumnos'] = Alumno.objects.count()
        context['apoderados'] = Apoderado.objects.count()
        context['fem'] = Alumno.objects.filter(sexo__icontains='0')
        context['masc'] = Alumno.objects.filter(sexo__icontains='1')
        return context

class AlumnosFiltros(LoginRequiredMixin,ListView):
    template_name = 'alumnos/alumnos.html'
    model = Alumno
    context_object_name = 'alumnos'
    paginate_by=9
    login_url = reverse_lazy('home_app:login')
    

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        f1=self.request.GET.get("fecha1",'')
        f2=self.request.GET.get("fecha2",'')
        sexo=self.request.GET.get("sexo",'')
        if sexo:
            if f1 and f2 and sexo:
                return Alumno.objects.buscar_alumno_fecha_s(palabra_clave,f1,f2,sexo)
            elif f1=="" and f2=="":
                return Alumno.objects.buscar_alumno_s(palabra_clave,sexo)
            else:
                return Alumno.objects.buscar_por_sexo(sexo)
        else:
            if f1 and f2:
                return Alumno.objects.buscar_alumno_fecha(palabra_clave,f1,f2)
            else:
                return Alumno.objects.buscar_alumno(palabra_clave)
class AlumnoDetalle(LoginRequiredMixin,DetailView):
    template_name = 'alumnos/alumno_detalle.html'
    model = Alumno
    def get_context_data(self, **kwargs):
        context = super(AlumnoDetalle, self).get_context_data(**kwargs)
        context['certificados'] =Alumno.objects.get_certificados(rut=self.kwargs['pk'])
        context['form'] =Alumno_AntecedenteForm()
        alumno=Alumno.objects.get(rut=self.kwargs['pk'])
        current_curso = ''
        for curso in alumno.curso_alumno_set.all():
            if curso.is_current:
                current_curso = curso
        # if current_curso != '':
        context['curso'] =current_curso
        return context

class Certificado(LoginRequiredMixin,FormView):
    template_name = 'alumnos/certificado.html'
    form_class = formset_factory(CertificadoForm, extra=1, max_num=5) 
    login_url = reverse_lazy('home_app:login')
    success_url = '.'
    
    def form_valid(self, form):
        nota_key = ''
        coef_key = ''
        key_asign = self.request.POST['asignatura']
        key_alumno = self.request.POST['alumno']

        for i in range(int(self.request.POST['form-TOTAL_FORMS'])):
            nota_key = 'form-'+str(i)+'-nota'
            coef_key = 'form-'+str(i)+'-coeficiente'
            fecha_key = 'form-'+str(i)+'-fecha'
            nota = self.request.POST[nota_key]
            coef = self.request.POST[coef_key]
            fecha = self.request.POST[fecha_key]
            for coe in range(int(coef)):
                Parciales.objects.create(
                    fecha = fecha,
                    calificacion = float(nota),
                    alumno = Alumno.objects.get(rut = key_alumno),
                    asignatura = Asignatura_Curso.objects.get(id = key_asign)
                )

        url = reverse('alumnos_app:certificado', 
        kwargs={'pk': self.kwargs['pk'],
        'year': self.kwargs['year'],
        'semestre': self.kwargs['semestre']
        }) 
        return HttpResponseRedirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['semestre'] =self.kwargs['semestre']
        context['año'] =self.kwargs['year']
        context['range'] =range(20)
        context['alumno'] =Alumno.objects.get(rut= self.kwargs['pk'])
        context['curso'] =Curso.objects.get_curso_with_fecha(
            year=self.kwargs['year'],
            semestre=self.kwargs['semestre'],
            rut=self.kwargs['pk']
        )
        return context
    # def get_form_kwargs(self):

    #     kwargs = {
    #         'initial': self.kwargs, #Lo unico que cambie de la herencia
    #         'prefix': self.get_prefix(),
    #     }
    #     if self.request.method in ('POST', 'PUT'):
    #         kwargs.update({
    #             'data': self.request.POST,
    #             'files': self.request.FILES,
    #         })
    #     return kwargs
            
class AlumnosRegister(LoginRequiredMixin,FormView):
    model = Alumno
    template_name = "alumnos/regist_alumn.html"
    form_class= AlumnosRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')
    
    def form_valid(self, form):
        Alumno.objects.create(
            rut=form.cleaned_data['rut'],
            nombre=form.cleaned_data['nombre'],
            apellido_paterno=form.cleaned_data['apellido_paterno'],
            apellido_materno=form.cleaned_data['apellido_materno'],
            fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
            rut_apoderado=form.cleaned_data['rut_apoderado'],
            sexo=form.cleaned_data['sexo'],
            telefono=form.cleaned_data['telefono'],
            direccion=form.cleaned_data['direccion'],
            estado=form.cleaned_data['estado'],

        )
        messages.success(self.request, 'Alumno ingresado Correctamente.')
        return HttpResponseRedirect(self.get_success_url())

class AlumnoEdit(LoginRequiredMixin,UpdateView):
    template_name = "alumnos/edit_alumn.html"
    form_class = AlumnosRegisterForm
    model = Alumno
    # success_url = reverse_lazy('alumnos_app:detailAlumn')
    login_url = reverse_lazy('home_app:login')
    def form_valid(self, form):
        messages.success(self.request, 'Alumno actualizado Satisfactoriamente.')
        form.save()
        url = reverse('alumnos_app:detailAlumn', kwargs={'pk': self.kwargs['pk']}) # Esto redirecciona al detalle
        return HttpResponseRedirect(url)
    
class ApoderadosList(LoginRequiredMixin,ListView):
    template_name= 'alumnos/apoderados.html'
    model=Apoderado
    context_object_name='apoderados'
    paginate_by=9
    login_url = reverse_lazy('home_app:login')

    def get_queryset(self):
        nombreclave=self.request.GET.get("nombre",'')   
        rut_clave=self.request.GET.get("rut",'')

        if rut_clave:
            return Apoderado.objects.buscar_apoderado_rut(nombreclave,rut_clave)

        else:
            return Apoderado.objects.buscar_apoderado(nombreclave)

           

class CreateApoderado(LoginRequiredMixin, FormView):
    model = Apoderado
    template_name = "alumnos/regist_apod.html"
    form_class= ApoderadosRegisterForm
    success_url='.'
    login_url = reverse_lazy('home_app:login')
    def form_valid(self, form):
        Apoderado.objects.create(
            rut=form.cleaned_data['rut'],
            nombre_apoderado=form.cleaned_data['nombre_apoderado'],
            apellido_paterno=form.cleaned_data['apellido_paterno'],
            apellido_materno=form.cleaned_data['apellido_materno'],
            telefono_apoderado=form.cleaned_data['telefono_apoderado'],
            correo=form.cleaned_data['correo'],
        )
        messages.success(self.request, 'Apoderado ingresado Correctamente.')
        return HttpResponseRedirect(self.get_success_url())

class ApoderadoEdit(LoginRequiredMixin,UpdateView):
    template_name = "alumnos/edit_apod.html"
    form_class = ApoderadosRegisterForm
    model = Apoderado
    success_url = reverse_lazy('alumnos_app:apoderados')
    login_url = reverse_lazy('home_app:login')
    def form_valid(self, form):
        messages.success(self.request, 'Apoderado actualizado Satisfactoriamente.')
        form.save()
        return HttpResponseRedirect(self.get_success_url())


   
def delete_alumno(request, pk):
    query = Alumno.objects.get(pk=pk)
    query.delete()
    messages.success(request,'Alumno elminado Satisfactoriamente.')
    return HttpResponseRedirect(reverse('alumnos_app:filtrar'))

def add_antecedente(request):
    if request.method == 'POST':
        alumno = Alumno.objects.get(rut = request.POST['alumno'])
        antecedente = Antecedente.objects.get(id = request.POST['antecedente'])
        Alumno_antecedente.objects.create(
            alumno = alumno,
            antecedente = antecedente,
            detalle = request.POST['detalle'],
            fecha = request.POST['fecha']
        )
    return HttpResponseRedirect(request.META['HTTP_REFERER'])