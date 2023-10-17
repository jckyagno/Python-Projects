from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import GameForm
from .models import Game
import requests
from bs4 import BeautifulSoup
import json
from .forms import WishListForm
from .models import WishList

## ADMIN CONSOLE-------------------------------------------------------------------------------------------------------
def admin_console(request):                                 #The general naming convention is that methods start with lower case letters
    tableContents = Game.GameModel.all()                    # Declare a variable to hold the model.modelManager.all(), which returns all records in the db
    wishListContents = WishList.WishListModelMgr.all()      # The general naming convention is that Models start with upper case letters.
    contents = {
        'tableContents':tableContents,
        'wishListContents':wishListContents
    }
    return render(request, 'GameHoard/GH_index.html', contents)   #render is the keyword to display the browser Syntax: {request object, the file, {context}


## ADMIN CONSOLE-------------------------------------------------------------------------------------------------------

## GH_index.html (CREAT, READ, RENDER BEAUTIFUL SOUP, RENDER API)------------------------------------------------------
# Notes: The index (home) page is where users can create a database record for a game in their collection.
#   CREATE function is accessed by a modal included from GH_create.html (see modal instructions in gameHoard.js). The function must be included as part of this view, since here is where the CREATE function is actually performed.
#   READ function access the model manager and returns all records. The html content is included from GH_read.html, where it is parsed as as_p and as as_table.
#   BEAUTIFULSOUP web scraping is rendered via the create_soup function
def GH_home(request):                           ##CREATE and READ RECORDS
    #CREATE a RECORD IN THE DB
    form = GameForm(data=request.POST or None)  # Declare a variable 'form' and equate it to the existing Account form (as defined in forms.py); request.Post or None is the default syntax to take any input from the form and put it into this form.
    if request.method == 'POST':
        if form.is_valid():
            form.save()                         # Apply save(), a built-in model Manager method to save an object back to the db
            return redirect('GameHoard')        # Redirect to the 'shortcut' (as defined in urls.py)
        else:
            print(form.errors)                  # If the form cannot meet the if statement, print the built-in method .errors
            form = GameForm()                   # Create an empty version of the form as the variable 'form'.

    #READ all RECORDs via the model Manager
    tableContents = Game.GameModel.all()        # Declare a variable to hold the model.modelManager.all(), which returns all records in the db
    wishListContents = WishList.WishListModelMgr.all()

    #BEAUTIFUL SOUP TO RENDER GAME REVIEWS
    soupList = create_soupList()['soupList']

    #API CALL TO RENDER VIDEO GAME SECTION
    responseList = api()["responseList"]        # Use the dictionary key to call a specific item from the api() functions results
    queryList = apiQuery(request)["responseList"]

    content = {                                 # Declare a variable to then pass via return render
        'form': form,                           # Pass the 'form' variable back as a dictionary.
        'tableContents': tableContents,
        'wishListContents':wishListContents,
        'soupList':soupList,
        'responseList':responseList,
        'queryList':queryList,
    }
    return render(request, "GameHoard/GH_index.html", content)

def includeGH_read(request):    ##Function to include a django tag in GH_index....So when GH_Home is loaded, this is loaded too.
    template = loader.get_template('GameHoard/GH_index.html')
    return HttpResponse(template.render())
## GH_index.html (CREAT, READ, RENDER BEAUTIFUL SOUP, RENDER API)-------------------------------------------------------------------------------------------------------


## GH_update.html (UPDATE and DELETE A RECORD IN THE DB) -------------------------------------------------------------------------------------------------
def update(request, pk):                        # When a request is called by the user, it goes to the url 'switchboard', which directs it to a certain method
    #GET FORM OBJECT VIA THE MODEL MANAGER
    item = get_object_or_404(Game, pk=pk)       # Assigns a variable to represent this built-in function from the django.shortcuts module. Query the responseListbase for the Product (using this built-in function) and it's value at that primary key (which is now converted to an integer).
    form = GameForm(data=request.POST or None, instance=item)    #Invoke the ProductForm, get the information from the form that was sent via the post method (or provide a none value), then use that information to create an instance called item. The instance 'item' then passes back all of its values from its various fields
    #UPDATE A RECORD
    if request.method == 'POST':
        if form.is_valid():                     # If the request method is possed, check the form
            form.save()                         # save() is a built-in model Manager method to save an object back to the db
            return redirect('GameHoard')        # Redirect to the 'shortcut' (as defined in urls.py)
        else:
            print(form.errors)
    else:
        content = {
            'form': form,                   #pass in the form as a dictionary
            'item':item,
        }
        return render(request, 'GameHoard/GH_update.html', content)  #Render the page that the user sees. This actually happens first, because nothing prior has had a chance to happen yet.
    #DELETE A RECORD
    if request.method == 'POST':
        item.delete()                       #delete() is a built-in model Manager method
        return redirect('GameHoard')
    return render(request, "GameHoard/GH_index.html")

def includeGH_delete(request):      ##Function to include a django tag in GH_update....##This is not strictly necessary at this time, but good to include
    template = loader.get_template('GameHoard/GH_update.html')
    return HttpResponse(template.render())
## GH_update.html (UPDATE and DELETE A RECORD IN THE DB) -------------------------------------------------------------------------------------------------


## GH_beautifulsoup.html --------------------------------------------------------------------------------------------------------
def beautifulsoup(request):
    soupChildren = create_soupList()["soupChildren"]    #Call the function [by using the name of one of dictionary's keys] to have the results available to pass in to the included page (GH_bsoup.html) so that it can render on this page
    soupList = create_soupList()["soupList"]    #Same as above but using a different dictionary key to get a different set of resutls
    content = {
        'soupChildren':soupChildren,            #Pass along the results of the function by using a variable, created above to hold the results of the function.
        'soupList':soupList,
    }
    return render(request, "GameHoard/GH_beautifulsoup.html", content)  #Render the page, passsing in the content so the included pages can load.
## GH_beautifulsoup.html --------------------------------------------------------------------------------------------------------


## GH_bsoup.html (BEAUTIFL SOUP web scraping)--------------------------------------------------------------------------
def create_soupList():
    page = requests.get("https://www.boardgamequest.com/category/game-reviews/")  # request the page to scrpate using the .get method
    soup = BeautifulSoup(page.content,'html.parser')    #define a variable to hold the BeautifulSoup page.content or page.text using 'html.parser' (there are others available)
    #Notes:
    #soupPretty = soup.prettify()               #use the prettify() method to make the scraped html code more readable by adding tabulation
    #soupType = [type(item) for item in list(soup.children)]    #for every list object, display it's type

    soupChildren = list(soup.children)[8]       #list the children elements at a specific index in 'soup' variable, this is the html content that is to be scraped.

    soupList = []
    n = 0   #the index number
    while n < 7:
        href = soup.find_all('h3')[n].find('a').get('href')     #Use various soup methods to select the desired content.
        thumb = soup.find(class_='td-main-content').find_all('img')[n].get('src')
        title = soup.find_all('h3')[n].get_text()
        author = soup.find_all('span', class_='td-post-author-name')[n].get_text()
        date = soup.find_all('span', class_='td-post-date')[n].get_text()
        excerpt = soup.find_all('div', class_='td-excerpt')[n].get_text()
        soupList.append({'href':href, 'thumb':thumb, 'title':title, 'author':author, 'date':date, 'excerpt':excerpt})
        n += 1

    content = {
        'soupList':soupList,
        'soupChildren':soupChildren,
    }
    return content
## GH_bsoup.html (BEAUTIFL SOUP web scraping)--------------------------------------------------------------------------


## GH_api_template.html------------------------------------------------------------------------------------------------
def api_template(request):
    #variable = functionName()["keyName"]
    responseList = api()["responseList"]
    response = api()["response"]
    queryList = apiQuery(request)["responseList"]

    content = {
        'responseList':responseList,
        'response':response,
        'queryList': queryList,
    }
    return render(request, "GameHoard/GH_api_template.html", content)
## GH_api_template.html------------------------------------------------------------------------------------------------


## GH_api.html (API CALL functions)---------------------------------------------------------------------------------------------
def api():
    parameters = {
        'storeID': 1,
        'upperPrice': 50,
    }
    response = requests.get("https://www.cheapshark.com/api/1.0/deals?", params=parameters)
    response = json.loads(response.text)

    responseList = []
    for i in response:
        id = i["dealID"]
        thumb = i["thumb"]
        title = i["title"]
        rating = i["steamRatingPercent"]
        salePrice = i["salePrice"]
        fullPrice = i["normalPrice"]
        responseList.append({'id': id, 'thumb': thumb, 'title': title, 'rating': rating, 'salePrice': salePrice,'fullPrice': fullPrice})

    content = {
        'response':response,
        'responseList':responseList,
    }
    return content

#Search the API based on user input (via a form and the .get method)
def apiQuery(request):
    query = request.POST.get('inputquery', None) #Create a variable to hold the game's name when it's called by the get request
    if query != None:
        title = query.replace(' ','%')     #replace any empty spaces with '%'.
    else:
        title = ""

    parameters = {
        'title': title,
        'limit':1,
    }
    response = requests.get("https://www.cheapshark.com/api/1.0/games?", params=parameters)
    response = json.loads(response.text)

    responseList = []
    for i in response:
        id = i["steamAppID"]
        thumb = i["thumb"]
        title = i["external"]
        salePrice = i["cheapest"]
        query = title.replace(' ', '%20')
        responseList.append({'id': id, 'thumb': thumb, 'title': title,'salePrice': salePrice, 'query':query})

    content = {
        'responseList':responseList,
    }
    return content
## GH_api.html (API CALL functions)------------------------------------------------------------------------------------


## GH_create_wishlist.html (CREATE a record from API results via a form in the api.html----------------------------------------------------------------------------------------------------
def create_wishlist(request):
    #Gather (API) info from the input form by using the .get method
    Name = request.POST.get('Name', None)
    Thumb = request.POST.get('Thumb', None)
    Price = request.POST.get('Price', None)
    if Price == "":         #Because Price is a decimal field in the model, it can only accept numbers - it will error if "" or None get passed to it. This ensures "00.00" is the 'default'.
        Price = 00.00;
    duplicate = WishList.WishListModelMgr.all().filter(Name=Name)
    #CREATE A RECORD IN THE DB
    if duplicate:
        delete_wishlist(request)
    else:
        WishList.WishListModelMgr.create(Name=Name, Thumb=Thumb, Price=Price)
    return redirect('GameHoard')  # Redirect to the 'shortcut' (as defined in urls.py)

###Notes:
# Make sure to add the wishList () 'wishList'] call to Gh_index.html, and then pass in the rusults to the content= {}
    #wishList = WishList.WishListModelMgr.all()      #This will go on whatever 'page view' that displays the list of WishList records
    #wishList = WishList.WishListModelMgr.all()      #This will go on whatever 'page view' that displays the list of WishList records
## GH_create_wishlist.html----------------------------------------------------------------------------------------------------

def delete_wishlist(request): # When a request is called by the user, it goes to the url 'switchboard', which directs it to a certain method
    Name = request.POST.get('Name', None)
    record = WishList.WishListModelMgr.get(Name=Name)
    record.delete()
    #WishList.WishListModelMgr.delete(Name)
    return redirect('GameHoard')  # Redirect to the 'shortcut' (as defined in urls.py)