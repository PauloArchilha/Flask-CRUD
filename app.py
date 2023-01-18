from flask import Flask
from config import DevelopmentConfig
from models.user import db
from flask_migrate import Migrate
from routes.user_bp import user_bp


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix="/usuarios")

if __name__ == "__main__":
    app.run(debug=DevelopmentConfig.DEBUG,
            host=DevelopmentConfig.IP_HOST, port=DevelopmentConfig.PORT_HOST)
