from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1><a href='/hello01/test'>Hello, Django</a></h1>")
# /를 붙이면 해당 페이지 밑이라는 의미이다.
# 클릭했을 때 다시 돌아오도록 만듬 -> urls.py 수정 필요
def test(request):
    return HttpResponse("<h1><a href='/hello01'>return</a></h1>")

def my(request):
    return HttpResponse("<h1>자기이름</h1>")