from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Beast, Monster
from .forms import BeastForm, BeastEditForm, MonsterForm
import requests
import json
from bs4 import BeautifulSoup
import random


# Story 1 - Build Basic App
def dfort_home(request):
    beast = Beast.Beasts.all().order_by("title")

    context = {'beast': beast}

    return render(request, 'DwarfFortGen/dfort_home.html', context)


# Story 2 - Build Model
def dfort_create(request):
    form = BeastForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')
    context = {'form': form}
    return render(request, 'DwarfFortGen/dfort_create.html', context)


# Story 3 - Display Database

def dfort_display(request):
    beast = Beast.Beasts.all().order_by("title")

    context = {'beast': beast}

    return render(request, 'DwarfFortGen/dfort_display.html', context)


# Display search results

def dfort_search(request):
    if request.method == "POST":
        name = request.POST.get('usr_query')
        beast = Beast.Beasts.filter(name=name)
        context = {'name': name, 'beast': beast}

        return render(request, 'DwarfFortGen/dfort_search.html', context)


# Story 4 - Details Page

def dfort_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Beast, pk=pk)
    form = BeastForm(data=request.POST or None, instance=item)
    beast = Beast.Beasts.all().order_by('pk')

    # Dictionary for visualizer
    # Builds a different dictionary to display different species types

    #        case : TEMPLATE

    #            beast_body = {'top1': '#######',
    #                          'top2': '#######',
    #                          'mid': '#######',
    #                          'bot1': '#######',
    #                          'bot2': '#######'}

    # Material Visual

    if item.skin == 'meat':
        material = 'meat'

    elif item.skin == 'metal':
        material = 'metal'

    elif item.skin == 'fungus':
        material = 'fungus'

    elif item.skin == 'scale':
        material = 'scale'

    elif item.skin == 'gem':
        material = 'gem'

    # Species Visual

    if item.species == 'reptilian':

        beast_body = {'top1': ' {(")} ',
                      'top2': '_--+--_',
                      'mid': ' / |   | \ ',
                      'bot1': '[  |__|  ]',
                      'bot2': ' _/  \_ '}

    elif item.species == 'avian':

        beast_body = {'top1': '  }B>  ',
                      'top2': ' o-^-o ',
                      'mid': '[|   |]',
                      'bot1': '[ \_/ ]',
                      'bot2': '  | |  '}

    elif item.species == 'canine':

        beast_body = {'top1': '  =:3  ',
                      'top2': ' <-|-> ',
                      'mid': '|| # ||',
                      'bot1': 'V \#/ V',
                      'bot2': ' _| |_ '}

    elif item.species == 'amphibian':

        beast_body = {'top1': '  ,_,  ',
                      'top2': ' (00) ',
                      'mid': 'T( ~ )T',
                      'bot1': '" \_/ "',
                      'bot2': '  ( )  '}

    else:
        # debug to check case being met
        print('none')

        beast_body = {'top1': '  ___  ',
                      'top2': ' ( ~ ) ',
                      'mid': '(  0  )',
                      'bot1': '(_____)',
                      'bot2': ' |   | '}

    context = {'form': form, 'item': item, 'beast_body': beast_body, 'beast': beast, 'material': material}

    return render(request, 'DwarfFortGen/dfort_details.html', context)


# Story 5 - Edit/Delete
def dfort_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Beast, pk=pk)
    form = BeastEditForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')

    context = {'form': form, 'item': item}

    return render(request, 'DwarfFortGen/dfort_edit.html', context)


def dfort_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Beast, pk=pk)
    context = {"item": item, }
    item.delete()

    return render(request, "DwarfFortGen/dfort_delete.html", context)


# Beautiful Soup
def dfort_news(request):
    # A status_code of 200 means that the page downloaded successfully.
    # function will scrape data from dwarf fortress website grabbing latest news
    news = requests.get("http://www.bay12games.com/dwarves/")  # Website
    soup = BeautifulSoup(news.content, 'html.parser')

    # all news posts are list items and the first is the latest so an easy grab
    # get text returns text instead of html elements
    # find stops after 1 result, find all keeps searching beyond first result

    # Dates of news posts
    all_dates = {
        'date1': soup.find_all(class_='date')[0].get_text(),
        'date2': soup.find_all(class_='date')[1].get_text(),
        'date3': soup.find_all(class_='date')[2].get_text(),
    }

    # text of news posts
    all_news = {
        'news1': soup.find_all('li')[0].get_text(),
        'news2': soup.find_all('li')[1].get_text(),
        'news3': soup.find_all('li')[2].get_text(),
    }

    context = {'all_news': all_news, 'all_dates': all_dates}

    return render(request, "DwarfFortGen/dfort_news.html", context)


def dfort_about(request):
    return render(request, 'DwarfFortGen/dfort_about.html')


def dfort_arena(request):
    fighters = Beast.Beasts.all().order_by('win')
    context = {"fighters": fighters}
    return render(request, "DwarfFortGen/dfort_arena.html", context)

def dfort_error(request):
    return render(request, 'DwarfFortGen/dfort_error.html')


def dfort_results(request):
    # Grabs value from selected options which is then linked to respective primary keys from database
    pk1 = request.POST.get('fighter1')
    pk2 = request.POST.get('fighter2')

    if pk1 != pk2:
        fighter1 = get_object_or_404(Beast, pk=pk1)
        fighter2 = get_object_or_404(Beast, pk=pk2)

        # Random Coin-Flip determining victor, 0-1 range for estimated %50 chance
        coinflip = random.randint(0, 1)
        print(coinflip)

        # Wins and losses are updated depending on victor and then saved, updating the records
        if coinflip == 0:
            fighter1.win = fighter1.win + 1
            fighter2.lose = fighter2.lose - 1
            fighter1.save()
            fighter2.save()
            winner = get_object_or_404(Beast, pk=pk1)
        else:
            fighter2.win = fighter2.win + 1
            fighter1.lose = fighter1.lose - 1
            fighter2.save()
            fighter1.save()
            winner = get_object_or_404(Beast, pk=pk2)

        # winner is assigned this way to display it after a delay with JavaScript
        context = {'fighter1': fighter1, 'fighter2': fighter2, 'winner': winner}

        return render(request, 'DwarfFortGen/dfort_results.html', context)

    # Way to catch if 2 instances of the same fighters are selected
    else:
        return redirect('dfort_error')

def dfort_api(request):
    if request.method == 'POST':
        name = request.POST.get('usr_query')
        temp = "https://api.open5e.com/monsters/?search="
        search = str(temp) + str(name)
        # fetches monster info from api - Various criteria can be used
        response = requests.get(search)

        # Formats json into a cleaner string
        def textprint(obj):
            text = (json.dumps(obj, indent=4))
            return text

        result1 = {}
        result2 = {}
        result3 = {}
        result4 = {}
        result5 = {}

        display1 = False
        display2 = False
        display3 = False
        display4 = False
        display5 = False

        # Debug printing full json to console
        info = textprint(response.json())
        print(info)

        # Pulls only needed fields and checks that there are results
        if len(response.json()['results']) > 0:
            result1 = {"slug": response.json()['results'][0]['slug'],
                       "type": response.json()['results'][0]['type'],
                       "size": response.json()['results'][0]['size'],
                       "HP": response.json()['results'][0]['hit_points'],
                       }
            display1 = True

        if len(response.json()['results']) > 1:
            result2 = {"slug": response.json()['results'][1]['slug'],
                       "type": response.json()['results'][1]['type'],
                       "size": response.json()['results'][1]['size'],
                       "HP": response.json()['results'][1]['hit_points'],
                       }
            display2 = True

        if len(response.json()['results']) > 2:
            result3 = {"slug": response.json()['results'][2]['slug'],
                       "type": response.json()['results'][2]['type'],
                       "size": response.json()['results'][2]['size'],
                       "HP": response.json()['results'][2]['hit_points'],
                       }
            display3 = True

        if len(response.json()['results']) > 3:
            result4 = {"slug": response.json()['results'][3]['slug'],
                       "type": response.json()['results'][3]['type'],
                       "size": response.json()['results'][3]['size'],
                       "HP": response.json()['results'][3]['hit_points'],
                       }
            display4 = True

        if len(response.json()['results']) > 4:
            result5 = {"slug": response.json()['results'][3]['slug'],
                       "type": response.json()['results'][3]['type'],
                       "size": response.json()['results'][3]['size'],
                       "HP": response.json()['results'][3]['hit_points'],
                       }
            display5 = True

        # Dictionary containing first 5 results
        results = {
            'result1': result1,
            'result2': result2,
            'result3': result3,
            'result4': result4,
            'result5': result5,
        }

        # Dictionary to check results have values
        displays = {
            'display1': display1,
            'display2': display2,
            'display3': display3,
            'display4': display4,
            'display5': display5,
        }

        context = {'response': response, 'name': name, 'results': results, 'displays': displays}

        return render(request, "DwarfFortGen/dfort_api.html", context)

    return render(request, "DwarfFortGen/dfort_api.html")

def dfort_save(request): #Save Api
    monster = Monster.Monsters.all()

    context = {'monster': monster}
    return render(request, "DwarfFortGen/dfort_save.html", context)

def dfort_list(request): #Display all saved API entries
    monster = Monster.Monsters.all()

    context = {'monster': monster}
    return render(request, "DwarfFortGen/dfort_list.html", context)
