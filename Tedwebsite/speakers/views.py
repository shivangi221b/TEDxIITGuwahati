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


