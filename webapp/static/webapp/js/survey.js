document.addEventListener('DOMContentLoaded', function() {
    loadQuestions();
});

function loadQuestions() {
    fetch('/poll/questions/')
        .then(res => res.json())
        .then(questions => {
            renderQuestions(questions);
        })
        .catch(err => {
            console.error('Ошибка загрузки вопросов:', err);
            document.getElementById('questions-container').innerHTML =
                '<p>Ошибка загрузки вопросов. Попробуйте позже.</p>';
        });
}

function renderQuestions(questions) {
    const container = document.getElementById('questions-container');
    container.innerHTML = '';

    questions.forEach(function(question) {
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';

        const questionText = document.createElement('div');
        questionText.className = 'question-text';
        questionText.textContent = question.text;
        questionDiv.appendChild(questionText);

        if (question.type === 'text') {
            const textarea = document.createElement('textarea');
            textarea.name = 'question_' + question.id;
            textarea.placeholder = 'Введите ваш ответ...';
            questionDiv.appendChild(textarea);
        } else {
            const choicesDiv = document.createElement('div');
            choicesDiv.className = 'choices';

            question.choices.forEach(function(choice) {
                const choiceItem = document.createElement('div');
                choiceItem.className = 'choice-item';

                const input = document.createElement('input');
                input.type = question.type === 'single' ? 'radio' : 'checkbox';
                input.name = 'question' + question.id;
                input.value = choice.id;
                input.id = 'choice' + choice.id;

                const label = document.createElement('label');
                label.htmlFor = 'choice_' + choice.id;
                label.textContent = choice.text;

                choiceItem.appendChild(input);
                choiceItem.appendChild(label);
                choicesDiv.appendChild(choiceItem);
            });
            questionDiv.appendChild(choicesDiv);
        }

        container.appendChild(questionDiv);
    });
}

document.getElementById('survey-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const answers = {};

    for (let [key, value] of formData.entries()) {
        if (key.startsWith('question_')) {
            const questionId = key.replace('question_', '');

            if (!answers[questionId]) {
                answers[questionId] = [];
            }

            if (isNaN(value)) {
                answers[questionId] = value;
            } else {
                answers[questionId].push(parseInt(value));
            }
        }
    }

    document.getElementById('survey-form').style.display = 'none';
    document.getElementById('loading').classList.add('active');

    fetch('/poll/questions/submit/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers)
    })
        .then(res => res.json())
        .then(data => {
            window.location.href = '/survey/result/' + data.response_id + '/';
        })
        .catch(err => {
            alert('Ошибка отправки: ' + err);
            document.getElementById('loading').classList.remove('active');
            document.getElementById('survey-form').style.display = 'block';
        });
});