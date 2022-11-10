import folium
import pandas
map1 = folium.Map(location=[50,30], zoom_start=6, tiles='Stamen Terrain')
fgm = folium.FeatureGroup(name='Mountains')
df = pandas.read_csv('web_mapping/Karpati.csv')

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

for row in df.index:
    height = df['Height'][row]
    mcolor = 'red' if height > 2030 else 'green'
    name_m = df['Name'][row]
    iframe = folium.IFrame(html=html % (name_m, name_m, height), width=200, height=100)
    
    fgm.add_child(folium.Marker(location=[df['Latitude'][row],
                                                 df['Longitude'][row]],
                                                  popup=folium.Popup(iframe),
                                                   icon=folium.Icon(color=mcolor)))
                                                   #fill=True, fill_color='orange',
                                                    #fill_opacity=0.7))
    # icon=folium.Icon(color=mcolor)
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('web_mapping/world.json', encoding='utf-8-sig').read(),
 style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
  else 'red'}))
map1.add_child(fgm)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save('map1.html')
