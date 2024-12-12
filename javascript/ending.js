'use strict';

const ending_modal = document.getElementById('ending_modal');
const ending_type_text = document.getElementById("end_type");
const ending_text = document.getElementById('ending_text')
const open_leaderboard = document.getElementById('open_leaderboard');
const close_leaderboard = document.getElementById('close_leaderboard');
const leaderboard_modal = document.getElementById('leaderboard_modal');
ending_modal.style.padding = 0;


async function leaderboard() {
    const response = await fetch('http://127.0.0.1:4000/sql/leaderboard');
    const data = await response.json();
    return data;
}

async function ending(end) {
    if (end == 'good_pill') {
        ending_type_text.textContent = 'You got the Good Pill ending!';
        ending_text.textContent = 'You have chosen the good pill, you live happy!';
    } else if (end == 'bad_pill') {
        ending_type_text.textContent = 'You got the Bad Pill ending!';
        ending_text.textContent = 'You have chosen the bad pill, you have "explosive diarrhea" and and your journey ends in jail';
    } else if (end == 'bad_shark') {
        ending_type_text.textContent = 'You got the Bad Shark ending!'
        ending_text.textContent = 'You got caught by the shark and are unable to pay him back!'
    } else if (end == 'good_shark') {
        ending_type_text.textContent = 'You got the Bad Shark ending!'
        ending_text.textContent = 'You got caught by the shark but you are able to pay him back!'
    } else {
        ending_type_text.textContent = 'You got the ??? ending!'
        ending_text.textContent = 'I dont know how you ended up here, but i guess enjoy your life then.';
    }
    
    

    const leaderboard_data = await leaderboard();
    for (let i = 0; i < leaderboard_data.length; i++) {
        const leaderboard_row = document.createElement('tr');
        const leaderboard_position = document.createElement('td');
        const leaderboard_name = document.createElement('td');
        const leaderboard_money = document.createElement('td');
        leaderboard_position.textContent = i + 1;
        leaderboard_name.textContent = leaderboard_data[i].player_name;
        leaderboard_money.textContent = leaderboard_data[i].money;
        leaderboard_row.appendChild(leaderboard_position);
        leaderboard_row.appendChild(leaderboard_name);
        leaderboard_row.appendChild(leaderboard_money);
        leaderboard_body.appendChild(leaderboard_row);
    }
    ending_modal.style.display = 'block';
}

open_leaderboard.addEventListener('click', () => {
    leaderboard_modal.style.display = 'block';
});
close_leaderboard.addEventListener('click', () => {
    leaderboard_modal.style.display = 'none';
});