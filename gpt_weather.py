import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Set up API key and location
api_key = "a4eba717407b4c9faba717407bcc9fee"
location = "NL/Amsterdam"

# Define start and end dates
start_date = "2019-01-01"
end_date = "2019-12-31"

# Build API request URL
url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={start_date}&end_dt={end_date}"

# Send API request
response = requests.get(url)

print(f"Response {response.content}")

# Convert response to JSON format
data = json.loads(response.content)

# Extract daily weather data
daily_data = []
for day in data['forecast']['forecastday']:
    date = day['date']
    avg_temp = day['day']['avgtemp_c']
    total_rain = day['day']['totalprecip_mm']
    total_sun = day['day']['sunhour']
    daily_data.append({'Date': date, 'AvgTemp': avg_temp, 'TotalRain': total_rain, 'TotalSun': total_sun})

# Convert daily data to pandas DataFrame
df = pd.DataFrame(daily_data)
df['Date'] = pd.to_datetime(df['Date'])

# Plot temperature, rainfall, and sun hours
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

axs[0].plot(df['Date'], df['AvgTemp'])
axs[0].set_ylabel('Temperature (°C)')

axs[1].bar(df['Date'], df['TotalRain'])
axs[1].set_ylabel('Rainfall (mm)')

axs[2].bar(df['Date'], df['TotalSun'])
axs[2].set_ylabel('Sun Hours')

plt.show()
