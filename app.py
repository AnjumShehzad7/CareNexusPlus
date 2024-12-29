from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.appointment_routes import appointment_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(appointment_bp, url_prefix='/api/appointments')


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
