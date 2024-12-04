'use strict';

const trivia_button = document.querySelector('#trivia_button');
const trivia_question = document.getElementById('trivia_question');
const option_1 = document.getElementById('option_1');
const option_2 = document.getElementById('option_2');
const option_3 = document.getElementById('option_3');
const option_4 = document.getElementById('option_4');
const trivia_result = document.getElementById('trivia_result');

let trivia_data = {};
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function display_question(id) {
    const question = trivia_data.results[id].question;
    const correct = trivia_data.results[id].correct_answer;
    const incorrect_list = trivia_data.results[id].incorrect_answers;
    const choices = shuffle([correct, ...incorrect_list]);

    trivia_question.textContent = question;
    option_1.textContent = choices[0];
    option_2.textContent = choices[1];
    option_3.textContent = choices[2];
    option_4.textContent = choices[3];
}

trivia_button.addEventListener('click', async (evt) => {
    const trivia_fetch = await fetch('http://127.0.0.1:4000/medium/trivia/questions');
    trivia_data = await trivia_fetch.json();
    if (trivia_data.response_code !== 0) {
        console.log('shit is fucked, try to retry');
    } else {
        console.log('Good job, shit works');
        display_question(0); // Display the first question
    }
});
function check_answer(selected_option) {
    const question_id = 0; // Assuming we are checking the first question
    const correct_answer = trivia_data.results[question_id].correct_answer;
    if (selected_option.textContent === correct_answer) {
        trivia_result.textContent = 'Correct!';
    } else {
        trivia_result.textContent = 'Incorrect!';
    }
}

option_1.addEventListener('click', () => check_answer(option_1));
option_2.addEventListener('click', () => check_answer(option_2));
option_3.addEventListener('click', () => check_answer(option_3));
option_4.addEventListener('click', () => check_answer(option_4));