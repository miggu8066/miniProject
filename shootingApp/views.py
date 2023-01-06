from django.shortcuts import render, redirect
from shootingApp.models import Space_shooting
from django.core.paginator import Paginator


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
    shooting = Space_shooting.objects.all().order_by('-score','time_info')
    return render(request, "shootingApp/show.html", {'rankdata':shooting})

def rank(request):
    
    spaceShooting = Space_shooting.objects.all() 
    spaceShooting = spaceShooting.order_by("-score", "time_info") #-score 역순
    
    page_info = {
        "startPage" : 1,
        "endPage" : 10,
        "underPageCount" : 10, #하단 페이지의 보여질 개수
        "currentPage" : 1,
        "totalPage" : 0,
        "countPerPage" : 10, #페이지당 보여질 데이터수
    }

    #현재페이지
    page_info["currentPage"] = request.GET.get('page')
    if not page_info["currentPage"]: #현재페이지를 가져오지 못하면 1페이지를 보여줌
        page_info["currentPage"] = 1
    else:
        page_info["currentPage"] = int(page_info["currentPage"]) #숫자로 형변환
        if page_info["currentPage"] <= 0:
            page_info["currentPage"] = 1

    #총페이지수
    page_info["totalPage"] = (spaceShooting.count() // page_info["countPerPage"]) + 1
    if (spaceShooting.count() % page_info["countPerPage"]) == 0: #한페이지에 보여질 수에 딱 맞아 떨어지면 1을 빼줘야됨
        page_info["totalPage"] -= 1

    #시작, 끝페이지
    page_info["startPage"] = (page_info["currentPage"] // page_info["underPageCount"]) * page_info["underPageCount"] + 1
    page_info["endPage"] = page_info["startPage"] + page_info["underPageCount"] - 1
    if page_info["endPage"] > page_info["totalPage"]: #끝 페이지가 전체페이지수를 넘어가면
        page_info["endPage"] = page_info["totalPage"]

    #장고 템플릿에서 for in에 쓸 리스트 (페이지 목록 보여주기)
    pageRange = range(page_info["startPage"], page_info["endPage"]+1)

    paginator = Paginator(spaceShooting, page_info["countPerPage"])  # 한페이지당 보여질 개수(데이터, 개수)
    rankinfo_s = paginator.get_page(page_info["currentPage"]) # 몇 페이지를 보여줄지 저장(1페이지의 10개의 데이터가 저장)

    return render(request, "shootingApp/show.html", {"rankdata":rankinfo_s, "page_info":page_info, "pageRange":pageRange})