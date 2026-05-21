import art
print("==============================Yusuf Calculator============================")
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
condition = True
operation ={"+":add,"-":subtract,"*":multiply,"/":divide}
first_number =int(input("Enter your first number:"))
while condition:
     function = input("""+, -, *, /.
Enter Operation:""")
     second_number = int(input("Enter your second number:"))
     if function not in operation:
         print(f"Please enter a valid operation")
         continue
     if function == "/" and second_number ==0:
        print("Cannot divide by zero")
        continue
     if function in operation:
         Result=(operation[function](first_number, second_number))
         print(f"The result is :{Result}")
     will_continue=input(f"Want to continue Calculation with {Result} Type 'y'. If not Type 'n' to start a new calculation.Type 's' to stop:").lower()
     if will_continue == "y":
         first_number= Result
     elif will_continue =="n":
         print("\n"* 100)
         first_number = int(input("Enter your first number: "))
     elif will_continue =="s":
         print("Thank you for using yusuf's calculator.")
         condition = False
     else:
         print("Please enter 'y','n' or 's'")
