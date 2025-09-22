def check_even(num):
    if num%2==0:
        return True
    else:
        return False
def  fibonacci(num_1):
    a=1
    b=1
    total=0
    while b<num_1:
        a,b=b,a+b
        if check_even(b):
            total=total+b
    print(total)
fibonacci(1000000)
