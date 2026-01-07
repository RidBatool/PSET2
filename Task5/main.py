def min_cancelled_bookings(intervals):
    ans_list=[]
    if not intervals:
        return 0

    sorted_arr = sorted(intervals, key=lambda x: x[0])
    ans_list+=[sorted_arr[0]]
    for i in range(1, len(intervals)):
        if ans_list[-1][-1]>sorted_arr[i][0]:
            if ans_list[-1][-1]>sorted_arr[i][1]:
                ans_list[-1]=sorted_arr[i]
            else:
                continue
        else:
            ans_list+=[sorted_arr[i]]
        # print(ans_list)
    return len(intervals)-len(ans_list)

print("First Test case: ")
print(min_cancelled_bookings([[1, 2], [2, 3], [3, 4], [1, 3]]))
print("Second Test case: ")
print(min_cancelled_bookings([[1, 3], [1, 3], [1, 3]]))
print("Third Test case: ")
print(min_cancelled_bookings([[1, 2], [5, 10], [18, 35]]))