# 2.
# 다음 예와 같이 패턴이 있는 문자열에서 숫자만 추출해서 총 합계 구하기
# str_data = "{a1:20},{a2:30},{a3:15},
# {a4:50},{a5-14},{a6:15},
# {a7:20},{a8:70},{a9:-100}"

str_data = "{a1:20},{a2:30},{a3:15},{a4:50},{a5:-14},{a6:15},{a7:20},{a8:70},{a9:-100}"
str_split = str_data.split(",")
for i in range(len(str_split)):
    if ":" in str_split[i]:
        str_split[i]= int(str_split[i][str_split[i].find(":"):-1].replace(":",""))
    else:
        str_split[i]= int(str_split[i][1:-1])
print('숫자의 개수 : ', len(str_split))
print('총 합계 : ', sum(str_split))

