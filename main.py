from flask import Flask
from routes.game import game_route
from routes.board import board_route
from routes.home import home_route
from routes.config import config_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(config_route, url_prefix='/config')
app.register_blueprint(game_route, url_prefix='/game')
app.register_blueprint(board_route, url_prefix='/board')

app.run(debug=True)