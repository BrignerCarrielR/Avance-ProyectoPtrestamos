from django.urls import path

from aplicaciones.novedades.views.empleados.views import ListaEmpleadosListView, CrearEmpleado, ActualizarEmpleado, \
    EliminarEmpleado
from aplicaciones.novedades.views.empresa.views import ListaEmpresaListView, CrearEmpresa, ActualizarEmpresa, \
    EliminarEmpresa
from aplicaciones.novedades.views.menuNovedades.views import NovedadesTemplateView
from aplicaciones.novedades.views.prestamos.views import lisPrestamos, CrearPrestamo, \
    ActualizarPrestamo, EliminarPrestamo

app_name = "novedades"
urlpatterns = [
    path('menunovedades', NovedadesTemplateView.as_view(), name="menunovedades"),
    # Empleado
    path('listaempleados', ListaEmpleadosListView.as_view(), name="listaempleados"),
    path('crearempleado', CrearEmpleado.as_view(), name="crearempleado"),
    path('actualizarempleado/<int:pk>', ActualizarEmpleado.as_view(), name="actualizarempleado"),
    path('eliminarempleado/<int:pk>', EliminarEmpleado.as_view(), name="eliminarempleado"),
    # Empresa
    path('lisempresa', ListaEmpresaListView.as_view(), name="lisempresa"),
    path('crearempresa', CrearEmpresa.as_view(), name="crearempresa"),
    path('actualizarempresa/<int:pk>', ActualizarEmpresa.as_view(), name="actualizarempresa"),
    path('eliminarempresa/<int:pk>', EliminarEmpresa.as_view(), name="eliminarempresa"),
# Prestamos
    path('lisprestamos',lisPrestamos.as_view(), name="lisprestamos"),
    path('crearprestamos',CrearPrestamo.as_view(), name="crearprestamos"),
    path('actualizarprestamos/<int:pk>', ActualizarPrestamo.as_view(), name="actualizarprestamos"),
    path('eliminarprestamos/<int:pk>', EliminarPrestamo.as_view(), name="eliminarprestamos"),

]