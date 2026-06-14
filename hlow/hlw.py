
try:
    age = int(input("enter your age "))
    if age < 0 or age > 120:
        print:("invalid age entered")
    else:
        print("valid age entered")
        

        if age % 2 == 0:
            print("the age is even")
        else:
            print("age is odd")
            
except ValueError:
    print:("please enter valid number.")