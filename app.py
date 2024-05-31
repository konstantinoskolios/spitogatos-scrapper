import json
import matplotlib.pyplot as plt
import numpy as np

# Load JSON data from file with utf-8 encoding
with open('output_all_json.json', 'r', encoding='utf-8') as json_file:
    jd = json.load(json_file)

# Initialize dictionary to hold location data
location_data = {}

# Process data
for k, v in jd.items():
    location = v['location']
    price = int(v['price'])
    sqm = int(v['title'].replace('τ.μ.', '').strip())
    
    if location not in location_data:
        location_data[location] = {'prices_per_sqm': [], 'total_price': 0, 'total_sqm': 0, 'count': 0}
        
    location_data[location]['prices_per_sqm'].append(price / sqm)
    location_data[location]['total_price'] += price
    location_data[location]['total_sqm'] += sqm
    location_data[location]['count'] += 1

# Calculate median and average price per square meter
median_price_per_sqm = {}
average_price_per_sqm = {}
for location, values in location_data.items():
    if values['count'] >= 10:  # Considering only locations with 10 or more samples
        median_price_per_sqm[location] = np.median(values['prices_per_sqm'])
        average_price_per_sqm[location] = values['total_price'] / values['total_sqm']

# Print results
for location, median_price in median_price_per_sqm.items():
    print(f"Location: {location}, Median Price per sqm: {median_price:.2f}, Average Price per sqm: {average_price_per_sqm[location]:.2f}")

# Create bar chart
locations = list(median_price_per_sqm.keys())
median_prices = list(median_price_per_sqm.values())
average_prices = [average_price_per_sqm[loc] for loc in locations]

x = np.arange(len(locations))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, median_prices, width, label='Median Price per sqm', color='skyblue')
bars2 = ax.bar(x + width/2, average_prices, width, label='Average Price per sqm', color='lightgreen')

ax.set_xlabel('Location')
ax.set_ylabel('Price per sqm (€)')
ax.set_title('Median and Average Price per Square Meter by Location for Renting')
ax.set_xticks(x)
ax.set_xticklabels(locations, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()
