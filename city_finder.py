from geopy.geocoders import Nominatim
import plotly.express as px

def get_coordinates(city):
    # Create Nominatim geocoder instance
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Try to geolocate the city
    location = geolocator.geocode(city)

    # Return None if the city was not found
    if not location:
        return None

    # Return the longitude and latitude coordinates
    return location.longitude, location.latitude

lats = []
lons = []
# Example usage
city = "Heemstede"
coordinates = get_coordinates(city)
if coordinates:
    print(f"The longitude and latitude coordinates for {city} are {coordinates}")
    lons.append(coordinates[0])
    lats.append(coordinates[1])
else:
    print(f"Could not find coordinates for {city}")

title = 'City Found'
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()