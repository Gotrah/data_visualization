import json
from pathlib import Path

import plotly.express as px

def save_formatted_data(data):
    # Write formatted earthquake data to file
    formatted_path = Path('eq_data/readable_eq_data.geojson')
    formatted_data = json.dumps(data, indent=4)
    formatted_path.write_text(formatted_data)


# Read earthquake data from file
file_path = Path('eq_data/eq_data_30_day_m1.geojson')
with file_path.open() as file:
    eq_data_json = file.read()

# Convert JSON data to Python object
all_eq_data = json.loads(eq_data_json)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
eq_title = [eq['properties']['title'] for eq in all_eq_dicts]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     )
fig.show()

