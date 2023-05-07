n1 = float(input("Enter First Number: "))

operator = input("Seclection an operator: (+,-,*,/): ")

n2 = float (input("Enter Second Number: "))

if operator == "+":
     print(n1+n2)

elif operator == "-":
     print(n1-n2)

elif operator == "*":
     print(n1*n2)

elif operator == "/":
     print(n1/n2)

else: 
     print("Invalid Input")
