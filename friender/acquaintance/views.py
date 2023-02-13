from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import NameForm
from django.views import generic


class UserListView(generic.ListView):
    model = User


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'main.html', {'form': form})


def my_users(request):
    users = User.objects.all()
    return render(request, 'main.html', {'users': users})


def main(request):
    count_users = User.objects.all().count()
    return render(
        request,
        'main.html',
        context=
        {'количество пользователей':count_users},
    )


def hosts(request):
    return render(request, 'hosts.html')


def guests(request):
    return render(request, 'guests.html')


def restaurants(request):
    return render(request, 'restaurants.html')


def grades(request):
    return render(request, 'grades.html')

