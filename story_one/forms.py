from django import forms
from .models import Schedule, Events, EventsParticipants
from django.forms import ModelForm

class Schedule_Form(forms.ModelForm):
    class Meta:
	    model = Schedule
	    fields = '__all__'
	    error_messages = {
		    'required' : 'Please Type'
	    }

class Events_Form(forms.ModelForm):
	class Meta:
		model = Events
		fields = '__all__'
		error_messages = {
			'required' : 'Please Type'
		}

class Applicants_Form(forms.ModelForm):
	class Meta:
		model = EventsParticipants
		fields = ['name','email']
		error_messages = {
			'required' : 'Please Type'
		}
