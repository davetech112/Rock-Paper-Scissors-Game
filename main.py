import random
while True:

  choices = ["r", "p", "s"]
  cpu = random.choice(choices)
       
  player = input("R=Rock, P=Paper or S=Scissors?: ").lower()
  if player not in choices:
    print("Invalid selection, try again...")
    continue
  if cpu == player:
    print("You drew with cpu try again")
    continue
  elif player == "r":
    if cpu == "p":
      print("cpu(",cpu, ") : player(",player,")")
      print("You lose HAHAHA!!!")
      
    if cpu == "s":
      print("cpu(",cpu, ") : player(",player,")")
      print("You win!")
      
  elif player == "s":
    if cpu == "r":
      print("cpu(",cpu, ") : player(",player,")")
      print("You lose HAHAHA!!!")
      
    if cpu == "p":
      print("cpu(",cpu, ") : player(",player,")")
      print("You win!")
      
  elif player == "p":
    if cpu == "s":
      print("cpu(",cpu, ") : player(",player,")")
      print("You lose HAHAHA!!!")
      
    if cpu == "r":
      print("cpu(",cpu, ") : player(",player,")")
      print("You win!")
      

  play_again = input("Play again? (y/n) y=yes n=no): ").lower()
  if play_again != "y":
    break

print("Bye!!! Come Again!!!")

 