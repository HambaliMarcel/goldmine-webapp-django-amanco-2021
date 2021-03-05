from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


@login_required
def index(request):
    context = {
        'title': 'Settings',
        'headline': 'Ini Adalah Settings',
    }
    if request.method == "POST":
        if request.POST['sout'] == "Submit":
            logout(request)

        return redirect('index')

    return render(request, 'settings/index.html', context)
