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
    if request.method == "GET":
        return render(request, "mainApp/main.html")
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
        return redirect("/ballmung/")
    
    return render(request, 'ballmungApp/rank.html')
# Create your views here.
