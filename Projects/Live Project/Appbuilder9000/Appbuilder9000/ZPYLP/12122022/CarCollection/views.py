from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import Vehicle
from .forms import VehicleForm


def carcollection_home(request):
    return render(request, 'CarCollection/CarCollection_home.html')



def vehicle_create(request):
    form = VehicleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../create')
    content = {'form': form}
    return render(request, 'CarCollection/vehicle_create.html', content)



def CarCollection_inventory(request):
    entry = Vehicle.vehicles.all()
    content = {'entry': entry}
    return render(request, 'CarCollection/CarCollection_inventory.html', content)

def CarCollection_details(request, pk):
    entry = get_object_or_404(Vehicle, pk=pk)
    content = {'entry': entry}
    return render(request, 'CarCollection/CarCollection_details.html', content)

def vehicle_delete(request):
    entry = get_object_or_404(Vehicle)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../inventory')
    content = {'entry': entry}
    return render(request, 'CarCollection/vehicle_delete.html', content)


def vehicle_update(request):
    entry = get_object_or_404(Vehicle)
    form = VehicleForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../inventory')
    content = {'form': form, 'entry': entry}
    return render(request, 'CarCollection/vehicle_update.html', content)

