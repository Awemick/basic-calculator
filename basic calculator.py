num1 = float(input("Enter first Number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter an expression(,+,-,*,/):")

if operation=='+':
   result = num1 + num2
   print(f"The result is: {result}")

elif operation =='-':
	reslut = num1 - num2
	print(f"The result is: {reslut}") 

elif operation == '*':
	result = num1 * num2
	print(f"The result is: {result}")

elif operation == '/':
	if num2 != 0:
		result= num1 / num2
		print(f"the result is: {result}")

	else:
		print("zero division not allowed")
