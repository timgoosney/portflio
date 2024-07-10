import random
number = random.randint(1, 10)

print ("Random Number Generator")
print("Hmmm... I am thinking of a number between 1-10, try and guess it!")
print ()

def guessing():
  num = int(input("Pick a number between 1 and 10: "))
  if num > number:
    print ("Too high! Try again")
    guessing()
  elif num < number: 
    print ("Too low! Try again")
    guessing()
  elif num == number:    
    print ("Congrats! You have guessed the number.")
guessing()



