from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Imported Messages
# Class Based View
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Search imports
from django.db.models import Q
from itertools import chain

from .forms import SnowmobileForm, WeatherForm
from .models import Snowmobile, Weather, Dealer
import json
import requests
from bs4 import BeautifulSoup


# Create your views here.
def snowmobiles_home(request):
    return render(request, 'Snowmobiles/snowmobiles_home.html')


def snowmobiles_add(request):
    form = SnowmobileForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Snowmobile Added Successfully')  # Added message for successful save
            return redirect('../all')
    content = {'form': form, 'messages': messages}
    return render(request, 'Snowmobiles/snowmobiles_add.html', content)


def snowmobiles_all(request):
    snowmobiles = Snowmobile.objects.all()
    return render(request, 'Snowmobiles/snowmobiles_all.html', {'snowmobiles': snowmobiles})


def snowmobiles_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Snowmobile, pk=pk)
    content = {'item': item}
    return render(request, 'Snowmobiles/snowmobiles_details.html', content)


def snowmobiles_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Snowmobile, pk=pk)
    form = SnowmobileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../all')
    content = {'form': form, 'item': item}
    return render(request, 'Snowmobiles/snowmobiles_edit.html', content)


def snowmobiles_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Snowmobile, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('snowmobiles_all')
    context = {'item': item, }
    return render(request, 'Snowmobiles/snowmobiles_confirm_delete.html', context)


def snowmobiles_confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = SnowmobileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('snowmobiles_all')
    else:
        return redirect('snowmobiles_all')


def snowmobiles_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "portland", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "90fa2802f4msh0c54814193aed3ap19c862jsnd465c68e3c07",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    weather_info = json.loads(response.text)
    temp_int = weather_info["current_observation"]["condition"]["temperature"]
    temperature = str(weather_info["current_observation"]["condition"]["temperature"]) + "\N{DEGREE SIGN}F"
    content = {"temperature": temperature, "temp_int": temp_int}
    return render(request, 'Snowmobiles/snowmobiles_api.html', content)


def snowmobiles_bs(request):  # BeautifulSoup example.
    # Page scraping data from
    page = requests.get("https://www.snowmobile.org/snowmobiling-statistics-and-facts.html")
    # Parsing data
    soup = BeautifulSoup(page.content, 'html.parser')
    # Getting title
    title = soup.find_all('h2')[1].get_text()
    # Getting slices of data to format it.
    words = soup.find_all('p')[1].get_text()[:290]
    words2 = soup.find_all('p')[1].get_text()[290:405]
    words3 = soup.find_all('p')[1].get_text()[406:520]
    # Preparing variables to provide for the HTML page.
    content = {"title": title, "words": words, "words2": words2, "words3": words3}
    # Calling and rendering page.
    return render(request, 'Snowmobiles/snowmobiles_bs.html', content)


def snowmobiles_save_api(request, m=1000):
    if m != 1000:
        current = Weather(
            temp=m
        )
        current.save()
    current = Weather.objects.all()
    content = {'current': current}
    return render(request, 'Snowmobiles/snowmobiles_save_api.html', content)


# Class Based Views
class MyView(View):
    template_name = 'Snowmobiles/snowmobiles_places.html'

    def get(self, request):
        return render(request, self.template_name)


class SnowmobileListView(ListView):
    model = Snowmobile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(stores=Dealer.objects.all())
        return context


class SnowmobileCreate(CreateView):
    model = Snowmobile
    fields = ['make', 'model', 'dateManufactured', 'description']

    def get_success_url(self):  # new
        return reverse('snowmobile-list')


class SnowmobileUpdate(UpdateView):
    model = Snowmobile
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):  # new
        return reverse('snowmobile-list')


class SnowmobileDelete(DeleteView):
    model = Snowmobile
    success_url = reverse_lazy('snowmobile-list')


class SnowmobileDetailView(DetailView):
    model = Snowmobile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchResultsView(ListView):
    model = Snowmobile
    template_name = 'Snowmobiles/snowmobiles_search_view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        item = request.GET.get('items', None)
        if query is not None:
            snowmobile_results = Snowmobile.objects.search(query=query)
            dealer_results = Dealer.objects.search(query=query)

            # Combine query sets
            if item == 'snowmobile':
                queryset_chain = chain(
                    snowmobile_results,
                )
            elif item == 'dealer':
                queryset_chain = chain(
                    dealer_results,
                )
            else:
                queryset_chain = chain(
                    snowmobile_results,
                    dealer_results
                )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Snowmobile.objects.none()  # Empty query default.


class DealerCreate(CreateView):
    model = Dealer
    fields = "__all__"
    template_name = 'Snowmobiles/snowmobiles_dealer_form.html'

    def get_success_url(self):  # new
        return reverse('snowmobile-list')


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'Snowmobiles/snowmobile_dealer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
