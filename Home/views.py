from django.shortcuts import render

# Create your views here.

def Home(request):
   #return HttpResponse('This is the home page.')
    return render(request, 'Home.html', {} )