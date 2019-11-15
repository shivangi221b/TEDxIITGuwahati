from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

# def index(request):
#     return HttpResponse("Gallery home page")

def index(request):
	queryset = Photo.objects.all()
	context = {
		"gallery": queryset,
	}

	return render(request, 'gallery/photo.html', context)
