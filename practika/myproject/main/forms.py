from .models import Service
from django.forms import ModelForm, TextInput


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ["name", "price", "ind"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "ind": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'
            }),

        }
