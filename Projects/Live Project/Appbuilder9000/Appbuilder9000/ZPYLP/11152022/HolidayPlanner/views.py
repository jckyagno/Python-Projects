from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntryForm
from .models import Entry
from django.contrib import messages
import requests
from bs4 import BeautifulSoup


# This function will render the Home page when requested
def holidayplanner_home(request):
    return render(request, 'HolidayPlanner/HolidayPlanner_home.html')


# This function will render the Create page when requested
def holidayplanner_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "That entry was successfully created!")
            return redirect('./')
    content = {'form': form}
    return render(request, 'HolidayPlanner/HolidayPlanner_create.html', content)


# This function will render the Read/List page when requested
def holidayplanner_list(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'HolidayPlanner/HolidayPlanner_read.html', content)


# This function will render the Details page when requested
def holidayplanner_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    content = {'entry': entry}
    return render(request, 'HolidayPlanner/HolidayPlanner_details.html', content)


# This function will render the Update page when requested
def holidayplanner_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, "That entry was successfully updated!")
            return redirect('HolidayPlanner_list')
    else:
        form = EntryForm(instance=entry)
        content = {'form': form, 'entry': entry}
    return render(request, 'HolidayPlanner/HolidayPlanner_edit.html', content)


# This function will render the Delete page when requested
def holidayplanner_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        entry.delete()
        messages.success(request, "That entry was successfully deleted!")
        return redirect('HolidayPlanner_list')
    else:
        content = {'entry': entry}
    return render(request, 'HolidayPlanner/HolidayPlanner_delete.html', content)


# This function will render the API page when requested
def holidayplanner_api(request):

    list_by_map_url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list-by-map"

    list_by_map_querystring = {
        "search_id": "none",
        "children_age": "",
        "price_filter_currencycode": "GBP",
        "languagecode": "en-us",
        "travel_purpose": "leisure",
        "categories_filter": "class%3A%3A1%2Cclass%3A%3A2%2Cclass%3A%3A3",
        "children_qty": "",
        "order_by": "popularity",
        "guest_qty": "1",
        "room_qty": "1",
        "departure_date": "2022-10-2",
        "bbox": "51.5560695%2C51.6560695%2C-0.2796034%2C-0.1796034",
        "arrival_date": "2022-10-1"
    }

    list_by_map_headers = {
        'x-rapidapi-host': "apidojo-booking-v1.p.rapidapi.com",
        'x-rapidapi-key': "54d78e5c98mshd2b3a25b4adf763p1674f2jsnb7535d954daf"
    }

    list_by_map_response = requests.request("GET", list_by_map_url, headers=list_by_map_headers,
                                            params=list_by_map_querystring).json()

    for list_result in list_by_map_response['result']:
        hotel_id = list_result['hotel_id']

        reviews_url = "https://apidojo-booking-v1.p.rapidapi.com/properties/get-featured-reviews"

        reviews_querystring = {
            "languagecode": "en-us",
            "hotel_id": hotel_id
        }

        reviews_headers = {
            'x-rapidapi-host': "apidojo-booking-v1.p.rapidapi.com",
            'x-rapidapi-key': "7bc001f75amsh6d42156d20adcadp15c7aejsn695341e0f83f"
        }

        reviews_response = requests.request("GET", reviews_url, headers=reviews_headers,
                                            params=reviews_querystring).json()
        # Loop through 2nd dictionary to be able to get values from within
        for review in reviews_response['vpm_featured_reviews']:
            if (review['title'] is None):
                print('')


        hotelname = list_result['hotel_name']
        minprice = list_result['min_total_price']
        address = list_result['address']
        review_title = review['title']
        prosreview = review['pros']
        averagescore = review['average_score_out_of_10']
        consreview = review['cons']

        content = {
            'hotelname': hotelname,
            'address': address,
            'minprice': minprice,
            'review_title': review_title,
            'prosreview': prosreview,
            'consreview': consreview,
            'averagescore': averagescore
        }

        return render(request, 'HolidayPlanner/HolidayPlanner_api.html', content)


def holidayplanner_bs(request):
    page = requests.get("https://www.farandwide.com/s/best-places-visit-world-0697723328374f59")
    soup = BeautifulSoup(page.content, 'html.parser')
    titles_tags = soup.find_all('h2')
    places = [place.get_text() for place in titles_tags]
    indexes = [59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31]
    placelist = []
    for i in indexes:
        placelist.append(places[i])
    content = {
        'placelist': placelist
    }
    return render(request, 'HolidayPlanner/HolidayPlanner_bs.html', content)


