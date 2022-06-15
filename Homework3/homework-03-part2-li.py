#Danielle Li
#June 13, 2022
#Homework 3, Part 2

####PRELIM STUFF
api_key='ceead243ab0145c4a1b202923221306'

# Import the requests library
import requests


####ACTUAL ANSWERS
# 
#1.  What is the URL to the documentation?
# https://www.weatherapi.com/docs/

#2.  Make a request for the current weather where you are born, or somewhere you've lived.
#According to the API explorer (https://www.weatherapi.com/api-explorer.aspx), the format of the call should look like this
#http://api.weatherapi.com/v1/current.json?key=ceead243ab0145c4a1b202923221306&q=London&aqi=no

###FINAL ANSWER HERE
url = 'http://api.weatherapi.com/v1/current.json'
place='Udaipur'
full_url=url+'?key='+api_key+'&q='+place+'&aqi=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
current_weather = response.json()

#3.  Print out the country this location is in.
#print(current_weather)
print(current_weather.keys())

###FINAL ANSWER HERE
print(f"{place} is located in {current_weather['location']['country']}")

#4.  Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

curr_temp_f=current_weather['current']['temp_f']
print(curr_temp_f)
curr_feels_f=current_weather['current']['feelslike_f']
print(curr_feels_f)

###FINAL ANSWER HERE
if curr_feels_f>curr_temp_f:
    print(f"It feels {curr_feels_f-curr_temp_f:.2f} degrees F warmer.")
else:   
    print(f"It feels {curr_temp_f-curr_feels_f:.2f} degrees F colder.")

#5.  What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
#According to docs, the query for airports looks like: q=iata:DXB

url = 'http://api.weatherapi.com/v1/current.json'
place='iata:LHR'
full_url=url+'?key='+api_key+'&q='+place+'&aqi=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
current_weather = response.json()

###FINAL ANSWER HERE
print(f"The current temperature at {place} in {current_weather['location']['name']} is {current_weather['current']['temp_f']} degrees F.")


#6.  What URL would I use to request a 3-day forecast at Heathrow?
#according to api explorer, the call is at http://api.weatherapi.com/v1/forecast.json?key=ceead243ab0145c4a1b202923221306&q=London&days=3&aqi=no&alerts=no

url = 'http://api.weatherapi.com/v1/forecast.json'
days = '3'
place='iata:LHR'
full_url=url+'?key='+api_key+'&q='+place+'&days='+days+'&aqi=no&alerts=no'

###FINAL ANSWER HERE
print(full_url)

#Finish loading the data for the next questions
response = requests.get(full_url)
# Turn the JSON into a dictionary
current_weather = response.json()

#7.  Print the date of each of the 3 days you're getting a forecast for.

#Just exploring what's in the data
print(current_weather.keys())
print(current_weather['forecast'].keys())
print(current_weather['forecast']['forecastday'])
#Looks like current_weather['forecast']['forecastday'] is a list with 1 element for each of 3 days, and each element is a big dictionary
print(len(current_weather['forecast']['forecastday']))
#Give the thing a new name so it's easier to loop over
forecast_list=current_weather['forecast']['forecastday']

###FINAL ANSWER HERE
#Pick out the dates associated with the dictionary for each of the forecast days
forecast_dates=[day['date'] for day in forecast_list]
print(forecast_dates)

#8.  Print the maximum temperature of each of the days.

###FINAL ANSWER HERE
#Pick out the max temp associated with the dictionary for each of the forecast days
forecast_maxtemp=[day['day']['maxtemp_f'] for day in forecast_list]
print(forecast_maxtemp)

#9.  Print the day with the highest maximum temperature.

###FINAL ANSWER HERE
#Create a var that is equal to the max temp, and then print the day whose own max temp matches that
max_temp_alldays=max(forecast_maxtemp)
for day in forecast_list:
    if day['day']['maxtemp_f']==max_temp_alldays:
        print(day['date'])


