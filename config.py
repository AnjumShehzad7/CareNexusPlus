import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Flask app secret key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')

    # Database connection string
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:admin@localhost:5432/carenexus'  # Default fallback
    )

    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration for Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'default-email@example.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'default-email-password')
