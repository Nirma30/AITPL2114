import folium
import pandas
data = pandas.read_csv("metro.csv")
lat = list(data["lat"])
lon = list(data["lon"])
# name = list(data['cname'])
color = list(data["color"])
map1 = folium.Map(location=(12.58, 77.48), zoom_start=6)
fg = folium.FeatureGroup(name="bangaloremap")
for lt, ln, col in zip(lat, lon, color):
    fg.add_child(folium.Marker(location=(lt, ln), icon=folium.Icon(color="col")))
map1.add_child(fg)
map1.save('bmap2.html')
