from django.shortcuts import render, get_object_or_404, redirect

from .forms import TrailsForm
from .models import Trails
from bs4 import BeautifulSoup
import requests
import json
import datetime


# Create your views here.
# Display home page
def mtb_dest_home(request):
    return render(request, "MTB_Destinations/mtb_dest_home.html")


# Display all trails
def mtb_dest_list(request):
    queryset = Trails.trails.all()
    content = {
        "trail_list": queryset
    }
    return render(request, "MTB_Destinations/mtb_dest_list.html", content)


# Add item object to list/database
def mtb_dest_add(request):
    if request.method == 'POST':
        form = TrailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mtb_dest_list')

    else:
        form = TrailsForm()

    content = {'form': form}
    return render(request, "MTB_Destinations/mtb_dest_add.html", content)


# Display trail system details
def mtb_dest_details(request, id):
    obj = Trails.trails.get(id=id)
    content = {
        "obj": obj
    }
    return render(request, "MTB_Destinations/mtb_dest_details.html", content)


def mtb_dest_edit(request, id):
    obj = get_object_or_404(Trails, id=id)
    form = TrailsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('mtb_dest_details', id)
    # Feed both the form and object. Form info builds the form and obj is used to fill variable in the title
    content = {
        "form": form,
        "obj": obj
    }

    return render(request, "MTB_Destinations/mtb_dest_edit.html", content)


def mtb_dest_delete(request, id):
    obj = get_object_or_404(Trails, id=id)
    obj.delete()
    return redirect('mtb_dest_confirm_delete')


def mtb_dest_confirm_delete(request):
    return render(request, "MTB_Destinations/mtb_dest_confirm_delete.html")


# Used to make json data more readable
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def mtb_dest_api(request):
    # I would like to show a basic 3-5 day forecast, ideally for the cities that have been
    # added to the trail list or user's current location (if this can be done securely.) This would
    # include temp, pop, and weather{description} https://www.weatherbit.io/api/weather-forecast-hourly
    parameters = {
        "key": "79f0bfcecbe248d48482bb2ff4b12871",
        "city": "NewYork,NY",
        "units": "I",
    }
    response = requests.get(
        "https://api.weatherbit.io/v2.0/forecast/hourly?", params=parameters)
    weather = response.json()['data']
    content = {
        'weather': weather
    }

    return render(request, "MTB_Destinations/mtb_dest_api.html", content)


def mtb_dest_bs(request):
    # This function scrapes the airbnb for homes for rent in the Rocky Mountains. It finds a title, a lead comment,
    # a price and a rating for each listing on the page.
    page = requests.get("https://www.airbnb.com/s/North-America/homes?tab_id=home_tab&flexible_trip_lengths%5B%5D="
                        "one_week&price_filter_input_type=0&query=rocky%20mountains&date_picker_type=calendar&"
                        "search_type=unknown&refinement_paths%5B%5D=%2Fhomes")
    soup = BeautifulSoup(page.content, 'html.parser')
    all_listings = soup.find(class_='_11ry7lz')
    #listing = all_listings.find_all(class_='c4mnd7m')
    #listing_1 = listing[0]
    # lead = listing_1.find(class_='t1jojoys').get_text()
    # title = listing_1.find(class_='tjbvqj3').get_text()
    # price = listing_1.find(class_='a8jt5op').get_text()
    # rating = listing_1.find(class_='ru0q88m').get_text()
    leads = [al.get_text() for al in all_listings.select('.c4mnd7m .t1jojoys')]
    titles = [ts.get_text() for ts in all_listings.select('.c4mnd7m .tjbvqj3')]
    prices = [pr.get_text() for pr in all_listings.select('.c4mnd7m .a8jt5op')]
    ratings = [ra.get_text() for ra in all_listings.select('.c4mnd7m .ru0q88m')]
    site = [ws.get('href') for ws in all_listings.select('.c4mnd7m .ln2bl2p')]
    mylist = zip(leads, titles, prices, ratings, site)
    content = {
        'mylist': mylist
    }
    return render(request, "MTB_Destinations/mtb_dest_bs.html", content)
