#Write a program that seives out the height description of children aged 3-6 years to print the Growth level Indicated ;to check for stunted growth in children's heght measurement, short, tall and accelerated growth 

#y=height a=age n=name 
#a=3 h=94cm -95.2cm
#a=4 h=100.3cm - 102.3cm
#a=5 h=107.9cm -109.2cm
#a=6 h=115.5cm- 115.5cm

name=input("Name of student")
x=int(input("Enter age"))
y=float(input("Enter height"))
if(x==3 and 94<=y<=95.2): #Average height
    print(name, "is of average growth height")
elif(x==3 and 80<=y<94):
    print(name, "is below his average growth height. He has a short stature.")#Short stature
elif(x==3 and y<80):
    print(name, "is experiencing stunted growth and requires medical review.")#Stunted Growth
elif(x==3 and y>95.2):
    print(name, "is above his average growth height. He has a tall stature.")#Tall Stature
elif(x==3 and y>100.3):
    print(name, "is experiencing accelerated growth, and has the propensity to join the Lakers  jr. basketball club")#Accelerated growth

elif(x==4 and 100.3<=y<=102.3): #Average height
    print(name, "is of average growth height")
elif(x==4 and 80<=y<100.3):
    print(name, "is below average growth height and has a short stature.")#Short stature
elif(x==4 and y<80):
    print(name, "is experiencing stunted growth and requires medical review.")#Stunted Growth
elif(x==4 and y>102.3):
    print(name, "is above average growth height and has a tall stature.")#Tall Stature
elif(x==4 and y>107.9):
    print(name, "is experiencing accelerated growth, and has the propensity to join the Lakers  jr. basketball club")#Accelerated growth

elif(x==5 and 107.9<=y<=109.2): #Average height
    print(name, "is of average growth height")
elif(x==5 and 90<=y<107.9):
    print(name, "is below average growth height and has a short stature.")#Short stature
elif(x==5 and y<90):
    print(name, "is experiencing stunted growth and requires medical review.")#Stunted Growth
elif(x==5 and y>109.2):
    print(name, "is above average growth height and has a tall stature.")#Tall Stature
elif(x==5 and y>115.5):
    print(name, "is experiencing accelerated growth, and has the propensity to join the Lakers  jr. basketball club")#Accelerated growth

elif(x==6 and 115.5<=y<=115.5): #Average height
    print(name, "is of average growth height")
elif(x==6 and 100<=y<115.5):
    print(name, "is below average growth height and has a short stature.")#Short stature
elif(x==6 and y<100):
    print(name, "is experiencing stunted growth and requires medical review.")#Stunted Growth
elif(x==6 and y>115.5):
    print(name, "is above average growth height and has a tall stature.")#Tall Stature
elif(x==6 and y>122.5):
    print(name, "is experiencing accelerated growth, and has the propensity to join the Lakers  jr. basketball club")#Accelerated growth

else:
    print (name, "has an interesting growth rate and requires urgent medical attention")

