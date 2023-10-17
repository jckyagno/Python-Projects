from django.shortcuts import render, get_object_or_404, redirect
from .forms import BoardGameForm
from .models import BoardGames
import requests
from bs4 import BeautifulSoup
import re
import json
from django.http import HttpResponse


# Story 1: build basic app -------------------------------------------------


def bgt_home(request):
    return render(request, "BoardGameTracker/BoardGameTracker_add.html")

# ---------------------------------------------------------------------------


# Story 2: Create Model------------------------------------------------------

def bgt_create(request):
    form = BoardGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bgt_home')
    else:
        print(form.errors)
        form = BoardGameForm()
    context = {
        'form': form,
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_add.html', context)

# --------------------------------------------------------------------------------


# Story 3: Create page to display all boardgames entered into database------------

def bgt_view(request):
    boardgames = BoardGames.objects.all()
    return render(request, 'BoardGameTracker/BoardGameTracker_read.html', {'boardgames': boardgames})

# Story 4: Create page to display details of single selected object--------------------------


def bgt_details(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    context = {'boardgame': boardgame}
    return render(request, 'BoardGameTracker/BoardGameTracker_details.html', context)
# --------------------------------------------------------------------------------------------


# Story 5: Create Edit and Delete functionality for objects in Board Game DB------------------

def bgt_edit(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    form = BoardGameForm(data=request.POST or None, instance=boardgame)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('bgt_view')
    context = {
        'form': form,
        'boardgame': boardgame,
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_edit.html', context)

# Delete object from DB-----------------------------------------------------------


def bgt_delete(request, pk):
    pk = int(pk)
    boardgame = get_object_or_404(BoardGames, pk=pk)
    boardgame.delete()
    return redirect('bgt_view')


# Story 6: Set up BeautifulSoup to scrape html and print navigable objects to console
def bgt_bsoup():
    page = requests.get("https://www.boardgamequest.com/category/game-reviews/")
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify()) #was run to examine the page contents
    # from soup.prettify() I can see that the elements I want contain titles and links to reviews specifically
    # these links and their titles are in <a> tags with no class, no id, and rel='bookmark'

    review_anchor = soup.find_all(href=re.compile('-review'), class_='td-image-wrap', id=False, rel='bookmark') # This line isolates the links to the actual review links I want to scrape
    imageSoup = BeautifulSoup(str(review_anchor), 'html.parser')
    #print(imageSoup.prettify())
    review_image = imageSoup.find_all('img')
    print("REVIEW IMAGE 0")
    print(review_image[0])
    #rimage = review_image[0].get('src')
    #print(rimage)
    # imgList = []
    # for element in review_anchor:
    #     review_image = (element.find_all(src=re.compile('jp')))
    #     #r_img = review_image.get('src')
    #     imgList.append({'review_image': review_image})
    # print (imgList)

    #     i = 0
    #     imgList = []
    #     while i < 7:
    #         r_img = review_image[i].get('src')
    #         imgList.append({'r_img': r_img})
    #         i += 1
    # print(imgList)

    #print("REVIEW IMAGE 0")
    #print(review_image[0])
    #r_img = review_image[0].get('src')
    #print(r_img)





    #print(review_anchor[0].contents)
    reviewList = []
    imageList = []
    n = 0
    while n < 7:
        #review_contents = review_anchor[n].next_element
        #print(review_contents)
        href = review_anchor[n].get('href')
        title = review_anchor[n].get('title')
        rtext = review_anchor[n].get_text()
        rimage = review_image[n].get('src')
        imageList.append(rimage)
        reviewList.append({'href': href, 'title': title, 'rtext': rtext, 'rimage': rimage})
        n += 1
    #print(list(review_anchor)) # This prints each anchor element containing the review title and link to the console
    print("IMAGE LIST 0")
    print(imageList[0])
    #print(reviewList[0])
    content = {"reviewList": reviewList} # right now the list of <a> elements renders on the BeautifulSoup page of my app with no formatting



    return content #render(request, 'BoardGameTracker/BoardGameTracker_bsoup.html', content)

def bgt_bsoup_render(request):
    reviewList = bgt_bsoup()["reviewList"]
    content = {
        'reviewList': reviewList
    }
    return render(request, 'BoardGameTracker/BoardGameTracker_bsoup.html', content)



def jprint(obj): # This function was used to examine JSON results, but is not required for rendering / display
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




def bgt_api(request):
    response = requests.get("https://www.gamerpower.com/api/giveaways?sort-by=date") # This API allows easy sorting of deals and giveaways by date
    print(response.status_code)
    #print(response.json())
    #info = json.dumps(response.text)
    #print(info)
    #jprint(response.json())
    # from the returned JSON I intend to render
    #   thumbnail images ("image"), link to the giveaway listing ("gamerpower_url"), and title ("title")
    #   Clicking on the thumbnail or title should redirect viewer to gamerpower URL.
    #   New entries should load and refresh based on what listings are most recent at gamerpower
    api_load = json.loads(response.text)
    #print(api_load)

    gamerpower_url = []
    title = []
    image_url = []

    for item in api_load:
        json_title = item["title"]
        title.append(json_title)

        json_gameurl = item["gamerpower_url"]
        gamerpower_url.append(json_gameurl)

        json_image = item["image"]
        image_url.append(json_image)

    api_list = zip(title, gamerpower_url, image_url)
    content = {"api_list": api_list}


    return render(request, "BoardGameTracker/BoardGameTracker_api.html", content)