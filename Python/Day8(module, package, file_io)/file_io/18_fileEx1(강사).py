# # 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# # 한줄의 두 숫자를 더한 연산 결과를 파일로 저장하기 (list_num.txt)

with open('list_num.txt' , 'r') as f:
    data = f.readlines()

with open('submission.txt' ,'w') as f:
    for d in data :
        if d != '':
            value = d.replace('\n' ,'').split()
            result = int(value[0]) + int(value[1])
            f.write (f'{value[0]}+{value[1]}={result}')
        else:
            continue

with open('submission.txt' ,'r') as f:
    f.read()


