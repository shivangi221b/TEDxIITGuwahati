"""Tedwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from speakers import views as sv
from attendees import views as av

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact.html', include('home.urls')),
    path('gallery.html', include('gallery.urls')),
    path('blog.html', include('blog.urls')),
    path('about_us.html', include('about_us.urls')),
    path('speakers.html', include('speakers.urls')),
    path('nominate_speaker.html', sv.addSpeaker),
    path('add_attendee.html', av.addAttendee),
    path('nominate_yourself.html', sv.nominate_yourself),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
