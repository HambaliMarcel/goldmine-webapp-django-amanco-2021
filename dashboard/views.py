from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    context = {
        'name': request.user.username,
        'title': 'Dashboard',
        'subtitle': 'Welcome1',
    }

    print(request.user)
    return render(request, 'dashboard/index.html', context)
