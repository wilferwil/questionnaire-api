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
            Question.right_answer,
            Answer.given_answer
            )
            .join(Answer, Answer.question_id == Question.id, isouter=True)
            .all())


    def update_or_insert_question_answer(self, question_id, option_id):
        question = self.retrieve_question_by_id(question_id)
        if not question.given_answer:
            db.session.add(
                Answer(question_id=question_id, given_answer=option_id)
            )
        else:
            (db.session.query(Answer)
            .filter(Answer.question_id == question_id)
            .update({Answer.given_answer: option_id}))
        db.session.commit()
        return self.retrieve_question_by_id(question_id)