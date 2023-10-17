from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Fbeast
from .forms import FbeastForm
import requests
import json
from bs4 import BeautifulSoup

# Story 1 - Build Basic App
def dfort_home(request):
    beast = Fbeast.Fbeasts.all().order_by('pk')
    context = {'beast' : beast}
    return  render(request, 'DwarfFort/dfort_home.html', context)


# Story 2 - Build Model
def dfort_create(request):
    form = FbeastForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')
    context = {'form': form}
    return  render(request, 'DwarfFort/dfort_create.html', context)

# Story 3 - Display Database

def dfort_display(request):
    beast = Fbeast.Fbeasts.all().order_by("title")

    # builds collection of models from beast and limits display to 3 at a time
    paginator = Paginator(beast, 3)
    page = request.GET.get('page')
    beastpage = paginator.get_page(page)


    context = {'beastpage' : beastpage, 'beast' : beast}

    return render(request, 'DwarfFort/dfort_display.html', context)

# Display search results

def dfort_search(request):
    if request.method == "POST":
        name = request.POST.get('usr_query')
        beast = Fbeast.Fbeasts.filter(name=name)
        context = { 'name' : name, 'beast' : beast}

        return render(request, 'DwarfFort/dfort_search.html', context)

# Story 5 - Edit/Delete

def dfort_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Fbeast, pk=pk)
    form = FbeastForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')

    context = {'form': form, 'item': item}

    return render(request, 'DwarfFort/dfort_edit.html', context)


def dfort_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Fbeast, pk=pk)
    context = {"item": item, }
    item.delete()

    return render(request, "DwarfFort/dfort_delete.html", context)

# Story 6/7 - Beautiful-Soup/Api

# Beautiful Soup
def dfort_news(request):
    # A status_code of 200 means that the page downloaded successfully.
    # function will scrape data from dwarf fortress website grabbing latest news
    news = requests.get("http://www.bay12games.com/dwarves/") # Website
    soup = BeautifulSoup(news.content, 'html.parser')

    # all news posts are list items and the first is the latest so an easy grab
    # get text returns text instead of html elements
    # find stops after 1 result, find all keeps searching beyond first result

    # Dates of news posts
    all_dates = {
        'date1' : soup.find_all(class_='date')[0].get_text(),
        'date2': soup.find_all(class_='date')[1].get_text(),
        'date3': soup.find_all(class_='date')[2].get_text(),
    }

    # text of news posts
    all_news = {
        'news1' : soup.find_all('li')[0].get_text(),
        'news2' : soup.find_all('li')[1].get_text(),
        'news3' : soup.find_all('li')[2].get_text(),
        }


    context = {'all_news' : all_news, 'all_dates' : all_dates}

    return render(request, "DwarfFort/dfort_news.html", context)

# Open5E API
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
            display1= True

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
            'result1' : result1,
            'result2' : result2,
            'result3' : result3,
            'result4' : result4,
            'result5' : result5,
        }

        # Dictionary to check results have values
        displays = {
            'display1' : display1,
            'display2' : display2,
            'display3' : display3,
            'display4' : display4,
            'display5' : display5,
        }



        context = {'response': response, 'name' : name, 'results' : results, 'displays' : displays}

        return render(request, "DwarfFort/dfort_api.html", context)



    return render(request, "DwarfFort/dfort_api.html")

def dfort_about(request):
    return  render(request, 'DwarfFort/dfort_about.html')


# Story 4 - Details Page

def dfort_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Fbeast, pk=pk)
    form = FbeastForm(data=request.POST or None, instance=item)
    beast = Fbeast.Fbeasts.all().order_by('pk')

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

        beast_body = {'top1': '  [:P  ',
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

    context = {'form': form, 'item': item, 'beast_body': beast_body, 'beast' : beast, 'material' : material}

    return render(request, 'DwarfFort/dfort_details.html', context)