from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "jan": "Eat no meat for the entire month!",
    "feb": "Walk for at least 20 minutes a day!",
    "march": "Learn django for at least 20 minutes a day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes a day!",
    "june": "Learn django for at least 20 minutes a day!",
    "july": "Eat no meat for the entire month!",
    "aug": "Walk for at least 20 minutes a day!",
    "sep": "Learn django for at least 20 minutes a day!",
    "oct": "Eat no meat for the entire month!",
    "nov": "Walk for at least 20 minutes a day!",
    "dec": "Learn django for at least 20 minutes a day!",
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
