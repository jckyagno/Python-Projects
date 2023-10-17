from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactForm, WeatherInfo
from .forms import ConForm
import requests
import json
from bs4 import BeautifulSoup


def navbar(request):
    return render(request, "Portfolio/cli_navbar.html")



def PortfolioIndex(request):
    context = (addInquiry(request))
    return render(request, "Portfolio_home.html", context)


def navbar(request):
    return render(request, "Portfolio/cli_navbar.html")

# rendering blank form template on page load


def addInquiry(request):
    form = ConForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return context
        else:
            print(form.errors)
    return context

# generating a list of all database items currently stored


def inqurieslist(request):
    inquries = ContactForm.ContactForm.all()
    context = addInquiry(request)
    context.update({
        'inquries': inquries,
    })

    return render(request, "Portfolio_data.html", context)

# referencing a single database item by its primary key so it can be modified


def inquiry(request, pk):
    pk = int(pk)
    inquries = get_object_or_404(ContactForm, pk=pk)
    content = {
        'inquries': inquries,
    }
    return render(request, 'portfolio_display.html', content)


def inquriesdetails(request, pk):
    pk = int(pk)
    inquiry = get_object_or_404(ContactForm, pk=pk)
    form = ConForm(data=request.POST or None, instance=inquiry)
    if request.method == 'POST':
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.save()
            return redirect('Portfolio_data')
    else:
        content = {
            'form': form,
            'inquiry': inquiry
        }
        return render(request, 'portfolio_details.html', content)

def inquirydelete(request, pk):
    inquiry = get_object_or_404(ContactForm, pk=pk)
    if request.method == 'POST':
        inquiry.delete()
        # removing primary key value from url
        return redirect('../../Portfolio_data.html')
    content = {'inquiry': inquiry}
    return render(request, 'portfolio_delete.html', content)

# using 2 APIs to retrieve data from an external source


def weather_api(request):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": "auto:ip", }
    headers = {
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
        "X-RapidAPI-Key": "7dc3090264msh649f16d611a817cp132d61jsnd0d8326e3d49"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    geo = api_info["location"]
    weather = api_info["current"]
    weathercon = weather["condition"]
    city = geo["name"]
    Time = geo["localtime"]
    condition = weathercon["text"]
    TempF = weather["temp_f"]


    context = {
        "Temperature": TempF,
        "City": city,
        "Time": Time,
        "Condition": condition,
    }
    return context



def beautifulsoup(request):
    page = requests.get("https://en.wikipedia.org/wiki/Falcon_9")
    soup = BeautifulSoup(page.content, 'html.parser')
    section = soup.find('div', {'class': 'mw-parser-output'})
    para = section.find_all('p')[1].get_text()

    content = {"para": para}
    return render(request, "portfolio_about.html", content)

def weatherview(request):
    context = (weather_api(request))
    return render(request, 'portfolio_weather.html', context)

def weathersave(request):
    context = (weather_api(request))
    Info = WeatherInfo(
        Temperature=context["Temperature"],
        City=context["City"],
        Condition=context["Condition"]
    )
    Info.save()
    data = WeatherInfo.WeatherInfo.all()
    return render(request, 'portfolio_weatherdata.html', {"Data": data})




    # Info = []
    # url = "https://weatherapi-com.p.rapidapi.com/current.json"
    # querystring = {"q": "auto:ip", }
    # headers = {
    #     "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    #     "X-RapidAPI-Key": "7dc3090264msh649f16d611a817cp132d61jsnd0d8326e3d49"
    # }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # api_info = json.loads(response.text)
    # geo = api_info["location"]
    # weather = api_info["current"]
    # weathercon = weather["condition"]
    # for i in geo:
    #     City = i["name"]
    #     Time = i["localtime"]
    #     Info.append(City)
    #     Info.append(Time)
    # for con in weather:
    #         Temperature = con["temp_f"]
    #         Info.append(Temperature)
    # for wc in weathercon:
    #         Condition = wc["text"]
    #         Info.append(Condition)
    #


