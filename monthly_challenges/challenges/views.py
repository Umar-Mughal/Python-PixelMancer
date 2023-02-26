from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def monthly_challenge(request, month):
    challengeText = None
    if month == 'jan':
        challengeText = "Eat no meat for the entire month!"
    elif month == 'feb':
        challengeText = "Walk for at least 20 minutes a day!"
    elif month == 'march':
        challengeText = "Learn django for at least 20 minutes a day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challengeText)
