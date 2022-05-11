import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from .routes import route
    
	# blueprint for auth routes in our app
    app.register_blueprint(route.route)
    
    return app


app = create_app()
