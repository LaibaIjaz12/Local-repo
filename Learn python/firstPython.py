print('Hi I am Laiba')

a = 10
b = 12
if a < b:
    print('a is less than b', a)
elif b < a: 
    print('b is less than a', b)
else:
    print(a ,b )

# _______________________Type conversion _____
# Python automatically convert the type of data accordingly 

name = 'laiba'
father_name = 'ijaz hussain'
age = 20
cgpa = 3.78


# sum = name + father_name + age ==>>> " we will get the error But in JS we can add them and JS do type coersion and it will convert int into str"
# print(sum, type(age))

print(age + cgpa) # it will convert age into float because float has high precedence " age = 20.00"
print(type(age))

#  _________type casting ==> we forcefully convert the type and then add them

convertAge = str(age)  # this is manually
sum = name +" "+ father_name +" " +convertAge  # noe it will concatenate coz we have now change the basics
print(sum)

# __________ how to get input from thr user___________
# userName = input(" Enter your Name:")
# interMarks = int(input(" Enter your intermediate marks :"))
# ecatMarks = int(input("Enter your Ecat marks:"))

# aggregate = ((interMarks) * 75/100) + ((ecatMarks) * 25/100)

# if aggregate >= 80:
#     print("congratulations " + userName + " !" + " your agregate is" + str(aggregate) +". " )
#     print('you have successfully enrolled in Computer Scinece')
# if aggregate >70 :
#     print("congratulations " + userName + " !" + " your agregate is" + str(aggregate) +". " )
#     print('you have successfully enrolled in IT')

# ____strings in python 


first_name = 'Laiba'
Last_name = 'Ijaz'
full_Name = first_name + Last_name #concatination 
#length of a string
print(full_Name, len(full_Name), )
# print(full_Name[9])  Error occure string index is out of range 

#  ____Slicing of strings 

para = 'My name is laiba, I am tech Enthausiats'
# want to print just 'laiba' from the whole string 
# Slicing it into chunks

cut_para = para[11 : 16] #para[starting index : ending index]
print(len(para), cut_para)
cut_para1 = para[18 :] #para[I : len(para)]
print(cut_para1)

# slicing with negative indexes
neg_para = "LaibaFaiz"
print(neg_para[-4 :]) #it will return an empty space if I used zero as an ending index




