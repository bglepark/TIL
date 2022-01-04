# main 예제

name = ''

def input_name():
    global name
    name = input('이름 입력 : ')
    return name

def get_name():
    if name =='':
        return '이름없음'
    else:
        return name

if __name__ == '__main__':
    input_name()
    print(get_name())

else:
    print('module main이 import')
