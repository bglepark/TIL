# 1부터 10까지 더하기
# add = 0
# for i in range(1,11) :
#     add += i
# print(add)


add = 0
add_2 =0
for i in range(1,101):
    if i %2 ==1:
        add += i
    elif i%2==0:
        add_2 +=i
print(add)
print(add_2)


# 다른 방법
a=0
b=0
for i in range(1,101,2):
    a+=i
    b+= i+1
print(a)
print(b)

c=0
for i in range(3,101,3):
    print(i)
    c+=i
print(c)
