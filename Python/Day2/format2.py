# .format() 함수와 {}를 사용하여 서식 지정

print(format(1234.567 , '10.2f'))
print('{:.2f}'.format(1234.567))
print('name:{} , phone : {}'.format('박현수' , 1234))

print('name:{1} , phone : {0}'.format(1234, '박현수'))

print('{0:d} , {1:d}' .format(100 , 123))
print('{1:d} , {0:d}' .format(100 , 123))

print('{0:d} , {1:5d}' .format(100 , 123))
print('%d %5d %10d' %(123,123,123))