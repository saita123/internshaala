import json
import requests
# Load the JSON data from the provided URL
url = "https://raw.githubusercontent.com/web3projectlinks/web3projectlinks/main/src/app/database/ethereum.json"
response = requests.get(url)
data = response.json()

# Find all the URLs and details for POLYGON
polygon_data = [project for project in data if 'name' in project and 'POLYGON' in project['name'].upper()]

# Save the filtered data into a new JSON file named 'polygon.json'
with open('polygon.json', 'w') as file:
    json.dump(polygon_data, file, indent=4)

print("Polygon data extracted and saved to 'polygon.json' successfully.")

list_of_dicts = []
for key, value in data.items():
    if isinstance(value, list):
        list_of_dicts.extend(value)

url=[]
# Accessing elements of each dictionary
for dictionary in list_of_dicts:
    # Check if 'url' exists in the dictionary before accessing it
    if 'url' in dictionary:
        url.append(dictionary['url'])

with open('polygon.json', 'w') as file:
    json.dump(url, file, indent=4)
    