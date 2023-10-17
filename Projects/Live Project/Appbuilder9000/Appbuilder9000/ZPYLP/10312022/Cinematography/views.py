from django.http import HttpResponse
from .forms import cameraForm
from .models import FieldOfView
from django.shortcuts import render, redirect, get_object_or_404
import requests


def camIndex(request):
    form = cameraForm(data=request.POST or None)
    # Grabbing API of sunset and sunrise times
    theTime = requests.get('https://api.sunrise-sunset.org/json')
    # Applying the API json script to a variable
    goldenHour = theTime.json()
    # Using two keys as the sunrise and sunset keys are within a 'results' dictionary key
    goldenMorning = goldenHour['results']['sunrise']
    goldenNight = goldenHour['results']['sunset']
    if request.method == 'POST':
        return addCamera(request)
    # Applying API variables into the content variable as only one key can be applied to the return,
    # srtime and sstime parameters can't be applied after the content variable inside of "render",
    # so they must go inside "content".
    content = {'form': form, "srtime": goldenMorning, "sstime": goldenNight}
    return render(request, "Camera_home.html", content)


def addCamera(request):
    form = cameraForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Camera_home')
    content = {'form': form}
    return render(request, "Camera_home.html", content)


def camList(request):
    pullCam = FieldOfView.Camera.all()
    content = {'pullCam': pullCam}
    return render(request, "Camera_database.html", content)


def camDeets(request, pk):
    theDeets = get_object_or_404(FieldOfView, pk=pk)
    content = {'theDeets': theDeets}
    return render(request, 'Camera_details.html', content)


def camEdit(request, pk, deleted):
    theDeets = get_object_or_404(FieldOfView, pk=pk)
    form = cameraForm(data=request.POST or None, instance=theDeets)
    if deleted == False:
        if request.method == 'POST':
            if form.is_valid():
                formB = form.save(commit=False)
                formB.save()
                return redirect('Camera_database')
            else:
                print(form.errors)
        else:
            content = {'theDeets': theDeets, 'form': form}
            return render(request, 'Camera_modify.html', content)
    else:
        camDelete(request, pk)


def camDelete(request, pk):
    theDeets = get_object_or_404(FieldOfView, pk=pk)
    if request.method == 'POST':
        theDeets.delete()
        return redirect('Camera_database')
    content = {'theDeets': theDeets}
    return render(request, 'Camera_modify.html', content)


def navbar(request):
    return render(request, "Cinematography/tasteseeker_navbar.html")


def colors(request):
    return render(request, "Cinematography/colors.html")


def comp(request):
    return render(request, "Cinematography/comp.html")
