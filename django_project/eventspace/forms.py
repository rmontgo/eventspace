from django import forms
from django.forms import ModelForm
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['host']
        widgets = {
            "date": DateInput(),
            "start": TimeInput(),
            "end": TimeInput(),
        }