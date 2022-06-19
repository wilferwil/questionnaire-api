from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Seeder():
    __abstract__ = True

    @classmethod
    def seed_all_tables(cls):
        Question().seed_questions()
        Answer().seed_answers()
        Option().seed_options()

class Question(Base):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String())
    right_answer = db.Column(db.SmallInteger())

    def seed_questions(self):
        questions = [
            {
                "question": "O que está escrito na bandeira do Brasil?",
                "right_answer": 3
            },
            {
                "question": "Quanto é o produto da multiplicação de 8 por 8?",
                "right_answer": 1
            },
            {
                "question": "Qual é a capital da Inglaterra?",
                "right_answer": 1
            }
        ]
        questions = [Question(**question) for question in questions]
        db.session.bulk_save_objects(questions)
        db.session.commit()

class Answer(Base):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer())
    given_answer = db.Column(db.SmallInteger())

    def seed_answers(self):
        answers = [
            {
                "question_id": 3,
                "given_answer": 2
            }
        ]
        answers = [Answer(**answer) for answer in answers]
        db.session.bulk_save_objects(answers)
        db.session.commit()

class Option(Base):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String())
    question_id = db.Column(db.Integer())

    def seed_options(self):
        options = [
            {"question_id": 1, "description": "Lei e Ordem"},
            {"question_id": 1, "description": "Progresso e Caos"},
            {"question_id": 1, "description": "Ordem e Progresso"}
        ]
        options = [Option(**option) for option in options]
        db.session.bulk_save_objects(options)
        db.session.commit()
