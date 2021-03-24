from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from settings.models import setting, parameter
# Create your views here.


@login_required
def index(request):
    param_table = parameter.objects.all()
    uname = request.user.username
    edit = setting.objects.get(uname=uname)

    context = {
        'tbl': param_table,
        'title': 'Settings',
        'name': request.user.username,
        'edit': edit,
    }
    if request.method == 'POST' and 'sout' in request.POST:
        logout(request)
        return redirect('index')

    if request.method == 'POST' and 'save' in request.POST:
        dp = request.POST.get("default-p")
        if (dp == "on"):
            dp = True
        else:
            dp = False

        extp = request.POST.get("exptype")
        if (extp == "on"):
            extp = True
        else:
            extp = False

        edit.param_def = dp
        edit.schedule = request.POST.get("schedule")
        edit.exptype = extp
        edit.save()
        return redirect('settings:index')

    return render(request, 'settings/index.html', context)
