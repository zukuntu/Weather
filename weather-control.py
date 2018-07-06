import RPi.GPIO as G
import time

import pyowm
myweather = pyowm.OWM('7e4f8a8e47e2011588293d20bf8a4766')

G.setmode(G.BOARD)
G.setup(3, G.OUT)
G.setup(13, G.OUT)
G.setup(29, G.OUT)

def getWeatherByLoc(location):
    observation = myweather.weather_at_place(location)
    w = observation.get_weather()
    return w , location

def getWeatherByLocUser():
    location = raw_input("please tell me a location \n")
    observation = myweather.weather_at_place(location)
    w = observation.get_weather()
    return (w, location)

def printHumInLoc(location, humidity):
    print "The humidity in " + str(location) + " is " + str(humidity)

def printWindInfoInLoc(location, speed, deg):
    print "The wind speed in " + str(location) + " is " + str(speed)
    print "The wind direction in " + str(location) + " is " + str(deg) + " degrees"

def getHumidity(weather):
    humidity = weather.get_humidity()
    return humidity

def getWindInfo(weather):
    wind = weather.get_wind()
    print(wind)
    
    degrees = 0
    try:
        degrees = wind['deg']
    except KeyError as e:
        print("Imperial system may be used instead - gust") 
        try:
            degrees = wind['gust']
        except:
            print("some other error happened")
        
        
    
    speed = wind['speed']
    return (speed, degrees)

def gettemp(weather):
    temp_dict = weather.get_temperature()
    temp = temp_dict['temp']
    celcius = temp - 273.15
    print "The temperature is " + str(celcius)
    return celcius

#ex = False
#while not ex:
cities = ['Koforidua', 'Helsinki', 'Auckland']

for city in cities:
    w, location = getWeatherByLoc(city)
    h = getHumidity(w)
    printHumInLoc(location, h)
    speed, degrees = getWindInfo(w)
    printWindInfoInLoc(location, speed, degrees)

    t = gettemp(w)

    if t < 10:
        G.output(3, True)
        time.sleep(5)
    elif 10 <= t <= 23:
        G.output(13, True)
        time.sleep(5)
    else:
        G.output(29, True)
        time.sleep(5)

    G.output(3, False)
    G.output(13, False)
    G.output(29, False)

    print "\n \n"

    #user_choice = int(raw_input("1: continue - 2: exit \n"))
    #if user_choice == 2:
        #ex = True
    
G.cleanup()
