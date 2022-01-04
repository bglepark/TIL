# 문자열 구성 파악
# isalpha() : 문자 여부 결과 반환(True, False)
# isdigit() : 숫자인지 결과 반환
# isspace() : 하나의 문자에 대하여 공백여부 반환
# isalnum() : 문자 또는 숫자인지 확인
# islower() : 소문자여부
# isupper() : 대문자여부

string = '내이름은 hspark이고 나이는 20 입니다'
str_split = string.split()
for result in str_split:
    if result.isdigit():
        print('숫자입니다')
    else:
        print('숫자가 아닙니다')

# 아이디 입력할때 문자 숫자 혼용 등 확인


# 연습문제
# 입력된 문자열에서 알파벳의 개수,숫자의 개수, 스페이스, 기타의 개수를 각각 계산하여 출력하기
ans = input('문장을 입력하세요 : ')

ans_alpha = [ ]
ans_digit = [ ]
ans_space = [ ]
ans_etc = [ ]
for c in ans:
    if c.isalpha():
        ans_alpha.append(c)
    elif c.isdigit():
        ans_digit.append(c)
    elif c.isspace():
        ans_space.append(c)
    else:
        ans_etc.append(c)
print('알파벳의 개수 : ', len(ans_alpha))
print('숫자의 개수 : ', len(ans_digit))
print('스페이스 개수 : ', len(ans_space))
print('기타의 개수 : ', len(ans_etc))


# 리스트 사용하지 않고 그냥 변수 하나 설정해서 +=1 해서 사용 가능



