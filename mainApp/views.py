from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from ballmungApp.models import rankInfo
from puzzleApp.models import Puzzle

#메인 화면
def main(request):
    return render(request, 'mainApp/main.html')

#전체순위표
def rank(request):
    if request.method == "GET":
        rankinfo = rankInfo.objects.all() 
        rankinfo = rankinfo.order_by("-score", "clearTime") #-score 역순
        
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
        page_info["totalPage"] = (rankinfo.count() // page_info["countPerPage"]) + 1
        if (rankinfo.count() % page_info["countPerPage"]) == 0: #한페이지에 보여질 수에 딱 맞아 떨어지면 1을 빼줘야됨
            page_info["totalPage"] -= 1

        #시작, 끝페이지
        page_info["startPage"] = (page_info["currentPage"] // page_info["underPageCount"]) * page_info["underPageCount"] + 1
        page_info["endPage"] = page_info["startPage"] + page_info["underPageCount"] - 1
        if page_info["endPage"] > page_info["totalPage"]: #끝 페이지가 전체페이지수를 넘어가면
            page_info["endPage"] = page_info["totalPage"]

        #장고 템플릿에서 for in에 쓸 리스트 (페이지 목록 보여주기)
        pageRange = range(page_info["startPage"], page_info["endPage"]+1)

        paginator = Paginator(rankinfo, page_info["countPerPage"])  # 한페이지당 보여질 개수(데이터, 개수)
        rankinfo_s = paginator.get_page(page_info["currentPage"]) # 몇 페이지를 보여줄지 저장(1페이지의 10개의 데이터가 저장)


        return render(request, "mainApp/rank.html", {"rankdata":rankinfo_s, "page_info":page_info, "pageRange":pageRange})
    elif request.method == "POST": 
        return render(request, "mainApp/main.html")
        #return redirect("/ballmung/")

#볼명랭크 
def ballmungRank(request):

    rankinfo = rankInfo.objects.all() 
    rankinfo = rankinfo.order_by("-score", "clearTime") #-score 역순
    
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
    page_info["totalPage"] = (rankinfo.count() // page_info["countPerPage"]) + 1
    if (rankinfo.count() % page_info["countPerPage"]) == 0: #한페이지에 보여질 수에 딱 맞아 떨어지면 1을 빼줘야됨
        page_info["totalPage"] -= 1

    #시작, 끝페이지
    page_info["startPage"] = (page_info["currentPage"] // page_info["underPageCount"]) * page_info["underPageCount"] + 1
    page_info["endPage"] = page_info["startPage"] + page_info["underPageCount"] - 1
    if page_info["endPage"] > page_info["totalPage"]: #끝 페이지가 전체페이지수를 넘어가면
        page_info["endPage"] = page_info["totalPage"]

    #장고 템플릿에서 for in에 쓸 리스트 (페이지 목록 보여주기)
    pageRange = range(page_info["startPage"], page_info["endPage"]+1)

    paginator = Paginator(rankinfo, page_info["countPerPage"])  # 한페이지당 보여질 개수(데이터, 개수)
    rankinfo_s = paginator.get_page(page_info["currentPage"]) # 몇 페이지를 보여줄지 저장(1페이지의 10개의 데이터가 저장)

    return render(request, "mainApp/ballmung_rank.html", {"rankdata":rankinfo_s, "page_info":page_info, "pageRange":pageRange})


#퍼즐랭크 
def puzzleRank(request):
    puzzle = Puzzle.objects.all().order_by('score','date')
    return render(request, 'puzzleApp/show.html', {'data':puzzle})

    
# Create your views here.
