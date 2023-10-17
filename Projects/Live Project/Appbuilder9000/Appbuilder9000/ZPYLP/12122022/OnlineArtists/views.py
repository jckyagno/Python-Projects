from django.shortcuts import render, redirect, get_object_or_404
from .models import onlineartists_add
from .forms import OnlineArtistsForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
import json

# Create your views here.
#story1
def onlineartists_home(request):
    return render(request, 'OnlineArtists/OnlineArtists_home.html')

#story2
def onlineartists_create(request):
    form = OnlineArtistsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../all')
    content = {'form': form}
    return render(request, 'OnlineArtists/OnlineArtists_add.html', content)

#story3
def onlineartists_all(request):
    onlineartists = onlineartists_add.objects.all()
    content = {'onlineartists': onlineartists}
    return render(request,'OnlineArtists/OnlineArtist_all.html', content)

#story4

def onlineartists_details(request,pk):
    onlineartist = get_object_or_404(onlineartists_add, pk=pk)
    content = {'onlineartist': onlineartist}
    return render(request, 'OnlineArtists/OnlineArtists_details.html', content)

#story5

def onlineartists_edit(request, pk):
    onlineartist = get_object_or_404(onlineartists_add, pk=pk)
    if request.method == 'POST':
        form = OnlineArtistsForm(request.POST, instance=onlineartist)
        if form.is_valid():
            onlineartist = form.save(commit=False)
            onlineartist.save()
            return render(request, 'OnlineArtists/OnlineArtists_details.html', {'onlineartist': onlineartist})
    else:
        form = OnlineArtistsForm(instance=onlineartist)
    primary_key = onlineartists_add.objects.get(pk=pk)
    return render(request, 'OnlineArtists/OnlineArtists_edit.html', {'form': form, 'primary_key': primary_key})


def onlineartists_delete(request, pk):
    onlineartist = onlineartists_add.objects.get(pk=pk)
    onlineartist.delete()
    return HttpResponseRedirect(reverse('onlineartists_all'))


#story6 api

def onlineartists_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "fontana,ca", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "031795bf9bmshd274d4c12cf68e3p11485cjsne17f1116f764"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'OnlineArtists/OnlineArtists_api.html', content)






