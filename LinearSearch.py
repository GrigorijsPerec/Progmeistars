def LinearSearch(vel, wn):
    for i in range (len(vel)):
        if vel[i] == wn:
            return i
    return -1