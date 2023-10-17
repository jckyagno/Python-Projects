from django.shortcuts import render, redirect, get_object_or_404
from .models import AddEntry
from.forms import AddEntryForm
import requests
import json
from bs4 import BeautifulSoup


# displays home page
def traveljapan_home(request):
    return render(request, 'TravelJapan/TravelJapan_home.html')


# displays create page and saves the data
def traveljapan_create(request):
    form = AddEntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../places')
    content = {'form': form}
    return render(request, 'TravelJapan/TravelJapan_create.html', content)


# displays items in the database
def traveljapan_places(request):
    addEntry = AddEntry.AddEntries.all()
    content = {'addEntry': addEntry}
    return render(request, 'TravelJapan/TravelJapan_places.html', content)


# displays details of seleceted database object
def traveljapan_details(request, pk):
    addEntry = get_object_or_404(AddEntry, pk=pk)
    content = {'addEntry': addEntry}
    return render(request, 'TravelJapan/TravelJapan_details.html', content)


# update function
def traveljapan_update(request, pk):
    addEntry = get_object_or_404(AddEntry, pk=pk)
    form = AddEntryForm(data=request.POST or None, instance=addEntry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../places')
    content = {'form': form, 'addEntry': addEntry}
    return render(request, 'TravelJapan/TravelJapan_update.html', content)


# delete function
def traveljapan_delete(request, pk):
    addEntry = get_object_or_404(AddEntry, pk=pk)
    if request.method == 'POST':
        addEntry.delete()
        return redirect('../../places')
    content = {'addEntry': addEntry}
    return render(request, 'TravelJapan/TravelJapan_delete.html', content)


# connects to API
def traveljapan_api(request):
    url = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/%E8%A8%AA"

    headers = {
        "X-RapidAPI-Key": "f3f220457cmsh6cae92504a1567ep160a94jsn96f0abf6f9e3",
        "X-RapidAPI-Host": "kanjialive-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    kanji = json.loads(response.text)

# displays character and meaning from a dictionary JSON object
    character = kanji["kanji"]["character"]
    meaning = kanji["kanji"]["meaning"]["english"]

    content = {"character": character, "meaning": meaning}

    return render(request, 'TravelJapan/TravelJapan_api.html', content)


# Beautiful Soup extraction
def traveljapan_bs(request):
    site = requests.get('https://www.planetware.com/tourist-attractions/japan-jpn.htm')
    soup = BeautifulSoup(site.content, 'html.parser')
    placelist = []
    info = soup.find_all('h2', class_='sitename')
    for i in info:
        placelist += list(i)

    content = {'placelist': placelist}
    return render(request, 'TravelJapan/TravelJapan_bs.html', content)
