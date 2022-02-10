import folium


# zoome => max랑 min 값 찾기
my_loc = folium.Map(location=[37.503632490067595, 127.04984302094226] , zoom_start=18)
folium.Marker([37.503632490067595, 127.04984302094226], popup=folium.Popup('멀티캠퍼스 선릉', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')