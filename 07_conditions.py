# conditions in python

#age > 18 , marks>77, percentage = 70+

name= input('Enter your name')
age = input('Enter your age')
s1 = input('Enter your marks in english')
s2 = input('Enter your marks in physics')
s3 = input('Enter your marks in chemistry')
s4 = input('Enter your marks in psychology')

percentage = s1+s2+s3+s4/4
total = s1+s2+s3+s4

if age>= 18: 
    print("You are elligible for addimission")
else:
    print("Your age is "+age+"Apply next year")

print("Your percentage is: "+percentage, type(int(percentage)))
print("Your total marks are "+total)
print("Confirm your name", name)

