# ______string functions ____

str = "I am Laiba, I am tech Enthausiats"
# __endswith()_____
print(str.endswith("ats")) #true

#______capatalize____ => it will only convert first character into uppercase

str1 = "laiba is a supper girl"
print(str1.capitalize()) #only convert first character
#___ replace ____ returns a new changeable string previous string is same as it is.
print(str1.replace("is", 'has'))
print(str1)

#____ find()___
print(str1.find('laiba')) #0 
print(str1.find('i')) #2 i exists at 2nd index for the first time
print(str1.find('qwerty')) #-1 for not existing word

#taking input from a user and print its lenght
f_name = input('enter your first name:')
print(f_name , len(f_name)) #Laiba , 5

#___________________ conditional statements ___________
marks = int(input("enter your marks:"))
if marks >= 90:
    print('Your grade is "A"')
elif marks < 90 and marks >= 80:
    print('your grade is "B"')
elif marks < 80 and marks >= 70:
    print('your grade is "C"')
else:
    print('your grade is "F"') 




