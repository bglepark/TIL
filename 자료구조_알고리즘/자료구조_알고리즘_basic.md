# 자료구조&알고리즘 basic

- 내용 

  - 자료구조 기본 개념
  - 기본 알고리즘
  - 파이썬 프로그래밍
  - 현업 알고리즘 문제



## 선형 자료 구조

> 데이터를 한 줄로 순차적으로 표현한 형태 --> 선형 리스트 , 연결 리스트 , 원형 연결 리스트 , 스택 , 큐



### 1. 선형 리스트

- 데이터를 일정한 순서로 나열한 자료 구조
- 순차 리스트(Ordered List)라고도 함
- 선형 리스트는 입력 순서대로 저장하는 데이터에 해당한다.
- 배열 형태이며 추가/삽입/삭제가 가능하다.
- 추가/삽입/삭제에 많은 작업이 필요하므로 오버헤드 발생(*)
- 공간적 및 논리적으로 배열이 형성되어 있다. -> 접근 속도가 빠르다.
  - ex) 시계열 데이터

> 오버헤드 발생 : 리스크가 큰 데이터일 때 , 무언가를 삽입 혹은 삭제하는 과정에서 많은 일이 발생



> 카톡 온 순서대로 데이터를 선형 리스트로 표현

```python
## 함수 선언부
def add_data(friend): # katok 배열에 friend 추가
    katok.append(None) #배열 맨 뒤에 빈칸 추가
    kLen = len(katok)
    katok[kLen-1] = friend # (배열 길이 - 1) 위치에 데이터 삽입
    
def insert_data(position , friend): #katok 배열 내 원하는 position에 friend 추가
    katok.append(None)
    kLen = len(katok) #position에 friend가 들어가도록 배열을 한칸씩 이동해줘야함
    for i in range(kLen-1 , position , -1):
   		katok[i] = katok[i-1]
    	katok[i-1] = None #옮긴 변수는 None으로 빈칸으로 만들어줌
    katok[position] = friend
    
def delete_data(position):
    katok[position] = None #빈칸으로 처리
    kLen = len(katok)
    for i in range(position+1, kLen , 1): #삭제한 position 뒤부터니까 position+1
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[kLen-1]) #칸 자체를 삭제
    
## 전역 변수부
katok = [] 
select = -1

## 메인 코드 부분
if __name__ =='__main__':

    while(select!=4):
        select = int(input('선택하세요(1:추가 , 2:삽입 , 3:삭제 , 4:종료) -->'))

        if select == 1:
            data= input("추가할 데이터 -->")
            add_data(data)
            print(katok)
        elif select ==2:
            pos = int(input('삽입할 위치 -->'))
            data = input('추가할 데이터 -->')
            insert_data(pos,data)
            print(katok)
        elif select ==3 :
            pos = int(input('삭제할 위치 -->'))
            delete_data(pos)
            print(katok)
        elif select ==4:
            print(katok)
            exit
        else:
            print('1~4 중 하나를 입력하세요.')
            continue
```



### 2. 단순 연결 리스트

- 노드라고 표현
- 논리적으로는 붙어있지만 물리적으로는 떨어져 있다.
- 화살표로 표시된 연결(링크 , Link)을 따라가면 선형 리스트 순서와 같다.
- 해당 노드의 앞뒤 링크만 수정하면 되므로 오버헤드가 거의 발생하지 않는다.(*)

```
노드는 데이터와 링크로 구성된 항목이다.
```

> head : 가장 앞의 노드의 값(주소값)을 가지고 있다.
>
> current : 현재 작업하고 있는 노드의 값을 가지고 있다.
>
> pre : 현재 작업 중인 노드의 앞 노드값을 가지고 있다.



> 단순 연결 리스트를 통한 데이터 추가/삽입/삭제

```python
## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None


## 전역

## 메인
node1 = Node()
node1.data = 'A'

node2 = Node()
node2.data = 'B'
node1.link = node2 #node1의 link는 node를 가리킴

node3 = Node()
node3.data = 'C'
node2.link = node3

node4 = Node()
node4.data = 'D'
node3.link = node4

node5 = Node()
node5.data = 'E'
node4.link = node5

# 다른 예시
# print(node1.data , end= ' ')
# print(node1.link.data , end = ' ')
# print(node1.link.link.data , end = ' ')
# print(node1.link.link.link.data , end = ' ')
# print(node1.link.link.link.link.data , end = ' ')

# 중간에 데이터 삽입
newNode = Node()
newNode.data = '홍길동'
newNode.link = node2.link
node2.link = newNode

# 중간 데이터 삭제
node2.link = node3.link
del(node3)

# link가 None이면 출력 그만 , 계속 연결해서 출력하는 방법
current = node1
print(current.data , end= ' ')
while current.link != None:
    current = current.link # 계속 그 다음 노드로 이동
    print(current.data, end=' ')
```



>  단순 연결 리스트를 통한 데이터 추가/삽입/삭제 (함수 이용)

```python
## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start): #출력하는 함수
    current = start
    print(current.data , end = ' ')
    while current.link != None:
        current = current.link
        print(current.dat , end = ' ')
    print()

# head 변경 : 첫 번째 노드 삽입
def insertNode(findData , insertData):
    global memory , head , current , pre
    
    # 첫번째 노드 앞에 삽입할 경우
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    # 두번째 노드 이후 삽입 (중간 노드 삽입)
    current = head # 첫번째부터 변경시작을 위해 변수 선언
    while current.link != None:
        pre = current #current가 다음 link로 가기 전에 pre에 저장
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current #node는 current에 연결
            pre.link = node #pre는 node에 연결
            return
        
    # findData가 없는 경우 맨 뒤에 삽입
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드 삭제하기
def deleteNode(deleteData):
    global memory , head , current , pre
    
    # 첫 노드 삭제 시
    if deleteData == head.data :
        current = head
        head = head.link #head 다음 변수를 head로 지정
        del(current)
        return
    
    # 두 번째 이후 노드 삭제 시
    current = head
    while current.link!=None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
        
# 노드 검색하기
def findNode(findData):
    global memory , head , current , pre
    current = head
    if current.data == findData:
        return current
    while current.link!=None:
        current = current.link
        if current.data == findData:
            return current
    return Node() # 못 찾았을 경우 빈 노드 return
        
    
## 전역
memory = []
head , current , pre = None , None , None , None 
dataArray = ['홍길동' , '이순신' , '사오정' , '손오공' , '강감찬']

## 메인
node = Node()
node.data = dataArray[0]
head = node # 첫 번째 변수를 head로 지정
memory.append(node) # 홍길동

for data in dataArray[1:] : # ['이순신' , '사오정' , '손오공' , '강감찬']
    pre = node
    node = Node() #새로운 node class를 생성하기 전에 pre 라는 변수에 저장
    node.data = data
    pre.link = node
    memory.append(node)
    

```



### 3. 원형 연결 리스트

- 단순 연결 리스트와 구조와 구현 코드가 상당히 유사하다
- 리스트 형태가 원(Circle) 형태로 구성(계속 회전하면서 연속 가능)
- 오버헤드가 발생하지 않음
- node의 link가 head이면 마지막 노드를 가리킨다.



### 4. 스택 

- 스택(Stack) 자료구조는 한쪽 끝이 막힌 형태
- 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조
- First In , Last Out
- top의 초깃값은 -1 이다.
- 스택 기본 구조
  - 스택에 데이터를 삽입하는 작동 : push => top을 한 칸 위로 이동/top 위치에 데이터 입력
  - 스택에 데이터를 추출하는 작동 : pop=> top 위치의 데이터를 추출/ top을 한 칸 아래로 이동
  - 스택에 들어 있는 가장 위의 데이터 : top

> 스택의 간단 구현

```python
## 함수

## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 #초기값

## 메인
# PUSH
top+=1
stack[top] = '커피'
top+=1
stack[top] = '녹차'
top+=1
stack[top] = '꿀물'
print(stack)

# POP
data = stack[top]
stack[top] = None
top-=1
print(stack)

data = stack[top]
stack[top] = None
top-=1
print(stack)

data = stack[top]
stack[top] = None
top-=1
print(stack)

```



> 스택 구현(함수 이용)

```python
## 함수
def isStackFull(): #stack이 꽉차있는지 확인하는 함수
    global SIZE , stack , top
    if (top-1)>=SIZE: #꽉 찬 경우
        return True
    else :
        return False
    
def push(data):
    global SIZE , stack , top
    if isStackFull() : #True일 경우(꽉 찬 경우)
        print('스택이 꽉 찼습니다.')
        return # 꽉 찬 경우 그냥 return
    top+=1
    stack[top]=data #stack의 top 부분에 data 삽입
    
def isStackEmpty():
    global SIZE , stack , top
    if (top<=-1):
        return True
    else:
        return False
    
def pop():
    global SIZE , stack , top
    if isStackEmpty:
        print('스택이 비었습니다.')
        return None #일관성을 위해 None을 씀
    data = stack[top]
    stack[top] = None
    top-=1
    return data

def peek():#검색 기능
    global SIZE , stack , top
    if isStackEmpty:
        print('스택이 비었습니다.')
        return None
    return stack[top]
    
        
## 전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 # 초기값

## 메인
push('커피1')
push('커피2')
print(stack)

print('다음 예정' , peek())

retrData = pop()
print('pop()-->' , retrData)
```



### 5. 큐

- 큐(Queue) 자료구조는 입구와 출구가 따로 있는 원통 형태
- 먼저 입력된 데이터가 가장 먼저 출력된다.
- First In , First Out
- 큐 기본 구조
  - 초기 상태의 빈 큐의 경우 front = reat = -1
  - 큐에 데이터를 삽입하는 작동 : enQueue(인큐) => rear을 오른쪽으로 한 칸 이동(+1) / rear 위치에 데이터 입력
  - 데이터를 추출하는 작동 : dqQueue(데큐) => front를 오른쪽으로 한 칸 이동(+1) / front 위치의 데이터를 출력
  - 저장된 데이터 중 첫번째 데이터 : front(머리)
  - 저장된 데이터 중 마지막 데이터 : rear(꼬리)


> 큐의 간단 구현

```python
#front와 rear가 같으면 que가 비어있다고 봄

## 함수

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 #초깃값으로 -1을 설정

## 메인
# eqQueue : 데이터 삽입 : 꼬리를 한칸 증가시키고, 꼬리 자리에 데이터삽입
rear +=1
queue[rear]='화사' #rear ==0
rear +=1
queue[rear]='솔라' # rear == 1
rear +=1
queue[rear]='문별' # rear == 2

print('출구<---' , queue , '<---입구')

#deQueue : 데이터 추출 : 머리를 하나 증가시키고 머리에 있는 애를 내보낸다.
front+=1
data = queue[front] # front == 0
queue[front] = None
print('손님 : ' , data)
front+=1
data = queue[front] # front == 1
queue[front] = None
print('손님 : ' , data)
front+=1
data = queue[front] # front == 2
queue[front] = None
print('손님 : ' , data)
print('출구<---' , queue , '<---입구')

```



> 큐 구현(함수 이용)

```python
## 함수
def  isQueueFull() : #queue가 꽉 차 있는가?
    global SIZE, queue, front, rear
    if (rear == SIZE-1) : #rear 가 queue의 SIZE -1이면 꽉 차 있다.
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1 # rear값 1 증가
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) : #front와 rear 값이 같으면 비어있다.
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front += 1 # front값을 1 증가
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅~')
        return None
    return queue[front+1]
## 전역
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('선미')
# enQueue('재남')
# print('출구<---', queue , '<--입구')
# enQueue('아이유')
# print('출구<---', queue , '<--입구')

print('출구<---', queue , '<--입구')
print('밥 손님:', deQueue())
print('다음 손님... 준비 : ', peek())
print('밥 손님:', deQueue())
print('출구<---', queue , '<--입구')
print('밥 손님:', deQueue())
```



> 큐의 기능 통합 버전
>
> => 다음과 같이 front , rear의 위치를 이동하는 경우 오버헤드가 발생한다.

```python
## rear = SIZE-1 의 경우 큐가 꽉 찼다고 가정했었다.
## 그러나 (rear = SIZE-1) and (front!=-1) 의 경우 앞쪽에 여유가 있어도 큐가 꽉 찼다고 표현된다.

## 1. front+1 위치부터 rear 위치까지 왼쪽으로 한 칸씩 이동시킨다.
## 2. front 값에서 1을 뺀다.
## 3. rear 값에서 1을 뺀다.

def  isQueueFull() :
    global SIZE, queue, front, rear
    if (rear!=SIZE-1):
        return False
    elif (rear ==SIZE-1) and (front == -1):  ##진짜 꽉찬경우
        return True
    else:
        for i in range(front,+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear -=1
        return False
```



#### * 원형 큐

- 일반 큐의 오버헤드를 보완한 원형 형태의 큐
- 일반 큐의 front와 rear를 붙여둔 원형 형태의 모습
- 일반 큐와 동일하게 front ==rear 의 경우 큐가 비어있다.
- 원형 큐에서는 front와 rear의 초깃값을 0으로 설정한다.
- front와 rear가 마지막 블럭에서 처음으로 이동할 때 그 값이 블럭의 수보다 커지는 것을 방지하기 위해 %SIZE로 값 초기화
  - SIZE=5 , rear가 4에서 0으로 넘어가지 않고 5가 되면 블럭의 크기를 초과하게 되어서 초기화가 필요하다.
- 원형 구조이기에 꽉 찬 상태에서도 front==rear가 되어 empty로 인식하는 경우가 있다.
  - 이를 방지하기 위해 한 칸 비워둔 상태인 (rear+1)%SIZE == front의 경우를 꽉 찬 상태로 처리한다.

```python
def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False
    
def  isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1) % SIZE == front) :
        return True
    else :
        return False
    
def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data
    
def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front= (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐 텅~')
        return None
    return queue[(front+1) % SIZE]

## 전역
SIZE = 5
queue = [ None for _ in range(SIZE)]
front = rear = 0

## 메인
enQueue('길동')
enQueue('세종')
enQueue('순신')
enQueue('민호')
enQueue('파이썬')
print('출구<---', queue , '<--입구')
print('밥 손님:', deQueue())
print('밥 손님:', deQueue())
print('출구<---', queue , '<--입구')
enQueue('넘파이')
print('출구<---', queue , '<--입구')
enQueue('판다스')
print('출구<---', queue , '<--입구')
```



## 비선형 자료 구조

> 하나의 데이터 뒤에 여러 데이터가 이어지는 형태 -> 트리 , 그래프



### 1. 트리

- 회사 사장을 필두로 그 아래 직책이 구성되어 있는 조직표 

- 컴퓨터의 상위 폴더 안에 하위 폴더가 계속 이어지는 구조

- 나무를 거꾸로 뒤집어 놓은 형태와 비슷해 Tree라고 부름

- 이진 트리(*)를 가장 많이 사용한다.

  > 맨 위의 노드 : root 
  >
  > 하위 노드를 갖는 노드 : 부모 노드
  >
  > 하위 노드 : 자식 노드
  >
  > 연결 선 : 에지
  >
  > 자식의 개수 : 차수
  >
  > 차수가 0인 노드 : 리프 노드 (자식이 없는 마지막 노드)



#### * 이진 트리

- 모든 노드의 자식이 최대 2개인 트리를 이진 트리라고 부른다. (자식이 2개 이하로 구성)

- 루트 입장에서 좌측 자식의 트리를 왼쪽 서브트리, 우측 자식의 트리를 오른쪽 서브트리라 부른다.
- 번호를 메길 땐 위에서 왼쪽으로 숫자를 메김. 자리가 비어있어도 번호는 가져간다.
- 포화 이진 트리 : 꽉 찬 이진 트리
- 완전 이진 트리 : 조금 비어있지만, 번호는 빈 번호가 없어야 한다.
- 일반 이진 트리 : 조금 비어있고, 빈 번호도 존재하는 트리
- 평향 이진 트리 : 좌측 혹은 우측으로만 에지가 뻗어있는 트리



> 이진 트리의 기본 구조

```python
## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
## 전역

## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data)
print(node1.left.data , node1.right.data)
print(node1.left.left.data , node1.left.right.data , node1.right.left.data)
```



> 이진 트리 구현(함수 이용 + 검색 기능)

```python
## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역변수
memory = []
root = None
nameAry = ['블랙핑크' , '레드벨벳' , '마마무' , '에이핑크' , '걸스데이' , '트와이스']

## 메인

# 첫 노드 생성(=루트 노드)
node = TreeNode()
node.data = nameAry[0] # 블랙핑크를 node.data로 설정
root = node #root를 node로 설정
memory.append(node) # 빈 메모리에 node를 삽입

for name in nameAry[1:] : #['레드벨벳' , '마마무' , '에이핑크' , '걸스데이' , '트와이스']
    node = TreeNode()
    node.data = name #node.data에 nameAry의 원소를 하나씩 삽입

    current = root #시작점 current
    while True: #depth가 엄청 깊은것을 감안해서 while문 사용
        if name < current.data : #루트 보다 크기가 작을 경우
            if current.left ==None: #좌측 노드가 비어 있을 경우 좌측 노드에 삽입
                current.left = node
                break
            current = current.left # current를 current.left의 주소로 변환
        else: # 우측 노드가 비어 있을 경우 우측 노드에 삽입
            if current.right == None: #우측 노드가 비어 있을 경우 우측 노드에 삽입
                 current.right = node
                 break
            current = current.right # current를 current.right의 주소로 변환
    memory.append(node)

print('이진 탐색 트리 완료')

# 이진탐색 트리에서 데이터 검색
findData = '마마무'
current = root
while True : #언제 끝날지 불명확할때 while True를 사용
    if current.data == findData:
        print(findData , '찾았습니다')
        break
    elif current.data > findData:
        if current.left == None : #값이 없을 경우
            print(findData, '이 트리에 없음')
            break
        current=current.left
    else :
        if current.right ==None:
            print(findData, '이 트리에 없음')
            break
        current = current.right
```



### 2. 그래프

- 버스 정류장이나 지하철 노선도와 같이 여러 노선이 함께 포함된 형태
- 여러 노드가 서로 연결된 자료구조
- 무방향 그래프
  - 간선에 방향이 없는 그래프 
  - 인접행렬 : 정점의 개수를 행과 열로 가진 정방향 행렬
    - 해당 행렬을 보고 무방향 그래프를 구축할 수 있다.
- 방향 그래프
  - 방향이 화살표로 표시되는 그래프
- 가중치 그래프
  - 간선(엣지)마다 가중치가 다르게 부여되는 그래프



> 무방향 그래프의 간단 구현
>
> => 무방향 그래프의 인접 행렬은 대각선을 기준으로 서로 대칭된다.

```python
## 함수
class Graph() :
    def __init__(self,size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]

## 전역
G = None

## 메인
G = Graph(4)
G.graph[0][1] = 1; G.graph[0][2] = 1; G.graph[0][3] = 1
G.graph[1][0] = 1; G.graph[1][2] = 1;
G.graph[2][0] = 1; G.graph[2][1] = 1; G.graph[2][3] = 1
G.graph[3][0] = 1; G.graph[3][2] = 1


for row in range(4):
    for col in range(4):
        print(G.graph[row][col] , end='  ')
    print()
```



## 알고리즘

### 1. 정렬(*)

- 종류에 따라 가지런히 놓여 있는 것처럼 데이터가 나열되어 있는 것이다.
- 중요 알고리즘 중 하나인 정렬은 자료들을 일정한 순서대로 나열한 것

- 선택 정렬(*)
  - 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬. 구현이 제일 쉽다.
- 삽입 정렬
- 버블 정렬
- 퀵 정렬 : 빠르게 정렬하지만 구현이 어렵다.



> 최솟값 찾기

```python
# 최솟값 찾기
import random

## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx]>ary[i]):
            minIdx = i
    return minIdx

## 전역
testAry = [random.randint(0,99) for _ in range(20)]

## 메인
print(testAry)
minPos = findMinIndex(testAry)
print('최솟값-->', testAry[minPos])
```



> 선택 정렬의 기본 구현 (빈 리스트에 추가하기)

```python
## 선택 정렬 1(완전) #빈 배열 만들기
import random

## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx]>ary[i]):
            minIdx = i
    return minIdx

## 전역
before = [ random.randint(100,200) for _ in range(10)]
after = [] #빈방으로 준비

## 메인
print('정렬 전 -->' , before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos]) #빈 리스트인 after에 작은 값부터 추가 후 before에서 삭제
    del (before[minPos])
print('정렬 후 -->' , after)
```



> 선택 정렬의 개선된 구현 (하나의 배열에서 처리)

```python
## 선택 정렬 2(완전) # 하나의 배열에서 처리
import random
## 함수
def selectionSort(ary):
    n = len(ary) #ary의 길이
    for cy in range(0, n-1):
        minIdx = cy
        for i in range(cy+1, n):
            if (ary[minIdx] > ary[i]):
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx] , ary[cy] # 위의 두번째 for문의 if문의 결과로 최소값을 찾을경우 값을 변경
    return ary

## 전역
dataAry = [ random.randint(100,200) for _ in range(10)]

## 메인
print('정렬 전 -->' , dataAry)
dataAry = selectionSort(dataAry)

print('정렬 후 -->' , dataAry)
```



### 2. 검색

- 검색은 정렬된 상태에서 원하는 값을 찾을 수 있다.

#### 1. 순차 검색

- 마구잡이로 섞여 있는 곳(정렬이 되지 않음)에서 검색
- 검색 데이터를 하나씩 비교하면서 동일한 값을 찾으면 위치(인덱스)를 반환
- 동일한 값을 찾지 못하면 -1을 반환

```python
## 순차 검색
import random
## 함수
def seqSearch(ary, fData) :
    pos = -1 
    size = len(ary)
    for i in range(0, size, 1) :
        if (ary[i] == fData) :
            pos = i
            break
    return pos #동일한 값을 찾지 못하면 -1을 반환

## 전역
SIZE = 10
dataAry = [ random.randint(1, 99) for _ in range(SIZE)]
findData = dataAry[random.randint(0,SIZE-1)]

## 메인
print('배열-->', dataAry)
positon = seqSearch(dataAry, findData)
if positon == -1 :
    print(findData, '값이 없습니다.')
else :
    print(findData, '가 ', positon, ' 에 있음')
```



#### 2. 이진검색(*) -> O(log n)

- 정렬이 되어 있는 상태에서 검색
- 순차검색에 비해 월등히 효율적이라 데이터가 많아도 빠르게 검색 가능
- 이진 검색은 전체를 반씩 잘라 내서 한쪽을 버리는 방식을 사용
- 검색하는 값을 목록에서 찾는 순서
  1. 중앙값을 찾아 비교값과 동일한지 확인
  2. 동일하다면 해당 값 반환, 동일하지 않다면 대소를 비교해 작다면 왼쪽 반을 , 크다면 오른쪽 반을 소거
  3. 나머지 버리지 않은 반에서 1번부터 반복
  4. 시작값과 끝값이 같거나(start==end) , 시작값과 끝값의 앞뒤가 바뀌면(start>end) 해당 값이 없다고 판단하고 -1을 리턴

```python
## 이진 검색
import random
# 함수 선언부
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        mid = (start + end) // 2 # 정수로 표시
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1 #왼쪽 반을 버림
        else :
            end = mid -1 # 오른쪽 반을 버림
    return pos # start>=end가 될때까지 반복문 내에서 리턴을 하지 못했다면 초기 pos 값인 -1을 반환

## 전역
SIZE = 10
dataAry = [ random.randint(1, 99) for _ in range(SIZE)]
findData = dataAry[random.randint(0,SIZE-1)]
dataAry.sort()

## 메인
print('배열-->', dataAry)
positon = binSearch(dataAry, findData)
if positon == -1 :
    print(findData, '값이 없습니다.')
else :
    print(findData, '가 ', positon, ' 에 있음') #반환된 mid가 position으로 출력됨
```



