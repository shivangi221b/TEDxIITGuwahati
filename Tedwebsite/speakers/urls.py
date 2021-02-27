from django.urls import path
from . import views

urlpatterns = [
    path('', views.speakers_home, name='speakers_home'),
    path('/Alana_Golmei', views.speakerDesc1, name='speaker_description1'),
    path('/Anamika_Barua', views.speakerDesc2, name='speaker_description2'),
    path('/Arup_Kumar_Dutta', views.speakerDesc3, name='speaker_description3'),
    path('/Binita_Jain', views.speakerDesc4, name='speaker_description4'),
    path('/Milin_Dutta', views.speakerDesc5, name='speaker_description5'),
    path('/Zoma_Sailo', views.speakerDesc6, name='speaker_description6'),
    path('/Pragnya_Ramjee', views.speakerDesc7, name='speaker_description7'),

    path('/Seema_Biswas', views.speakerDesc8, name='speaker_description8'),
    path('/Uddhab_Bharali', views.speakerDesc9, name='speaker_description9'),
    path('/Sankara_Subramaniam', views.speakerDesc10, name='speaker_description10'),
    path('/Hasina_Kharbhih', views.speakerDesc11, name='speaker_description11'),
    path('/Sonjoy_Hazarika', views.speakerDesc12, name='speaker_description12'),
    path('/Ravindranath_Ravi', views.speakerDesc13, name='speaker_description13'),

    path('/Aashish_Chandratreya', views.speakerDesc14, name='speaker_description14'),
    path('/Aditya_Gupta', views.speakerDesc15, name='speaker_description15'),
    path('/Bhagvan_Kommadi', views.speakerDesc16, name='speaker_description16'),
    path('/Bidisha_Som', views.speakerDesc17, name='speaker_description17'),
    path('/Nisha_Bora', views.speakerDesc18, name='speaker_description18'),
    path('/Prabhagaran', views.speakerDesc19, name='speaker_description19'),
    path('/Rudy_Wallang', views.speakerDesc20, name='speaker_description20'),
    path('/Seema_Gupta', views.speakerDesc21, name='speaker_description21'),
    path('/Shiva_Sah', views.speakerDesc22, name='speaker_description22'),

    # path('add_speaker', views.addSpeaker),
]
