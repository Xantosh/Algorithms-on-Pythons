def binary_search(list, item):
    low = 0
    high = len(list) - 1

    if low <= high :
        mid = (low + high)// 2
        choice = list[mid]

        if choice == item:
            return mid

        if choice > item:
            high = mid -1

        else:
            low = mid + 1

    return None

print(binary_search([1,4,5,7,8,9], 5))
print(binary_search([1,4,5,7,8,9], -1))