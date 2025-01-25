import geocoder
import folium
import webbrowser

# Function to get location based on IP address
def get_location(ip_address):
    location = geocoder.ip(ip_address)
    if location.ok and location.latlng:
        return location
    else:
        raise Exception("Could not retrieve location information.")

# Fetching your public IP address dynamically
try:
    myip = geocoder.ip('me').ip
    print("Your public IP address:", myip)

    # Getting location information
    location_info = get_location(myip)

    # Extracting coordinates
    coordinate = location_info.latlng
    print('Country:', location_info.country)
    print('City:', location_info.city)
    print('Latitude, Longitude:', coordinate[0], coordinate[1])

    # Creating a Folium map
    myloc = folium.Map(location=coordinate, zoom_start=14)

    # Adding a marker
    folium.Marker(
        location=coordinate,
        icon=folium.Icon(color='blue', icon='male', prefix='fa')
    ).add_to(myloc)

    # Adding a circle around the location
    folium.Circle(
        location=coordinate,
        radius=200,
        color='blue',
        fill=True,
        fill_opacity=0.3
    ).add_to(myloc)

    # Saving the map as an HTML file
    map_file = 'mymap.html'
    myloc.save(map_file)
    print(f"Map saved as '{map_file}'.")

    # Opening the map in the default web browser
    webbrowser.open('file://' + map_file)

except Exception as e:
    print("Error:", e)
