import folium

my_loc = folium.Map(location = [37.503632490067595, 127.04984302094226] , zoom_start=18)
# zoom : 얼마나 확대할지
my_loc.save('visual01.html')
