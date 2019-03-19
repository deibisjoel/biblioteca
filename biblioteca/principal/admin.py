from django.contrib import admin

from principal.models import Perfiles,Libro,Prestamo

class LibroAdmin(admin.ModelAdmin):
	list_display = ('idlibro','nombre_libro','sinopsis','autor','imagen_libro')
	list_filter =('autor',) #filtrar libros
	search_fields= ('nombre_libro','autor',)  #busqueda
	list_editable =('nombre_libro','sinopsis') #editar campos del admin
	#filter_horizontal = ('autor') , para relaciones many to many
	def imagen_libro(self ,libro):
		url = libro.traer_url_imagen()
		tag = "<img src='%s' style='width:100px;'>" % url
		return tag


	#Permite ingresar targs al administrador	
	imagen_libro.allow_tags=True

class PrestamoAdmin(admin.ModelAdmin):
	list_display= ('idprestamo','idlibro','idperfil','tiempo_registro','fecha_devolucion')
	list_filter =('idlibro','idperfil','tiempo_registro','fecha_devolucion')
	


class PerfilesAdmin(admin.ModelAdmin):
	list_display= ('idperfil','nombre','apellidos','direccion','telefono')
	list_filter =('idperfil','nombre','apellidos',)
	search_fields = ('apellidos','nombre','telefono',)
	list_editable =('nombre','apellidos','direccion','telefono')


admin.site.register(Perfiles,PerfilesAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Prestamo,PrestamoAdmin)

