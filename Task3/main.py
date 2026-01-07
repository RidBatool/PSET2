def find_longest_mirror_length(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1

    if s[0] == s[-1]:
        return 2 + find_longest_mirror_length(s[1:-1])
    else:
        return max(
            find_longest_mirror_length(s[1:]),
            find_longest_mirror_length(s[:-1])
        )
    
print("First Test case: ")
print(find_longest_mirror_length("bbabcbcab"))  
print("Second Test case: ")
print(find_longest_mirror_length("ABCD")) 
print("Third Test case: ")      
print(find_longest_mirror_length("RACECAR"))    
