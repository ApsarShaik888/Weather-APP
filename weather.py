import requests
from dotenv import load_dotenv
import os

#load the API Keys from .env file
load_dotenv()

api_key=os.getenv("OPENWEATHER_API_KEY")

#define a function to call
def get_weather(city):
    return city
def display_weather(data):
    print(f"City : ",city_name)
    print(f"temperature : {temp_celvin:.1f}")
    print(f"Description : ",description)
    print(f"Humidity : ",humidity)
while True:
    city=input("enter city name or quit: \n")
    if city.lower()=="quit":
        print("bye")
        break
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data=requests.get(url).json()
    #extract the data
        city_name=data['name']
        temp_kelvin=data['main']['temp']
        description=data['weather'][0]['description']
        humidity=data['main']['humidity']
        temp_celvin=temp_kelvin-273.15
        display_weather(data)