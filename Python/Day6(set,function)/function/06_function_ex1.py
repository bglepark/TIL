# 산술 연산 함수 작성
# add() : 두 수 더하기
# sub() : 두 수 빼기
# mul() : 두 수 곱하기
# div() : 두 수 나누기
# mod() : 나머지

# a = 9 , b = 3
# 두 개의 숫자를 전달 받아서 연산 결과 반환

def cal_result(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    elif op == '%':
        return a%b

num1 = int(input('숫자 1 입력 :'))
num2 = int(input('숫자 2 입력 :'))
operation = input('연산 방식 입력(+,-,*,/,%) : ')
print(num1 , operation , num2 , '=' , cal_result(num1,num2,operation))

# 강사 코드
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

a = 9; b=3
result_add = add(a,b)
print(f'{a} + {b} = {result_add}')

result_sub = sub(a,b)
print(f'{a} - {b} = {result_sub}')

result_mul = mul(a,b)
print(f'{a} * {b} = {result_mul}')

result_div = div(a,b)
print(f'{a} / {b} = {result_div}')

result_mod = mod(a,b)
print(f'{a} % {b} = {result_mod}')

# 혹은 위의 출력문을 함수로 만드는것도 가능하다






