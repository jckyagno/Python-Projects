from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddBookForm
from .models import AddBook

# Renders BookRatings home page
def BookRatings_home(request):
    return render(request, 'BookRatings/BookRatings_home.html')

# Renders BookRatings Add Book page
def BookRatings_Add_Book(request):
    # Retrieves the Add Book form
    form = AddBookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BookRatings_Ratings')
    form_content = {'form': form}
    return render(request, 'BookRatings/BookRatings_AddBook.html', form_content)

# Renders BookRatings Ratings page
def BookRatings_Ratings(request):
    rated_books = AddBook.objects.all()
    rated_content = {'rated_books': rated_books}
    return render(request, 'BookRatings/BookRatings_Ratings.html', rated_content)

# Renders BookRatings Details page - Retrieves details from database about specific book
def BookRatings_Details(request, pk):
    pk = int(pk)
    details_books = get_object_or_404(AddBook, pk=pk)
    details_content = {'details_books': details_books}
    return render(request, 'BookRatings/BookRatings_Details.html', details_content)
