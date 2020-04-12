#Implemmentation of binary search in python3.7

def binary_search(sorted_list, item):
    low = 0 
    high = len(sorted_list) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = sorted_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None

li = [10,40,110,230,451,1234, 12322]

print(binary_search(li, 110))