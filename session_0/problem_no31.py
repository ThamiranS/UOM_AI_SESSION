coins=[1,2,5,10,20,50,100,200]
def count_times(num,coins):
    if num==0:
        return 1
    if num<0:
        return 0
    if len(coins)<=0 and num>=1:
        return 0
    return count_times(num-coins[-1],coins)+count_times(num,coins[:-1])
print(count_times(200,coins))

