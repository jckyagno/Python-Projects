from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm, UpdateForm
from .models import player, update
import requests

# This function will render the home page when requested

def Sports_home(request):
    form = UpdateForm(data=request.POST or None) # Retrieve Update form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['player'] # If the form is submitted, retrieve which player the user wants to view
        return scores(request, pk) # Call score function to render that player's total score
    content = {'form': form} # Pass content to the template in a dictionary
    # Adds content of the form to page
    return render(request, 'Sportsapp/Sportsapp_home.html', content)


def Sports_create(request):
    form = PlayerForm(data=request.POST or None) # Retrieve the Player form
    # Checks if requested method is POST
    if request.method == 'POST':
        if form.is_valid(): # Check to see if the submitted form is valid and if so, saves the form
            form.save() # Saves new account
            return redirect('Sports_home') # Returns user back to the home page
    content = {'form': form} # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'Sportsapp/Sports_create.html', content)

def Sports_scores(request):
    scores = player.players.all()
    content = {'scores': scores}
    return render(request, 'Sportsapp/Sports_scores.html', content)

def Sports_details(request, pk):
    pk = int(pk)
    scores = player.players.get(pk=pk)
    content = {'scores': scores}
    return render(request, 'Sportsapp/Sports_details.html', content)

def Sports_delete(request, pk):
    pk = int(pk)
    scores = get_object_or_404(player, pk=pk)
    if scores is not None:
        scores.delete()
        return redirect('Sports_scores')
    else:
        return redirect('Sports_home')

def Sports_edit(request, pk):
    pk = int(pk)
    scores = get_object_or_404(player, pk=pk)
    form = PlayerForm(data=request.POST or None, instance=scores)
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves new account
            return redirect('Sports_home')  # Returns user back to the home page
    content = {'form': form}  # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'Sportsapp/Sports_edit.html', content)

def Sports_update(request):
    form = UpdateForm(data=request.POST or None) # Retrieve the Update form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_Valid(): # Check to see if the submitted form is valid and if so, saves the form
            pk = request.POST['player'] # Retrieve which player the update was for
            form.save() # Saves the update form
            return scores(request, pk) # Renders score balance of the player's scores
        # Pass content to the template in a dictionary
    content = {'form': form}
    # Adds content of the form to page
    return render(request, 'Sportsapp/Sports_update.html', content)

def Sports_api(request):
    response = requests.get('http://api.football-data.org/v4/competitions/2021/teams', headers={'X-Auth-Token': '80d440842cc54cfa842eb6339f8a4013'})
    soccer_data = response.json()
    content = {'competitions': soccer_data}
    return render(request, 'Sportsapp/Sports_api.html', content)

"""
def Sports_update(request, pk):
    scores = get_object_or_404(Entry, pk=pk)
    form = scoreForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../detail')
    content = {'form': form, 'scores': scores}
    return render(request, 'Sportsapp/Sports_update.html', content)

def Sports_scores(request, pk):
    player = get_object_or_404(player, pk=pk) # Retrieve the requested account using its primary key
    update = Update.Update.filter(player=pk) # Retrieve all of that player's update
    current_scores = player.initial_goal # Create player total goals, starting with the initial goal
    table_contents = {}  # Create a dictionary into which transaction update information will be placed
    for u in updates: # Loop through updates and determines which is delete or update
        if u.type == 'Addscore':
            current_scores += u.score # If addscore, add scores to the initial scores
            table_contents.update({u: current_scores}) # Add updated scores and current scores to the dictionary
        else:
            current_scores -= u.score # If subtractscore, subtract the score from the balance
            table_contents.update({u: current_scores}) # Add update scores and total to the dictionary
        # Pass player, score total, and update information to the template
    content = {'player': player, 'table_content': table_contents, 'scores': current_scores}
    return render(request, 'Sportsapp/Sports_scores.html', content)
"""


