from django.urls import path

from aplicaciones.novedades.views.descuentos.views import lisDescuentos, CrearDescuentos, ActualizarDescuento, \
    EliminarDescuento, ListaDescuentosPDF, DescuentoPDF
from aplicaciones.novedades.views.empleados.views import ListaEmpleadosListView, CrearEmpleado, ActualizarEmpleado, \
    EliminarEmpleado, ListaempleadosPDF
from aplicaciones.novedades.views.empresa.views import ListaEmpresaListView, CrearEmpresa, ActualizarEmpresa, \
    EliminarEmpresa, ListaempresaPDF
from aplicaciones.novedades.views.menuNovedades.views import NovedadesTemplateView
from aplicaciones.novedades.views.prestamos.views import lisPrestamos, CrearPrestamo, \
    ActualizarPrestamo, EliminarPrestamo, ListaPrestamosPDF

app_name = "novedades"
urlpatterns = [
    path('menunovedades', NovedadesTemplateView.as_view(), name="menunovedades"),
    # Empleado
    path('listaempleados', ListaEmpleadosListView.as_view(), name="listaempleados"),
    path('crearempleado', CrearEmpleado.as_view(), name="crearempleado"),
    path('actualizarempleado/<int:pk>', ActualizarEmpleado.as_view(), name="actualizarempleado"),
    path('eliminarempleado/<int:pk>', EliminarEmpleado.as_view(), name="eliminarempleado"),
    path('pdf_empleado',ListaempleadosPDF.as_view(),name="pdf_empleado"),
    # Empresa
    path('lisempresa', ListaEmpresaListView.as_view(), name="lisempresa"),
    path('crearempresa', CrearEmpresa.as_view(), name="crearempresa"),
    path('actualizarempresa/<int:pk>', ActualizarEmpresa.as_view(), name="actualizarempresa"),
    path('eliminarempresa/<int:pk>', EliminarEmpresa.as_view(), name="eliminarempresa"),
    path('pdf_empresa',ListaempresaPDF.as_view(),name="pdf_empresa"),
    # Prestamos
    path('lisprestamos',lisPrestamos.as_view(), name="lisprestamos"),
    path('crearprestamos',CrearPrestamo.as_view(), name="crearprestamos"),
    path('actualizarprestamos/<int:pk>', ActualizarPrestamo.as_view(), name="actualizarprestamos"),
    path('eliminarprestamos/<int:pk>', EliminarPrestamo.as_view(), name="eliminarprestamos"),
    path('pdf_prestamos',ListaPrestamosPDF.as_view(),name="pdf_prestamos"),
    # Descuentos
    path('lisdescuentos', lisDescuentos.as_view(), name="lisdescuentos"),
    path('creardescuentos',CrearDescuentos.as_view(), name="creardescuentos"),
    path('actualizardescuentos/<int:pk>', ActualizarDescuento.as_view(), name="actualizardescuentos"),
    path('eleminardescuento/<int:pk>', EliminarDescuento.as_view(), name="eleminardescuento"),
    path('pdf_descuentos', ListaDescuentosPDF.as_view(), name="pdf_descuentos"),
    path('pdf_descuentosfac', DescuentoPDF.as_view(), name="pdf_descuentosfac"),
]