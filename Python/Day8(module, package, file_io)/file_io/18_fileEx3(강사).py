# 회원명단을 입력받아 저장하거나, 회원명단파일을 열어 저장되어 있는 회원 명단을 출력
# 하는 프로그램 작성

def input_member(infile):
    with open(infile, 'w' , encoding='utf-8') as f:
        while True :
            member = input('멤버를 입력하세요. (종료는 q)')
            if member == 'q':
                break
            else:
                f.write(member + '\n')


def output_member(outfile):
    with open(outfile, 'r' , encoding='utf-8') as f:
        print(f.read())


while True:
    opt = input('저장 1 , 출력 2 , 종료 q : ')
    if opt == '1':
        infile = input('멤버명단을 저장할 파일명을 입력하세요 : ')
        input_member(infile)
    elif opt == '2':
        outfile = input('멤버명단이 저장된 파일명을 입력하세요 : ')
        output_member(outfile)
    elif opt == 'q':
        break
    else :
        print('잘 못 누르셨습니다.')
        continue





