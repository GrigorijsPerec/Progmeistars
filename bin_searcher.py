def BinarySearch_game(vel, searched):
    left = 0
    right = len(vel)-1
    index = -1
    while (left <= right) and (index == -1):
        mid = (left + right)//2
        if vel[mid] == searched:
            index = mid
        else:
            if searched<vel[mid]:
                right = mid -1
            else:
                left = mid +1
    return index