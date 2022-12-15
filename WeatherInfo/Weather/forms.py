from django.forms import ModelForm, TextInput
from Preferences.models import Preference

class CityForm(ModelForm):
    class Meta:
        model = Preference
        fields = ['city_name']
        widgets = {
            'city_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }