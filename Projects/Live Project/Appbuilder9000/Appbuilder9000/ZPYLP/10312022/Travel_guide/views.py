from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination, WeatherMoment
from .forms import DestinationForm, WeatherMomentForm
import requests
import json
from bs4 import BeautifulSoup


def travel_home(request):
    return render(request, 'Travel_home.html')


def travel_create(request):
    form = DestinationForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Travel_read')
    else:
        print(form.errors)
        form = DestinationForm()
    context = {
        'form': form,
    }
    return render(request, "Travel_create.html", context)


def travel_read(request):
    d = Destination.objects.all()
    return render(request, 'Travel_read.html', {'Destination': d})


def travel_details(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    content = {'entry': entry}
    return render(request, 'Travel_details.html', content)


def travel_edit(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    form = DestinationForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Travel_read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Travel_edit.html', content)


def travel_delete(request, pk):
    entry = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('Travel_read')
    content = {'entry': entry}
    return render(request, 'Travel_delete.html', content)


def travel_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "Sacramento", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "aa3d3af1d8mshe07b323c70b5c20p174de6jsn68e2b0bf2a3b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'Travel_API.html', content)


def travel_bs(request):
    page = requests.get("https://gretastravels.com/20-best-travel-quotes/")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[8].get_text()
    content = {"info": info}
    return render(request, 'Travel_BS.html', content)


def travel_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'Travel_save_api.html', content)
