# lambda(람다) 함수 : 함수를 한줄로 간단하게 작성
# 변수 = (lambda 매개변수들 : 식)
# 변수(인수들)

def add(x,y):
    return x+y

# 함수의 이름 , 함수의 매개변수 , return 등 길다

print(add(10,20))

#lambda x,y : x+y
add2 = lambda x,y : x+y
print(add2(10,20))

add3 = lambda x=10, y=10 : x+y  # default 값으로도 지정 가능
print(add3())
print(add3(20,30))

# 문제 . 리스트의 각 요소에 10을 더하는 함수
# def add10(numList):
#     for i in range(len(numList)):
#         numList[i]+=10


num = [1,2,3]
# add10(num)
# print(num)


# 그냥 10을 더하는 함수를 만들고 for문으로 반환
def add10(num):
    return num+10

# lambda num : num+ 10           과 같은 기능

for i in range(len(num)):
    num[i]=add10(num[i])
print(num)

# map() 함수
map(add10 , num) # num에 각각 add10 함수를 적용 (map 객체로 반환됨)
num2 = list(map(add10,num))
print(num2)

# lambda 함수 & map() 같이 사용
num3 = list(map(lambda num:num+10,num2))
print(num3)


# (lambda 매개변수들 : 식)(인수들)
# 람다 표현식을 변수에 할당하지 않고 그 자체를 호출해서 사용가능
(lambda x:x+10)(25) #콘솔에서 바로 실행 가능

# 람다 표현식안에서 변수 생성 불가
# (lambda x : y = 10 ; x+y)(5)

y=10
(lambda x : x+y)(5)


# 문제2. 두 리스트의 각 자리수의 값을 합해서 새로운 리스트를 생성

list1 = [1,2,3,4]
list2 = [10,20,30,40]

# 함수로 정의
def newlist(x,y):
    new = list(zip(list1, list2))
    for i in range(len(new)):
        new[i] = sum(new[i])
    return new

print(newlist(list1 , list2))


# lambda & map 사용  
new = list(map(lambda x,y : x+y , list1 , list2))
print(new)

# new = (list(zip(list1,list2)))
# for i in range(len(new)):
#     new[i] = sum(new[i])
# print(new)



# 결과는 [11,22,33,44] 로 나오게 작업


# "list1 = [1,2,3,4]
# list2 = [10,20,30,40]
#
# def addList(x,y):
#     list = []
#     for i in range(len(x)):
#         list.append(x[i] + y[i])
#     return list
# new_list = addList(list1,list2)
# print(new_list)
#
# # lambda & map 사용
# new_list2 = list(map(lambda x,y : x + y, list1,list2))
# print(new_list2)"

