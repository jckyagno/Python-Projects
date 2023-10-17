from django.shortcuts import render, redirect,   get_object_or_404
from .models import Item
from .forms import ItemForm
import requests


# Story #1 -- Building the basic app --

def bucketlist_home(request):
    return render(request, 'BucketList/bucketlist_home.html')

# Story #2: Create your model ------------------------------------------------------------------------------------------

def bucketlist_create(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'BucketList/bucketlist_create.html', content)

# Story #3: Display all items from database ----------------------------------------------------------------------------

def bucketlist_read(request):
    item = Item.Items.all()
    content = {'item': item}
    return render(request, 'BucketList/bucketlist_read.html', content)

# Story #4: Details page -----------------------------------------------------------------------------------------------

def bucketlist_details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    content = {'item': item}
    return render(request, 'BucketList/bucketlist_details.html', content)

# Story #5: Edit and Delete Functions ----------------------------------------------------------------------------------

def bucketlist_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'item': item}
    return render(request, 'BucketList/bucketlist_update.html', content)

def bucketlist_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('../../read')
    content = {'item': item}
    return render(request, 'BucketList/bucketlist_delete.html', content)



