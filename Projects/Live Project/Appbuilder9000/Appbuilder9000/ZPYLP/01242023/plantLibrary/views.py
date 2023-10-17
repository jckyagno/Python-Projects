from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant
from .forms import PlantForm
from django.contrib import messages
from django.db.models import Q


def plant_home(request):
    return render(request, 'plantLibrary/plant_home.html')

# add plants function


def plant_addplant(request):
    if request.method == "POST":
        form = PlantForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            plant_name = request.POST['plant_name']
            sunlight_needs = request.POST['sunlight_needs']
            water_needs = request.POST['water_needs']
            location = request.POST['location']

            messages.success(request, 'There was an error in your form! Please try again...')
            return render(request, 'plantLibrary/plant_addplant.html', {
                'plant_name': plant_name,
                'sunlight_needs': sunlight_needs,
                'water_needs': water_needs,
                'location': location,
            })

        messages.success(request, 'Your plant was successfully added to the library!')
        return redirect('plant_home')
    else:
        return render(request, 'plantLibrary/plant_addplant.html')

# view plant library database


def plant_myplantlibrary(request):
    all_plants = Plant.objects.all
    return render(request, 'plantLibrary/plant_myplantlibrary.html', {'all_plants': all_plants})


# details search function
def plant_details(request, pk):
    info = get_object_or_404(Plant, pk=pk)
    content = {'info': info}
    return render(request, 'plantLibrary/plant_details.html', content)
