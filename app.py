from flask import Flask
from routes.home import home_route
from routes.board import board_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(board_route, url_prefix='/board')

app.run(debug=True)