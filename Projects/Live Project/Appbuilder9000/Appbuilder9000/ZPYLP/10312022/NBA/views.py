from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player


# Create your views here.
def NBA_home(request):
    return render(request, 'NBA/NBA_home.html')

def createPlayer(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('NBA_home')
    content = {'form': form}
    return render(request, 'NBA/NBA_create.html', content)


# # Story #3: Display all items from database ----------------------------------------------------------------------------
#
def nbaRead(request):
    player = Player.objects.all()
    content = {'player': player}
    return render(request, 'NBA/NBA_read.html', content)
#
#
# # Story #4: Details page -----------------------------------------------------------------------------------------------
#
def nbaDetails(request, id):
    player = get_object_or_404(Player, pk=id)
    content = {'player': player}
    return render(request, 'NBA/NBA_details.html', content)



