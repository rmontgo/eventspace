from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('events/', views.EventListView.as_view(), name='event-list'),
        path('events/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
        path('events/create', views.createEvent, name='create-event'),
        path('events/<int:id>/update', views.updateEvent, name="update-event"),
        path('events/<int:id>/delete', views.deleteEvent, name='delete-event'),
]