from django.urls import path
from . import views
urlpatterns = [
    path('', views.speakers_home, name='speakers_home'),
    path('speaker1', views.speakers_home, name='speakers_home'),
    # path('add_speaker', views.addSpeaker),
]