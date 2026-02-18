from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import CarsDb,BrandDb


# Create your views here.

def Cars(request):
   Cars = CarsDb.objects.all()
   
   data = {'Cars': Cars}
   
   return render(request, 'Cars.html', data )

def ExploreCars(request):
   All_Cars = CarsDb.objects.all()
   selected_brand_id = request.GET.get('selectC')
   if request.method == 'GET':
      if selected_brand_id is not None:
         All_Cars = CarsDb.objects.filter(category=selected_brand_id)


   data = {'All_Cars': All_Cars, 'selected_brand_id':selected_brand_id}
   
   return render(request,'ExploreCars.html',data)


def Car_Detail_View(request, id):
    # 1. Look for the car with that specific ID
    # 2. If it doesn't exist, show a 404 error page
    Car_instance = get_object_or_404(CarsDb,id=id)

    data = {'Car': Car_instance,}
    # 3. Send that specific car data to a new template
    return render(request, 'Car_Detail_Page.html', data)