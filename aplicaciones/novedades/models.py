from django.db import models
from aplicaciones.core.models import Base
from proyecto_administrativo.constantes import Opciones
from django.utils.timezone import now
motivos = Opciones()
GENERO = motivos.genero()
MOTIVO = motivos.motivo()
# Create your models here.

class Empleado(Base):
    nombres = models.CharField(max_length=200, unique=True)
    ruc = models.CharField(max_length=10, unique=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    genero = models.CharField(max_length=1, choices=GENERO,default=GENERO[0][0], blank=True, null=True)
    telefonos = models.CharField(max_length=10, blank=True, null=True, unique=True)
    email = models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.nombres)

class Empresas(Base):
    nombre = models.CharField(max_length=30,)
    direccion = models.CharField(max_length=100,)
    ruc = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.nombre)

class FacturaPrestamo(models.Model):
    id = models.AutoField(primary_key=True)
    capital = models.FloatField(blank=False, null=True ,default=0)
    motivo = models.CharField(max_length=1, choices=MOTIVO,default=MOTIVO[0][0], blank=True, null=True)
    cuotas = models.IntegerField(blank=False, null=True,default=1)
    interes = models.FloatField(blank=False, null=True,default=10)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,unique=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    totalinteres = models.FloatField(blank=False, null=True, default=0)
    total =models.FloatField(blank=False, null=True, default=0)
    fecha = models.DateField(default=now, blank=False, null=True)
    fechainicio= models.DateField(blank=False, null=True)
    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.empleado)

class Descuentos(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,unique=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100,blank=True, null=True)
    fecha = models.DateField(default=now, blank=False, null=True)
    fechainicio = models.DateField(blank=False, null=True)
    precio = models.FloatField(blank=False, null=True)
    cuotas = models.IntegerField(blank=False, null=True)
    valorcuota = models.FloatField(blank=False, null=True, default=0)
    class Meta:
        verbose_name = "Descuentos"
        verbose_name_plural = "Descuentos"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.empleado)