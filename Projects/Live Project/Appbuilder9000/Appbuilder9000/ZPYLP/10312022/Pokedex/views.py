from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateUserForm, AddPokemonForm, TrainerProfileForm
from .models import CreateUser, AddPokemon



# Render Pokedex home page
def Pokedex_home(request):
    form = AddPokemonForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['create_user.pk']
        return render(request, pk)
    content = {'form': form}
    return render(request, 'Pokedex/Pokedex_home.html', content)


#This function will render the Create Trainer Page when requested
def create_user(request):
    form = CreateUserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid(): #checks if the form from forms.py is valid
            form.save() #saves the form
            return redirect('Pokedex_home') #and returns user to the home page
    content = {'form': form}
    return render(request, 'Pokedex/create_user.html', content)


def add_pkmn(request):
    form = AddPokemonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():  # checks if the form from forms.py is valid
            form.save()  # saves the form
            return redirect('Pokedex_home')  # and returns user to the home page
    content = {'form': form}
    return render(request, 'Pokedex/add_pkmn.html', content)

def view_pkmn(request):
    pokemon = AddPokemon.Pokemon.all()
    return render(request, 'Pokedex/view_pkmn.html', {'pokemon': pokemon})


def Pokedex_details(request, pk):
    selected_pokemon = get_object_or_404(AddPokemon, pk=pk)
    content = {'selected_pokemon': selected_pokemon}
    #show_detail = pkmn_detail.pkmn_name.get()
    return render(request, 'Pokedex/details.html', content)



def view_profile(request):
    if request.method == 'POST':
        form = TrainerProfileForm(request.POST)
        if form.is_valid():
            return redirect('add_pkmn')
        else:
            form = TrainerProfileForm()

    return render(request, 'Pokedex/view_profile.html')
