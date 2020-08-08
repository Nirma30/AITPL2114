import folium
import pandas
data = pandas.read_csv("metro.csv")
lat = list(data["lat"])
lon = list(data["lon"])
# name = list(data['cname'])
color = list(data["color"])
map = folium.Map(location=(12.58, 77.48), zoom_start=6)
fg = folium.FeatureGroup(name="bangaloremap")
for lt, ln, col in zip(lat, lon, color):
    fg.add_child(folium.Marker(location=(lt, ln), icon=folium.Icon(color="col")))
map.add_child(fg)
map.save('bmap2.html')
