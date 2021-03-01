from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Settings',
        'headline': 'Ini Adalah Settings',
    }
    return render(request, 'settings/index.html', context)
