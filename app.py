from flask import Flask
from api.routes.questionnaire import questionnaire

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(questionnaire)

    return app

if __name__ == "__main__":
    app = create_app('config')
    app.run(host='0.0.0.0')