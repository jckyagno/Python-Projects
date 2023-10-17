from django.shortcuts import render, redirect, get_object_or_404
from .models import Procreate
from .forms import ProcreateForm

# Create your views here.
def procreate_home(request):
    return render(request, "Procreate/Procreate_home.html")

def procreate_seeartist(request):
    procreate = Procreate.ProcreateArt.all()
    content = {'procreate': procreate}
    return render(request, "Procreate/Procreate_SeeArtist.html", content)

def procreate_create(request):
    form = ProcreateForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../seeartist')
    content = {'form': form}
    return render(request, 'Procreate/Procreate_create.html', content)

def procreate_details (request, pk):
    procreate = get_object_or_404(Procreate, pk=pk)
    content = {'procreate': procreate}
    return render(request, 'Procreate/Procreate_details.html', content)