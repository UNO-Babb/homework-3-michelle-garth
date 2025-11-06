#Example Flask App for a hexaganal tile game
#Logic is in this python file

from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Keep track of the current player
current_player = 1
player1_pos = 0
player2_pos = 0

def saveTurn(turndata):
    with open("eventfile.csv", "a+") as eventfile:
        turn = {
            "positions": {
                "Player1": turndata['positions']['1'],
                "Player2": turndata['positions']['2']
            },
            "scores": {
                "Player1": turndata['scores']['1'],
                "Player2": turndata['scores']['2']
            },
            "turn": turndata['turn']
        }
        eventfile.write(str(turndata['positions']['1'])+","+str(turndata['positions']['2'])+","+str(turndata['scores']['1'])+","+str(turndata['scores']['2'])+","+str(turndata['turn'])+"\n")
        
        
            

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_tile')
def add_tile():
    global current_player
    color = 'green' if current_player == 1 else 'blue'  # Alternate between green and blue
    current_player = 2 if current_player == 1 else 1  # Switch to the other player
    return jsonify(color=color)

@app.route('/update-events', methods=["POST"])
def player_moved():
    if request.method == "POST":
        #print(request.get_json())
        saveTurn(request.get_json())
    return "success"

if __name__ == "__main__":
    with open("eventfile.csv", "w+") as eventfile:
        eventfile.write("Player1Position,Player2Position,Player1Score,Player2Score,Turn\n")
    app.run(debug=True)
