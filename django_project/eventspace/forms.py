from django import forms
from django.forms import ModelForm
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start', 'end', 'location', 'image']
        widgets = {
            "date": DateInput(),
            "start": TimeInput(),
            "end": TimeInput(),
        }