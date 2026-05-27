# if/elif function - it means if a python has 1 condition 

age = int(input("Enter your age"))

if age >= 18 :
    print("You are an adult!")
else:
    print("Your are a minor!")

# elif funtion - it means if the python has more than 2 conditions 

marks = int(input("Enter your marks "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Filed")

# mini project - student Result checker 
name = input("Enter your name :")
maths = int(input("Enter maths marks :"))
science = int(input("Enter science marks :"))
english = int(input("Enter english marks :"))

total = maths + english + science 
Average = total / 3

print("Student Name :" , name )
print("Total Mrks:" , total)
print("Average marks :", Average)

if Average >= 90 :
  print("Grade : A  - Excellent!")
elif Average >= 70:
  print("Grade : B - Very Good!")
elif Average >= 50:
    print("Grade : C - Good!")
else:
    print("Grade : D - Fialed")