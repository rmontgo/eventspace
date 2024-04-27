from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('events/', views.EventListView.as_view(), name='event-list'),
        path('events/<int:pk>', views.EventDetailView.as_view(), name="event-detail"),
        path('events/create', views.createEvent, name='create-event'),
        path('events/<int:id>/update', views.updateEvent, name="update-event"),
        path('events/<int:id>/delete', views.deleteEvent, name='delete-event'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('accounts/register/', views.registerPage, name = 'register_page'),
        path('user/', views.userPage, name='user_page'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)