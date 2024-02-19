from django import forms

class clienteFormulario(forms.Form):
    nombre= forms.CharField()
    fecha_nacimiento= forms.DateField()
    email= forms.EmailField()
    
class empleadoFormulario(forms.Form):
    nombre= forms.CharField()
    fecha_nacimiento= forms.DateField()
    email= forms.EmailField()
    puesto = forms.CharField()
   
class articuloFormulario(forms.Form):
    nombreArticulo= forms.CharField()
    modelo = forms.CharField()