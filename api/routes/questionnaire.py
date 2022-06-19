import json
from flask import Blueprint, Response
from api.business.questionnaire_business import QuestionnaireBusiness
from api.repositories.questionnaire_repository import QuestionnaireRepository


questionnaire = Blueprint('questionnaire', __name__)


@questionnaire.route("/questions/<id>", methods=['GET'])
def get_question(id):
    questionnaire = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).get_question(int(id))
    return Response(
        response=json.dumps(questionnaire) if questionnaire else '',
        status=200 if questionnaire else 404,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/questions", methods=['GET'])
def get_questions():
    questionnaire = QuestionnaireBusiness(
        QuestionnaireRepository()
        ).get_questions()
    return Response(
        response=json.dumps(questionnaire) if questionnaire else '',
        status=200 if questionnaire else 404,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/", methods=['GET'])
def root():
    return Response(
        response='',
        status=200,
        headers={'Content-Type': 'application/json'})
