from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')


def hosts(request):

    return render(request, 'hosts.html')


def guests(request):
    return render(request, 'guests.html')


def restaurants(request):
    return render(request, 'restaurants.html')


def grades(request):
    return render(request, 'grades.html')

