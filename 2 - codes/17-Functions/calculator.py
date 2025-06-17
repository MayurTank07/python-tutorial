def sum():
    print("\n\n\t\t***************** Addition *****************\n\n")

    num1 = int(input("\t\t\tEnter number 1 : "))
    num2 = int(input("\t\t\tEnter number 2 : "))
    print(f'\t\t\tAddition of {num1} and {num2} : {num1+num2}')
    
    print("\n\n\t\t*******************************************\n\n")

def sub():
    print("\n\n\t\t***************** Subtraction *****************\n\n")

    num1 = int(input("\t\t\tEnter number 1 : "))
    num2 = int(input("\t\t\tEnter number 2 : "))
    print(f'\t\t\tSubtraction of {num1} and {num2} : {num1-num2}')
    
    print("\n\n\t\t*******************************************\n\n")

def mul():
    print("\n\n\t\t***************** Multiplication *****************\n\n")

    num1 = int(input("\t\t\tEnter number 1 : "))
    num2 = int(input("\t\t\tEnter number 2 : "))
    print(f'\t\t\tMultiplication of {num1} and {num2} : {num1*num2}')
    
    print("\n\n\t\t*******************************************\n\n")

def divi():
    print("\n\n\t\t***************** Division *****************\n\n")

    num1 = int(input("\t\t\tEnter number 1 : "))
    num2 = int(input("\t\t\tEnter number 2 : "))
    print(f'\t\t\tDivision of {num1} and {num2} : {num1/num2}')
    
    print("\n\n\t\t*******************************************\n\n")


## to continue a loop we have created a loopy variable
loopy = "Y"

while(loopy == "Y"):

    print("\n\n\t\t***************** CALCULATOR *****************\n\n")
    print("\t\t\t\t 1. ADDITION \n")
    print("\t\t\t\t 2. SUBTRACTION \n")
    print("\t\t\t\t 3. MULTIPLICATION\n")
    print("\t\t\t\t 4. DIVISION \n")

    print("\n\n\t\t***************** CHOOSE ONE OPTION BELOW *****************\n\n")

    choice = int(input("\t\t\tEnter your choice between (1-4) : "))

    if choice == 1:
        sum()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        divi()
    else:
        print("\n\n\t\t***************** Invalid choice! *****************\n\n")
    
    loopy = input("\t\t\tDo you want to continue ? (Y/N) ")

print("\n\n\t\t***************** Exited *****************\n\n")


