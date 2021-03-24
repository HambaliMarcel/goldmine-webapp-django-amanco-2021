from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from engine.models import Source, breaker
from engine.table import EngineForm
from .formans import Formans
from .scraperName import scrapeName
# Create your views here.


@login_required
def index(request):
    enginetable = Source.objects.all()
    context = {
        'title': 'Scrape Engine',
        'src': enginetable,
        'name': request.user.username,
        'stat': breaker.objects.get(username=request.user.username)
    }
    name = request.user.username
    if request.method == 'POST' and 'sout' in request.POST:
        logout(request)
        return redirect('index')

    if request.method == 'POST' and 'scrap' in request.POST:
        broker = breaker.objects.get(username=request.user.username)
        if (broker.status == "stop"):
            print("proses menghidupkan dari keadaan", broker.status)
            broker.status = "run"
            broker.save(update_fields=['status'])
            print("status saat ini : ", broker.status)
            return scrapeName(name, 1)

        if (broker.status == "run"):
            print("proses mematikan dari keadaan", broker.status)
            broker.status = "stop"
            broker.save(update_fields=['status'])
            print("status saat ini : ", broker.status)
            return redirect('engine:index')

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
