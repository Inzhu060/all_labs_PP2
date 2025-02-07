def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

elements = list(map(int, input("Enter: ").split()))
print(unique_list(elements))