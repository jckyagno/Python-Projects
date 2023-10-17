from django.shortcuts import render, redirect,  get_object_or_404
from django.views.generic import ListView
from .models import Material
from .forms import MaterialForm

def inventory_home(request):
    return render(request, 'Inventory/Inventory_home.html')

def inventory_create(request):
    form = MaterialForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Inventory/Inventory_create.html', content)

def inventory_read(request):
    material = Material.Materials.all()
    content = {'material': material}
    return render(request, 'Inventory/Inventory_read.html', content)

class SearchResultsView(ListView):
    model = Material
    template_name = 'Inventory/Inventory_search.html'

def inventory_details(request, pk):
    material = get_object_or_404(Material, pk=pk)
    content = {'material': material}
    return render(request, 'Inventory/Inventory_details.html', content)

def inventory_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    form = MaterialForm(data=request.POST or None, instance=material)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'material': material}
    return render(request, 'Inventory/inventory_update.html', content)


def inventory_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('../../read')
    content = {'material': material}
    return render(request, 'Inventory/inventory_delete.html', content)

