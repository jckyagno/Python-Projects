from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CharacterForm, CommentForm, QuoteForm
from .models import Character, Comment, Quote
from django.http import HttpResponseRedirect
import requests
import json


# Create your views here.

# Story #1: Build the basic app

def marvel_home(request):
    return render(request, "Marvel/marvel_home.html", )


# Story #2: Create your model

def marvel_create(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvel_roster')
    content = {'form': form}
    return render(request, 'Marvel/marvel_create.html', content)


# Story #3: Display all items from the database

def marvel_roster(request):
    character = Character.Characters.all()
    content = {'character': character}
    return render(request, 'Marvel/marvel_roster.html', content)


# Story #4: Details page

def marvel_details(request, pk):
    character = get_object_or_404(Character, pk=pk)
    form = CommentForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.character_id = pk
            form.save()
            return redirect('../details')
    content = {'character': character, 'form': form}
    return render(request, 'Marvel/marvel_details.html', content)


# Story #5: Edit and Delete Functions

def marvel_update(request, pk):
    character = get_object_or_404(Character, pk=pk)
    form = CharacterForm(data=request.POST or None, instance=character)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('marvel_roster')
    content = {'form': form, 'character': character}
    return render(request, 'Marvel/marvel_update.html', content)


def marvel_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'POST':
        character.delete()
        return redirect('marvel_roster')
    content = {'character': character}
    return render(request, 'Marvel/marvel_delete.html', content)


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    path = '../../../' + str(comment.character_id) + '/details'
    return redirect(path)


# Story 6/7: API

def marvel_api(request):
    url = "https://marvel-quote-api.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Host": "marvel-quote-api.p.rapidapi.com",
        "X-RapidAPI-Key": "bca2057807mshfe7effe0d91b0fap1b9154jsnceb9849a546b"
    }

    response = requests.request("GET", url, headers=headers, )

    api_info = json.loads(response.text)
    quote = api_info["Quote"]
    speaker = api_info["Speaker"]
    combo = quote + '       :  ' + speaker
    content = {"quote": quote, "speaker": speaker, "combo": combo}
    return render(request, 'Marvel/marvel_api.html', content)


# Story 6/7: Setup Beautiful Soup

def marvel_bs(request):
    page = requests.get("https://www.qualitycomix.com/learn/marvel-characters-list")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[2].get_text()
    content = {"info": info}
    return render(request, 'Marvel/marvel_bs.html', content)


# Story 9: Save API or scraped results

def marvel_api_saved(request, combo):
    if combo != 'title':
        savedapi = Quote(
            quote=combo,
        )
        # adds api data to database
        savedapi.save()
    quote = Quote.Quotes.all()
    content = {'quote': quote, }
    return render(request, 'Marvel/marvel_save_api.html', content)


# Story 10: Final touches
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        characters = Character.Characters.filter(name__contains=searched)
        quotes = Quote.Quotes.filter(quote__contains=searched)
        return render(request, 'Marvel/search.html', {'searched': searched, 'characters': characters, 'quotes': quotes})
    else:
        return render(request, 'Marvel/search.html')
