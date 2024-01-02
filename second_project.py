# print("ASSAMULAIKUM BRO OR BHAI OR SIR OR DEAR PROGRAMMER.")
import random
top_of_range=int(input("Enter the number:"))
if top_of_range.int():
     top_of_range=int(top_of_range)
     
     
     if top_of_range<=0:
      print("enter the next time greather than 0")
      quit()
else:
     print("Enter the type next time.")
     quit()
  
random_range=random.randint(0,top_of_range)
guessess=0

while True:
 guessess +=1
 user_guess=int(input("make a guess"))
 if user_guess.isdigit():
  user_guess=int(user_guess)
 
 else:
     print("type a number in the next time ")
     continue
 if user_guess==random_range:
     print("your got a number")
 elif user_guess>random_range:
     print("enter the above the number")
 else:
     print("enter the below number")

 print("your guessess is ",guessess)
      
 
     




