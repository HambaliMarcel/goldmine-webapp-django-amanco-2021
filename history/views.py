from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


@login_required
def index(request):
    context = {
        'title': 'History',
        'headline': 'Ini Adalah History'
    }
    if request.method == "POST":
        if request.POST['sout'] == "Submit":
            logout(request)

        return redirect('index')

    return render(request, 'engine/index.html', context)
