from django.contrib import admin
from .models import Servicio, Trabajo, Empleado

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class TrabajoAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")
    list_display = ('empleado','servicio','estrellas','precio')
    list_filter = ('servicio','valoracion','costo')


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)