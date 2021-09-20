from models.player import *
from tests.game_test import *

class Game:

    def __init__(self, choice1, choice2):
        self.choice1 = choice1
        self.choice2 = choice2

    player1 = Player("Dave", "Rock") 
    player2 = Player("Linda", "Scissors")   
    player3 = Player("John", "Paper")

    players = [player1, player2, player3]
    
    def play_game(self):
         if self.choice1 == "rock" and self.choice2 == "scissors":
            return "Player 1 Wins by playing rock"
         elif self.choice1 == "rock" and self.choice2 == "paper":
            return "Player 2 Wins by playing paper"
         elif self.choice1 == "scissors" and self.choice2 == "paper":
            return "Player 1 Wins by playing scissors"
         elif self.choice1 == "paper" and self.choice2 == "rock":
            return "Player 1 Wins by playing paper"
         elif self.choice1 == "scissors" and self.choice2 == "rock":
            return "Player 2 Wins by playing rock"
         elif self.choice1 == "paper" and self.choice2 == "scissors":
            return "Player 2 Wins by playing scissors"
         else:
             return "Its a draw"
     


      
        
        









    
    









        
           