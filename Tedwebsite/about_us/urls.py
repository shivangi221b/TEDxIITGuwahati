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
    path('/Jaikishan_Mansukhani', views.memberDesc1, name='member_description1'),
    path('/Anvita_Kodru', views.memberDesc2, name='member_description2'),
    path('/Sreesiddesh_Bhavanasi', views.memberDesc3, name='member_description3'),
    path('/Shivangi_Kumar', views.memberDesc4, name='member_description4'),
    path('/Vishwaprasanna_Hariharan', views.memberDesc5, name='member_description5'),
    path('/Samarth_Saraswat', views.memberDesc6, name='member_description6'),
    path('/Aarya_Shrivastava', views.memberDesc7, name='member_description7'),
    path('/Amey_Varhade', views.memberDesc8, name='member_description8'),
    path('/Anindya_Rajan', views.memberDesc9, name='member_description9'),
    path('/Anisha_Khati', views.memberDesc10, name='member_description10'),
    path('/Ankit_Raj', views.memberDesc11, name='member_description11'),
    path('/Anushka_Anand', views.memberDesc12, name='member_description12'),
    path('/Anushka_Srivastava', views.memberDesc13, name='member_description13'),
    path('/Arpita_Mohapatra', views.memberDesc14, name='member_description14'),
    path('/Ayush_Srivastava', views.memberDesc15, name='member_description15'),
    path('/Digisha_Verma', views.memberDesc16, name='member_description16'),
    path('/Emily_Huiling', views.memberDesc17, name='member_description17'),
    path('/Gourav_Kumar', views.memberDesc18, name='member_description18'),
    path('/Govind_Singh', views.memberDesc19, name='member_description19'),
    path('/Jaideep_Buksagarmath', views.memberDesc20, name='member_description20'),
    path('/Janhavi_Lande', views.memberDesc21, name='member_description21'),
    path('/Lalika_Laya_K', views.memberDesc22, name='member_description22'),
    path('/Miloni_Patel', views.memberDesc23, name='member_description23'),
    path('/Monalisha_Majumder', views.memberDesc24, name='member_description24'),
    path('/Niladri_Sarkar', views.memberDesc25, name='member_description25'),
    path('/Nishant', views.memberDesc26, name='member_description26'),
    path('/Nishtha_Sharma', views.memberDesc27, name='member_description27'),
    path('/Pragnya_Ramjee', views.memberDesc28, name='member_description28'),
    path('/Pratyanshu_Raj_Singh', views.memberDesc29, name='member_description29'),
    path('/Ritik_Singh', views.memberDesc30, name='member_description30'),
    path('/Sai_Sreyas_Ray', views.memberDesc31, name='member_description31'),
    path('/Shatakshi_Kaushal', views.memberDesc32, name='member_description32'),
    path('/Shiva_Sah', views.memberDesc33, name='member_description33'),
    path('/Sudarshan_Birla', views.memberDesc34, name='member_description34'),
    path('/Titiksha', views.memberDesc35, name='member_description35'),
]