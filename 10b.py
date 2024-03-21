import json
with open('weather_data.json') as f:
    data = json.load(f)
print(f"Current temperature: { data['temp']}°C")
print(f"Humidity: {data['humidity']}%")
print(f"Weather description: {data['description']}")