from django.shortcuts import render, redirect
from .models import MyBoard , MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password , check_password

# def index(request):
#return render(request, 'index.html' , {'list' : MyBoard.objects.all().order_by('-id')})
# # VIEWS에서 객체 all을 가지고 list에 보내줘야 한다 -> 최신순으로 정렬하기 위해 내림차순

def index(request):
    myboard = MyBoard.objects.all().order_by('-id')
    paginator = Paginator(myboard, 5) #5개씩 자른다 => 페이지당 5개씩 보여주기
    page_num = request.GET.get('page', '1') #현재 페이지가 없으면 1로 불러온다
    # http://localhost:8000/myboard/?page=1 처럼 GET 방식으로 호출된 URL에서 page값을 가져옴
    # page값이 없이 호출된 경우 디폴트로 1이라는 값을 설정한다

    # 페이지에 맞는 모델 가져오기
    page_obj = paginator.get_page(page_num)
    #요청된 페이지에 해당하는 페이징 객체를 생성 -> 장고 내부적으로는 데이터 전체를 조회하지 않고 해당 페이지의 데이터만 조회

    # 관련 메서드 (찾아보기) --> 검사하지 않는 숙제
    print(type(page_obj)) #<class 'django.core.paginator.Page'>
    print(page_obj.count) #<bound method Sequence.count of <Page 1 of 22>>
    print(page_obj.paginator.num_pages) #전체 게시물 개수
    print(page_obj.paginator.page_range) # range(1,23)
    print(page_obj.has_next()) #다음 페이지 유무
    print(page_obj.has_previous()) # 이전 페이지 유무
    try:
        print(page_obj.next_page_number()) #다음 페이지 번호
        print(page_obj.previous_page_number()) #이전 페이지 번호 -> 첫페이지에선 오류 발생

    except:
        print(page_obj.start_index()) #현재 페이지 시작 인덱스(1부터 시작) -> 1이 나옴
        print(page_obj.end_index()) #현재 페이지의 끝 인덱스(1부터 시작) -> 5개씩이니까 5가 나옴
        
    return render(request, 'index.html' , {'list':page_obj})
    # index.html에 페이징 객체를 전달



def insert_form(request):
    return render(request , 'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = MyBoard.objects.create(myname=myname , mytitle=mytitle, mycontent=mycontent, mydate= timezone.now())
    # 값을 가지고 객체를 만들었다(Django는 프레임워크)
    if result:
        return redirect('index')
    else:
        return redirect('insertform')

# id값을 같이 보내야 해서 id도 매개변수로 지정
def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})

# 데이터를 받아줌
def update_form(request , id):

    return render(request , 'update.html' , {'dto':MyBoard.objects.get(id=id)})
# 요청된 값을 가지고 해당하는 값을 하나 가지고 와서 update.html에 보낼건데 render=>그려준다

# 실제로 데이터를 업데이트 하고 제대로 업데이트 됐다면 원하는 페이지로 전달해라
def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    # where부분으로 생각하자(조건부분) -> 해당하는 id의 값을 가져와서 title값의 속성과 content값의 속성을 바꿔준다
    myboard = MyBoard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    # print 해보면 왜 더한 결과가 2인지 알 것이다.

    # 원하는대로 동작했다면 detail로 가라 -> 뒤에 id값이 같이 오기 때문에 +id 해준다
    if result_title + result_content == 2:
        return redirect('/detail/'+id)
    # 원하는대로 동작 안했다면 updateform으로 가라
    else:
        return redirect('/updateform/'+id)

# 메소드 체이닝이 발생한 상태에서 메소드가 실행된 결과를 리턴한다
def delete(request , id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    # print(result_delete)

    if result_delete[0]:
        return redirect('index')
    else:
        return redirect('/detail/'+id)

# get방식으로 요청한다면 register 페이지가 응답될거고, post방식으로 요청됐다면 해당 값을 받아서 회원가입한다.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        mymember = MyMember(myname=myname , mypassword=make_password(mypassword) , myemail=myemail)
        mymember.save()
        
        return redirect('/') #root로 돌아가기


    return redirect('/') #root로 돌아가기

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        myname = request.POST['myname'] #request에 post로 넘어온 my name
        mypassword = request.POST['mypassword']

        mymember = MyMember.objects.get(myname=myname)
        
        if check_password(mypassword, mymember.mypassword): #mymemeber에 저장되어 있는 mypassword
            request.session['myname'] = mymember.myname # 같다면 변수로 저장 -> 클라이언트가 요구하는 정보를 session에서 미리 받음(?)
            return redirect('/')
        else:
            return redirect('/login') #아니라면 로그인화면으로 다시 이동

def logout(request):
    del request.session['myname']
    return redirect('/')
