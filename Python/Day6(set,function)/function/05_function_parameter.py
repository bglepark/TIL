# 함수의 매개변수


# 매개변수(parameter) : 함수로 전달되는 값을 받는 변수
# 예시 )  width , height : 매개변수
def getArea(width , height):
    return width*height

# 인수(arguments) : 함수 호출 시 함수에게 전달되는 값
# 10, 5 : 인수
getArea(10,5)


def getAvg(k,e,m):
    return (k+e+m)/3

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
mat = int(input('수학점수 입력 : '))

print('평균:' , getAvg(kor,eng,mat))