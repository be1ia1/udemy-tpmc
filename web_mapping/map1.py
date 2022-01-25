import folium
import pandas
map1 = folium.Map(location=[50,30], zoom_start=6, tiles='Stamen Terrain')
fgm = folium.FeatureGroup(name='Mountains')
df = pandas.read_csv('Karpati.csv')

html = """
Mountain name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for row in df.index:
    height = df['Height'][row]
    mcolor = 'red' if height > 2030 else 'green'
    iframe = folium.IFrame(html=html % (df['Name'][row], df['Name'][row], height), width=200, height=100)
    fgm.add_child(folium.CircleMarker(location=[df['Latitude'][row], df['Longitude'][row]], popup=folium.Popup(iframe), fill=True, fill_color='orange', fill_opacity=0.7))
    # icon=folium.Icon(color=mcolor)
fgp = folium.FeatureGroup(name='Popilation')
fgp.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
 style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
  else 'red'}))
map1.add_child(fgm)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save('map1.html')
