from flask import Flask
from routes.game import game_route
from routes.home import home_route
from routes.config import config_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(config_route, url_prefix='/config')
app.register_blueprint(game_route, url_prefix='/game')

if __name__ == "__main__":
    app.run(debug=True)