def count_payment_combinations(coins, total_sum, ind=0, memo=None):
    if memo is None:
        memo = {}
    
    if total_sum == 0:
        return 1
    if total_sum < 0 or ind == len(coins):
        return 0
    
    if (total_sum, ind) in memo:
        return memo[(total_sum, ind)]
    
    include = count_payment_combinations(coins, total_sum - coins[ind], ind, memo)
    exclude = count_payment_combinations(coins, total_sum, ind + 1, memo)
    
    memo[(total_sum, ind)] = include + exclude
    return memo[(total_sum, ind)]

print("First test case: ")
print(count_payment_combinations([1, 2, 3], 4)) 
print("second test case:")
print(count_payment_combinations([2, 5, 3, 6], 10))  
print("third test case: ")
print(count_payment_combinations([5],4))  