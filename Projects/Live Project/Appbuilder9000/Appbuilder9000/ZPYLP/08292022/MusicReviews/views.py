from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddMusicForm
from .models import AddMusic
#from .models import AddMusic Favorite_Music
#from rest_framework.response import Response
#from rest_framework.decorators import api_view
import requests
from django.contrib import messages


# render home page
def MusicReviews_home(request):
    return render(request, 'MusicReviews/MusicReviews_home.html')


# function to render built in form from my model AddMusic
def MusicReviews_AddMusic(request):
    form = AddMusicForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'MusicReviews/MusicReviews_AddMusic.html', content)


# function to fetch all objects created from form and render
def MusicReviews_reviews(request):
    music_entries = AddMusic.objects.all()
    content = {'music_entries': music_entries}
    return render(request, 'MusicReviews/MusicReviews_reviews.html', content)


# function to get all attributes of object and render on details page
def MusicReviews_details(request, pk):
    details = get_object_or_404(AddMusic, pk=pk)
    context = {'details': details}
    return render(request, 'MusicReviews/music_details.html', context)


# function to delete AddMusic object
def music_delete(request, pk):
    delete_music = AddMusic.objects.get(pk=pk)
    if request.method == 'POST':
        delete_music.delete()
        return redirect('MusicReviews_reviews')
    return render(request, 'MusicReviews/MusicReviews_delete.html')


# function to update AddMusic form, instance argument fills fields with selected element.
def music_update(request, pk):
    update_music = AddMusic.objects.get(pk=pk)
    form = AddMusicForm(request.POST or None, instance=update_music)
    if form.is_valid():
        form.save()
        return redirect('MusicReviews_reviews')
    return render(request, 'MusicReviews/MusicReviews_update.html',
                  {'update_music': update_music,
                   'form': form})

#def view_fav_music(request):
#    added_favorites = FavoriteMusic.Favorite_Music.all()
 #   context = {'added_favorites': added_favorites}
   # return render(request, 'MusicReviews/MusicReviews_viewfav.html', context)


# Create your views here.
