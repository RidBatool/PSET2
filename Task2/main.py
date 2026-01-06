def balancedchallenges(list_):
    sum_= sum(list_)
    if sum_%2!=0:
        return False
    value= sum_//2
    dp=[False]*(value+1)
    dp[0]=True
    for s in list_:
        for j in range(value, s-1, -1):
            dp[j]= dp[j] or dp[j - s]
           
    return dp[value]
print("first run  : [1, 5, 11, 5]")
print(balancedchallenges([1, 5, 11, 5]))
print("second run  : [1, 3, 5]")
print(balancedchallenges([1, 3, 5]))

