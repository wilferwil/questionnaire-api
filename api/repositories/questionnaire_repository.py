from api.model import db, Question, Answer

class QuestionnaireRepository:

    def retrieve_all_questions(self):
        return (db.session.query(
            Question.id,
            Question.question,
            Answer.given_answer
            )
            .join(Answer, Answer.question_id == Question.id, isouter=True)
            .all())