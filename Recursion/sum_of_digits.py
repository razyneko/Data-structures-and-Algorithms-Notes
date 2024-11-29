n = int(input())
def sum_of_digits(n):
    assert n >= 0 and int(n) == n ,"Number must be an integer greater than or equal to zero."
    if n == 0:
        return 0;
    else:
        digit = n % 10
        return digit + sum_of_digits(n//10)
    
print(sum_of_digits(n))