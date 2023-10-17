from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import PlayerModel
from bs4 import BeautifulSoup
import requests

def sportstats_home(request):
    return render(request, 'SportStats/sportstats_home.html')

def sportstats_create(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    content = {'form': form}
    return render(request, 'SportStats/sportstats_create.html', content)



def sportstats_displayall(request):
    entry = PlayerModel.PlayerModels.all()
    content = {'entry': entry}
    return render(request, 'SportStats/sportstats_displayall.html', content)


def sportstats_details(request, pk):
    entry = get_object_or_404(PlayerModel, pk=pk)
    content = {'entry': entry}
    return render(request, 'SportStats/sportstats_details.html', content)



def sportstats_edit(request, pk):
    entry = get_object_or_404(PlayerModel, pk=pk)
    form = PlayerForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sportstats_displayall')
    content = {'form': form, 'entry': entry}
    return render(request, 'SportStats/sportstats_edit.html', content)

def sportstats_delete(request, pk):
    entry = get_object_or_404(PlayerModel, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('sportstats_displayall')
    content = {'entry': entry}
    return render(request, 'SportStats/sportstats_delete.html', content)

def sportstats_soup(request):
    page = requests.get("https://www.thoughtco.com/know-your-favorite-basketball-players-2832291")
    soup = BeautifulSoup(page.content, 'html.parser')
    mvp = soup.find_all('h2')[7].get_text()
    player_quote = soup.find_all('blockquote')[0].get_text()
    content = {"mvp": mvp, "player_quote": player_quote}
    return render(request, 'SportStats/sportstats_soup.html', content)
