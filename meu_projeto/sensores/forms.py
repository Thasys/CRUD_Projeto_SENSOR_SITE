from django import forms
from .models import Sensor, Leitura

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['nome', 'descricao']

class LeituraForm(forms.ModelForm):
    class Meta:
        model = Leitura
        fields = ['temperatura', 'umidade']

