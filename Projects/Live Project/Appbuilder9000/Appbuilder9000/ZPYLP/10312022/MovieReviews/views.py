from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Movie
import requests
import json
from bs4 import BeautifulSoup
# Create your views here.


def moviereviews_Home(request):
    return render(request, 'MovieReviews/MovieReviews_home.html')


def moviereviews_add(request):
    form = MovieForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../all/')
    content = {'form': form}
    return render(request, 'MovieReviews/MovieReviews_add.html', content)


def moviereviews_all(request):
    movies = Movie.objects.all()
    return render(request, 'MovieReviews/MovieReviews_all.html', {'movies': movies})


def moviereviews_details(request, pk):
    pk = int(pk)
    details = get_object_or_404(Movie, pk=pk)
    context = {'details': details}
    return render(request, 'MovieReviews/MovieReviews_details.html', context)


def moviereviews_edit(request, pk):
    details = get_object_or_404(Movie, pk=pk)
    form = MovieForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../all/')
    context = {'form': form, 'details': details}
    return render(request, 'MovieReviews/MovieReviews_edit.html', context)


def moviereviews_delete(request, pk):
    details = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('../../all/')
    context = {'details': details}
    return render(request, 'MovieReviews/MovieReviews_delete.html', context)

# API ------------------------------------------------------------------
def moviereviews_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "sunnyvale,ca", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "031795bf9bmshd274d4c12cf68e3p11485cjsne17f1116f764"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    temp_int = api_info["current_observation"]["condition"]["temperature"]
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature, "temp_int": temp_int}
    return render(request, "MovieReviews/MovieReviews_api.html", content)


# Function for scraping a paragraph element from the Wikipedia site.
def moviereviews_bs(request):
    page = requests.get("https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[0].get_text()
    content = {"info": info}
    return render(request, "MovieReviews/MovieReviews_bs.html", content)
