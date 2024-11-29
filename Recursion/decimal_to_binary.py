n = int(input("Enter the number : "))
def to_binary(n):
    assert n >= 0 and int(n) == n , "Enter correct number"
    if n == 0:
        return 0
    else:
        return (n % 2) + 10* to_binary(n//2)

print(to_binary(n))
     