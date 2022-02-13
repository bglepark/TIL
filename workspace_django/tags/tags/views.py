from django.shortcuts import render

# index에 있는 name이라는 변수 안에 본인 이름을 전달해준다
# render : 해당 요청에 맞게 그려준다. 요청을 받으면 해당 index.html 템플릿을 찾아서 거기에 name에 변수를 넣어줘서 그려줘라
# server-sider-rendering
def index(request):
    return render(request , 'index.html' , {'name': 'hyunsoo'})