#Example Flask App for a hexaganal tile game
#Logic is in this python file

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Keep track of the current player
current_player = 1
player1_pos = 0
player2_pos = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_tile')
def add_tile():
    global current_player
    color = 'green' if current_player == 1 else 'blue'  # Alternate between green and blue
    current_player = 2 if current_player == 1 else 1  # Switch to the other player
    return jsonify(color=color)

@app.route('/player-moved')
def player_moved():
    rollresult = int(request.args.get('result'))
    global current_player
    global player2_pos
    global player1_pos
    
    if current_player == 1:
        color = 'green'
        player1_pos += rollresult 
        current_player = 2 if current_player == 1 else 1
        return jsonify({"move_to": player1_pos, "player": 1})
    else:
        color ='blue'  # Alternate between green and blue
        player2_pos += rollresult
        current_player = 2 if current_player == 1 else 1
        return jsonify({"move_to": player2_pos, "player": 2})
      # Switch to the other player
    

if __name__ == "__main__":
    app.run(debug=True)
