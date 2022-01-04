# # 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어와서
# # 한줄의 두 숫자를 더한 연산 결과를 파일로 저장하기 (list_num.txt)
#
# f1 = open('list_num.txt' , 'r')
# list_1 = []
# for line in f1:
#     list_1.append(line.split(' '))
#
# list_1.pop(1)
# list_f = []
# list_s = []
# for i in range(len(list_1)):
#     list_f.append(list_1[i][0])
#     list_s.append((list_1[i][1]))
#
# for i in range(len(list_s)):
#     list_s[i]=list_s[i].rstrip()
#
# list_new = []
# result = []
# for i in range(8):
#     result.append(int(list_f[i])+int(list_s[i]))
#     list_new.append(f'{list_f[i]}+{list_s[i]}={result[i]}')
#
# f = open('submission.txt' , 'w')
# for i in range(len(list_new)):
#     f.write((list_new[i]))
#     f.write('\n')
# f1.close()
# f.close()

# def sum(f1,f):
#
#     f1 = open('list_num.txt', 'r')
#     list_1 = []
#     for line in f1:
#         list_1.append(line.split(' '))
#
#     list_1.pop(1)
#     list_f = []
#     list_s = []
#     for i in range(len(list_1)):
#         list_f.append(list_1[i][0])
#         list_s.append((list_1[i][1]))
#
#     for i in range(len(list_s)):
#         list_s[i] = list_s[i].rstrip()
#
#     list_new = []
#     result = []
#     for i in range(8):
#         result.append(int(list_f[i]) + int(list_s[i]))
#         list_new.append(f'{list_f[i]}+{list_s[i]}={result[i]}')
#     f = open('submission.txt', 'w')
#     for i in range(len(list_new)):
#         f.write((list_new[i]))
#         f.write('\n')
#     f1.close()
#     f.close()
#
# sum(f1 , f)



# 2. 텍스트파일로 되어 있는 가사의 단어를 count (yesterday.txt)
# 리스트, 세트 , 딕셔너리 등의 자료구조를 이용
# 단어들은 모두 소문자로 변환하여 사용한다.




# 3. 회원명단을 입력받아 파일로 저장하는 함수 작성


def sum(path1 , path2):
    with open(path1 , 'r') as f1:
        lines = f1.readlines()
    with open(path2 , 'w') as f2:
        newline=[]
        for line in lines:
            newline.append(line.rstrip().split())
        newline.pop(1)

        for i in range(len(newline)):
            result = round((float(newline[i][0])+float(newline[i][1])), 1)
            f2.write(f'{newline[i][0]}+{newline[i][1]}={result}\n')


path1 = 'list_num.txt'
path2 = 'submission.txt'
if __name__ =='__main__':
    sum(path1, path2)



