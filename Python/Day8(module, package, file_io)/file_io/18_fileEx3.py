# 회원명단을 입력받아 저장하거나, 회원명단파일을 열어 저장되어 있는 회원 명단을 출력
# 하는 프로그램 작성
member = ''
def input_member(path):
    while True:
        member = input('멤버를 입력하세요.(종료는 q) : ')
        if member !='q':
            with open(path, 'a') as f1:
                f1.write('\n%s'%member)
                print('저장되었습니다.')
        else:
            break

def output_member(path):
    with open(path, 'r') as f2:
        for member in f2.readlines():
            print(member)

def main_fun():
    while True :
        num = input('저장 1 , 출력 2 , 종료 q : ')
        if num == '1':
            file = input('멤버 명단을 저장할 파일명을 입력하세요 : ')
            member_file = path+'/'+file
            input_member(member_file)
        elif num == '2':
            file = input('멤버 명단이 저장된 파일명을 입력하세요 : ')
            member_file = file
            output_member(member_file)
        elif num == 'q':
            break
        else:
            print('다시 입력해주세요')
            continue

if __name__ == '__main__':
    path = 'C:/PythonStudy/Day8/file_io'
    main_fun()







