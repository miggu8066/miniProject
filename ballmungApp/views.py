from django.shortcuts import render, redirect
from ballmungApp.models import rankInfo
from datetime import datetime
from django.core.paginator import Paginator

def ballmung(request):
    rankinfo = rankInfo.objects.all() #순위정보를 불러와 
    rankinfo = rankinfo.order_by("-score", "clearTime") #-score 역순

    paginator = Paginator(rankinfo, 10)  # 한페이지당 보여질 개수(데이터, 개수)
    rankinfo_10 = paginator.get_page(1) # 몇 페이지를 보여줄지 저장(1페이지의 10개의 데이터가 저장)
    return render(request, "ballmungApp/ballmung.html", {"rankdata":rankinfo_10})

def rank(request):
    if request.method == "GET": #명예의전당에서 전체순위표로 눌렀을때

        pageInfo = getPageInfo(request)

        return render(request, "ballmungApp/rank.html", {"rankdata":pageInfo})

    elif request.method == "POST": #게임화면에서 순위표에 post로 등록할떄
        name = request.POST.get("name")
        score = request.POST.get("score")
        clearTime = request.POST.get("clearTime")
        r = rankInfo()
        r.nickname = name
        r.score = score
        r.clearTime = clearTime
        r.regiDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        r.save()
        return redirect("/ballmung/rank/")

def getPageInfo(request):
    rankinfo = rankInfo.objects.all()
    rankinfo = rankinfo.order_by("-score", "clearTime") #-score 역순

    page_info = {
            "startPage" : 1,
            "endPage" : 10,
            "underPageCount" : 10, #하단 페이지의 보여질 개수
            "currentPage" : 1,
            "totalPage" : 0,
            "countPerPage" : 10, #페이지당 보여질 데이터수
            "pageRange" : [],
            "rankinfo_s" : [],
        }

        #현재페이지
    page_info["currentPage"] = request.GET.get("page")
    print(page_info["currentPage"])
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

    if page_info["currentPage"] >= page_info["totalPage"]:
            page_info["currentPage"] = page_info["totalPage"]
    #시작, 끝페이지
    page_info["startPage"] = (page_info["currentPage"] // page_info["underPageCount"]) * page_info["underPageCount"] + 1
    page_info["endPage"] = page_info["startPage"] + page_info["underPageCount"] - 1
    if page_info["endPage"] > page_info["totalPage"]: #끝 페이지가 전체페이지수를 넘어가면
        page_info["endPage"] = page_info["totalPage"]

    #장고 템플릿에서 for in에 쓸 리스트 (페이지 목록 보여주기)
    page_info["pageRange"] = range(page_info["startPage"], page_info["endPage"]+1)

    paginator = Paginator(rankinfo, page_info["countPerPage"])  # 한페이지당 보여질 개수(데이터, 개수)
    page_info["rankinfo_s"] = paginator.get_page(page_info["currentPage"]) # 몇 페이지를 보여줄지 저장(countPerPage 수 만큼 데이터 저장)

    return page_info
    
# Create your views here.
