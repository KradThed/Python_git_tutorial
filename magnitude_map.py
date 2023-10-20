import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
# Изучение структуры данных.
filename = 'D:\WORK\Learning\mapping\eq_data\eq_data_30_day_m1.geojson'
with open(filename,  encoding="utf-8") as f:
  all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']

mags = []
lats = []
lons = []
hover_text = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties'] ['mag']
    title = eq_dict['properties']['title']
    lat = eq_dict['geometry'] ['coordinates'] [0]
    lon = eq_dict['geometry'] ['coordinates'] [1]
    mags.append(mag)
    lats.append(lat)
    lons.append(lon) 

#нанесение данных на карту
data = [{
 'type': 'scattergeo',
 'lon': lons,
 'lat': lats,
 'marker': {
    'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'Viridis',
    'reversescale': True,
    'colorbar': {'title': 'Magnitude'},
    },
 }]
my_layout = Layout(title='Global Earthquakes 30 days')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

print(mags[:10])
print(lats[:5])
print(lons[:5])
 
 
