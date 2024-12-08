'use strict';

const close_diving = document.getElementById('close_diving');
const diving_text = document.getElementById('diving_text');
const diving_reward = document.getElementById('diving_reward');

async function get_diving() {
    let response = await fetch('http://127.0.0.1:4000/small/diving');
    let data = await response.json();
    console.log(data);
    diving_text.innerText = data.text;
    diving_reward.innerText = 'You got ' + data.reward;
    update_stats();
}

close_diving.addEventListener('click', async (evt) => {
    diving_modal.style.display = 'none';
});