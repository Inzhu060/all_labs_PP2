def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = list(map(int, input("List of numbers: ").split()))
prime_numbers = filter_prime(numbers)
print(prime_numbers)