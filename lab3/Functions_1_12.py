def histogram(lst):
    for num in lst:
        print("*" * num)

numbers = list(map(int, input("Enter: ").split()))
histogram(numbers)