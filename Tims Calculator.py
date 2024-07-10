#functions
#function to add two numbers
def add(x, y):
  return x + y
#function to subtract two numbers
def subtract(x, y):
  return x - y
#function to multiply two numbers
def multiply(x, y):
  return x * y
#function to divide two numbers
def divide(x, y):
  return x / y

print ("Tims Calculator!")
print ("Select operation.")
print ("1.Add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")
while True:
  #take input from the user
  choice = input("Enter choice(1/2/3/4): ")
  #check if choice is one of the four options
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
      if num2 == 0:
        print("No zeros please!")
      print(num1, "/", num2, "=", divide(num1, num2)) #division by 0 isnt possible

#check if user wants to continue
    next = input("Let's do next calculation? (yes/no): ")
    if next == "no":
      print("Thank you for using Tims Calculator!")
      break
    elif next == "yes":
      continue
    else:
      print("Invalid Input")
      print