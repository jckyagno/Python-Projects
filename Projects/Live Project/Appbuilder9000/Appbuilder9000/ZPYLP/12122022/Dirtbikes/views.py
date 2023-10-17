from django.shortcuts import render, redirect,  get_object_or_404
from .models import Entry
from .forms import EntryForm
import requests


# Story #1 Build the basic app ------------------------------------------------------------

def dirtbikes_home(request):
    return render(request, 'Dirtbikes/dirtbikes_home.html')


# Story #2 Create your model -------------------------------------------------------------
def dirtbikes_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../create')
    content = {'form': form}
    return render(request, 'Dirtbikes/dirtbikes_create.html', content)

# Story #3 Display all items from database -----------------------------------------------
def dirtbikes_read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'Dirtbikes/dirtbikes_read.html', content)

# Story #4: Details page ------------------------------------------------------------------
def dirtbikes_details(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    content = {'entry': entry}
    return render(request, 'Dirtbikes/dirtbikes_details.html', content)

# Story #5: Edit and Delete Functions -----------------------------------------------------

def dirtbikes_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Dirtbikes/dirtbikes_update.html', content)


def dirtbikes_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'Dirtbikes/dirtbikes_delete.html', content)