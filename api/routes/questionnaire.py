import json
from flask import Blueprint, Response, request
from api.business.questionnaire_business import QuestionnaireBusiness
from api.repositories.questionnaire_repository import QuestionnaireRepository


questionnaire = Blueprint('questionnaire', __name__)


@questionnaire.route("/questions/<id>", methods=['GET'])
def get_question(id):
    question = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).get_question(int(id))
    return Response(
        response=json.dumps(question) if question else '',
        status=200 if question else 404,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/questions", methods=['GET'])
def get_questions():
    questions = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).get_questions()
    return Response(
        response=json.dumps(questions) if questions else '',
        status=200 if questions else 404,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/questions/<id>/answer", methods=['POST'])
def set_answet(id):
    data = request.get_json()
    answer = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).set_question_answer(id, data)
    return Response(
        response=json.dumps(answer) if answer else '',
        status=200 if answer else 404,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/score", methods=['GET'])
def show_score():
    score = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).show_score()
    return Response(
        response=json.dumps(score),
        status=200,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/", methods=['GET'])
def root():
    return Response(
        response='',
        status=200,
        headers={'Content-Type': 'application/json'})
