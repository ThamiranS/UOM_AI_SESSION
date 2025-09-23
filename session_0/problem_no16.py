def power_digits(base,number):
    power_digit=base**number
    total=0
    power_digit_str=str(power_digit)
    for i in range(len(power_digit_str)):
        total+=int(power_digit_str[i])
    return total
print(power_digits(2,1000))