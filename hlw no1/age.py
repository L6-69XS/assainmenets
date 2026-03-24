age = input("are you above 10 years old? (Y/N)").strip().upper()

if age =="Y":
    print("you are allowed")
else:
    age= int(input("enter the age of the child"))

    if age <= 10 :
        print ("allowed")
    else:
        print (" not allowed")