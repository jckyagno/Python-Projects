from django.shortcuts import render, redirect, get_object_or_404
from .models import Itinerary
from .forms import EntryForm
import requests
import json


# Renders the home page
def SLCRestaurantGuide_home(request):
    return render(request, 'SLCRestaurantGuide/SLCRestaurantGuide_home.html')


# Story #2: Create the model
def SLCRestaurantGuide_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("../SLCRestaurantGuide_view")
    content = {'form': form}
    return render(request, 'SLCRestaurantGuide/SLCRestaurantGuide_create.html', content)


def SLCRestaurantGuide_view(request):
    entry = Itinerary.objects.all()
    content = {'entry': entry}
    return render(request, "SLCRestaurantGuide/SLCRestaurantGuide_view.html", content)


def SLCRestaurantGuide_details(request, pk):
    entry = get_object_or_404(Itinerary, pk=pk)
    content = {'entry': entry}
    return render(request, "SLCRestaurantGuide/SLCRestaurantGuide_details.html", content)


def SLCRestaurantGuide_update(request, pk):
    entry = get_object_or_404(Itinerary, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('SLCRestaurantGuide_view')
    content = {'form': form, 'entry': entry}
    return render(request, 'SLCRestaurantGuide/SLCRestaurantGuide_update.html', content)


def SLCRestaurantGuide_delete(request, pk):
    entry = get_object_or_404(Itinerary, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('SLCRestaurantGuide_view')
    content = {'entry': entry}
    return render(request, 'SLCRestaurantGuide/SLCRestaurantGuide_delete.html', content)


def SLCRestaurantGuide_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "saltlakecity", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "2525f28a94msh11c9bf6281f226ap14d2f7jsndbe722a868b6",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'SLCRestaurantGuide/SLCRestaurantGuide_api.html', content)
