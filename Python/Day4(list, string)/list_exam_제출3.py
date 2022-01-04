# 3.
# 다 음 과 같 이 입 력 한 숫 자 만 큼 의 하 트 를 출 력 하 도 록 작 성 하 시오

num = input('숫자를 여러개 입력하세요.')
num_list = list(num)
for i in num_list:
    print(int(i)*'\u2665')


