def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

numbers = list(map(int, input("Enter numbers: ").split()))
print(spy_game(numbers))