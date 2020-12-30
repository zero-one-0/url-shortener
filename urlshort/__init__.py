from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    app.secret_key = 'h3hrcjr4qcq4h5q54qdq45f232hk24u52f35uhf2'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app
