from django.urls import path
from . import views

urlpatterns = [
    path('Cars', views.Cars, name='Cars'),
    path('ExploreCars', views.ExploreCars, name='ExploreCars'),
    path('Car/<int:id>', views.Car_Detail_View, name='Car_Detail_View'),
    
]
