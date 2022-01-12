import random

def SimpleSearch(vel, wn):
    for i in range (len(vel)):
        search = (random.choice(vel))
        if search == wn:
            searched = vel.index(search)
            print("Это число с индексом: " + str(searched))