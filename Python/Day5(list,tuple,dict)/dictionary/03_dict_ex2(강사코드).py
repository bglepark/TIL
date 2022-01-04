# 딕셔너리를 이용해 사용자로부터 영어 단어와 뜻을 입력 받아서 사전을 구성하고
# 사용자가 입력한 단어를 검색하여 뜻을 출력하기

# 영어 단어 등록
eng_dic = dict()

while True :
    eng = input('영어 단어 등록 (종료는 quit) : ')
    if eng == 'quit':
        break
    elif eng not in eng_dic :
        kor =input('%s의 뜻 입력 (종료는 quit) : ' %eng)
        eng_dic[eng] = kor
    else :
        print('%s는 이미 등록된 단어 입니다.' %eng)
print()

# 영어 단어 검색
while True:
    eng = input('검색할 영어 단어 입력 (종료는 quit) : ')
    if eng == 'quit':
        break
    elif eng in eng_dic :
        print('%s의 뜻은 %s 입니다.' %(eng , eng_dic[eng]))
    else :
        print('%s는 사전에 없는 단어 입니다.' %eng)
print('\n종료합니다')