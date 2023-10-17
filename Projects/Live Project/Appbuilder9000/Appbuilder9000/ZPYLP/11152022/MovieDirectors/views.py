from django.shortcuts import render, redirect, get_object_or_404
import requests
import random
from bs4 import BeautifulSoup

from .models import Director
from .forms import DirectorForm


# Render the home page
def directors_home(request):
    return render(request, 'MovieDirectors/directors_home.html')


# Render page with form to add records to the database
def directors_add(request):
    form = DirectorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('directors_view')
    else:
        print(form.errors)
        form = DirectorForm()
    context = {
        'form': form,
    }
    return render(request, 'MovieDirectors/directors_add.html', context)


# Render page with a list of all entered directors
def directors_view(request):
    directors = Director.objects.all()
    return render(request, 'MovieDirectors/directors_view.html', {'directors': directors})


# Render a page with details about a specific director when selected from the list
def directors_details(request, pk):
    pk = int(pk)
    director = get_object_or_404(Director, pk=pk)
    context = {
        'director': director,
    }
    return render(request, 'MovieDirectors/directors_details.html', context)


# Render a page that allows the user to edit an existing record
def directors_edit(request, pk):
    pk = int(pk)
    director = get_object_or_404(Director, pk=pk)
    form = DirectorForm(data=request.POST or None, instance=director)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('directors_view')
    context = {
        'form': form,
        'director': director,
    }
    return render(request, 'MovieDirectors/directors_edit.html', context)


# Delete selected record from the database
def directors_delete(request, pk):
    pk = int(pk)
    director = get_object_or_404(Director, pk=pk)
    director.delete()
    return redirect('directors_view')


# Render a page that contains info obtained through an API
def directors_api(request):
    # A free Bob's Burgers API, I am getting a random burger of the day of the 333 available
    num = random.randrange(1, 333)
    response = requests.get('https://bobsburgers-api.herokuapp.com/burgerOfTheDay/{}'.format(num))
    context = response.json()
    return render(request, 'MovieDirectors/directors_api.html', context)


# Render a page to display data scraped by Beautiful Soup
def directors_beautifulsoup(request):
    # Scrape and print the first paragraph from the wikipedia page on web scraping
    page = requests.get('https://en.wikipedia.org/wiki/Web_scraping')
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[2]
    body = list(html.children)[3]
    div1 = list(body.children)[4]
    div2 = list(div1.children)[9]
    div3 = list(div2.children)[13]
    div4 = list(div3.children)[0]
    p = list(div4.children)[8].get_text()
    context = {
        'p': p,
    }
    return render(request, 'MovieDirectors/directors_beautifulsoup.html', context)
