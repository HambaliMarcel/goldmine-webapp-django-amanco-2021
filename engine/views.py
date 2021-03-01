from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Scrape Engine',
        'heading': 'Selamat Datang di Engine',
    }
    return render(request, 'engine/index.html', context)
