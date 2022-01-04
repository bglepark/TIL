# 연습문제
# 구구단
# 구구단의 단수를 입력받아서 구구단을 출력하자

num = int(input('단수를 입력하세요 :'))
for i in range(1,10) :
    print(num , '*' , i , '=' , (num*i))