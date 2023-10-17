###############################################
# imports

# [get_object_or_404] is needed to use pk to find account data.
from django.shortcuts import render, redirect, get_object_or_404

# importing from our models.py and forms.py
from .models import Report
from .forms import ReportForm, UpdateReportForm

# imports needed for API
import requests
import json

###############################################
# CRUD functionality


# Function to render our home page
def be_home(request):
    # accessing modelForm-> UpdateReportForm for dropdown effect.
    form = UpdateReportForm(data=request.POST or None)

    # Checks if request method is POST
    if request.method == 'POST':
        # If the form is submitted, retrieve which Report the user wants to view
        pk = request.POST['report'] # assigning pk as the tag to identify report's fk to Report model
        # upon selection confirmation redirect to display page with pk
        return redirect('../displayReport/' + str(pk))

    content = {'form': form}  # Saves content to the template as a dictionary
    # Initial load renders the page; adds content of form to page
    return render(request, 'Brother_EDGAR/BrotherEDGAR_home.html', content)


# Function to render the Create New Reports page when requested.
def be_create(request):
    # accessing modelForm --> Report model with all fields
    form = ReportForm(data=request.POST or None)

    # Checks if request method is POST
    if request.method == 'POST':
        # This is a user input, so we need to validate entry.
        if form.is_valid():  # check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves the location identified in BrotherEDGAR_create.html form section.
            # Returns user back to the home page after saving the entry
            return redirect('BrotherEDGAR_home')

    content = {'form': form}
    return render(request, 'Brother_EDGAR/BrotherEDGAR_create.html', content)


# Function to render the Display Report page when requested
def be_displayReport(request, pk):
    # Retrieve the requested report using its primary key
    report = get_object_or_404(Report, pk=pk)

    response = report.searchType  # set variable for search type

    # Checks if request method is POST --> 'view details' button
    if request.method == 'POST':
        # direct user to selected search method
        if response == "yahoo-Finance":
            return redirect('../yahooFinance/' + str(report.pk))
        elif response == "EDGAR-Search":
            return redirect('../searchPage/' + str(report.pk))

    # Pass report info to the template
    content = {'report': report}
    return render(request, 'Brother_EDGAR/BrotherEDGAR_displayReport.html', content)


# Function to render the Update Report page when requested
def be_updateReport(request, pk):
    item = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, instance=item)

    # User defined entry so we need to validate before saving
    if form.is_valid():
        form.save()
        return redirect('../displayReport/'+str(item.pk))  # Redirect back to display page after updates are made

    context = {'form': form}
    return render(request, 'Brother_EDGAR/BrotherEDGAR_updateReport.html', context)


# Function to handle delete report requests
def be_deleteReport(request, pk):
    report = get_object_or_404(Report, pk=pk)

    # Confirming delete choice
    if request.method == "POST":
        report.delete()  # Delete entry from dB
        return redirect('BrotherEDGAR_home')

    context = {'item': report}  # item is used to display report name in the page
    return render(request, 'Brother_EDGAR/BrotherEDGAR_deleteReport.html', context)


################################################
# API functionality

# For EDGAR search page
def be_searchPage(request, pk):
    item = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, instance=item)

    context = {'form': form}
    return render(request, 'Brother_EDGAR/BrotherEDGAR_searchPage.html', context)


# For Yahoo Finance page. Includes using API
def be_yahooFinance(request, pk):
    item = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, instance=item)
    # user input ticker symbol
    symbol = item.tickerSymbol.lower()

    # yahoo Finance API using rapidapi services
    url = "https://yahoo-finance97.p.rapidapi.com/stock-info"

    payload = "symbol={}".format(symbol)  # passes in the ticker symbol of desired report

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "60b850c41amsh7a79b2aa401269cp1baaffjsn60ac1ee5d0d7",
        "X-RapidAPI-Host": "yahoo-finance97.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    # print('Json Response:', response.text)  # For dev use

    # parsing through the JSON response
    api_info = json.loads(response.text)
    company_name = api_info["data"]["longName"]
    business_summary = api_info["data"]["longBusinessSummary"]
    insider_confidence = api_info["data"]["heldPercentInsiders"]
    industry_confidence = api_info["data"]["heldPercentInstitutions"]
    fiftyDayAverage = api_info["data"]["fiftyDayAverage"]
    dayHigh = api_info["data"]["dayHigh"]
    dayLow = api_info["data"]["dayLow"]
    fullTimeEmployees = api_info["data"]["fullTimeEmployees"]
    debtToEquity = api_info["data"]["debtToEquity"]
    grossMargins = api_info["data"]["grossMargins"]
    grossProfits = api_info["data"]["grossProfits"]
    ask = api_info["data"]["ask"]
    askSize = api_info["data"]["askSize"]

    context = {'form': form, "company_name": company_name, "business_summary": business_summary,\
            "insider_confidence": insider_confidence, "industry_confidence": industry_confidence, "fiftyDayAverage": fiftyDayAverage,\
            "dayHigh": dayHigh, "dayLow": dayLow, "fullTimeEmployees": fullTimeEmployees, "debtToEquity": debtToEquity,\
            "grossMargins": grossMargins, "grossProfits": grossProfits, "ask": ask, "askSize": askSize}
    return render(request, 'Brother_EDGAR/BrotherEDGAR_yahooFinance.html', context)
