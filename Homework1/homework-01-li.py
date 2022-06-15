#Danielle Li
#June 12, 2022
#Homework 1

yob=int(input("What year were you born in?"))
if yob>2022:    
    print("You are already born.  Try again")
    yob=int(input("What year were you born in?"))
elif yob<=2022:
    i=0

print("Great!  Here is some info you didn't ask for")

#1. How old the user is
age=2022-yob
print("You are",age,"years old")

#2. How many times the user's heart has beaten
#stats are from https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979#:~:text=A%20normal%20resting%20heart%20rate%20for%20adults%20ranges%20from%2060,to%2040%20beats%20per%20minute.
hb_human=round(75*60*24*365*age/1000000, 2)
print("Your heart has beaten", hb_human, "million times since you were born")

#3. How many times a blue whale's heart has beaten
#stats from https://www.theatlantic.com/science/archive/2019/11/diving-blue-whales-heart-beats-very-very-slowly/602557/
#11 beats per minute 
#11*60*24*365
hb_whale=round(11*60*24*365*age/1000000, 2)
print("A blue whale's heart has beaten", hb_whale, "million times since you were born")

#4. How many times a rabbit's heart has beaten
#stats from https://rabbit.org/temperature-and-respiration-rates/
#120-150 beats per minute 
#135*60*24*365
hb_rabbit=round((135*60*24*365*age)/1000000, 2)
print("A rabbit's heart has beaten", hb_rabbit, "million times since you were born")

#5. How old they are in Venus years
#stats from https://www.spacecentre.nz/resources/faq/solar-system/venus/how-old-would-i-be.html#:~:text=A%20year%20on%20Venus%20is,the%20orbit%20of%20Earth's%20Moon.
age_venus=round(age/.615, 2)
print("You are", age_venus, "years old on Venus")

#5. How old they are in Neptune years
#stats from https://www.spacecentre.nz/resources/faq/solar-system/neptune/how-old-would-i-be.html
age_nep=round(age/165, 2)
print("You are", age_nep, "years old on Neptune")


#6. Whether they are the same age as you, older or younger.  If older or younger, how many years difference
age_dif=(2022-1983)-age
abs_age_dif=abs(age_dif)
if age_dif>0:
    print("I am",abs_age_dif, "years older than you")
elif age_dif<0:
    print("I am",abs_age_dif, "years younger than you")
elif age_dif==0:
    print("You are the same age as me")

#7. If they were born in an even or odd year
agemod2=age%2
if agemod2==0:
    print("You were born in an even year")
elif age!=0:
    print("You were born in an odd year")

#8. How many times there has been a president from the D Party in office since they were born (1960 onward, and each president only counts once)
#dictionary input taken from Shreya  Raman
presidents={
"Dwight Eisenhower": ["R", 1960, 1961],
"John Kennedy" : ["D", 1961, 1963],
"Lyndon Johnson": ["D", 1963, 1969],
"Richard Nixon": ["R", 1969, 1974],
"Gerald Ford": ["R", 1974, 1977],
"Jimmy Carter": ["D", 1977, 1981],
"Ronald Reagan": ["R", 1981, 1989],
"George Bush": ["R", 1989, 1993],
"Bill Clinton": ["D", 1993, 2001],
"George W Bush": ["R", 2001, 2009],
"Barack Obama": ["D", 2009, 2017],
"Donald Trump": ["R", 2017, 2021],
"Joe Biden": ["D", 2021, 2022]
}

pres_count=0
print("Here are the presidents who have been in office since you were born")
#Loop over each row of presidents dataset.  curr pres is name of the row we are on
for currpres in presidents.keys():
    #This picks out the 3rd feature (since we count from 0) of the current row.  That element is the year they left office.  So if they left office after we were born, they have been in office at some point since we were born. 
    if presidents.get(currpres)[2]>=yob:
        pres_count=pres_count+1
        print(currpres)

print("There have been", pres_count, "presidents since you were born")

demopres_count=0
print("Here are the Democratic presidents who have been in office since you were born")
       
#Loop over each row of presidents dataset
#same as above, but with the and to only count if someone was in office and also a democrat.
for currpres in presidents.keys():
    if presidents.get(currpres)[0]=="D" and presidents.get(currpres)[2]>=yob:
        demopres_count=demopres_count+1
        print(currpres)

print("There have been", demopres_count, "Democratic presidents since you were born")













