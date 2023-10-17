import requests
import json
import datetime as dt
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm


# renders home page
def crochet_home(request):
    return render(request, 'crochet_home.html')

# renders new project page
def create_project(request):
    form = ProjectForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projects_page')
    else:
        print(form.errors)
    content = {
        'form': form,
    }
    return render(request, 'project/create_project.html', content)

# renders details page
def details(request, pk):
    pk = int(pk)
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'project/details_page.html', context)

# renders all projects page
def display_project(request):
    query_results = Project.objects.all()
    context = {'query_results': query_results}
    return render(request, 'project/projects_page.html', context)

# renders edit project form
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(data=request.POST or None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('projects_page')
        else:
            print(form.errors)
    else:
        return render(request, 'project/edit_project.html', {'form': form, 'project': project})

# renders delete project page
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects_page')
    else:
        return render(request, 'project/delete_project.html', {'project': project})

# renders beautiful soup
def crochet_bs(request):
    page = requests.get('https://www.jaarn.co.za/5-facts-about-crocheting-you-didnt-know/')
    soup = BeautifulSoup(page.content, 'html.parser')
    # this grabs the first paragraph from the html page, only the 'crochet' definition
    paragraph = soup.find_all('p')[7]
    paragraph1 = paragraph.prettify()
    return render(request, 'project/crochet_bs.html', {'paragraph1': paragraph1})

# renders API page for part 1 and 2
def crochet_api(request):
    # has lat and lng for Atlanta, Georgia
    response = requests.get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400').json()
    sunrise_time = response['results']["sunrise"]
    sunset_time = response['results']["sunset"]
    context = {
        'sunrise_time': sunrise_time,
        'sunset_time': sunset_time,
    }
    return render(request, 'project/crochet_api.html', context)

