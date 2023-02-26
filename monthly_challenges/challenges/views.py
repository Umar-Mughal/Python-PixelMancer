from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month == 0 or month > len(months):
            return HttpResponseNotFound("Invalid month!")
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Something went wrong!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
