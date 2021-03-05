from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    logForm = LoginForm()
    context = {
        'title': 'Goldmine',
        'subtitle': '- Login ',
        'logform': logForm,
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        else:
            return render(request, 'index.html', context)

    if request.method == "POST":

        uname_login = request.POST['username']
        pass_login = request.POST['password']

        user = authenticate(
            request, username=uname_login, password=pass_login)

        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return redirect('index')

    return render(request, 'index.html', context)
