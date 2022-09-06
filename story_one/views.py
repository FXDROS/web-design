from django.shortcuts import render
from .models import Schedule, Events, EventsParticipants
from .forms import Schedule_Form, Events_Form, Applicants_Form
from django.http import HttpResponseRedirect, JsonResponse
import json
import requests


def home_view(request):
	return render(request, "profile.html")

def profile(request):
	return render(request, "profile.html")

def gallery(request):
	return render(request, "gallery.html")

def schedule(request):
	schedules = Schedule.objects.all()
	form = Schedule_Form(request.POST or None)
	content = {
		'form' : form,
		'schedules' : schedules
	}
	if (form.is_valid and request.method == 'POST'):
		form.save()
		form.cleaned_data['subject']
		return HttpResponseRedirect(request.path_info, content)
	return render(request, "schedule.html", content)

def detail(request, id_=None):
	try:
		subDesc = Schedule.objects.get(id = id_)
		context = {'subDesc' : subDesc}
		return render(request, 'subjectDetail.html', context)
	except Exception:
		return HttpResponseRedirect('/schedule')

def delete(request, id_=None):
	content = Schedule.objects.filter(id = id_)
	content.delete()
	return HttpResponseRedirect('/schedule')

def events(request):
	events = Events.objects.all()
	applicants = EventsParticipants.objects.all()
	form = Events_Form(request.POST or None)
	content = {
		'form' : form,
		'events' : events,
		'applicants' : applicants
	}
	if (request.method == 'POST'):
		form = Events_Form(request.POST)
		if form.is_valid() :
			form.save()
			form.cleaned_data['event']
		return HttpResponseRedirect(request.path_info, content)
	return render(request, "events.html", content)

def apply (request, id_):
	if (request.method == 'POST'):
		form = Applicants_Form(request.POST)
		# print("post")
		if form.is_valid():
			# print("valid")
			form = EventsParticipants(eventName = Events.objects.get(id = id_), name = form.data['name'], email= form.data['email'])
			form.save()
		return HttpResponseRedirect('/events/')
	else :
		form = Applicants_Form()
		# print("get")
		applyEve = Events.objects.get(id = id_)
		context = {
			'form' : form,
			'applyEve' : applyEve
		}	
	return render(request, "applyEvent.html", context)

def books(request): 
	return render(request, "searchBook.html")

def books_data(request):
	url = "https://www.googleapis.com/books/v1/volumes?q=" + request.GET['q']
	ret = requests.get(url)
	data = 	json.loads(ret.content)
	return JsonResponse(data, safe=False)