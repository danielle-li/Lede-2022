#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# ## Start by setting some preliminaries.  I'll be using Chengdu, China.

# In[1]:


import requests


# In[2]:


api_key='ceead243ab0145c4a1b202923221306'


# In[3]:


place='Chengdu'


# In[4]:


date='2022-06-15'


# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[20]:


url = 'http://api.weatherapi.com/v1/current.json'
place='Chengdu'
full_url=url+'?key='+api_key+'&q='+place+'&aqi=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
current_weather = response.json()


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# ## Windspeed

# In[6]:


wind_speed=current_weather['current']['wind_mph']

print(f"The current windspeed is {wind_speed} MPH.")


# ## Feels - Actual Temp

# In[7]:


curr_temp_f=current_weather['current']['temp_f']
print("Current temp:",curr_temp_f)
curr_feels_f=current_weather['current']['feelslike_f']
print("Current feels like:",curr_feels_f)

if curr_feels_f>curr_temp_f:
    print(f"It feels {curr_feels_f-curr_temp_f:.2f} degrees F warmer.")
elif curr_feels_f<curr_temp_f:   
    print(f"It feels {curr_temp_f-curr_feels_f:.2f} degrees F colder.")
else:
    print("If feels the same as it is.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# ## Start by requesting new astro data

# In[8]:


url = 'http://api.weatherapi.com/v1/astronomy.json'
place='Chengdu'
full_url=url+'?key='+api_key+'&q='+place+'&dt='+date
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
astro = response.json()


# ## Now ask for moon visability

# In[9]:


moon_vis=astro['astronomy']['astro']['moon_phase']
print(moon_vis)


# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# ## Get a new data pull
# (I can't find the max and min for the current weather pull, so just asking the historical data for today)

# In[10]:


url = 'http://api.weatherapi.com/v1/history.json'
full_url=url+'?key='+api_key+'&q='+place+'&dt='+date
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
current_weather = response.json()


# In[11]:


high_temp_f=current_weather['forecast']['forecastday'][0]['day']['maxtemp_f']
print("High temp:",high_temp_f)
low_temp_f=current_weather['forecast']['forecastday'][0]['day']['mintemp_f']
print("Low temp:",low_temp_f)

print(f"The temp difference is {high_temp_f-low_temp_f:.2f} degrees F.")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# I would rewrite the url variable and save the resulting dataset a different name.  That way, when I ask for a specific thing, I would have something like 
# ```
# dataA.keys()
# dataB.keys()
# ```

# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# ## Pull the 3 day forecast

# In[12]:


url = 'http://api.weatherapi.com/v1/forecast.json'
days = '3'
full_url=url+'?key='+api_key+'&q='+place+'&days='+days+'&aqi=no&alerts=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
forecast_weather = response.json()


# ## Do the analysis

# In[13]:


forecast_days=forecast_weather['forecast']['forecastday']

forecast_maxtemp=[day['day']['maxtemp_f'] for day in forecast_days]
print("The high temps are:",forecast_maxtemp)

for temp in forecast_maxtemp:
    if temp>75:
        print(f"{temp} F. is hot")
    elif temp>65:
        print(f"{temp} F. is warm")
    else:
        print(f"{temp} F. is cold")


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# ## Here is my naive attempt, just changing days=7

# In[14]:


url = 'http://api.weatherapi.com/v1/forecast.json'
days = '7'
full_url=url+'?key='+api_key+'&q='+place+'&days='+days+'&aqi=no&alerts=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
forecast_weather = response.json()


# In[15]:


forecast_days=forecast_weather['forecast']['forecastday']
print(len(forecast_days))


forecast_maxtemp=[day['day']['maxtemp_f'] for day in forecast_days]
print("The high temps are:",forecast_maxtemp)

for temp in forecast_maxtemp:
    if temp>75:
        print(f"{temp} F. is hot")
    elif temp>65:
        print(f"{temp} F. is warm")
    else:
        print(f"{temp} F. is cold")


# ## I am still somehow only pulling 3 days rather than 7
# 
# #### I looked at the air quality documentation, which says that air quality data is only for 3 days.  But I had turned aq off in my request so I am still not sure why it is not pulling 7 days.  Skipping for now.  
# 
# # INCOMPLETE COME BACK TO THIS

# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[16]:


forecast_maxtemp=[day['day']['maxtemp_f'] for day in forecast_days]
print(forecast_maxtemp)

#9.  Print the day with the highest maximum temperature.

###FINAL ANSWER HERE
#Create a var that is equal to the max temp, and then print the day whose own max temp matches that
max_temp_alldays=max(forecast_maxtemp)
for day in forecast_days:
    if day['day']['maxtemp_f']==max_temp_alldays:
        print(f"{day['date']} will be the hottest day, with a temperature of {day['day']['maxtemp_f']} F.")


# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# ## Pull Miami data

# In[17]:


url = 'http://api.weatherapi.com/v1/forecast.json'
days = '1'
place='Miami'
full_url=url+'?key='+api_key+'&q='+place+'&days='+days+'&aqi=no&alerts=no'
print(full_url)
response = requests.get(full_url)
# Turn the JSON into a dictionary
forecast_miami = response.json()


# ## Do the analysis

# In[18]:


#Create a list of the 24 hrs in the coming forecast -- this is a list of dictionariees
hours_list=forecast_miami['forecast']['forecastday'][0]['hour']

#Print the info
for hour in hours_list:
    if hour['cloud']>50:
        print(f"At {hour['time']}, it will be {hour['temp_f']} F and cloudy.")
    else:
        print(f"At {hour['time']}, it will be {hour['temp_f']} F.")


# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[19]:


count=0
hot_count=0
threshold=85
for hour in hours_list:
    if hour['temp_f']>threshold:
        hot_count=hot_count+1
    count=count+1

hot_percent=(hot_count/count)*100

print(f"It will be over {threshold} degrees {hot_percent}% of the time.")



# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# ### According to [https://www.weatherapi.com/pricing.aspx], it would cost 4 dollars a month.

# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# ### Would need to generate more more API keys, so sign up for multiple free accounts.  

# In[ ]:




