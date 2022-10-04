# Code written 10.04.22

from getpass import getpass as input

print("EPIC rock, paper, scissors BATTLE")
print()
print("Select you move (R, P, or S)")
print()
player1 = input("Player 1: ").lower()
print()
player2 = input("Player 2: ").lower()
print()

if player1 == "r" and player2 == "r":
   print("The game is a tie! 🪨 🪨")
elif player1 == "r" and player2 == "p":
  print("Player 2's 📄 COVERS Player 1's 🪨")
  print("Player 2 wins!")
elif player1 == "r" and player2 == "s""":
  print("Player 1's 🪨 CRUSHES Player 2's ✂️")
  print("Player 1 wins!")

elif player1 == "p" and player2 == "r":
  print("Player 1's 📄 COVERS Player 2's 🪨")
  print("Player 1 wins!")
elif player1 == "p" and player2 == "p":
  print("The game is a tie! 📄📄")
elif player1 == "p" and player2 == "s":
  print("Player 2's ✂️ CUTS Player 1's 📄")
  print("Player 2 wins!")
  
elif player1 == "s" and player2 == "r":
  print("Player 2's 🪨 CRUSHES Player 1's ✂️")
  print("Player 2 wins!")
elif player1 == "s" and player2 == "p":
  print("Player 1's ✂️ CUTS Player 2's 📄")
  print("Player 1 wins!")
elif player1 == "s" and player2 == "s":
  print("The game is a tie! ✂️ ✂️")
else:
  print("Something went wrong")
