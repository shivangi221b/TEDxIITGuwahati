# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
from django.urls import path
from . import views
urlpatterns = [
    path('', views.about_us_home, name='about_us_home'),
]