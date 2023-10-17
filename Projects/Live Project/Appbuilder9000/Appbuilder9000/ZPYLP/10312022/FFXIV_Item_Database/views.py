from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCollectionForm
from .models import Collection, ItemInfo
import requests
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def ffxiv_db_home(request):
    return render(request, 'FFXIV_Item_Database/ffxiv_db_home.html')


def create_collection(request):
    form = CreateCollectionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('collections')
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'FFXIV_Item_Database/create_collection.html', content)


def collections(request):
    collection_list = Collection.collections.all()
    content = {'collection_list': collection_list}
    return render(request, 'FFXIV_Item_Database/collections.html', content)


def items(request):
    items_list = ItemInfo.items.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(items_list, 1000)
    try:
        items_list = paginator.page(page)
    except PageNotAnInteger:
        items_list = paginator.page(1)
    except EmptyPage:
        items_list = paginator.page(paginator.num_pages)

    return render(request, 'FFXIV_Item_Database/items.html', {'items_list': items_list})


def item_detail(request, item_id):

    #   Need to format the endpoint URL based on the item ID we're requesting info on
    url = "http://xivapi.com/item/{}".format(item_id)

    params = {
        "private_key": "79ff8553e6e74ec7babeb0e8161ea806d2e589b9630f41f8a564dc729952d22d"
    }

    #   API call for the information that we need to pass to the template
    response = requests.request("GET", url, params=params)
    print(response)
    #   Stashing the details in items_details. This is a HEAVILY nested return.
    item_details = json.loads(response.text)

    #   Pass the context to the template.
    context = {
        'item_details': item_details,
    }
    return render(request, 'FFXIV_Item_Database/item_detail.html', context)


def items_api(request):

    url = "https://xivapi.com/item"

    params = {
        "limit": "3000",
        "page": 1
    }

    response = requests.request("GET", url, params=params)
    items_info = json.loads(response.text)
    for page in range(0,items_info['Pagination']['PageTotal']+2):
        for item_return in items_info['Results']:
            # Break out the returns into easy variables
            item_id_returned = item_return['ID']
            item_icon_returned = item_return['Icon']
            item_name_returned = item_return['Name']
            item_url_returned = item_return['Url']

            #   Call the model.save() function for each attribute.
            item_returned = ItemInfo(
                ID=item_id_returned,
                Icon=item_icon_returned,
                Name=item_name_returned,
                Url=item_url_returned)
            item_returned.save()
        response = requests.request("GET", url, params={
            "limit": "3000",
            "page": page
        })
        print('Processing Page# {}...'.format(page))
        items_info = json.loads(response.text)

    return render(request, 'FFXIV_Item_Database/item_detail.html')






