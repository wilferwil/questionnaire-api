import json

def test_get_questions_list_status_200(client):
    response = client.get('/questions')

    assert response.status_code == 200

def test_get_questions_list(client):
    response = client.get('/questions')

    expected_return = [
        {
            "id": 1,
            "question": "O que está escrito na bandeira do Brasil?",
            "given_answer": None
        },
        {
            "id": 2,
            "question": "Quanto é o produto da multiplicação de 8 por 8?",
            "given_answer": None
        },
        {
            "id": 3,
            "question": "Qual é a capital da Inglaterra?",
            "given_answer": 8
        }
    ]

    assert response.text == json.dumps(expected_return)


def test_get_question_details_status_200(client):
    response = client.get('/questions/1')

    assert response.status_code == 200


def test_get_question_details(client):
    response = client.get('/questions/1')

    expected_return = {
        "id": 1,
        "question": "O que está escrito na bandeira do Brasil?",
        "options": [
            {"id": 1, "description": "Lei e Ordem"},
            {"id": 2, "description": "Progresso e Caos"},
            {"id": 3, "description": "Ordem e Progresso"},
        ],
        "given_answer": None
    }

    assert response.text == json.dumps(expected_return)


def test_post_question_answer_status_200(client):
    payload = {'given_answer': 3}
    response = client.post('/questions/1/answer', json=payload)
    
    assert response.status_code == 200


def test_post_question_answer(client):
    payload = {'given_answer': 3}
    response = client.post('/questions/1/answer', json=payload)

    expected_return = {
        "id": 1,
        "question": "O que está escrito na bandeira do Brasil?",
        "options": [
            {"id": 1, "description": "Lei e Ordem"},
            {"id": 2, "description": "Progresso e Caos"},
            {"id": 3, "description": "Ordem e Progresso"},
        ],
        "given_answer": 3
    }

    assert response.text == json.dumps(expected_return)


def test_get_score_status_200(client):
    response = client.get('/score')
    
    assert response.status_code == 200


def test_get_score(client):
    response = client.get('/score')
    
    expected_return = {
        "right_answers": 2,
        "wrong_answers": 1,
        "score": "67%"
        }

    assert response.text == json.dumps(expected_return)
