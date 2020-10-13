from django.urls import path
from . import views
urlpatterns = [
    path('', views.speakers_home, name='speakers_home'),
    path('speaker1', views.speakers_home, name='speakers_home'),
    path('/speaker21', views.speakerDesc, name = 'speaker_description'),
    path('/speaker22', views.speakerDesc, name = 'speaker_description'),
    path('/speaker23', views.speakerDesc, name = 'speaker_description'),
    path('/speaker24', views.speakerDesc, name = 'speaker_description'),
    path('/speaker25', views.speakerDesc, name = 'speaker_description'),
    path('/speaker26', views.speakerDesc, name = 'speaker_description'),
    path('/speaker27', views.speakerDesc, name = 'speaker_description'),
    path('/speaker11', views.speakerDesc, name = 'speaker_description'),
    path('/speaker12', views.speakerDesc, name = 'speaker_description'),
    path('/speaker13', views.speakerDesc, name = 'speaker_description'),
    path('/speaker14', views.speakerDesc, name = 'speaker_description'),
    path('/speaker15', views.speakerDesc, name = 'speaker_description'),
    path('/speaker16', views.speakerDesc, name = 'speaker_description')
    

    # path('add_speaker', views.addSpeaker),
]