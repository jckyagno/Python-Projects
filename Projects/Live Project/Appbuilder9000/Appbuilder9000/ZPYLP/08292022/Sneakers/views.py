from django.shortcuts import render, redirect
from .forms import sneakerForm
from .models import Sneaker

# This function renders a page for a single item in our db
def sneakersDetails(request, shoe_id):
	selectedSnkr = Sneaker.sneaker.get(pk=shoe_id)
	return render(request, "Sneakers/Sneakers_sneakerSlct.html", {'selectedSnkr': selectedSnkr} )


# This function Renders the home page.
def Sneakers_home(request):
    return render(request, "Sneakers/Sneakers_home.html")

# This function renders the current sneakers page, which grabs the sneakers from the db
def current_sneakers(request):
	currSneak = Sneaker.sneaker.all()
	return render(request, "Sneakers/Sneakers_currentSnkrs.html", {'currSneak': currSneak})

# This function allows the user to add a sneaker to the db
def create_sneaker(request):
	form = sneakerForm(data=request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('../')
	content = {'form': form}
	return render(request, "Sneakers/Sneakers_createSnkr.html", content)
	""" Pull all fields from account and puts inside variable form. Then checks if
		request method is post and if it is it well redirect user to index page. 
		Then sends them to create a new account"""