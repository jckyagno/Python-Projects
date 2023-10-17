from django.shortcuts import render, redirect, get_object_or_404
from .forms import ScheduleForm
from .models import Schedule
import requests
from bs4 import BeautifulSoup


# Creates function to render home page
def puppy_home(request):
    return render(request, 'Puppy_Potty_Schedule/puppy_home.html')


# function to render built in form from my model puppy_add
def puppy_add(request):
    form = ScheduleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../time')
    content = {'form': form}
    return render(request, 'Puppy_Potty_Schedule/puppy_add.html', content)

# function to fetch all objects created from form and render
def puppy_all(request):
    pups = Schedule.objects.all()
    content = {'pups': pups}
    return render(request, 'Puppy_Potty_Schedule/puppy_list.html', content)

def puppy_details(request, pk):
    details = get_object_or_404(Schedule, pk=pk)
    content = {'details': details}
    return render(request, 'Puppy_Potty_Schedule/puppy_details.html', content)

def puppy_delete(request, pk):
    delete_post = get_object_or_404(Schedule, pk=pk)
    if request.method == "POST":
        delete_post.delete()
        return redirect('puppy_all')
    content = {'delete_post': delete_post}
    return render(request, 'Puppy_Potty_Schedule/puppy_delete.html', content)

def puppy_update(request, pk):
    update_post = get_object_or_404(Schedule, pk=pk)
    form = ScheduleForm(request.POST or None, instance=update_post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('puppy_all')
    content = {'form': form, 'update_post': update_post}
    return render(request, 'Puppy_Potty_Schedule/puppy_update.html', content)

def puppy_bs(request):
    page = requests.get("https://www.akc.org/expert-advice/training/potty-training-your-puppy-timeline-and-tips/")
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find_all('p')[0].get_text()
    content = {"info": info}
    return render(request, 'Puppy_Potty_Schedule/puppy_bs.html', content)






