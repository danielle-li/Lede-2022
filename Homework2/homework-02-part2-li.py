#Danielle Li
#June 12, 2022
#Homework 2 Part 2


##############################PART TWO: Lists

#1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries=["Russia", "Italy", "USA", "Mexico"]

#2) Using a for loop, print each element of the list
for c in countries:
    print(c)

#3) Sort the list permanently.
countries=sorted(countries)

#4) Display the first element of the list.
print(countries[0])

#5) Display the second-to-last element of the list.
print(countries[-2])

#6) Delete one of the countries from the list using its name.
countries.remove('USA')
print(countries)

#7) Using a for loop, print each country's name in all caps.
for c in countries:
    print(c.upper())


##############################PART TWO: Dictionaries

#These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*, or use any other tool that exists online.

#Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. (See here for explanation (Links to an external site.))

#1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
   'name': 'khat',
   'species' : 'C. edulis',
   'age': 5,
   'location_name': 'Nairobi',
   'lat': -1.29,
   'long': 36.82
}

#2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"
print(f"{tree['name']} is a {tree['age']} year old tree that is in {tree['location_name']}.")

#3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
nyc_lat=40.7
if tree['lat']<nyc_lat:
    print(f"The tree {tree['name']} in {tree['location_name']} is south of NYC")
else:
    print(f"The tree {tree['name']} in {tree['location_name']} is north of NYC")


#4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

your_age=int(input("How old are you (in years)?"))
if your_age>tree['age']:
    print(f"You are {your_age-tree['age']} years older than {tree['name']}")
else:
    print(f"You are {tree['age']-your_age} years younger than {tree['name']}")



##############################PART TWO: Lists of dictionaries

#1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

cities = [
	{
        'name':'Moscow',
		'lat':55.76,
		'long':37.62
	},
	{
        'name': 'Tehran',
        'lat': 35.72,
        'long': 51.33
	},
	{
        'name': 'Falkland Islands',
        'lat': -51.80,
        'long':-59.52
	},
    {
        'name': 'Seoul',
        'lat': 37.57,
        'long': 126.98
	},
    {
        'name': 'Santiago',
        'lat': -33.45,
        'long': -70.67
    }
]

print(cities)


#2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

for c in cities:
    #First check for Falkland island matches
    if c['lat']>0 and c['name'].startswith('Falk'):
        print(f"{c['name']} are above the equator.  The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
    elif c['lat']<0 and c['name'].startswith('Falk'):
        print(f"{c['name']} are below the equator.  The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    #Then check others
    elif c['lat']>0:
        print(f"{c['name']} is above the equator.")
    else:
        print(f"{c['name']} is below the equator.")

#3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

for c in cities:
    if c['lat']>tree['lat']:
        print(f"{c['name']} is above {tree['name']}")
    else:
        print(f"{c['name']} is below {tree['name']}")