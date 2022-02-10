import folium
import json

# 1. starbucks01.json 파일을 읽어드랒

# 2. 지도 만들자

#3. starbucks01.json 파일을 읽어드린 내용(1에서 실행한 결과)을 가지고
# 반복해서 starbucks 매장의 marker를 만들어 지도에 추가하자

#4. 지도 저장하자


with open('starbuck01.json' ,'r' , encoding='UTF8') as f:
    data = json.load(f)


my_loc = folium.Map(location=[37.503632490067595, 127.04984302094226] , zoom_start=18)

data2 = data['store_list']
for i in range(len(data2)):
    folium.Marker([data2[i]['lat'] , data2[i]['lot']] ,
                  popup=folium.Popup(data2[i]['s_name'],
                  max_width=100)).add_to(my_loc)

my_loc.save('visual03.html')