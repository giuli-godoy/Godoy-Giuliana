from django.urls import path, include

from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', HomeView.as_view(), name = 'Inicio' ),

    path('sobremi/', AboutCreate.as_view(), name = 'Sobre mí' ),
    path('servicios/', ListaServicios.as_view(), name = 'Servicios' ),
    path('reseñas/', ListaEmpleados.as_view(), name = 'Reseñas' ),
    path('filtrar', FiltrarEmpleados.as_view(), name = "Buscar"),
    path('empresas/', EmpresasView.as_view(), name = 'Empresas' ),
    path('crear_reseñas/', EmpleadoCreate.as_view(), name = 'Crear_Reseñas' ),
    path('actualizar_reseña/<int:pk>/', EmpleadoUpdate.as_view(), name = 'Actualizar_Reseña' ),
    path('eliminar_reseña/<int:pk>/', EmpleadoDelete.as_view(), name = 'Eliminar_Reseña' ),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

]