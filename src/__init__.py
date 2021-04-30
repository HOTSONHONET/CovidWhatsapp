from flask import Flask


def init_app():
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from . import routes
        print(f"[INFO] Initializing App...")
        
        return app