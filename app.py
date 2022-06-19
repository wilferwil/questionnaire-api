from flask import Flask
from api.model import Seeder, db
from api.routes.questionnaire import questionnaire

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        Seeder().seed_all_tables()

    app.register_blueprint(questionnaire)

    return app

if __name__ == "__main__":
    app = create_app('config')
    app.run(host='0.0.0.0')