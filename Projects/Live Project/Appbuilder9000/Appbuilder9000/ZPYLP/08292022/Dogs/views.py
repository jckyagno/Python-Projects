#importing render and redirect to help render the webpages and redirect when necessary
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
#import the dogs form form the forms.py
from .forms import DogsForm
#import the class dogs from the models.py
from .models import Dogs


# calls the Dogs_home home page when requested
def Dogs_home(request):
    return render(request, 'Dogs/Dogs_home.html')

# calls the Dogs Create page, here they will have a form to fill out
# to add to the database
def Dogs_create(request):
    form = DogsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Dogs_home')
    else:
        print(form.errors)
        form = DogsForm()
    content = {'form': form}
    return render(request, 'Dogs/Dogs_create.html', content)

# Display the dog's in the Database
def display_dogs(request):
    all_Dogs = Dogs.Dog.all()
    content = {
        'all_Dogs': all_Dogs,
    }
    return render(request, 'Dogs/Dogs_lists.html', content)


# Calling the details template
def details_dogs(request, pk):
    pk = int(pk)
    doggo = get_object_or_404(Dogs, pk=pk)
    form = DogsForm(data=request.POST or None, instance=doggo)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('../details')
        else:
            print(form.errors)
    else:
        content = {
            'doggo': doggo,
            'form': form,
        }
        return render(request, "Dogs/Dogs_details.html", content)

def delete_dog(request, pk):
    pk = int(pk)
    doggo = get_object_or_404(Dogs, pk=pk)
    if request.method == 'POST':
        doggo.delete()
        return redirect('lists')
    context = {"doggo": doggo,}
    return render(request, "Dogs/Dogs_confirm_Delete.html", context)

def confirm_delete(request):
    if request.method == 'POST':
        form =  DogsForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Dogs_home')
    else:
        return redirect('Dogs_home')
