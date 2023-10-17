from django.shortcuts import render
from django.http import HttpResponse
from .forms import RecipeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.http import JsonResponse
import requests
import json
from bs4 import BeautifulSoup


# Render the home page
def veggie_home(request):
    return render(request, "Veggie_home.html")


# Render the form page for adding a new recipe
def create_recipe(request):
    form = RecipeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../veggie_recipe')
    context = {'form': form}
    return render(request, "Veggie/veggie_form.html", context)


# Render the page that displays all the recipes one by one
def display_veggie(request):
    all_recipe = Recipe.objects.all()
    return render(request, "Veggie/veggie_recipe.html", {'all_recipe': all_recipe})


# Render the page that display one recipe
def single_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'Veggie/veggie_details.html',  {'recipe': recipe})


# Render the page that allows you to edit / update the recipe
def veggie_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(data=request.POST or None, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../veggie_recipe')
    content = {'form': form, 'recipe': recipe}
    return render(request, 'Veggie/veggie_edit.html', content)


# Deleting a recipe from the database
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('veggie_recipe')
    return render(request, 'Veggie/veggie_delete.html', {'recipe': recipe})


# Receives an element from the API response, and sends it to the template
def recipe_api(request):
    url = "http://api.icndb.com/jokes/random"
    response = requests.get(url).json()
    print(response) # print a JSON response in the terminal when the API page loads
    joke = response['value']['joke']
    return render(request, 'Veggie/veggie_api.html', context={'text': joke })

# Use the API from rapidAPI to find a wine description. Users can select the type of wine to be described.
def recipe_api_2(request, wine='1'):
    wine_number = wine
    if( wine_number == '1'):
        wine_name = 'Malbec'
    elif ( wine_number == '2'):
        wine_name = 'Riesling'
    elif ( wine_number == '3'):
        wine_name = 'Merlot'
    else:
        print("Value Error")
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/description"
    querystring = {"wine": wine_name}
    headers = {
        "X-RapidAPI-Key": "97df4ba39emsh613258c0b605a1ep1b6693jsnecb70a6ce8af",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    api_wine = json.loads(response.text)
    content = {"api_wine": api_wine}
    return render(request, 'Veggie/veggie_api_2.html', content)


# Website scraping with Beautifulsoup, finding the highlights of the site.
def recipe_bs(request):
    page = requests.get("https://simple-veganista.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find('p', class_='has-text-align-center').get_text()
    content = {"info": info}
    print(info)
    return render(request, 'Veggie/veggie_bs.html', content)




