from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from django.views.generic.list import ListView
from django.db.models import Q  # Used for queries
from django.urls import reverse
import requests
import json
from bs4 import BeautifulSoup


# Renders home page
def video_game_home(request):
    return render(request, "VideoGameReviews/VideoGameReviews_home.html")


# Renders create page
def video_game_create(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Redirects to home page after form is saved
            return redirect('video_game_display')
    content = {'form': form}
    return render(request, "VideoGameReviews/VideoGameReviews_create.html", content)


# Renders page that displays database items
def video_game_display(request):
    reviews = Review.Reviews.all()
    content = {'reviews': reviews}
    return render(request, "VideoGameReviews/VideoGameReviews_display.html", content)


class SearchResults(ListView):
    model = Review
    template_name = 'VideoGameReviews/VideoGameReviews_search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchResults, self).get_queryset()
        # Storing user input from form as variable
        query = self.request.GET.get('search')
        if query:
            # User can search by either game title or reviewer name
            postresult = Review.Reviews.filter(
                Q(game_title__contains=query) | Q(reviewer_name__contains=query)
            )
            result = postresult
        else:
            result = None
        return result


# Primary key used to identify entry in database
def video_game_details(request, pk):
    review = get_object_or_404(Review, pk=pk)
    content = {'review': review}
    return render(request, "VideoGameReviews/VideoGameReviews_details.html", content)


def video_game_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return render(request, "VideoGameReviews/VideoGameReviews_details.html", {'review': review})
    else:
        form = ReviewForm(instance=review)
    primary_key = Review.Reviews.get(pk=pk)
    return render(request, "VideoGameReviews/VideoGameReviews_edit.html", {'form': form, 'primary_key': primary_key})


def video_game_delete(request, pk):
    record = Review.Reviews.get(pk=pk)
    record.delete()
    return HttpResponseRedirect(reverse('video_game_display'))


def video_game_api(request):
    # Getting information/api from giantbomb.com
    # Getting game id, name, summary, the date it was added to the site, and a link to the game page on the site
    # It updates upon the page loading, so there may be display errors due to errors on giantbomb's end
    response = requests.get(
        "https://www.giantbomb.com/api/games/?api_key=78a5703f113b9e0a2ab98bdd6255a23ac6ee5cd2&format=json&limit=10&sort=date_added:desc&field_list=name,deck,site_detail_url,id,date_added",
        headers={'User-Agent': 'required'}  # This header is required for the api to work
    )
    info = json.loads(response.text)

    # Creating empty lists to later store info from api
    game_id = []
    name = []
    summary = []
    date_added = []
    link = []

    # Loops through all items in dictionary named "results"
    for item in info["results"]:
        json_id = item["id"]
        game_id.append(json_id)

        json_name = item["name"]
        name.append(json_name)

        json_summary = item["deck"]
        summary.append(json_summary)

        json_date = item["date_added"]
        date_added.append(json_date)

        json_link = item["site_detail_url"]
        link.append(json_link)

    # Zipping together in order to match up items from lists above at each index
    full_list = zip(game_id, name, summary, date_added, link)
    content = {"full_list": full_list}
    return render(request, "VideoGameReviews/VideoGameReviews_api.html", content)


def video_game_beautiful_soup(request):
    response = requests.get("https://en.wikipedia.org/wiki/List_of_best-selling_video_games")
    soup = BeautifulSoup(response.content, 'html.parser')
    # Gets specific table I'm looking for on the original page
    table = soup.find_all('table')[1]
    # Cleans up table formatting
    pretty_table = table.prettify()
    content = {"pretty_table": pretty_table}
    return render(request, "VideoGameReviews/VideoGameReviews_beautiful_soup.html", content)
