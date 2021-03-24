from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from engine.models import results
import sys
from engine.scraperName import scrapeName
import xlwt

from django.http import HttpResponse
# Create your views here.


@login_required
def index(request):
    enginetable = results.objects.all()
    context = {
        'title': 'History',
        'src': enginetable,
        'name': request.user.username
    }

    if request.method == 'POST' and 'sout' in request.POST:
        logout(request)
        return redirect('index')

    return render(request, 'history/index.html', context)


@login_required
def export_users_xls(request):
    from datetime import datetime

    now = datetime.now()
    response = HttpResponse(content_type='application/ms-excel')
    response[
        'Content-Disposition'] = f'attachment; filename="GOLDMINE-Scrape-Result-{now}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Number', 'Name', 'Loc', 'Contact', 'Sector', 'Likelihood', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = results.objects.all().values_list(
        'number', 'name', 'loc', 'contact', 'sector', 'likelihood')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
