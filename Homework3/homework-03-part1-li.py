#Danielle Li
#June 13, 2022
#Homework 3, Part 1

####PRELIM STUFF
# Import the requests library
import requests


####ACTUAL ANSWERS

#1.  What is the URL to the documentation?
#https://pokeapi.co/docs/v2

#2.  What pokemon has the ID of 55?

#IMPORT INFO FOR 55
url = "https://pokeapi.co/api/v2/pokemon/55"
# Ask for the data from the website
response = requests.get(url)
# Turn the JSON into a dictionary
pokemon_55 = response.json()

#FINAL ANSWER HERE
print(pokemon_55['name'])

#3.  How tall is that pokemon? 

#FINAL ANSWER HERE
#According to doc, height is in decimeters -- results printed in feet
print(f"{pokemon_55['name']} is {(pokemon_55['height']/10)*3.28} feet tall")


#4.  How many versions of Pokemon games have been released?

#IMPORT INFO FOR VERSIONS
url = "https://pokeapi.co/api/v2/version/"
# Ask for the data from the website
response = requests.get(url)
# Turn the JSON into a dictionary
pokemon_version = response.json()

#Explore the data.
pokemon_version.keys()
#It looks like the versions are just listed in order
print(pokemon_version['results'][0])
print(pokemon_version['results'][1])
print(pokemon_version['results'][2])

#FINAL ANSWER HERE
print(f"There have been {len(pokemon_version['results'])} version of the Pokemon Games")

#5.  Print out the name of every electric-type pokemon.

#IMPORT INFO FOR ELETRIC TYPE
url = "https://pokeapi.co/api/v2/type/electric"
# Ask for the data from the website
response = requests.get(url)
# Turn the JSON into a dictionary
pokemon_elec = response.json()

pokemon_elec.keys()
#This seems like a list of dictionaries w/ a name element for the pokemon
print(pokemon_elec['pokemon'])
print(pokemon_elec['pokemon'][0].keys())
print(pokemon_elec['pokemon'][0]['pokemon']['name'])

#So now we use a list comprehension to get the name values of the elements of this list
main_list=pokemon_elec['pokemon']
pokemon_list=[item['pokemon']['name'] for item in main_list]

#FINAL ANSWER HERE
#This lists all the names for electric type
print(pokemon_list)

#6.  What are electric-type Pokemon called in the Korean version of the game?
pokemon_elec.keys()
#This seems like a list of names for what the eletric type is called
#pokemon_elec['names'] is a list with dictionary elements
print(pokemon_elec['names'])
#Each dictionary element has info on the language and the name of the type in the specified language.
print(pokemon_elec['names'][0].keys())
#This is the name of the type
print(pokemon_elec['names'][5]['name'])
#This is the associated language
print(pokemon_elec['names'][2]['language']['name'])

#So we just need to pick out the item that has the korean match
main_list=pokemon_elec['names']

#First just make sure I can grab all the languages before I start adding ifs
lang_list=[item['name'] for item in main_list]
print(lang_list)

#FINAL ANSWER HERE
#This lists just the Korean
ko_lang_list=[item['name'] for item in main_list if item['language']['name']=='ko']
print(ko_lang_list)

#7.  Who has a higher speed stat, Eevee or Pikachu?

#IMPORT INFO FOR BOTH 
url = "https://pokeapi.co/api/v2/pokemon/eevee"
# Ask for the data from the website
response = requests.get(url)
# Turn the JSON into a dictionary
pokemon_eevee = response.json()

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
# Ask for the data from the website
response = requests.get(url)
# Turn the JSON into a dictionary
pokemon_pikachu = response.json()

#Trying to understand the data -- looks like pokemon_eevee['stats'] is a list of dictionary elements, which of which describes a stat (speed, defense, etc.) 
print(pokemon_eevee['stats'])
print(pokemon_eevee['stats'][2].keys())

#For loop approach
for stat in pokemon_eevee['stats']:
    if stat['stat']['name']=='speed':
        eevee_speed=stat['base_stat'] 
print(eevee_speed)

for stat in pokemon_pikachu['stats']:
    if stat['stat']['name']=='speed':
        pikachu_speed=stat['base_stat'] 
print(pikachu_speed)

#List comprehension approach
eevee_speed2=[stat['base_stat'] for stat in pokemon_eevee['stats'] if stat['stat']['name']=='speed']
print(eevee_speed2)

pikachu_speed2=[stat['base_stat'] for stat in pokemon_pikachu['stats'] if stat['stat']['name']=='speed']
print(pikachu_speed2)

#FINAL ANSWER HERE
if pikachu_speed2>eevee_speed2:
    print("Pikachu is faster")
else:
    print("Eevee is faster")