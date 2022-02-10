from xml.etree import ElementTree
import requests
import re 
# re : 정규식 표현

service_key = 'yJJch5dkTvNq384FXvKHPRbl3Dnlvu0%2FZ5OmpKlnmwivbF4EYygwTm7jR2tAOt0FCp9h6I1gYBNfYZ5FV8HaqA%3D%3D'
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'

# 필수항목 넣는다 -> 서비스 url 확인하고, service key 넣기
# service_key : 일반 인증키(Encoding)

# print(url)
# url 들어가면 xml 형식이다

resp = requests.get(url)
# print(resp.text)
tree = ElementTree.fromstring(resp.text)
#xml형태의 문서에 대해 문자열로 가져온 객체를 parse-tree로 만든다

# 공식홈페이지에서 https://docs.python.org/3/search.html?q=xml.etree&check_keywords=yes&area=default
# xml.etree 찾기
# print(tree)
for item in tree[1][0]:
    # print(item.find('gubun').text)
    if item.find('gubun').text == '합계':
        # print({item.find('createDt').text})
        # print('일일합계 :' , item.find('incDec').text)
        # print('국내발생 : ' , item.find('localOccCnt').text)
        # print(item.find('overFlowCnt').text)
        stdDay = re.sub(r'(\D)+' , '', item.find('stdDay').text)
        # print(stdDay)
        stdDay = stdDay[:2] + "/" + stdDay[4:6] + '/' + stdDay[6:8]
        # print(stdDay)
        incDec = item.find('incDec').text
        localOccCnt = item.find('localOccCnt').text
        overFlowCnt = item.find('overFlowCnt').text
        print(f'[{stdDay}]\n일일합계:{incDec}\n국내발생:{localOccCnt}\n해외발생:{overFlowCnt}')

