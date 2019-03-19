# -*- coding: utf8 -*- 
from django.views.generic import TemplateView,FormView

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from principal.models import Perfiles
from principal.models import Libro
from principal.models import Prestamo

from principal.forms import prestamoform
from principal.forms import ContactoForm
from django.db.models import Q
from django.core.mail import EmailMessage

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from principal.forms import UserForm
from django.core.urlresolvers import reverse_lazy
from models import Perfiles

from wkhtmltopdf.views import PDFTemplateResponse
from django.db.models.expressions import F

from datetime import date

def index(request):
	#libro =  libros.objects.all()
	return render_to_response("index.html",context_instance = RequestContext(request))
# Create your views here.


def nosotros(request):
	#libro =  libros.objects.all()
	return render_to_response("nosotros.html",context_instance = RequestContext(request))
# Create your views here.




def contacto(request):
	#libro =  libros.objects.all()
	return render_to_response("contacto.html",context_instance = RequestContext(request))


def libros(request):
	libros =  Libro.objects.filter(estado=True)
	return render_to_response("libros.html",{"libros":libros},context_instance = RequestContext(request))


"""def agregar_prestamo(request,idlibro):
	libro = Libro.objects.get(pk=idlibro)
	if request.method =="POST":
		formulario= prestamoform(request.POST,instance=libro)
		if formulario.is_valid():
			libro.estado= False
			formulario.save()
			return HttpResponseRedirect("/")
	else:
		formulario = prestamoform(instance= libro)

	return render_to_response("agregar_prestamo.html",{"formulario":formulario}, context_instance = RequestContext(request))"""


@login_required(login_url = '/login/')
def agregar_prestamo(request,idlibro):
	
	libro = Libro.objects.get(pk=idlibro)
	prestamo = Prestamo()
	prestamo.idlibro = libro
	
	if request.method =="POST":
		#estado = False
		formulario= prestamoform(request.POST)
		if formulario.is_valid():
			libro.estado= 0
			libro.save()
			formulario.save()
			#estado=True
			return HttpResponseRedirect("/prestado/")
			
	else:
		formulario = prestamoform(instance= prestamo)
		#estado=False
	
	contx = {"formulario": formulario }	

	return render_to_response("agregar_prestamo.html",contx, context_instance = RequestContext(request))




def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre_libro__icontains=query) 
            #Q(autor__icontains=query) |
            #Q(sinopsis__icontains=query)
        )
        results = Libro.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("buscar.html", {
        "results": results,
        "query": query
    },context_instance = RequestContext(request))



def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje '
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['Correo_Usuario']
			correo= EmailMessage(titulo, contenido, to=['zlokazo@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render(request, 'contacto.html',{'formulario':formulario})




"""def nuevo_usuario(request):
	if request.method=="POST":
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/")
	else:
		formulario = UserCreationForm()

	return render_to_response("new_user.html",{"formulario":formulario},context_instance= RequestContext(request))"""	

class Registrarse(FormView):
	template_name = 'registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')


	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.nombre = form.cleaned_data['nombre']
		perfil.apellidos =  form.cleaned_data['apellidos']
		perfil.direccion = form.cleaned_data['direccion']
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)




#@permission_required('auth.add_user',login_url="/")
def iniciar_sesion(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method=="POST":
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username= request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=username,password= clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect("/")
				else:
					return HttpResponseRedirect("/login/")	
			else:
				return HttpResponseRedirect("/login/")
	else:
		formulario=AuthenticationForm()

	return render_to_response("login.html",{"formulario":formulario}, context_instance = RequestContext(request))


@login_required(login_url = '/login/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect("/")


def reportelibros(request):
    libros =  Libro.objects.all()
    return PDFTemplateResponse(request,"reporte.html",{"libros":libros})




def reporteprestamo(request):
	prestamo =  Prestamo.objects.all()
	fecha = date.today()
	vencidos = Prestamo.objects.filter(fecha_devolucion= fecha)
	print vencidos
	return PDFTemplateResponse(request,"reporteprestamo.html",{"prestamo":prestamo , "vencidos":vencidos})