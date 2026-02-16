from django.shortcuts import render

# Create your views here.

def Cars(request):
   Cars = Car.objects.all()
   
   data = {'Cars': Cars}
   
   return render(request, 'AllMenus/Cars.html', data )