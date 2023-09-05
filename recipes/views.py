from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return HttpResponse('home')
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Patrick'
    })


def contact(request):
    return HttpResponse('contato')


def about(request):
    return HttpResponse('sobre')
