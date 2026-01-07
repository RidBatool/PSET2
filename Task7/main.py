def calculate_minimum_speed(piles, k):
    left = 1
    right = max(piles)
    
    while left < right:
        mid = (left + right) // 2
        hours_needed = 0
        for pile in piles:
            hours_needed += pile // mid
            if pile % mid != 0:
                hours_needed += 1
        
        if hours_needed <= k:
            right = mid
        else:
            left = mid + 1
    
    return f'{left} bananas/hour'

print("First test case: ")
print(calculate_minimum_speed([5, 10, 3], 4))   
print("Second test case: ")       
print(calculate_minimum_speed([5, 10, 15, 20], 7))     

