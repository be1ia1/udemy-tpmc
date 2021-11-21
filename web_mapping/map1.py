import folium
import pandas
map1 = folium.Map(location=[50,30],zoom_start=6, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')
df = pandas.read_csv('Karpati.csv')
for row in df.index:
    fg.add_child(folium.Marker(location=[df['Latitude'][row], df['Longitude'][row]], popup=df['Name'][row], icon=folium.Icon(color='green')))
map1.add_child(fg)
map1.save('map1.html')
