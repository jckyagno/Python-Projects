from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobsForm
from .models import Jobs, Temp
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json

def saveSearch(request):
    # gets the date that the job was posted from the model
    initDate = (request.POST['date_added'])

    # This block of code pulls the Month, Date, and Year data received from the API search to a format that can be
    # converted to a datetime
    # below is the function that adjusts where the day of the month is pulled from based on the length
    # of the Month's name
    def stripDateData():
        if ',' in (initDate[(len(Month)):(len(Month) + 3)]):
            Date = initDate[(len(Month) + 1)]
        else:
            Date = initDate[(len(Month) + 1):(len(Month) + 3)]
        return Date

    # This block of code pulls the Month, Year, and Date data from a string based on which month name is found
    # in the string
    if 'January' in initDate:
        Month = 'January'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'February' in initDate:
        Month = 'February'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'March' in initDate:
        Month = 'March'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'April' in initDate:
        Month = 'April'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'May' in initDate:
        Month = 'May'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'June' in initDate:
        Month = 'June'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'July' in initDate:
        Month = 'July'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'August' in initDate:
        Month = 'August'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'September' in initDate:
        Month = 'September'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'October' in initDate:
        Month = 'October'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'November' in initDate:
        Month = 'November'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()
    elif 'December' in initDate:
        Month = 'December'
        Year = initDate[(len(initDate) - 4):(len(initDate))]
        Date = stripDateData()

    # This puts the data from the block above in the format necessary to convert it to a datetime with strptime()
    if len(Date) < 2:
        adjustedDate = ('{}-{}-0{}'.format(Year, Month, Date))
    else:
        adjustedDate = ('{}-{}-{}'.format(Year, Month, Date))

    # This converts the formatted data from above to a datetime
    formattedDate = datetime.strptime(adjustedDate, '%Y-%B-%d')

    # This saves all the data that are selected from the form in search results (which is populated from the temp table)
    # to the actual permanent Jobs table
    savedJob = Jobs(
        title=(request.POST['title']),
        company=(request.POST['company']),
        stack='unknown',
        startup='unknown',
        location='',
        exp_required='',
        minimum_pay=(request.POST['minimum_pay']),
        maximum_pay=(request.POST['maximum_pay']),
        date_added=formattedDate,
        job_url=(request.POST['job_url']),
    )
    savedJob.save()

    # This gives the context to print all the Jobs table data into the JobScraping_history page.
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs,
    }



    return render(request, 'JobScraping/JobScraping_history.html', context)

# This view takes the user to the home page
def JobScraping_home(request):

    # Gets the request of the data from the website.
    page = requests.get('https://forecast.weather.gov/MapClick.php?lat=45.5118&lon=-122.6756#.YqN-yXbMIuU')
    soup = BeautifulSoup(page.content, 'html.parser')
    today = soup.select('li.forecast-tombstone:first-child')

    # We will be extracting the current day's weather only.
    current = today[0].find(class_='period-name').get_text()
    description = today[0].find(class_='short-desc').get_text()
    temp = today[0].find(class_='temp-high').get_text()

    data = [current, description, temp]
    context = {'data': data}
    return render(request, 'jobScraping/JobScraping_home.html', context)


# This view takes the user to the API job search page
def searchAPI(request):
    return render(request, 'JobScraping/APIJobSearch.html')


# This view sends the data input by the user an initiates the API request and returns APIJobSearch.html with the
# returned values from the API response
def searchResults(request):
    # This line clears the temp table for the next search
    Temp.objects.all().delete()

    # This gets the location information submitted with the form on APIJobSearch.html
    description = request.POST['what']
    # This changes the string received from the form to a syntax that the url can recognize (e.g. exchange " " for %20)
    formattedDescription = (description.replace(" ", "%20")).replace(",", "%2C")
    # This gets the location information submitted with the form on APIJobSearch.html
    location = request.POST['location']
    # This changes the string received from the form to a syntax that the url can recognize (e.g. exchange " " for %20)
    formattedLocation = (location.replace(" ", "%20")).replace(",", "%2C")

    # creates an array that will be sent to the page as context so that the search bars will maintain their data when
    # the page is re-loaded
    search = [description, location]

    # Queries an API for 20 results based on the location and description received above
    response = requests.get(
        'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=41b593cb&app_key=58bb774dace8a185a8cc32fbdff00416&results_per_page=5&what={}&where={}&sort_by=date'.format(
            formattedDescription, formattedLocation))


    print(response.status_code)

    # Sends up to the error page if the request does not work.
    if not response.status_code == 200:
        return render(request, 'JobScraping/error.html')


    # pulls the json data from the API response
    json_data = response.json()
    # json_data is a dictionary with a single key which contains an array of the job objects. This sets the variable
    # results to that array.
    results = json_data['results']

    # This takes the results and puts them in a form to add them to the Temp database
    for i in results:
        try:
            jobData = Temp(
                minimum_pay=i['salary_min'],
                maximum_pay=i['salary_max'],
                title=i['title'],
                company=i['company']['display_name'],
                job_url=i['redirect_url'],
                date_added=(i['created'])[0:10],
            )
        except:
            jobData = Temp(
                minimum_pay='',
                maximum_pay='',
                title=i['title'],
                company=i['company']['display_name'],
                job_url=i['redirect_url'],
                date_added=(i['created'])[0:10],
            )
        # This saves the data that I gather with the code above to the Temp database table
        jobData.save()

    # This collects all data currently stored on the Temp table
    jobs = Temp.objects.all()

    return render(request, 'JobScraping/APIJobSearch.html', {'jobs': jobs, 'search': search})


# This view takes the user to the JobScraping_input.html page where they can input job data into a form
def JobScraping_input(request):
    form = JobsForm(request.POST or None)
    context = {'form': form}
    return render(request, 'JobScraping/JobScraping_input.html', context)


# This view is activated from JobScraping_input.html, and saves any data that was in the form to the database.
def inputJob(request):
    # This line creates a form element and binds data to it
    form = JobsForm(request.POST or None)
    # This check if the data in the form are valid, and if they are it saves them and returns the user to the homepage
    if form.is_valid():
        form.save()
        return redirect('JobScraping_history')
    else:
        # If the form data are not valid the respective errors are printed
        print(form.errors)
        # the form variable is reset to represent the base JobsForm() object
        form = JobsForm()
    context = {
        'form': form,
    }
    return render(request, 'JobScraping/JobScraping_input.html', context)


# This view requests all the information in the database and sends it as context to JobScraping_history.html and then
# renders that html page.
def JobScraping_history(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_history.html', context)


# This view saves the changes made to a form on JobScraping_editJob.html
def saveEdit(request, pk):
    # converts the argument pk (which is a string) to an integer
    pk = int(pk)
    # This line gets the item with the requested primary key from the database
    item = get_object_or_404(Jobs, pk=pk)
    # Again, creates a form objects and binds data to it
    form = JobsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            # this creates a new jobs object of all the database so this if statement can redirect you to the hist page.
            jobs = Jobs.objects.all()
            form2 = form.save(commit=False)
            form2.save()
            return render(request, 'JobScraping/JobScraping_history.html', {'jobs': jobs})
        else:
            print(form.errors)
    else:
        return render(request, 'JobScraping/JobScraping_history.html')


# This view is a two-part view. If the request sent to this view is in POST it will delete the db item with the
# respective pk. If the request sent to this view is in GET it will send the user to a page that will ask them to
# confirm the choice to delete. When they confirm the request is sent back to this view again this time as POST.
def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Jobs, pk=pk)
    # if POST then delete
    if request.method == 'POST':
        item.delete()
        return redirect('JobScraping_history')
    # if anything other than POST check if they really want ot delete
    context = {'item': item,}
    return render(request, 'JobScraping/JobScraping_confirmDelete.html', context)


# This view loads the JobScraping_details.html which shows the data for a single job
def JobScraping_details(request, pk):
    # Changes pk from string to int
    pk = int(pk)
    # Gets the specific job data from the database by using the primary key (pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    # Creates an object with the data that can be sent to the html file
    context = {'job': jobs}
    print(context)
    # Renders the html file and sends the data to it in the variable 'context'
    return render(request, 'JobScraping/JobScraping_details.html', context)


# This view loads the editJob.html and passes it information so that it can display a form with the current data
# (which uses {'form': form},) and also save that form to the database with (which uses {'jobs': jobs},)
def JobScraping_editJob(request, pk):
    pk = int(pk)
    jobs = get_object_or_404(Jobs, pk=pk)
    form = JobsForm(data=request.POST or None, instance=jobs)
    context = {
        'form': form,
        'jobs': jobs,
    }
    return render(request, 'JobScraping/JobScraping_editJob.html', context)