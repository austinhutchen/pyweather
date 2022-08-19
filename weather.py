
import requests
import math


def weather():
    city = input("Enter your city name: ")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=76875c2ba9d949cbf7e9c0e76057de73&units=imperial'.format(city.lower())
    output = requests.get(url)
    data = output.json()
    temp = data['main']['temp']
    feelslike = data['main']['feels_like']
    print("The temperature in " + city + " in celcius is:", temp,',but it feels more like',feelslike)
    choice=input('Would you like to quit? y/n: ')
    if choice.lower()=='y' or choice.lower()=='yes':
     quit()
    else:
     return weather()
     
weather()