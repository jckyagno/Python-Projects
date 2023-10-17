from django.shortcuts import render, redirect, get_object_or_404
from .models import Gift, ChristmasJoke
from .forms import GiftForm, ChristmasJokeForm
import requests
import json
from bs4 import BeautifulSoup

def ChristmasList_home(request):
    return render(request, 'ChristmasList/ChristmasList_home.html')

def gift_create(request):
    form = GiftForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../create')
    content = {'form': form}
    return render(request, 'ChristmasList/gift_create.html', content)

def gift_list(request):
    entry = Gift.objects.all()
    content = {'entry': entry}
    return render(request, 'ChristmasList/gift_list.html', content)

def gift_details(request, pk):
    entry = get_object_or_404(Gift, pk=pk)
    content = {'entry': entry}
    return render(request, 'ChristmasList/gift_details.html', content)

def gift_edit(request, pk):
    entry = get_object_or_404(Gift, pk=pk)
    form = GiftForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../list')
    content = {'form': form, 'entry': entry}
    return render(request, 'ChristmasList/gift_edit.html', content)

def gift_delete(request, pk):
    entry = get_object_or_404(Gift, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../list')
    content = {'entry': entry}
    return render(request, 'ChristmasList/gift_delete.html', content)

def christmas_api(request):
    url = "https://christmascountdown.live/api/joke"

    response = requests.request("GET",url)
    print(response)
    api_info = json.loads(response.text)
    parse1 = api_info["question"]
    parse2 = api_info["answer"]

    #This portion is added to because the content I get from the API uses a non Unicode 8 charter for apostropes that is interperted as â€™.
    parse1 = parse1.replace("â€™", "'")
    parse2 = parse2.replace("â€™", "'")

    print(api_info)
    content = {"parse1": parse1, "parse2": parse2}
    return render(request, 'ChristmasList/api.html', content)

def christmas_bs(request):
#   Using beautiful soup I wanted to extract the christmas poem from the website below.
#   Each poem was in a div "listicle-slide-dek" so I used that as my target to extract the first poem
    url = requests.get("https://www.countryliving.com/life/kids-pets/g29539102/christmas-poems-for-kids/")
    soup = BeautifulSoup(url.content, 'html.parser')
    info = soup.find_all(class_="listicle-slide-dek")[0].get_text().split('\n')
    text = list(info)
    content = {"text": text}
    return render(request, 'ChristmasList/bs.html', content)


def saved_api(request, p1, p2):
    if p1 != "p1" and p2 != "p2":
        joke = ChristmasJoke(
            answer=p2,
            question=p1
        )
        joke.save()
    joke = ChristmasJoke.Jokes.all()
    content = {"joke": joke}
    return render(request, 'ChristmasList/saved_api.html', content)