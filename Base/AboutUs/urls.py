from django.urls import path
from . import views

urlpatterns = [
     path('AboutUs', views.AboutUs, name='AboutUs')
    
]
