from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Event
from .forms import EventForm

# Create your views here.
def index(request):
    total_events = Event.objects.all().count()
    print("Found " + str(total_events) + " events")
    return render(request, 'eventspace/index.html', {'total_events':total_events})

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event


def createEvent(request):
    form = EventForm()

    if request.method == 'POST':
        event_data = request.POST.copy()
        form = EventForm(event_data)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()

            return redirect('event-list')
        
    context = {'form': form}
    return render(request, 'eventspace/event_form.html', context)

def updateEvent(request, id):
    event = Event.objects.get(pk=id)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event-list')
    context = {'form': form}
    return render(request, 'eventspace/event_form.html', context)

def deleteEvent(request, id):
    event = Event.objects.get(pk=id)

    if request.method == 'POST':
        event.delete()
        return redirect('event-list')

    context = {'event':event}
    return render(request, 'eventspace/delete_event.html', context)