from flask import render_template
from app import app
from models.game import *
from models.player import Player

@app.route('/rps')
def index():
    return render_template("index.html", title="Rock Paper Scissors")

@app.route("/rps/<choice1>/<choice2>")
def play(choice1, choice2):
    game = Game(choice1, choice2)
    result = game.play_game()
    return render_template("rock_paper_scissors.html", result=result)


    






    

  


