from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import SpeakerModelForm
from django.contrib import messages


def speakers_home(request):
    return render(request, 'speakers/speakers.html')


def addSpeaker(request):
    if request.method == 'POST':
        form = SpeakerModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = SpeakerModelForm()
    return render(request, 'speakers/form.html', {'form': form})


def nominate_yourself(request):
    return render(request, 'speakers/form2.html')

def speakerDesc(request):
    return render(request, 'speakers/speaker21.html')

def speakerDesc(request):
    return render(request, 'speakers/speaker22.html')
    
def speakerDesc(request):
    return render(request, 'speakers/speaker11.html')  

def speakerDesc(request):
    return render(request, 'speakers/speaker12.html')
    
def speakerDesc(request):
    return render(request, 'speakers/speaker13.html')
    
def speakerDesc(request):
    return rende(request, 'speakers/speaker14.html')
    
def speakerDesc(request):
    return render(request, 'speakers/speaker15.html')