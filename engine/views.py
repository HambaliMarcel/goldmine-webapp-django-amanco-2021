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
    add = Formans(request.POST or None)
    context = {
        'title': 'Add Source',
        'name': request.user.username,
        'addsrc': add
    }

    if request.method == 'POST' and 'sout' in request.POST:
        logout(request)
        return redirect('index')

    if request.method == 'POST' and 'addsrc' in request.POST:
        if add.is_valid():
            add.save()
            return redirect('engine:index')

    return render(request, 'engine/addsource.html', context)


@login_required
def edit(request, id):
    edit = Source.objects.get(id=id)
    valid = Formans(request.POST or None, instance=edit)
    context = {
        'title': 'Edit',
        'name': request.user.username,
        'edt': edit,
    }

    if request.method == 'POST' and 'sout' in request.POST:
        logout(request)
        return redirect('index')

    if request.method == 'POST' and 'addsrc' in request.POST:
        if valid.is_valid():
            valid.save()
            return redirect('engine:index')

    return render(request, 'engine/edit.html', context)


@login_required
def delete(request, id):
    edit = Source.objects.get(id=id)
    edit.delete()
    return redirect('engine:index')
