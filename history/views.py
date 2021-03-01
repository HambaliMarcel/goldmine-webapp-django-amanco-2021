from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'History',
        'headline': 'Ini Adalah History'
    }
    return render(request, 'history/index.html', context)
