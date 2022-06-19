from api.repositories.questionnaire_repository import QuestionnaireRepository

class QuestionnaireController:

    def get_questions(self):
        questions = []
        for question in QuestionnaireRepository().retrieve_all_questions():
            questions.append(
                {
                    "id": question.id,
                    "question": question.question,
                    "given_answer": question.given_answer
                }
            )
        return questions