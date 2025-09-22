def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def sum_of_primenumbers(num_1):
    total=0
    for i in range(2,num_1):
        if check_prime(i):
            total=total+i
    print(total)
sum_of_primenumbers(2000000)

        
        