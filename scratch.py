#Random stuff
n=10
if n>0:
    print("A")
    if n>=3:
        print("B")
    elif n>2:
        print("E")
elif n>-2:
    print(G)
else:
    print(H)

cat = {
    'name':'Jack',
    'age': 6,
    'color': 'white'
}


cat = {
    'Jack':[6, 'white'],
    'Abby':[8, 'tabby']
}


art_pieces = [
    {'title': 'Gold Star', 'year': 1805},
    {'title': 'Blunderbuss', 'year': 1800},
    {'title': 'Chairlift', 'year': 1976},
    {'title': 'Rancor', 'year': 2002}
]

for piece in art_pieces:    
    print(piece['title'])

#But say yuou just want a list of the titles: [Gold start, etc. ]

#I have a list of dictionaries, but I just want one thing from each dictionary.  So I want a list of the elements of the dictionary
# 
titles=[piece['title'] for piece in art_pieces]
print(titles)

#If you want years?
titles=[piece['year'] for piece in art_pieces]
print(statistics.mean(titles))

#What about the names of the stuff before 1900

titles=[piece['title'] for piece in art_pieces if piece['year']<1900]
print(titles)