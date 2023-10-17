from django.shortcuts import render, redirect, get_object_or_404
from .forms import BettingForm
from .models import Bet

# Creating View for Home page aka story 1
def BettingLinesHome(request):
    return render(request, 'BettingLines/BettingLinesHome.html')

#Creating a form to add bets
def BettingLines_Add(request):
    form = BettingForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../')
    content = {'form': form}
    return render(request, 'BettingLines/BettingLines_Add.html', content)

#displays database items
def BettingLines_View(request):
    bets = Bet.BettingLinesModel.all()
    content = {'bets': bets}
    return render(request, "BettingLines/BettingLines_View.html", content)


#Details function to view wager details
def BettingLines_Details(request, pk):
    info = get_object_or_404(Bet, pk=pk)
    content = {'info': info}
    return render(request, "BettingLines/BettingLines_Details.html", content)
#Edit Function
def BettingLines_Edit(request, pk):
    info = get_object_or_404(Bet, pk=pk)
    form = BettingForm(data=request.POST or None, instance=info)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../view')
    content = {'form': form, 'info': info}
    return render(request, 'BettingLines/BettingLines_Edit.html', content)

#Delete Function
def BettingLines_Delete(request, pk):
    info = get_object_or_404(Bet, pk=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('../../view')
    content = {'info': info}
    return render(request, 'BettingLines/BettingLines_Delete.html', content)


