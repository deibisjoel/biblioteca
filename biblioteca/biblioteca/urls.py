from django.conf.urls import patterns, include, url
import settings
from principal.views import Registrarse
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'principal.views.index'),
    url(r'^Nosotros/', 'principal.views.nosotros'),
    url(r'^login/', 'principal.views.iniciar_sesion',name='iniciar_sesion'),
    #url(r'^registro/', 'principal.views.nuevo_usuario',name='nuevo_usuario'),
    url(r'^registro/$', Registrarse.as_view() , name = 'registrarse'),
    url(r'^libros/', 'principal.views.libros'),
    url(r'^contacto/', 'principal.views.contacto'),
    url(r'^prestamo/(?P<idlibro>\d+)/$', 'principal.views.agregar_prestamo'),
    url(r'^buscar/','principal.views.search'),
    url(r'^Salir/$', 'principal.views.cerrar_sesion'),
    url(r'^reporte_libros/$','principal.views.reportelibros',name= "to_pdf"),
    url(r'^reporte_prestamo/$','principal.views.reporteprestamo',name= "reporteprestamo"),

    

    url(r'media/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
 
)
