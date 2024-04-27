from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Event
from .forms import EventForm, CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# from .decorators import allowed_users
from django.contrib import messages

# Create your views here.
def index(request):
    total_events = Event.objects.all().count()
    print("Found " + str(total_events) + " events")
    return render(request, 'eventspace/index.html', {'total_events':total_events})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='event_host')
            user.groups.add(group)
            
            messages.success(request, "Account was created for " + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
def userPage(request):
    events = Event.objects.filter(host = request.user)
    print(events)
    messages.success(request, "Successfully logged in")
    return render(request, 'eventspace/user_page.html', {'events': events})
    

class EventListView(generic.ListView):
    model = Event


class EventDetailView(generic.DetailView):
    model = Event


@login_required(login_url="login")
# @allowed_users(allowed_roles=['event_host'])
def createEvent(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            print(event)
            event.host = request.user
            event.save()
            messages.success(request, "Event successfully created")
            return redirect('user_page')
    return render(request, 'eventspace/event_form.html', {'form' : form})

@login_required(login_url='login')
def updateEvent(request, id):
    event = Event.objects.get(pk=id)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            event.save()
            messages.success(request, "Event successfully updated")
            return redirect('user_page')

    return render(request, 'eventspace/event_form.html', {'form': form})

@login_required(login_url='login')
def deleteEvent(request, id):
    event = Event.objects.get(pk=id)

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event successfully deleted")
        return redirect('user_page')

    context = {'event':event}

    return render(request, 'eventspace/delete_event.html', context)