import json
from flask import Blueprint, Response
from api.controllers.questionnaire_controller import QuestionnaireController


questionnaire = Blueprint('questionnaire', __name__)


@questionnaire.route("/questions", methods=['GET'])
def get_questions():
    questionnaire = QuestionnaireController().get_questions()
    return Response(
        response=json.dumps(questionnaire),
        status=200,
        headers={'Content-Type': 'application/json'})


@questionnaire.route("/", methods=['GET'])
def root():
    return Response(
        response='',
        status=200,
        headers={'Content-Type': 'application/json'})
