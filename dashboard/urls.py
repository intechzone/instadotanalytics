from django.urls import path

from . import views

urlpatterns = [

    path('dashboard/',views.backindex),
    path('login/',views.login),
    
]