def check_palindomic(num):
    l_1=list(str(num))
    if len(l_1)%2==0:
        for i in range(int(len(l_1)/2)):
            if not (l_1[i]==l_1[len(l_1)-1-i]) :
                return False
        return True
    else:
        for i in range(int((len(l_1)-1)/2)):
            if not (l_1[i]==l_1[len(l_1)-1-i]) :
                return False
        return True
print(check_palindomic(906609))
def find_palindrome(num_1):
    starting_no=int('1'+'0'*(num_1-1))
    ending_no=int('9'*num_1)
    highest_palindrome=0
    for i in range(starting_no,ending_no+1):
        for j in range(starting_no,ending_no+1):
            if check_palindomic(i*j)==True and (i*j)>highest_palindrome:
                highest_palindrome=i*j
                highest_no=i
                highest_no_2=j
    return highest_no,highest_no_2,highest_palindrome
print(find_palindrome(3))