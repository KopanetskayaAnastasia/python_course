from .models import Workers, Professions
from django.forms import ModelForm, TextInput


class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        fields = ['name', 'phone', 'email']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почтовый адрес'
            })
        }


class ProfessionsForm(ModelForm):
    class Meta:
        model = Professions
        fields = ['profession']

        widgets = {
            "profession": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Профессия'
            })
        }


