from django.shortcuts import render, redirect,  get_object_or_404
from .models import JournalEntry
from .forms import JournalEntryForm



def journalbs_home(request):
    return render(request, 'JournalBoostrap/journalbs_home.html')

def journalbs_create(request):
    form = JournalEntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'JournalBoostrap/journalbs_create.html', content)

def journalbs_read(request):
    entry = JournalEntry.Entries.all()
    content = {'entry': entry}
    return render(request, 'JournalBoostrap/journalbs_read.html', content)

def journalbs_details(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    content = {'entry': entry}
    return render(request, 'JournalBoostrap/journalbs_details.html', content)

def journalbs_update(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    form = JournalEntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'JournalBoostrap/journalbs_update.html', content)

def journalbs_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'JournalBoostrap/journalbs_delete.html', content)
