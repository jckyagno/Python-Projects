from django.shortcuts import render, redirect, get_object_or_404
from .models import Vampire
from .forms import VampireForm
import requests


def vampire_home(request):
    return render(request, 'Vampire_Tracker/vampire_home.html')

def vampire_entry(request):
    form = VampireForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vampire_view')
    content = {'form': form}
    return render(request, 'vampire_tracker/vampire_entry.html', content)

def vampire_view(request):
    entry = Vampire.objects.all()
    content = {'entry': entry}
    return render(request, 'vampire_tracker/vampire_view.html', content)

def vampire_details(request, pk):
    entry = get_object_or_404(Vampire, pk=pk)
    content = {'entry': entry}
    return render(request, 'vampire_tracker/vampire_details.html', content)

def vampire_edit(request, pk):
    entry = get_object_or_404(Vampire, pk=pk)
    form = VampireForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('vampire_view')
    content = {'form': form, 'entry': entry}
    return render(request, 'vampire_tracker/vampire_edit.html', content)

def vampire_delete(request, pk):
    entry = get_object_or_404(Vampire, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('vampire_view')
    content = {'entry': entry}
    return render(request, 'vampire_tracker/vampire_delete.html', content)