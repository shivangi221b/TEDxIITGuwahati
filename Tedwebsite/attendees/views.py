from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import AttendeeModelForm


def addAttendee(request):
    if request.method == 'POST':
        form = AttendeeModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = AttendeeModelForm()
    return render(request, 'attendees/form.html', {'form': form})
