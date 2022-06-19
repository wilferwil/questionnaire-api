import json
from flask import Blueprint, Response
from api.controllers.questionnaire_controller import QuestionnaireController

questionnaire = Blueprint('questionnaire', __name__)

@questionnaire.route("/", methods=['GET'])
def get_questionnaire():
    questionnaire = QuestionnaireController().get_questionnaire()
    return Response(
        response=json.dumps(questionnaire),
        status=200,
        headers={'Content-Type': 'application/json'})
