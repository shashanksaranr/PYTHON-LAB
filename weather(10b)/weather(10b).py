import json
with open('C:\\Users\\HP\\Desktop\\PROGRAMMING\\Python Practice\\weather.json')as f:
    data=json.load(f)

current_temp=data['main']['temp']
humidity=data['main']['humidity']
weather_desc=data['weather'][0]['description']

print(f"Current temperature:{current_temp}C")
print(f"Humidity:{humidity}%")
print(f"Weather Description:{weather_desc}")
