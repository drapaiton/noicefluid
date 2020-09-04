from django.shortcuts import render


def index(request):
    # return render(request, 'lobby/index.html', {})
    return render(request, 'lobby/comingsoon.html', {})
