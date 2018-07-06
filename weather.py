import pyowm
myweather = pyowm.OWM('7e4f8a8e47e2011588293d20bf8a4766')


def getWeatherByLoc(location):
    observation = myweather.weather_at_place(location)
    w = observation.get_weather()
    return w

def getWeatherByLocUser():
    location = raw_input("please tell me a location")
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

w, location = getWeatherByLocUser()
h = getHumidity(w)
printHumInLoc(location, h)
speed, degrees = getWindInfo(w)
printWindInfoInLoc(location, speed, degrees)



