from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Home,name="Home"),
    path('cars/', views.Home, name="Cars"),
    path('about/', views.Home, name="AboutUs"),
    path('contact/', views.Home, name="ContactUs"),
    path('explore/', views.Home, name="ExploreCars"),
]
#also for adding img  write by Tuhin
