# 중첩 for

# for y in range(3):
#     print(y)
#     for x in range(5):
#         print(x, end=' ')
#
#     print()

# 출력 결과
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

for y in range(3):
    for x in range(1,5):
        print(x+y*4, end=' ')
    print()


