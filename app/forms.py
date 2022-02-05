from django.forms import ModelForm
from app.models import Tratamentos


# Create the form class.
class TratametosForm(ModelForm):
    class Meta:
        model = Tratamentos
        fields = ['paciente', 'medicamento', 'duracao']