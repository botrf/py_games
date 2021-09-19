print("Stat games")

playing = input("Do you wont to play? ")

if playing.lower() != "yes":
   quit()

print("Okay! Let's play ")
score = 0 

answer = input("What does CPU stand for? \n")
if answer.lower() == "central processing unit":
   print("Correct!")
   score += 1
else:
   print("Incorrect!")
 
print("You got " + str(score) + " questions correct")