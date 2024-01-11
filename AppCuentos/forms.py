from django import forms
from .models import Cuento, Historia

class CuentoForm(forms.ModelForm):
    class Meta:
        model = Cuento
        fields = ['autor', 'titulo', 'contenido', 'puntuacion']

        # Opcional: Puedes agregar widgets personalizados para controlar cómo se renderizan los campos HTML
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'puntuacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # Opcional: Puedes definir etiquetas personalizadas para los campos
        labels = {
            'autor': 'Autor del cuento',
            'titulo': 'Título del cuento',
            'contenido': 'Contenido del cuento',
            'puntuacion': 'Puntuación del cuento',
        }

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = ['autor', 'titulo', 'contenido', 'puntuacion']

        # Opcional: Personalizar los widgets de los campos del formulario
        widgets = {
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'puntuacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

        # Opcional: Definir etiquetas personalizadas para los campos
        labels = {
            'autor': 'Autor de la historia',
            'titulo': 'Título de la historia',
            'contenido': 'Contenido de la historia',
            'puntuacion': 'Puntuación de la historia',
            'fecha_creacion': 'Fecha de creación de la historia',
        }
