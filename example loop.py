a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("Press 1 for addition, 2 for subtraction, 3 for multiplication")
operation=int(input("Enter the operation you want to perform?"))

if operation==1:
  sum=a+b
  print("Summation: ",sum)
elif operation==2:
  multip=a*B
  print("Multiplication: ",multip)
else:
  print("Press 1/2/3. Invalid Number")