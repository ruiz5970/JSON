import json

in_file = open('US_fires_9_14.json','r')

out_file = open('readable_fire_data2.json','w')

fire_data = json.load(in_file)

json.dump(fire_data,out_file,indent=4)

'''list_of_fires = fire_data[]

print(len(fire_data))'''

brightness,lons,lats = [],[],[]

for fire in fire_data:
    bright = fire['brightness']
    lon = fire['longitude']
    lat = fire['latitude']
    if bright > 450:
        brightness.append(bright)
        lons.append(lon)
        lats.append(lat)

print('brightness')
print(brightness[:10])

print('longitude')
print(lons[:10])

print('latitude')
print(lats[:10])



from  plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat':lats,
    'marker':{
        'color':brightness,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorband':{'title':'Brightness'}

    }
}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {'data': data,'layout':my_layout}

offline.plot(fig,filename='US_Fires9_14.html')

