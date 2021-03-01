from django.shortcuts import render
from .forms import LoginForm


def index(request):
    logForm = LoginForm()
    context = {
        'title': 'Goldmine',
        'subtitle': '- Login ',
        'logform': logForm,
    }
    return render(request, 'index.html', context)
