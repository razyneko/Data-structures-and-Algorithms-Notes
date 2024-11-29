n = int(input("Enter the number : "))
x = int(input("Enter the power for the number : "))

def power(n,x):
    assert int(x) == x and x >=0 , "Power must be postive integer including zero"
    if x == 0:
        return 1
    else:
        return n * power(n,x - 1)
    
print(power(n,x))
    