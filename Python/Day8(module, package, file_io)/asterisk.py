# * : 변수 앞에 붙은 경우 *args , **kwagrs => 언패킹(unpacking)

def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5)

def asterisk_test2(a,*args):
    print(a,*args)
    print(type(args))

asterisk_test2(1,2,3,4,5)


a , b , c = [1,2,3]
a , b , c = ([1,2,3] , [3,4,5] , [5,6,7])
print(a,b,c)

data = ([1,2,3] , [3,4,5] , [5,6,7])
print(*data)

def asterisk_test3(a,**args):
    print(a,args)
    print(type(args))

asterisk_test3(1 , b=2 , c=3 , d=4 , e=5)


data2 = {'b': 2, 'c': 3, 'd': 4, 'e': 5}
asterisk_test3(1, **data2)