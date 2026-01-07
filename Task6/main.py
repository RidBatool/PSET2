def maximize_freelance_profit(deadlines, profits):
    jobs = [[profits[i], deadlines[i]] for i in range(len(deadlines))]
    jobs.sort(reverse=True, key=lambda x: x[0])
    max_deadline = max(deadlines)
    slots = [0] * (max_deadline + 1)
    total_profit = 0
    total_jobs = 0

    for profit, deadline in jobs:
        for d in range(deadline, 0, -1):
            if slots[d] == 0:
                slots[d] = 1
                total_profit += profit
                total_jobs += 1
                break

    return [f'{total_jobs} Jobs,  {total_profit} Profit']

print("First test case: ")
print(maximize_freelance_profit([4, 1, 1, 1], [20, 10, 40, 30]))
print("Second test case: ")
print(maximize_freelance_profit([2, 1, 2, 1, 1], [100, 19, 27, 25, 15]))

