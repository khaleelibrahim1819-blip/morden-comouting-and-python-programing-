# decision making and branching 

# true o false 

# Expression-> combination of operand and operator 

# a greater than b
a = int(input("enter the  value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c: "))
d = int(input("enter the value of d: "))

# a=10, b=20 and c=30 d=40
if ( a > b):
    print(f"{a} is largest")
elif ( b > c ): 
    print(f"{b} is the largest ")
    
elif ( c > d ):
    print(f"{c} is largest ")
    
else: 
    print(f"{d} is the largest ")
    