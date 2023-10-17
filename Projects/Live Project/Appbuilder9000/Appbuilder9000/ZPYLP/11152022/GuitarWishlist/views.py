from django.shortcuts import render, redirect,  get_object_or_404
from .forms import GuitarForm
from .models import GitFiddle
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.http import HttpResponse



#Story 1:===============================================================================


#view for home page
def guitar_wishlist_home(request):
    return render(request, 'GuitarWishlist/guitar_wishlist.html')


#Story 2===============================================================================
#view for create page
#the GuitarForm corresponds to form we made in forms.py
def guitar_wishlist_create(request):
    form = GuitarForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../create')
    content = {'form': form}
    return render(request, 'GuitarWishlist/guitar_wishlist_create.html', content)




#Story 3 Display all items from database TBD this is where we make the viewall/read view===========
#============================================================================================
def guitar_wishlist_viewall(request):
    list_name = GitFiddle.objects.all()
    content = {'list_name': list_name}
    return render(request, 'GuitarWishlist/guitar_wishlist_viewall.html', content)




#Story 4 Create a details view/page=================================================================
def guitar_wishlist_details(request, pk):
    chosenList = get_object_or_404(GitFiddle, pk=pk)
    content = {'chosenList': chosenList}
    return render(request, 'GuitarWishlist/guitar_wishlist_details.html', content)



#Story 5 Edit/Delete Views=====================================================
#view for edit page
def guitar_wishlist_edit(request, pk):
    chosenList = get_object_or_404(GitFiddle, pk=pk)
    form = GuitarForm(data=request.POST or None, instance=chosenList)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('GuitarWishlist_viewall')
    content = {'form': form, 'chosenList': chosenList}
    return render(request, 'GuitarWishlist/guitar_wishlist_edit.html', content)

#view for delete page
def guitar_wishlist_delete(request, pk):
    chosenList = get_object_or_404(GitFiddle, pk=pk)
    if request.method == 'POST':
        chosenList.delete()
        return redirect('GuitarWishlist_viewall')
    content = {'chosenList': chosenList}
    return render(request, 'GuitarWishlist/guitar_wishlist_delete.html', content)



#Story 6 Setup Beautiful Soup==============================================

def guitar_wishlist_bs(request):
    #1950's Les Paul
    page = requests.get("https://www.musiciansfriend.com/guitars/gibson-les-paul-standard-50s-electric-guitar/l54575000003000")
    soup = BeautifulSoup(page.content, 'html.parser')

    #ESP EC 1000
    pagea = requests.get("https://www.musiciansfriend.com/guitars/esp-ltd-deluxe-ec-1000-electric-guitar/516629000001000")
    soupa = BeautifulSoup(pagea.content, 'html.parser')

    #Rosewood Telecaster
    pageb = requests.get("https://www.musiciansfriend.com/guitars/fender-american-professional-ii-telecaster-rosewood-fingerboard-electric-guitar")
    soupb = BeautifulSoup(pageb.content, 'html.parser')

    #Gibson SG
    pagec = requests.get("https://www.musiciansfriend.com/guitars/gibson-sg-standard-electric-guitar")
    soupc = BeautifulSoup(pagec.content, 'html.parser')

    #PRS
    paged = requests.get("https://www.musiciansfriend.com/guitars/prs-dw-ce24-24-floyd-electric-guitar")
    soupd = BeautifulSoup(paged.content, 'html.parser')

    #description/brand name definitions-----------------------------
    # Format: info = soup.find_all('a', 'ui-link')[0].get_text()    **skip increment(s) between desc's when mult links present otherwise wrong text is returned**
    desc = soup.find_all('h1', 'pdp-section-title_title')[0].get_text()
    desca = soupa.find_all('h1', 'pdp-section-title_title')[0].get_text()
    descb = soupb.find_all('h1', 'pdp-section-title_title')[0].get_text()
    descc = soupc.find_all('h1', 'pdp-section-title_title')[0].get_text()
    descd = soupd.find_all('h1', 'pdp-section-title_title')[0].get_text()




    content = {"desc": desc,
               "desca": desca,
               "descb": descb,
               "descc": descc,
               "descd": descd,

}  #try making multiple dictionaries so we can display multiple elements

    return render(request, 'GuitarWishlist/guitar_wishlist_bs.html', content)
