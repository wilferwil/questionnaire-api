class QuestionnaireBusiness:

    def __init__(self, questionnaire_repository):
        self.repository = questionnaire_repository
        

    def get_question(self, id):
        question = self.repository.retrieve_question_by_id(id)
        if question:
            options = self.repository.retrieve_question_options(id)
            return {
                "id": question.id,
                "question": question.question,
                "options": [dict(option) for option in options],
                "given_answer": question.given_answer
            }
        return question if question else None


    def get_questions(self):
        questions = []
        for question in self.repository.retrieve_all_questions():
            questions.append(
                {
                    "id": question.id,
                    "question": question.question,
                    "given_answer": question.given_answer
                }
            )
        return questions