from django.urls import path
from . import views

urlpatterns = [
     path('ContactUs', views.ContactUs, name='ContactUs'),
    
]
