from django.shortcuts import render, redirect,  get_object_or_404
from .models import Merc
from .forms import MercForm
# In order to read a .js response from a link in Python
from urllib.request import urlopen
import requests
import json


# Pathway to Homepage
def ja3_home(request):
    return render(request, 'JA3Mercs/ja3_home.html')

# Pathway to Enroll page
def ja3_enroll(request):
    mercs = Merc.objects.all()
    return render(request, 'JA3Mercs/ja3_enroll.html', {'mercs': mercs})

# Function to
def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Merc, pk=pk)
    form = MercForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('ja3_roster')
        else:
            print(form.errors)
    else:
        return render(request, 'JA3Mercs/ja3_details.html', {'form': form})



def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Merc, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('ja3_roster')
    context = {"item": item,}
    return render(request, "JA3Mercs/ja3_confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        form = MercForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('ja3_enroll')
    else:
        return redirect('ja3_enroll')

def createRecord(request):
    form = MercForm(request.POST or None)
    form = MercForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ja3_roster')
    else:
        print(form.errors)
        form = MercForm()
    context = { 'form': form }
    return render(request, "JA3Mercs/ja3_createRecord.html", context)

def roster(request):
    mercs = Merc.objects.all
    return render(request, "JA3Mercs/ja3_roster.html", {'mercs': mercs})

# def for the api grab request. look at functions.js
def api(request):
    url = "https://api.github.com/emojis"
    response = requests.get(url)

    if response.status_code == 200:
        emojis = response.json()
        newContent = []
        for emoji in list(emojis.keys())[4:7]:
            content = {}
            content['name'] = emoji
            content['url'] = emojis[emoji]

            newContent.append(content)
        print(newContent)
        viewModel = {}
        viewModel = newContent

        return render(request, 'JA3Mercs/ja3_api.html', {'content': viewModel})
    else:
        print("Error Code %d" % response.status_code)

    # # Grabbing API
    # response = requests.get('https://api.github.com/')
    # # Prints status code
    # print('Status Code = ')
    # print(response.status_code)
    # # url for API
    # url = "https://api.github.com/emojis"
    # # stores url response
    # response = urlopen(url)
    # # stores json response from url in data
    # data_json = json.loads(response.read())
    # # print json response
    # print(data_json)
    #
    #
    # def jprint(obj):
    #     text = json.dumps(obj, sort_keys=True, indent=4)
    #     print(text)
    #
    # jprint(data_json)
    #
    # # renders webpage
    # return render(request, "JA3Mercs/ja3_api.html")



