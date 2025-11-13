# run.py
"""
Application Entry Point for Move Right

This file serves as the starting point for the Flask application.
When you execute 'python run.py', this file:
1. Imports the app factory
2. Creates an app instance
3. Starts the development server
"""
from app import create_app, socketio

# create flask app instance
app = create_app()

if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    from werkzeug.middleware.dispatcher import DispatcherMiddleware

    # Use eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
