weight = float(input("enter your weight kilograms "))
height = float(input("enter your height centimeters "))
height = height/100

bmi = weight/(height*height)

if(bmi>0):
    if(bmi<=18.5):
        print("You are severely Underweight.")
    elif(18.5<bmi<24.9):
        print("You are healthy.")
    elif(25<bmi<29.9):
        print("You are overweight.")
    else:
        print("You are severely overweight.")
else:
    print("Enter valid details")