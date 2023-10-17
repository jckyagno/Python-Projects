
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event
from django.http import JsonResponse
from .forms import EventForm


def render_main(request):
	return render(request, 'clip_home.html')


def render_options(request):
	return render(request, 'clip_options.html')


def render_about(request):
	return render(request, 'clip_about.html')


def get_events(request):
	data = list(Event.objects.all().values())
	return JsonResponse(data, safe=False)


def create_event(request):
	form = EventForm(data=request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('clip_home')
	content = {'form': form}
	return render(request, 'clip_create.html', content)