#Danielle Li
#June 12, 2022
#Homework 2 Part 1


##############################PART ONE: Lists


#1. Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
list=[22, 90, 0, -10, 3, 22, 48]

#2.  Display the number of elements in the list.
print(len(list))

#3.  Display the 4th element of this list.
print(list[3])

#4.  Display the sum of the 2nd and 4th element of the list.
print(list[1]+list[3])

#5.  Display the 2nd-largest value in the list.
list_sorted=sorted(list)
print(list_sorted)
print(list_sorted[-2])

#6.  Display the last element of the original unsorted list
print(list[-1])

#7.  Display the sum of all of the numbers divided by two.
print(sum(list)/2)

#8.  Print whether the median or the mean of the numbers is higher
import statistics
mean=statistics.mean(list)
med=statistics.median(list)
print("Median is", med)
print("Mean is", mean)
if mean>med:
    print("Mean is higher")
elif med<mean:
    print("Median is higher")
else:
    print("They are equal")


##############################PART ONE: Dictionaries

#1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
    'title':'Eurotrip',
    'year': 2004,
    'director': 'No clue'
}

print(f"My favorite movie is {movie['title']}, which was released in {movie['year']} and was directed by {movie['director']}")

#2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

movie = {
    'title':'Eurotrip',
    'year': 2004,
    'director': 'No clue',
    'revenue': 20.8,
    'budget': 25,
}

profit=round(movie['revenue']-movie['budget'], 2)
print(profit)

#3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

if profit<0:
    print("That was a bad investment")
elif movie['revenue']/movie['budget']>5:
    print("That was a great investment")
else:
    print("That was an ok investment")

#4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

pop = {
'Manhattan': 1.6,
'Brooklyn': 2.6,
'Bronx': 1.4,
'Staten Island': .47
}

#5) Display the population of Brooklyn.
print(f"The population of Brooklyn is {pop['Brooklyn']:.2f} million")

#6) Display the combined population of all five boroughs.
total_pop=sum(pop.values())
print(f"Total population of NYC is {total_pop:.2f} million")

#7) Display what percent of NYC's population lives in Manhattan.
print(f"The population of Manhattan is {pop['Manhattan']:.2f} million")
print(f"Manhattan's share of total population of NYC is {(pop['Manhattan']/total_pop):.2f}")

