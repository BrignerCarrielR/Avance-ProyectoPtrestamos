from django import forms
from django.forms import ModelForm

from aplicaciones.novedades.models import Empleado, Empresas, FacturaPrestamo


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        exclude=['usuario']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresas
        fields = '__all__'
        exclude=['usuario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PrestamoForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['empresa'].widget.attrs['autofocus'] = True
        self.fields['totalinteres'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['total'].widget.attrs = {'readonly':True,'class':'form-control'}
    class Meta:
        model = FacturaPrestamo
        fields = '__all__'
        widgets = {

        }