# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# import sys
# n1 , n2 = map(int , sys.stdin.readline().split())
#
# max_common = []
# min_multiple = []
#
# for i in range(min(n1,n2)+1, 0 , -1):
#     if (n1%i==0) and (n2%i==0):
#         max_common.append(i)
#         break
#     else:
#         max_common.append(1)
#
#
# print(max(max_common))
#
# for i in range(max(n1,n2) , (n1*n2)+1):
#
#     if (i%n1==0) and (i%n2==0):
#         min_multiple.append(i)
#         break
#     else:
#         min_multiple.append(n1*n2)
#
# print(min(min_multiple))


# 라이브러리 사용!!!
import sys
import math
number = list(map(int , sys.stdin.readline().split()))
print(math.gcd(number[0] , number[1])) # gcd : Greatest Common Divisor 최대 공약수
print(math.lcm(number[0] , number[1])) # lcm : Least Common Multiple 최소 공배수

