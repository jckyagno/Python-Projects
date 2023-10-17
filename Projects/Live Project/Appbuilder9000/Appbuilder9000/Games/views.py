from django.shortcuts import render, redirect, get_object_or_404
from .forms import GamesForm
from .models import Games

def games_home(request):
    return render(request, 'Games/games_home.html')

def add_games(request):
    form = GamesForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves new account
            return redirect('games_home')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'Games/games_create.html', content)

def details_games(request):
    # Gets all the games from the database
    games = Games.Games.all()
    # Saves the games to the template as a dictionary
    content = {'games': games}
    # Adds content of games to page
    return render(request, 'Games/games_details.html', content)

def games_info(request, pk):
    pk = int(pk)
    item = get_object_or_404(Games, pk=pk)
    content = {'item': item}
    return render(request, 'Games/games_info.html', content)