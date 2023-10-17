from django.shortcuts import render

# Create your views here.

def dyd_home(request):
    return render(request, 'Design_Your_Day/dyd_home.html')
