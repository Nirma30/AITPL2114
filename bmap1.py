import folium
import pandas
data = pandas.read_csv("new.csv")
lat = list(data["lat"])
lon = list(data["lon"])
map = folium.Map(location=(12.58, 77.48), zoom_start=6)
fg = folium.FeatureGroup(name="bangaloremap")
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=(lt, ln), icon=folium.Icon(colour="red")))
map.add_child(fg)
map.save('bmap1.html')
