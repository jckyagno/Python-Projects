from django.shortcuts import render, redirect, get_object_or_404
from .models import Crew, WeatherMoment
from .forms import EntryForm, WeatherMomentForm
import requests
import json
from bs4 import BeautifulSoup
import datetime


# Creates function to render home page
def rowing_home(request):
    return render(request, 'Rowing/Rowing_home.html')

# creates function to render create page
def rowing_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../rowing_read')
    content = {'form': form}
    return render(request, 'Rowing/Rowing_create.html', content)

def rowing_read(request):
    entry = Crew.Entry.all()
    content = {'entry': entry}
    return render(request, 'Rowing/Rowing_read.html', content)

def rowing_details(request, pk):
    entry = get_object_or_404(Crew, pk=pk)
    content = {'entry': entry}
    return render(request, 'Rowing/Rowing_details.html', content)

def rowing_update(request, pk):
    entry = get_object_or_404(Crew, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../rowing_read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Rowing/Rowing_update.html', content)

def rowing_delete(request, pk):
    entry = get_object_or_404(Crew, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../rowing_read')
    content = {'entry': entry}
    return render(request, 'Rowing/Rowing_delete.html', content)

def rowing_bs(request):
    page = requests.get("https://www.britannica.com/topic/rowing-boat-propulsion-and-sport")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[6].get_text()
    content = {"info": info}
    return render(request, 'Rowing/Rowing_bs.html', content)

def rowing_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "portland", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "aa3d3af1d8mshe07b323c70b5c20p174de6jsn68e2b0bf2a3b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'Rowing/Rowing_api.html', content)


def rowing_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'Rowing/Rowing_save_api.html', content)
