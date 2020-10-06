from django.shortcuts import render


def about_us_home(request):
    return render(request, 'about_us/about_us.html')
