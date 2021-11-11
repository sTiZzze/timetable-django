from django.shortcuts import render
from .models import New, TimeTable
from django.contrib.auth.decorators import login_required
import datetime



@login_required(login_url='login')
def create_home(request):
    value = datetime.datetime.now()
    list = TimeTable.objects.all()
    if value.isoweekday() == 1:
        create = TimeTable.objects.order_by('time').filter(day='Понедельник')
        return render(request, 'create/create_home.html', {'create': create, 'value': value})
    elif value.isoweekday() == 2:
        create = TimeTable.objects.order_by('time').filter(day='Вторник')
        return render(request, 'create/create_home.html', {'create': create, 'value': value})
    elif value.isoweekday() == 3:
        create = TimeTable.objects.order_by('time').filter(day='Среда')
        return render(request, 'create/create_home.html', {'create': create, 'value': value})
    elif value.isoweekday() == 4:
        create = TimeTable.objects.order_by('time').filter(day='Четверг')
        return render(request, 'create/create_home.html', {'create': create, 'value': value, 'list': list})
    elif value.isoweekday() == 5:
        create = TimeTable.objects.order_by('time').filter(day='Пятница')
        return render(request, 'create/create_home.html', {'create': create, 'value': value})
    else:
        create = TimeTable.objects.order_by('time').filter(day='Понедельник')
        return render(request, 'create/create_home.html', {'create': create, 'value': value})



@login_required(login_url='login')
def mond(request):
    create = TimeTable.objects.order_by('time').filter(day='Понедельник')
    return render(request, 'create/mond.html', {'list': create})

def Tuesday(request):
    create = TimeTable.objects.order_by('time').filter(day='Вторник')
    return render(request, 'create/mond.html', {'list': create})

def Wednesday(request):
    create = TimeTable.objects.order_by('time').filter(day='Среда')
    return render(request, 'create/mond.html', {'list': create})

def Thursday(request):
    create = TimeTable.objects.order_by('time').filter(day='Четверг')
    return render(request, 'create/mond.html', {'list': create})

def Friday(request):
    create = TimeTable.objects.order_by('time').filter(day='Пятница')
    return render(request, 'create/mond.html', {'list': create})
