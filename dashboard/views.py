from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from settings.models import setting, parameter
from engine.models import breaker
import subprocess
import sys
import os
# Create your views here.


@login_required
def index(request):
    context = {
        'name': request.user.username,
        'title': 'Dashboard',
        'subtitle': 'Welcome1',
    }
    name = request.user.username
    try:
        exist = setting.objects.get(uname=name)
        broker = breaker.objects.get(username=name)
    except:
        if request.method == 'POST' and 'newacc' in request.POST:
            obj = setting(param_def=True,
                          schedule="Daily",
                          exptype=True,
                          export="Anonym",
                          uname=name)
            obj.save()
            obj2 = breaker(username=name, status="stop")
            obj2.save()
            initializing()
            return redirect('engine:index')

    if request.method == 'POST' and 'newacc' in request.POST:
        initializing()
        return redirect('engine:index')

    return render(request, 'dashboard/index.html', context)


def initializing():
    # after webdriver installed, we can accross the sea
    osname = sys.platform
    if osname == 'win32':
        subprocess.call(
            'start /B /wait cmd /c "pip install webdriver-manager"', shell=True)

    elif osname == 'darwin':
        subprocess.call(
            'start /B /wait cmd /c "pip3 install webdriver-manager"', shell=True)
    else:
        print(sys.platform)
