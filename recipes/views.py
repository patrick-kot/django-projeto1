from django.shortcuts import render


# def home(request):
#     return HttpResponse('home')
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Patrick'
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Patrick'
    })
