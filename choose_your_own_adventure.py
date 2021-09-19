name = input("Type your name: ")
print("Welcome", name, "tothis adventure!")

answer = input("You are on dirt road, it has come to am end and you can go left or right. Which way world you like to go? ").lower()

if answer == "left":
   answer = input("You came to a river, you can walk around it or swim accross? Type  walk around and swin to swin accross: ")

   if answer == "siwm":
      print("You swam acrross and were eaten by an alligator.")
   elif answer == "walk":
      print("You walked for many miles, ran out of water and lost the games.")

   else:
      print("Not a valid option. You lose.")


elif answer == "right":
   answer = input()
   if answer == "back":
      print("You go back and lose.")
   elif answer == "cross":
      answer = input().lower()
      if answer == "yes":
         print("You talk to the stanger and they give gold. You win!")
      elif answer == "no":
         print("You ignore the stranger and they are offended and yor lose.")
      else:
         print("Not a valid option. You lose.")

   else:
      print("Not a valid option. You lose.")
else:
   print("Not a valid option. You lose.")