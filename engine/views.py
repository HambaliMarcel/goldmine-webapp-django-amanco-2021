from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from engine.models import Source
from engine.table import EngineForm
from .formans import Formans
# Create your views here.


@login_required
def index(request):
    enginetable = Source.objects.all()
    context = {
        'title': 'Scrape Engine',
        'src': enginetable,
        'name': request.user.username
    }

    if request.method == "POST":
        if request.POST['sout'] == "Submit":
            logout(request)

        return redirect('index')

    return render(request, 'engine/index.html', context)


@login_required
def addnewsource(request):
    ans = Formans()
    context = {
        'title': 'Add Source',
        'name': request.user.username,
        'addsource': ans
    }
    if request.method == "POST":

        src = request.POST['source']
        auth = request.POST['auth']
        role = request.POST['role']

    return render(request, 'engine/addsource.html', context)
