from flask import Flask
from routes.game import game_route
from routes.home import home_route
from routes.world_config import world_config_route
# from routes.config import config_route
# from routes.result import result_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(game_route, url_prefix='/game')
app.register_blueprint(world_config_route, url_prefix='/world-config')

if __name__ == "__main__":
    app.run(debug=True)