import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_portfolio_project'
    
    # This automatically creates a file named 'site.db' to store your users
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Email Config (Keep this if you want email to work)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')