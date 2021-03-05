from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from engine.models import Source
from engine.table import EngineForm
# Create your views here.


@login_required
def index(request):
    enginetable = Source.objects.all()
    context = {
        'title': 'Scrape Engine',
        'heading': 'Selamat Datang di Engine',
        'src': enginetable,
    }

    if request.method == "POST":
        if request.POST['sout'] == "Submit":
            logout(request)

        return redirect('index')

    return render(request, 'engine/index.html', context)
