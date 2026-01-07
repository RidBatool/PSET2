def calculate_minimum_speed(piles, k):
    value = sum(piles)
    print(value)
    if value%k==0:
        return value//k
    else:
        return (value//k)+1
    
print("First test case: ")
print(calculate_minimum_speed([5, 10, 3], 4))
print("Second test case: ")
print(calculate_minimum_speed([5, 10, 15, 20], 7))