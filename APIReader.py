import requests as req
import json 

def readAPI(url_path,parameters):
    response =""
    if parameters == "":
        response = req.get(url_path)
    else:
        response = req.get(url_path,params=parameters)
    print(response.status_code)
    return response

def jprint(obj):
    text = json.dumps(obj,sort_keys=True,indent=4)
    print(text)

# Space Station code---------------------------------------------------------
# how many people in space api
# response = readAPI("http://api.open-notify.org/astros.json","")
# jprint(response.json())
# How many times the space station will orbit my location
# param = {
#     "lat": [40.71],
#     "lon":[-74]
# }
# response = readAPI(" http://api.open-notify.org/iss-pass.json",param)
# jprint(response)
# -----------------------------------------------------------------------------
#WeatherMAP API----------------------------------------------------------------
#check https://rapidapi.com/community/api/open-weather-map?endpoint=53aa6042e4b051a76d241b79 for the code
url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

querystring = {"q":"san francisco,us","lat":"35","lon":"139","cnt":"10","units":"metric"}

headers = {
    'x-rapidapi-key': "8b710e73afmshaa75416c57a4369p19b39cjsnca03a7f71899",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = req.request("GET", url, headers=headers, params=querystring)
print(response.text)
#Only gets the values from the city key in the dictionary
# print(response.json()['city'])
# # from the city key it gets the vaue from the name key
# print(response.json()['city']['name'])
print(response.json()['city']['coord']['lon'])
print(response.json()['city']['population'])
# return the first day of data from the list
print(response.json()['list'][0])
# Returns the timestamp stored in the dt key of the list key
print(response.json()['list'][0]['dt'])
