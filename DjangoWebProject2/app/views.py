from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    now = datetime.now() 

    return render(request, "app/index.html",{'content':'index에들어갈 content입니다.' + now.strftime("%A, %d %B, %Y at %X")})

def about(request):
    return render(
        request,
        "app/about.html",
        {
            'title' : "About 용 title입니다.",
            'content' : "about용content입니다."
        }
    )    