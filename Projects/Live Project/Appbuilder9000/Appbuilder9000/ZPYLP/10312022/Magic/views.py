from django.shortcuts import render, redirect,  get_object_or_404
from .models import Deck, Comment
from .forms import DeckForm, CommentForm
import requests
import json

#Story 1: Build the basic app


def magic_home(request):
    return render(request, 'Magic/magic_home.html')


#Story 2: Create a model


def magic_create(request):
    form = DeckForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../browse')
    content = {'form': form}
    return render(request, 'Magic/magic_create.html', content)

#Story 3: Display items from database


def magic_browse(request):
    deck = Deck.Deck.all()
    content = {
        'deck': deck,
    }
    return render(request, 'Magic/magic_browse.html', content)


#Story 4: Details Page


def magic_details(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    form = CommentForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment_instance = form.save(commit=False)
            comment_instance.deck_id = pk
            form.save()
            return redirect('../details')
    content = {
        'deck': deck,
        'form': form,
    }
    return render(request, 'Magic/magic_details.html', content)

#Story 5 Edit and Delete


def magic_edit(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    form = DeckForm(data=request.POST or None, instance=deck)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../browse')
    content = {'form': form, 'deck': deck}
    return render(request, 'Magic/magic_edit.html', content)


def magic_delete(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect('../../browse')
    content = {'deck': deck}
    return render(request, 'Magic/magic_delete.html', content)

#Delete comments


def delete_c(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    path = '../../../' + str(comment.deck_id) + '/details'
    return redirect(path)

#Story 6 Connect to API
'''I am connecting to the Scryfall API. I am pulling the information for the card named 'Shock'. 
Then I am getting the value for the name key.
 I am using 'fuzzy' in my call because it allows for the api to find the card with the closest 
 spelling instead of needing to spell the card name exactly right'''

def magic_api(request):

    card_name = "shock"

    url = "https://api.scryfall.com/cards/named?fuzzy=" + card_name

    response = requests.request("GET", url)
    card_info = json.loads(response.text)
    name = card_info['name']
    content = {
        'name': name
    }
    print(content)
    return render(request, 'Magic/magic_api.html', content)

