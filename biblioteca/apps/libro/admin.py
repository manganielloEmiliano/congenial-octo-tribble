from django.contrib import admin
from .models import Libro




class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autores', 'anio_publicacion', 'editorial')
    list_filter = ('anio_publicacion', 'editorial')
    search_fields = ('titulo', 'autores')


admin.site.register(Libro, LibroAdmin)

