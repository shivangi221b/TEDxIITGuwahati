from django.shortcuts import render
from django.utils import timezone
from datetime import datetime


def index(request):
    now = timezone.now()
    date1 = datetime.now()
    date2 = datetime(2021, 2, 10, 12, 30,
                     0)  # setting to 10th feb 2021 , 6:00pm, decreased by 5:30 hrs to offset timezone
    diff = date2 - date1
    print(date1)
    print(date2)
    print(diff)
    duration_in_sec = diff.total_seconds()
    days = divmod(duration_in_sec, 86400)  # Get days (without [0]!)
    hours = divmod(days[1], 3600)  # Use remainder of days to calc hours
    minutes = divmod(hours[1], 60)  # Use remainder of hours to calc minutes
    seconds = divmod(minutes[1], 1)  # Use remainder of minutes to calc seconds
    print(diff)
    days = int(days[0])
    hours = int(hours[0])
    minutes = int(minutes[0])
    seconds = int(seconds[0])
    print(days)
    print(hours)
    print(minutes)
    print(seconds)
    context = {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, }
    return render(request, 'home/index.html', context)
