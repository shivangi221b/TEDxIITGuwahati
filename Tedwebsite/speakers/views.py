
from django.shortcuts import render
from django.utils import timezone


def speakers_home(request):

    return render(request, 'speakers/speakers.html')