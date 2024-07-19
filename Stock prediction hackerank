from __future__ import division
from math import sqrt
from heapq import heappush, heappop

def printTransactions(money, k, d, names, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        avg = mean(nums)
        return sqrt(sum((x - avg) ** 2 for x in nums) / len(nums))

    def info(price):
        if price[-2] == 0:  # Prevent division by zero
            return 0
        return (price[-1] - price[-2]) / price[-2]

    infos = [info(prices[i]) for i in range(k)]
    res = []
    drop = []

    # Determine which stocks to sell and which to buy
    for i in range(k):
        cur_info = infos[i]
        if cur_info > 0 and owned[i] > 0:
            res.append((names[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heappush(drop, (cur_info, i, names[i]))

    # Buy stocks from the drop list if there's money available
    while money > 0.0 and drop:
        rate, idx, name = heappop(drop)
        price = prices[idx][-1]
        amount = int(money / price)
        if amount > 0:
            res.append((name, 'BUY', str(amount)))
            money -= amount * price

    # Output the results
    print(len(res))
    for r in res:
        print(' '.join(r))

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    
    # Read all input at once
    data = input().strip().split('\n')
    
    # First line: initial money, number of stocks, number of days
    m, k, d = map(float, data[0].strip().split())
    k = int(k)
    d = int(d)
    
    names = []
    owned = []
    prices = []

    # Read each stock's data
    for i in range(1, k + 1):
        temp = data[i].strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:]])

    # Process and print transactions
    printTransactions(m, k, d, names, owned, prices)
