import datetime
#Create a program that will accept one word and display it in the following patterns:
def As_Entered():
   a = str(input("enter a String: "))
   print(a)

def Capital_First_Letter():
   a = str(input("enter String: "))
   print(a.capitalize())

def All_Uppercase():
    a = str(input("enter String: "))
    print(a.upper())

def All_Lowercase():
    a = str(input("enter String: "))
    print(a.lower())

def Repeat_Word_1():
    a = str(input("enter String: "))
    print(a+a+a+a+a)

def Repeat_Word_2():
    a = str(input("enter String: "))
    print(a*5)

#Create a program that will accept a person’s first name, middle name, and last name then display the following messages:
def Hello():
    a = str(input("enter Firstname: "))
    b = str(input("enter Middlename: "))
    c = str(input("enter Lastname: "))
    print("Hello "+ a + " " + b + " " + c)
def Hi():
    a = str(input("enter Firstname: "))
    b = str(input("enter Middlename: "))
    c = str(input("enter Lastname: "))
    print("Hi "+ a + " " + b + " " + c)

#Create a program that accepts 2 Numbers and displays the sum, difference, product, quotient, 1st Number modulo 2nd Number, and 1stnumber raise to 2nd number.
def Calculator():
    a = int(input("Enter First number: "))
    b = int(input("Enter Second number: "))
    print("Sum: " + str(a+b))
    print("Difference: " + str(a-b))
    print("Product: " + str(a*b))
    print("Quotient: " + str(a/b))
    print("Modulo: " + str(a%b))
    print("Raise: " + str(a**b))

#Create a program that will accept a person’s whole name and their current age then display the following messages:
def yourself():
    a = str(input("enter name: "))
    b = int(input("enter Age: "))
    y = int(datetime.datetime.now().strftime("%Y"))
    x = y-b
    z = 100 - b + y
    k = z - y
    message = 'Hello %s, you are currently %d years old\nYou were born on %d\nBy %d you will be 100 years old\nYou will have to wait %d years to be 100 years old' %(a,b,x,z,k)
    print(" ")
    print(message)
    


#A loop for the program to keep running
while True:
    print(
          "1. As_Entered\n" +
          "2. Capital_First_Letter\n" +
          "3. All_Uppercase\n" +
          "4. All_Lowercase\n" +
          "5. Repeat_Word_1\n" +
          "6. Repeat_Word_2\n" +
          "7. Hello\n" +
          "8. Hi\n" +
          "9. Calculator\n" +
          "10. Yourself\n")

    selection = input("Enter Selection: ")
    
    print()
#The selection from the program
    {"1":As_Entered,
     "2":Capital_First_Letter,
     "3":All_Uppercase,
     "4":All_Lowercase,
     "5":Repeat_Word_1,
     "6":Repeat_Word_2,
     "7":Hello,
     "8":Hi,
     "9":Calculator,
     "10":yourself
    }[selection]()
    
    print()
        
        
