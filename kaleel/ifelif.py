psum = psum = 0 
number = int(input("enter a number: "))

while (number != -1):
    if (number > 0):
        print("positive")
        psum = psum + number 
    elif (number < 0 ):
        print("Negative")
        nsum = nsum + number 
    else:
        print("Zero")
        
        number = int(input("enter a number: "))
        
print("total of positive numbers:", psum)
print("total of negative numbers:", nsum)
        
        