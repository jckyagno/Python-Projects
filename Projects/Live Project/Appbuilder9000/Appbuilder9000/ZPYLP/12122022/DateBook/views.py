from django.shortcuts import render, redirect,  get_object_or_404
from .forms import BookForm
from .models import Information

# story 1: Building the basic app
def datebook_home(request):
    return render(request, 'DateBook/datebook_home.html')

# story 2: Create your model
def datebook_entry(request):
    form = BookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    content = {'form': form}
    return render(request, 'DateBook/datebook_entry.html', content)

# story 3: Display all items from db
def datebook_all(request):
    entry = Information.objects.all()
    content = {'entry': entry}
    return render(request, 'Datebook/datebook_all.html', content)

# story 4: Details page
def datebook_details(request, pk):
    entry = get_object_or_404(Information, pk=pk)
    content = {'entry': entry}
    return render(request, 'Datebook/datebook_details.html', content)

def datebook_update(request, pk):
    entry = get_object_or_404(Information, pk=pk)
    form = BookForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../all')
    content = {'form': form, 'entry': entry}
    return render(request, 'DateBook/datebook_update.html', content)


def datebook_delete(request, pk):
    entry = get_object_or_404(Information, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../all')
    content = {'entry': entry}
    return render(request, 'DateBook/datebook_delete.html', content)