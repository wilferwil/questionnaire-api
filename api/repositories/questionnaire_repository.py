from api.model import db, Question, Answer, Option

class QuestionnaireRepository:

    def retrieve_question_by_id(self, id):
        return (db.session.query(
            Question.id,
            Question.question,
            Answer.given_answer
            )
            .join(Answer, Answer.question_id == Question.id, isouter=True)
            .join(Option, Option.question_id == Question.id, isouter=True)
            .filter(Question.id == id)
            .first())


    def retrieve_question_options(self, question_id):
        return (db.session.query(
            Option.id,
            Option.description
            )
            .filter(Option.question_id == question_id)
            .all())


    def retrieve_all_questions(self):
        return (db.session.query(
            Question.id,
            Question.question,
            Answer.given_answer
            )
            .join(Answer, Answer.question_id == Question.id, isouter=True)
            .all())