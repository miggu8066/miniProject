from django.http import HttpResponse
from django.shortcuts import redirect, render
from puzzleApp.models import *
from django.core.paginator import Paginator
from .forms import FileUploadForm


def start(request):
    return render(request, "puzzleApp/puzzle_name.html")

def name(request):
    if request.method == 'GET':
        return render(request, 'puzzleApp/puzzle_name')
    nameck = request.POST.get('username')
    # if Puzzle.objects.filter(name=nameck).exists():
    #     return HttpResponse("<script>alert('이름이 중복되었습니다');location.href='/puzzleApp/';</script>")
    return render(request, 'puzzleApp/puzzle1.html', {'username':nameck})

def insert(request):
    if request.method == 'GET':
        return render(request, 'puzzleApp/puzzle1.html')
    username = request.POST.get('username')
    score = request.POST.get('temptime')
    date = request.POST.get('tempdate')
    p = Puzzle(name=username, score=score, date=date)
    p.save()
    return redirect('/puzzleApp/rank/')


def rank(request):
    puzzle = Puzzle.objects.all().order_by('score','date')

    page_info = {
        "startPage" : 1,
        "endPage" : 10,
        "underPageCount" : 10,
        "currentPage" : 1,
        "totalPage" : 0,
        "countPerPage" : 10,
    }
    page_info["currentPage"] = request.GET.get('page')
    if not page_info["currentPage"]:
        page_info["currentPage"] = 1
    else:
        page_info["currentPage"] = int(page_info["currentPage"])
        if page_info["currentPage"] <= 0:
            page_info["currentPage"] = 1
    page_info["totalPage"] = (puzzle.count() // page_info["countPerPage"]) + 1
    if (puzzle.count() % page_info["countPerPage"]) == 0:
        page_info["totalPage"] -= 1
    page_info["startPage"] = (page_info["currentPage"] // page_info["underPageCount"]) * page_info["underPageCount"] + 1
    page_info["endPage"] = page_info["startPage"] + page_info["underPageCount"] - 1
    if page_info["endPage"] > page_info["totalPage"]:
        page_info["endPage"] = page_info["totalPage"]
    pageRange = range(page_info["startPage"], page_info["endPage"]+1)
    paginator = Paginator(puzzle, page_info["countPerPage"]) 
    rankinfo_s = paginator.get_page(page_info["currentPage"]) 

    return render(request, 'puzzleApp/rank.html', {"rankdata":rankinfo_s, "page_info":page_info, "pageRange":pageRange})
    # return render(request, 'puzzleApp/rank.html', {'rankdata':puzzle})

def fileUpload(request):
    if request.method == 'POST':
        namecka = request.POST.get('username')
        img = request.FILES["imgfile"]
        fileupload = FileUpload(imgfile=img)
        filename = fileupload.imgfile.name
        fileupload.save()
        # imgre = Image.open("/media/images.png")
        # image_a = imgre.resize((400, 400))
        # image_a.save("/media/images_re.png/")

        return render(request, "puzzleApp/puzzle2.html", {'filename':filename,'username':namecka})

def fileUpload1(request):
    if request.method == 'POST':
        namecka = request.POST.get('username')
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
            'username':namecka
        }
        return render(request, 'puzzleApp/fileupload.html', context)

def file(request):
    return render(request, "puzzleApp/puzzle2.html")