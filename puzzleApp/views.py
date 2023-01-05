from django.http import HttpResponse
from django.shortcuts import redirect, render
from puzzleApp.models import Puzzle


def start(request):
    return render(request, "puzzleApp/puzzle_name.html")

def name(request):
    if request.method == 'GET':
        return render(request, 'puzzleApp/puzzle_name')
    nameck = request.POST.get('username')
    if Puzzle.objects.filter(name=nameck).exists():
        return HttpResponse("<script>alert('이름이 중복되었습니다');location.href='/puzzleApp/start';</script>")
    return render(request, 'puzzleApp/puzzle1.html', {'username':nameck})

def insert(request):
    if request.method == 'GET':
        return render(request, 'puzzleApp/puzzle1.html')
    username = request.POST.get('username')
    score = request.POST.get('temptime')
    date = request.POST.get('tempdate')
    p = Puzzle(name=username, score=score, date=date)
    p.save()
    return redirect('/puzzleApp/show/')


def show(request):
    puzzle = Puzzle.objects.all().order_by('score','date')
    return render(request, 'puzzleApp/show.html', {'data':puzzle})

def test(request):
    return render(request, "test.html")