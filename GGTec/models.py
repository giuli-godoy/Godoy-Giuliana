from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Servicio(models.Model):  #Servicios técnicos 
    name = models.CharField(verbose_name="Servicios", max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
    def __str__(self):
        return self.name
    
class Trabajo(models.Model):  #Trabajos a realizar
    name = models.CharField(verbose_name="Trabajo", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Trabajo"
        verbose_name_plural = "Trabajos"
    
    def __str__(self):
        return self.name
    
class Empleado(models.Model):
    name = models.CharField(verbose_name="Empleado/s o Empresa", max_length=50) 
    description = models.TextField(verbose_name="Desempeño")
    servicio = models.ForeignKey(Servicio, verbose_name="Servicios", on_delete=models.CASCADE, null=False)
    trabajos = models.ManyToManyField(Trabajo, verbose_name="Trabajos")
    VALORACION = [
        (1, "Deficiente"),
        (2, "A mejorar"),
        (3, "Aceptable"),
        (4, "Bueno"),
        (5, "Excelente"),
    ]
    valoracion = models.PositiveSmallIntegerField(choices=VALORACION)
    COSTO = [
        (1, "$"),
        (2, "$$"),
        (3, "$$$"),
    ]
    costo = models.PositiveSmallIntegerField(choices=COSTO,null=True)
    contacto = models.TextField(verbose_name="Contacto",null=True)
    image = models.ImageField(upload_to="valoraciones", null=True, blank=True, verbose_name="Trabajos realizados")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return self.name
    
    @admin.display(ordering="name")
    def empleado(self):
        return format_html(f"<span style='color:grey;'>{self.name}</span>")
    
    @admin.display(ordering="valoracion")
    def estrellas(self):
        stars = "★"*self.valoracion
        return format_html(f"<span style='color:yellow;'>{stars}</span>")
    
    @admin.display(ordering="costo")
    def precio(self):
        pesos="$"*self.costo
        return format_html(f"<span style='color:green;'>{pesos}</span>")