from django.shortcuts import render, get_object_or_404, redirect
from .forms import FoodForm
from .models import Food
import requests
import json
from bs4 import BeautifulSoup


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def texmex_home(request):
    return render(request, 'TexMex/texmex_home.html')


# Story #2 CreateModel -------------------------------------------------------------------------------------------------

def createRecord(request):
    form = FoodForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_recipes')
    else:
        print(form.errors)
        form = FoodForm()
    context = {
        'form': form,
    }
    return render(request, "TexMex/createRecord.html", context)


# Story #3: Display all items from database ----------------------------------------------------------------------------

def view_recipes(request):
    foods = Food.objects.all()
    return render(request, 'TexMex/texmex_display.html', {'foods': foods})


# Story #4: Details page -----------------------------------------------------------------------------------------------

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    return render(request, 'TexMex/present_food.html', {'item': item})


# Story #5: Edit and Delete Functions ----------------------------------------------------------------------------------

def recipe_page(request):
    foods = Food.objects.all()
    return render(request, 'TexMex/recipe_page.html', {'foods': foods})


def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    form = FoodForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('recipe_page')
        else:
            print(form.errors)
    else:
        return render(request, 'TexMex/texmex_edit.html', {'form': form, 'item': item})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('recipe_page')
    content = {"item": item}
    return render(request, "TexMex/confirmDelete.html", content)


def confirmed(request):
    if request.method == 'POST':
        #creates form instance and binds data to it
        form = FoodForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('recipe_page')
    else:
        return redirect('recipe_page')

# Story #6-(API Pt 1): Connect to API ----------------------------------------------------------------------------------
# Story #7-(API Pt 2): Parse through JSON

def texmex_api(request):
    url = "https://tasty.p.rapidapi.com/recipes/list"

    querystring = {"from": "0", "size": "20", "tags": "mexican"}

    headers = {
        "X-RapidAPI-Host": "tasty.p.rapidapi.com",
        "X-RapidAPI-Key": "ab0f8ef407msh2ecaa66fb018526p1d19a0jsn802e4681dd3e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    api_info = json.loads(response.text)

    recipe_list = []

    for x in range(20):
        recipe_list.append([api_info["results"][x]["slug"], api_info["results"][x]["name"]])
    content = {"recipe_list": recipe_list}
    return render(request, 'TexMex/texmex_api.html', content)

def texmex_bs(request):
    menu = []
    page = requests.get("https://www.allrecipes.com/recipes/17502/us-recipes/tex-mex/")
    soup = BeautifulSoup(page.content, 'html.parser')
    pork = soup.find(title="Tex-Mex Pork")
    menu.append(["Tex-Mex Pork", pork.get('href')])
    fajitas = soup.find(title="Sizzling Steak Fajitas")
    menu.append(["Sizzling Steak Fajitas", fajitas.get('href')])
    salad = soup.find(title="Spicy Tex-Mex Salad")
    menu.append(["Spicy Tex-Mex Salad", salad.get('href')])
    casserole = soup.find(title="King Ranch Chicken Casserole III")
    menu.append(["King Ranch Chicken Casserole III", casserole.get('href')])
    tacos = soup.find(title="Grilled Tex-Mex Fish Tacos")
    menu.append(["Grilled Tex-Mex Fish Tacos", tacos.get('href')])
    content = {"menu": menu}
    return render(request, 'TexMex/texmex_bs.html', content)





