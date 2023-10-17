from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Patient_EntryForm
from .models import Patient_Entry


# Create your views here.
def loso_home(request):
    return render(request, 'LosoVision/LosoVision_home.html')

# Renders create.html where patient input is made.
def loso_create(request):
    form = Patient_EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('LosoVision_home')
    content = {'form': form}
    return render(request, 'LosoVision/LosoVision_create.html', content)

# Renders read.html where patient info displays
def loso_read(request):
    entry = Patient_Entry.Patient_Entries.all()
    content = {'entry': entry}
    return render(request, 'LosoVision/LosoVision_read.html', content)