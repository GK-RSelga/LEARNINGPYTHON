'''Activity 2 - Write a Python program that allows two players to play Rock, Paper, Scissors.
The program should prompt each player to enter their choice (rock, paper, or scissors)
and then determine the winner based on the game rules. Rock beats scissors, scissors
beats paper, and paper beats rock. The program should display the result and declare the
winner.'''
p1 = input("Enter player 1's choice (R/P/S): ")  
p2 = input("Enter player 2's choice (R/P/S): ")  
  
if p1.lower() == "r" and p2.lower() == "r":
      print("Draw!")
if p1.lower() == "p" and p2.lower() == "p":
      print("Draw!")
if p1.lower() == "s" and p2.lower() == "s":  
      print("Draw!")  
elif p1.lower() == "r" and p2.lower() == "s":  
      print("Player 1 Wins, Rock Wins!")
elif p1.lower() == "r" and p2.lower() == "p":
      print("Player 2 Wins, Paper Wins!")
elif p1.lower() == "p" and p2.lower() == "s":
      print("Player 2 Wins, Scissors Wins!")    
elif p2.lower() == "r" and p1.lower() == "s":  
      print("Player 2 Wins, Rock Wins!")
elif p2.lower() == "r" and p1.lower() == "p":
      print("Player 1 Wins, Paper Wins!")
elif p2.lower() == "p" and p1.lower() == "s":
      print("Player 1 Wins, Scissors Wins!") 
            