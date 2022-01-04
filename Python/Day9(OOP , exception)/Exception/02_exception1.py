# 예외 처리 (Exception)
# 에러 종류와 상관없이 에러가 발생하면 처리

# try :
#     # 에러가 발생할 문장들
#
# except 에러모드 as e:
#     # 에러가 발생하면 처리하는 코드들
#       e를 출력해서 에러도 같이 명시해줌
#
# else :
#     # 에러가 발생하지 않으면 처리하는 문장
#
# finally:
#     # 에러와 상관없이 항상 수행하는 문장


# 에러의 종류와 상관없이 에러를 처리하는 경우
# 예제. 0으로 나누는 경우 처리
# try :
#     print(10/0)
#     print('나이: ' + 23 + '살')
# except:
#     # print('0으로 나눌 수 없습니다.')
#     print('오류발생')
#
# # 에러 종류를 명시해서 에러 처리하는 방법
# # try :
# #     print(10/0)
# # except ZeroDivisionError:
# #     print('0으로 나눌 수 없습니다.')
#
# try :
#     print(10/0)
# except ZeroDivisionError as e: #에러 메세지 변수
#     print('0으로 나눌 수 없습니다.' , e)
#
# # ValueError 처리
# try:
#     num = int(input('숫자를 입력하세요 : '))
# except ValueError as e:
#     print('숫자가 아닙니다.' , e)
#
# # 에러 표시 여러개 -> 처음 발생한 에러만 예외 처리된것을 표기함
# try :
#     print(10/0)
#     print('나이: ' + 23 + '살')
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없습니다.' , e)
#
# except TypeError as e:
#     print('형식이 잘못지정되었습니다.' , e)
#
# # except에 여러개를 사용하면됨 -> 하지만 결국 메세지는 1개만 나옴
# try :
#     print(10/0)
#     print('나이: ' + 23 + '살')
# except (ZeroDivisionError, TypeError) as e:
#     print('오류가 발생했습니다.' , e)


# 오류가 발생하지 않을 경우엔 else 진행
try :
    f = open('test2.txt' , 'r')

except FileNotFoundError as e:
    print(e)

else:
    data = f.read()
    print(data)
    f.close()
# finally 는 예외가 발생하든 발생 안하든 finally 안의 구문을 실행
finally:
    print('End----')

    