from django.shortcuts import render, redirect, get_object_or_404
from .models import Sitcom, WeatherMoment
from .forms import SitcomForm
import requests
import json


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def sitcoms_home(request):
    return render(request, 'Sitcoms/sitcoms_home.html')

# Story #2: Create your model ------------------------------------------------------------------------------------------


def sitcom_create(request):
    form = SitcomForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Sitcoms/sitcoms_create.html', content)

# Story #3: Display all items from database ----------------------------------------------------------------------------


def sitcom_read(request):
    sitcom = Sitcom.Sitcoms.all()
    content = {'sitcom': sitcom}
    return render(request, 'Sitcoms/sitcoms_read.html', content)

# Story #4: Details page -----------------------------------------------------------------------------------------------


def sitcom_details(request, pk):
    sitcom = get_object_or_404(Sitcom, pk=pk)
    content = {'sitcom': sitcom}
    return render(request, 'Sitcoms/sitcoms_details.html', content)

# Story #5: Edit and Delete Functions ----------------------------------------------------------------------------------


def sitcom_update(request, pk):
    sitcom = get_object_or_404(Sitcom, pk=pk)
    form = SitcomForm(data=request.POST or None, instance=sitcom)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'sitcom': sitcom}
    return render(request, 'Sitcoms/sitcoms_update.html', content)


def sitcom_delete(request, pk):
    sitcom = get_object_or_404(Sitcom, pk=pk)
    if request.method == 'POST':
        sitcom.delete()
        return redirect('../../read')
    content = {'sitcom': sitcom}
    return render(request, 'Sitcoms/sitcoms_delete.html', content)


# Story #6-(API Pt 1): Connect to API ----------------------------------------------------------------------------------
# Story #7-(API Pt 2): Parse through JSON

def sitcom_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "longview,wa", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "1ba8d27b19mshd71557ea88643ebp14a569jsnc81e62fac8f7",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'Sitcoms/sitcoms_api.html', content)

# Story #9: Save API or scraped results --------------------------------------------------------------------------------


def sitcom_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'Sitcoms/sitcoms_save_api.html', content)
