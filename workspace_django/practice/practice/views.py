from django.shortcuts import render, redirect
from .models import Practice
from django.utils import timezone

def index(request):
    return render(request, 'index.html' , {'list' : Practice.objects.all().order_by('-id')})
# VIEWS에서 객체 all을 가지고 list에 보내줘야 한다 -> 최신순으로 정렬하기 위해 내림차순

def insert_form(request):
    return render(request , 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = Practice.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
    # 값을 가지고 객체를 만들었다(Django는 프레임워크)
    if result:
        return redirect('index')
    else:
        return redirect('insertform')


# id값을 같이 보내야 해서 id도 매개변수로 지정
def detail(request, id):
    return render(request, 'detail.html', {'dto': Practice.objects.get(id=id)})

def update_form(request , id):

    return render(request , 'update.html' , {'dto':Practice.objects.get(id=id)})
# 요청된 값을 가지고 해당하는 값을 하나 가지고 와서 update.html에 보낼건데 render=>그려준다

# 실제로 데이터를 업데이트 하고 제대로 업데이트 됐다면 원하는 페이지로 전달해라
def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    # where부분으로 생각하자(조건부분) -> 해당하는 id의 값을 가져와서 title값의 속성과 content값의 속성을 바꿔준다
    myboard = Practice.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    # print 해보면 왜 더한 결과가 2인지 알 것이다.
    print(result_title)
    print(result_content)
    print(type(result_title))
    print(type(result_content))

    # 원하는대로 동작했다면 detail로 가라 -> 뒤에 id값이 같이 오기 때문에 +id 해준다
    if result_title + result_content == 2:
        return redirect('/detail/'+id)
    # 원하는대로 동작 안했다면 updateform으로 가라
    else:
        return redirect('/updateform/'+id)

# 메소드 체이닝이 발생한 상태에서 메소드가 실행된 결과를 리턴한다
def delete(request , id):
    result_delete = Practice.objects.filter(id=id).delete()
    # print(result_delete)

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)