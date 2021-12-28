def BinarySearch(sda, ser):
    left = 0
    right = len(sda)-1
    index = -1
    while (left <= right) and (index == -1):
        mid = (left + right)//2
        if sda[mid] == ser:
            index = mid
        else:
            if ser<sda[mid]:
                right = mid -1
            else:
                left = mid +1
    return index