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


    def set_question_answer(self, id, data):
        option_id = data.get('given_answer', None)
        question = self.repository.update_or_insert_question_answer(id, option_id)
        if question:
            options = self.repository.retrieve_question_options(id)
            return {
                "id": question.id,
                "question": question.question,
                "options": [dict(option) for option in options],
                "given_answer": question.given_answer
            }
        return question if question else None


    def show_score(self):
        questions = self.repository.retrieve_all_questions()

        score = self.calculate_score(questions)

        return score


    def calculate_score(self, questions):
        score = {
            "right_answers": 0,
            "wrong_answers": 0,
            "score": 0
        }

        for question in questions:
            if question.given_answer == question.right_answer:
                score['right_answers'] += 1

        score['wrong_answers'] = len(questions) - score['right_answers']
        score['score'] = "{:.0%}".format(score['right_answers']/len(questions))

        return score