from django import forms
from apps.core.models import Sensor

class SensorInLineForm(forms.ModelForm):

    class Meta:
        model = Sensor
        fields = ["sensor"]