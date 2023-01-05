from django.shortcuts import render, redirect
from shootingApp.models import Space_shooting



def main(request):
    return render(request, "shootingApp/sht.html")


def insert(request):
    if request.method == 'GET':
        return render(request, 'shooting/sht.html')
    username = request.POST.get('username')
    score = request.POST.get('temptime')
    date = request.POST.get('tempdate')
    p = Space_shooting(name=username, score=score, time_info=date)
    p.save()
    return redirect('/shootingApp/show/')


def show(request):
    shooting = Space_shooting.objects.all().order_by('score','time_info')
    return render(request, "shootingApp/show.html", {'data':shooting})