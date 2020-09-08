from django.urls import path
from . import views
urlpatterns = [
    path('', views.addAttendee, name='speakers_home'),
]