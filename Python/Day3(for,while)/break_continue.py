# while & continue

for i in range(10):
    if i%2 == 0:
        break
    print(i)
#break 는 반복문을 빠져나옴


print('----------------------------')
for i in range(10):
    if i%2 == 0:
        continue
    print(i)
# continue는 그 다음 반복문을 수행

print('\n--------------')

i = 0
while i<10 :
    i+=1
    if i % 2 ==0:
        continue
    print(i)
