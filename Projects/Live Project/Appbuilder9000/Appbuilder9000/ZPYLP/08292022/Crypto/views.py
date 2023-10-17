from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCryptoForm
from .models import AddCrypto
# Create your views here.
def crypto_home(request):
    return render(request, 'Crypto/Crypto_Home.html')

# function to render built in form from my model AddCrypto
def crypto_addcrypto(request):
    form = AddCryptoForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'Crypto/Crypto_AddCrypto.html', content)

# function to fetch all objects created from form and render
def crypto_ratings(request):
    crypto_entries = AddCrypto.objects.all()
    content = {'crypto_entries': crypto_entries}
    return render(request, 'Crypto/Crypto_Ratings.html', content)

# function to get all attributes of object and render on details page
def crypto_details(request, pk):
    details = get_object_or_404(AddCrypto, pk=pk)
    context = {'details': details}
    return render(request, 'Crypto/Crypto_Details.html', context)

# function to update AddCrypto form, instance argument fills fields with selected element.
def crypto_update(request, pk):
    update_rating = AddCrypto.objects.get(pk=pk)
    form = AddCryptoForm(request.POST or None, instance=update_rating)
    if form.is_valid():
        form.save()
        return redirect('crypto_ratings')
    return render(request, 'Crypto/Crypto_Update.html',
                  {'update_rating': update_rating,
                   'form': form})

# function to delete AddCrypto object
def crypto_delete(request, pk):
    delete_rating = AddCrypto.objects.get(pk=pk)
    if request.method == 'POST':
        delete_rating.delete()
        return redirect('crypto_ratings')
    return render(request, 'Crypto/Crypto_Delete.html')
