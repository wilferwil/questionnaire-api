# Project: Questionnaire API

Pre-requirements:

* Docker

After you certify that you have Docker installed on your operating system, start the application running this simple command:
<pre><code>docker-compose up</code></pre>

Run unit tests inside Docker container using the following line:

<pre><code>docker exec -ti questionnaire-api_app_1 python -m pytest</code></pre>

This way, all the unit tests will be run on the original environment.

# API Usage / Endpoints:

### Base URI
http://localhost:8080/

Base URI will be up on 8080 port of your localhost, through automatic container setup.


## End-point: Get Score
### Method: GET
>```
>http://localhost:8080/score
>```
### Headers

|Content-Type|application/json|
|Accept|application/json|


### Response: 200
```json
{
    "right_answers": 1,
    "wrong_answers": 2,
    "score": "33%"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Questions
### Method: GET
>```
>http://localhost:8080/questions
>```
### Headers

|Content-Type|application/json|
|Accept|application/json|


### Response: 200
```json
[
    {
        "id": 1,
        "question": "O que está escrito na bandeira do Brasil?",
        "given_answer": 3
    },
    {
        "id": 2,
        "question": "Quanto é o produto da multiplicação de 8 por 8?",
        "given_answer": null
    },
    {
        "id": 3,
        "question": "Qual é a capital da Inglaterra?",
        "given_answer": 2
    }
]
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Get Question
### Method: GET
>```
>http://localhost:8080/questions/1
>```
### Headers

|Content-Type|application/json|
|Accept|application/json|


### Response: 200
```json
{
    "id": 1,
    "question": "O que está escrito na bandeira do Brasil?",
    "options": [
        {
            "id": 1,
            "description": "Lei e Ordem"
        },
        {
            "id": 2,
            "description": "Progresso e Caos"
        },
        {
            "id": 3,
            "description": "Ordem e Progresso"
        }
    ],
    "given_answer": 3
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Post Answer
### Method: POST
>```
>http://localhost:8080/questions/1/answer
>```
### Headers

|Content-Type|application/json|
|Accept|application/json|


### Body (**raw**)

```json
{
    "given_answer": 3
}
```

### Response: 200
```json
{
    "id": 1,
    "question": "O que está escrito na bandeira do Brasil?",
    "options": [
        {
            "id": 1,
            "description": "Lei e Ordem"
        },
        {
            "id": 2,
            "description": "Progresso e Caos"
        },
        {
            "id": 3,
            "description": "Ordem e Progresso"
        }
    ],
    "given_answer": 3
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________