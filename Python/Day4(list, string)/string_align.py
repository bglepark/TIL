# 문자열 정렬
# 문자 : 왼쪽 정렬이 기본
# 숫자 : 오른쪽 정렬이 기본
# 문자열 정렬 : 정렬 문자 < , > , ^

# 정렬문자
# < : 왼쪽 정렬 , >: 오른쪽 정렬 , ^: 가운데 정렬
string = 'python'
num = 1234
print(string)
print('{:<10}'.format(string))
print('{:>10}'.format(string))
print('{:^10}'.format(string))
print('{:6d}'.format(num))
print('{:06d}'.format(num))
print('{:-^10}'.format(string))
print('{:-<10}'.format(string))

# 메소드 사용
# ljust() : 왼쪽 정렬 , rjust() : 오른쪽 정렬 , center() : 가운데 정렬
print(string.ljust(10))
print(string.rjust(10))
print(string.center(10))
