import os

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))
