'use strict';

const trivia_modal = document.getElementById('trivia-modal');
const trivia_question = document.getElementById('trivia-question');
const trivia_intro = document.querySelector('.trivia-intro');
const trivia_category = document.querySelectorAll('#trivia-category');
const trivia_question_div = document.querySelector('.trivia-questions');
const loading = document.getElementById('loading');
const close_trivia = document.getElementById('close-trivia');
const trivia_end_result_text = document.getElementById('trivia-end-result-text');
const trivia_result_modal = document.getElementById('trivia-result');
const trivia_end_result_modal = document.getElementById('trivia-end-result-modal');
const trivia_result_text = document.getElementById('trivia-result-text');
const trivia_continue = document.getElementById('trivia-continue');


const rewards = { '0': 'nothing', '1': '100€', '2': '300€', '3': '700', '4': '1200€ and 500 Carbon' }

async function get_trivia_category() {
  trivia_modal.style.display = 'block';
  trivia_intro.style.display = 'block';
  trivia_question_div.style.display = 'none';
  trivia_result_modal.style.display = 'none';
  loading.innerText = '';
  trivia_question.innerHTML = '';
  [...trivia_category].forEach(item => {
    item.addEventListener('click', async function () {
      let questions = await trivia_fetch(item.name);
      if (questions) {
        console.log(questions);
        await start_trivia(questions);
      }
    });
  });
}

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
async function start_trivia(questions) {
  let currentQuestionIndex = 0;
  let correctAnswers = 0;
  currentQuestionIndex == 0;
  correctAnswers == 0;
  console.log(questions.length);
  trivia_question_div.style.display = 'block';


  async function askQuestion() {
    if (currentQuestionIndex >= 4) {
      endTrivia(correctAnswers);
      return;
    }
    trivia_result_modal.style.display = 'none';
    console.log(currentQuestionIndex);
    console.log(questions);

    const questionData = questions[`question_${currentQuestionIndex + 1}`];
    console.log(questionData);
    console.log(questions);
    trivia_question.innerHTML = decodeHTMLEntities(questionData.question);

    const answers = shuffle([
      questionData.correct_answer,
      ...questionData.incorrect_answers
    ]).map(decodeHTMLEntities);

    const buttons = answers.map(answer => {
      const button = document.createElement('button');
      button.className = 'button';
      button.innerHTML = answer;
      const handleClick = () => {
        if (answer === questionData.correct_answer) {
          trivia_result_text.innerText = `Correct!`;
          trivia_result_modal.style.display = 'flex';
          correctAnswers++;
        } else {
          trivia_result_text.innerHTML = `Incorrect! The correct answer was: ${questionData.correct_answer}`;
          trivia_result_modal.style.display = 'flex';
        }
        currentQuestionIndex++;
        button.removeEventListener('click', handleClick);
      };
      button.addEventListener('click', handleClick);
      return button;
    });

    trivia_question_div.innerHTML = '';
    buttons.forEach(button => trivia_question_div.appendChild(button));
  }

  trivia_continue.onclick = () => {
    trivia_result_modal.style.display = 'none';
    askQuestion();
  };

  askQuestion();
}

function decodeHTMLEntities(text) {
  const textArea = document.createElement('textarea');
  textArea.innerHTML = text;
  return textArea.value;
}

async function endTrivia(correct) {
  trivia_end_result_modal.style.display = 'block';
  trivia_end_result_text.innerText = `You answered ${correct} questions correctly! You won ${rewards[correct]}`;
  trivia_modal.style.display = 'none';
  trivia_intro.style.display = 'none';
  trivia_question_div.style.display = 'none';
  trivia_result_modal.style.display = 'none';
  loading.innerText = '';
  trivia_question.innerHTML = '';

  await fetch(`http://127.0.0.1:4000/medium/trivia/reward/${correct}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ correct })
  });
  update_stats();


}

async function trivia_fetch(category) {
  loading.innerText = 'Loading...';
  const response = await fetch(`http://127.0.0.1:4000/medium/trivia/questions/${category}`);
  const data = await response.json();
  if (data.error == 404) {
    loading.innerText = 'Failed to load questions. Try again in a moment.';
    return;
  }
  trivia_intro.style.display = 'none';
  return data;
}

close_trivia.addEventListener('click', function () {
  trivia_end_result_modal.style.display = 'none';
  trivia_modal.style.display = 'none';
});

