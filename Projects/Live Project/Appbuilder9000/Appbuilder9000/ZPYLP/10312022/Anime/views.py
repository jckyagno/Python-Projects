from django.shortcuts import render, redirect, get_object_or_404
from .models import Ani
from .forms import AniForm
import requests

# Story #1: Build the basic app -----------------------------------------------------
def anime_home(request):
    return render(request, 'Anime/anime_home.html')


# Story #2: Create your model ------------------------------------------------------
def create_anime(request):
    form = AniForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'Anime/create_anime.html', context)


# Story #3: Display all items from database --------------------------------------------
def anime_archive(request):
    anime = Ani.animes.all()
    content = {'anime': anime}
    return render(request, 'Anime/anime_archive.html', content)


# Story #4: Details page ----------------------------------------------------------
def anime_details(request, pk):
    pk = int(pk)
    anime = get_object_or_404(Ani, pk=pk)
    content = {'anime': anime}
    return render(request, 'Anime/anime_details.html', content)


# Story #5: Edit and Delete Functions -------------------------------------------------
def anime_update(request, pk):
    pk = int(pk)
    anime = get_object_or_404(Ani, pk=pk)
    form = AniForm(data=request.POST or None, instance=anime)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('../details')
    content = {'form': form, 'anime': anime}
    return render(request, 'Anime/anime_update.html', content)


def anime_delete(request, pk):
    pk = int(pk)
    anime = get_object_or_404(Ani, pk=pk)
    if request.method == 'POST':
        anime.delete()
        return redirect('anime_archive')
    content = {'anime': anime}
    return render(request, 'Anime/anime_delete.html', content)









