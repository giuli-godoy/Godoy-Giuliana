from django import forms
from .models import Empleado
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['name', 'description', 'servicio', 'trabajos', 'valoracion', 'costo', 'contacto', 'image' ]
        VALORACION = [
            (1, "Deficiente"),
            (2, "A mejorar"),
            (3, "Aceptable"),
            (4, "Bueno"),
            (5, "Excelente")
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Empleado o Empresa"}),
            'description': CKEditorWidget(),
            'servicio': forms.Select(attrs={'class':'form-control', 'placeholder':'Servicio'}),
            'trabajos': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Trabajos brindados'}),
            'valoracion': forms.Select(attrs={'class':'form-control', 'placeholder':'Valoración'}),
            'costo': forms.Select(attrs={'class':'form-control', 'placeholder':'Costo'}),
            'contacto': CKEditorWidget()
        }

        labels = {
            'name': "",
            'description': ""
        }