from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Avg
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import ReleaseForm, ArtistForm
from .models import Release, Artist
from .pitchfork import *
from .discogs import *
import datetime

# renders homepage and saves albums to database if
# it receives a post request
def home(request):
    if request.method == 'POST':
        form = ReleaseForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('collection')
    else:
        form = ReleaseForm()
    return render(request, 'VinylCollection/Rhinoplasty_home.html', {'form': form})

# renders collection page
def collection(request):
    releases = Release.objects.all()
    context = {
        'releases': releases,
    }
    return render(request, 'VinylCollection/collection.html', context)

# renders the scores page
def scores(request):
    releases_with_scores = Release.objects.filter(pf_rating__gt=0).order_by('-pf_rating')
    average_score = releases_with_scores.aggregate(Avg('pf_rating'))
    clean_average = round(average_score['pf_rating__avg'], 1)
    context = {
        'releases': releases_with_scores,
        'average_score': clean_average,
    }
    return render(request, 'VinylCollection/scores.html', context)

# renders individual release pages
def details(request, pk):
    pk = int(pk)
    release = get_object_or_404(Release, pk=pk)
    context = {
        'release': release
    }
    return render(request, 'VinylCollection/details.html', context)

# renders update page
class ReleaseUpdateView(UpdateView):
    model = Release
    fields = '__all__'
    success_url = reverse_lazy('collection')

# renders delete page
class ReleaseDeleteView(DeleteView):
    model = Release
    success_url = reverse_lazy('collection')

# handles discogs/pitchfork requests
# gets discogs info as json
# scrapes pitchfork score from website
# adds score to discogs json
# returns json
def get_discogs_and_pitchfork_data(request):
    cat_number = request.GET['cat_number']
    release_json = get_discogs_data(cat_number)
    pitchfork_score = get_score(release_json)
    release_json['pitchfork_score'] = pitchfork_score
    release_json['release_date'] = datetime.datetime.strptime(release_json['year'] + ' 01 01 12 00 00', '%Y %m %d %H %M %S')
    return JsonResponse(release_json, safe=False)

