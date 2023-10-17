from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry, WeatherMoment
from .forms import EntryForm, WeatherMomentForm
import requests
import json
from bs4 import BeautifulSoup
import datetime


# Story #1: Build the basic App---------------------------------------------------------------------
def cl_home(request):
    return render(request, 'CampingListTracker/CampingListTracker_home.html')

# Story #2: Create your model -----------------------------------------------------------------------

def cl_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../list')
    content = {'form': form}
    return render(request, 'CampingListTracker/CampingListTracker_create.html', content)

# Story #3: Display all items from database ---------------------------------------------------------

def cl_list(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'CampingListTracker/CampingListTracker_list.html', content)

# Story #4: Display Details Page --------------------------------------------------------------------

def cl_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    content = {'entry': entry}
    return render(request, 'CampingListTracker/CampingListTracker_details.html', content)

# Story #5: Edit and Delete Function-----------------------------------------------------------------

def cl_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../list')
    content = {'form': form, 'entry': entry}
    return render(request, 'CampingListTracker/CampingListTracker_update.html', content)


def cl_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../list')
    content = {'entry': entry}
    return render(request, 'CampingListTracker/CampingListTracker_delete.html', content)


# Story #6 (API pt 1): Connect to API -------------------------------------------------------------------------
# Story #7 (API pt 2): Parse through JSON

def cl_api(request):

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "salt lake city", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "63b79f712amsh8b4ef18375a2b6cp1b42b0jsnb6af9c7dc5dc",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, 'CampingListTracker/CampingListTracker_api.html', content)


# Story #6 (BS Pt 1): Setup Beautiful Soup----------------------------------------------------------------------------------------------
# Story #7 (BS Pt 2): Parse through html

def cl_bs(request):
    page = requests.get("https://www.rei.com/blog/camp/22-camp-hacks-from-rei-experts")
    soup = BeautifulSoup(page.content, 'html.parser')
    # This is pulling the first <h4> tag of the site and the <p> index that matches that tip
    header = soup.find('h4').get_text()
    info = soup.find_all('p')[2].get_text()
    content = {"info": info, "header": header}
    return render(request, 'CampingListTracker/CampingListTracker_bs.html', content)

# Story #9: Save API or scraped results --------------------------------------------------------------------------------------------------------

def cl_save_api(request, m=1000):
    if m != 1000:
        moment = WeatherMoment(
            temperature=m
        )
        moment.save()
    moment = WeatherMoment.WeatherMoments.all()
    content = {"moment": moment}
    return render(request, 'CampingListTracker/CampingListTracker_save_api.html', content)
