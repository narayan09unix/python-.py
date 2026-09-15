# Number guessing game
import random 

print(" --- WELCOME TO THE NUMBER GUESSING GAME ---") 
print("     GUESS THE NUMBER BETWEEN 1 TO 100")
print("     MAXIMUM ATTEMPTS: 7 ")


num = random.randint(1,100)
n = 0
attempts = 0

while attempts != 7 and n != num:
   print("")
   n = int(input("Enter the number you guessed: "))

   attempts = attempts + 1
   print("ATTEMPT: ", attempts)

   if( n == num):
       print("")
       print("CORRECT ANSWER, YOU WON THE GAME")
       print("Attempts taken: ", attempts)

   elif ( n < num and (num - n) > 15):
       print("YOUR GUESS IS TOO LOW.")

   elif ( n > num and (n - num) > 15):
       print("YOUR GUESS IS TOO HIGH.")

   else:
       print("INCORRECT GUESS.")

  
if( attempts == 7 ):
   print("")
   print("Attempts over, YOU LOSE.")
   print("The correct answer is: ", num)
   print("")