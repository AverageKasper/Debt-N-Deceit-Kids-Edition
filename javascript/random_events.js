'use strict';

const event_modal = document.getElementById('random-modal');
const event_text = document.getElementById('event_text');
const event_reward = document.getElementById('event_reward');
const close_random = document.getElementById('close_random');
const event_buttons = document.getElementById('random_buttons');
const random_image = document.getElementById('random_image');


async function random_event() {
    close_random.style.display = 'block';
    let random_chance = Math.floor(Math.random() * 5) + 1;
    if (random_chance !== 5) {
        return {'event': false}
    } else {
        const event_select = await fetch('http://127.0.0.1:4000/random/event');
        const event_json = await event_select.json();
        if (event_json.event == false) {
            return {'event': false}
        } else if (event_json.event_type == 'morpheus') {
            close_random.style.display = 'none';
            morpheus(event_json);
        }
        
        event_modal.style.display = 'block';
        event_text.innerText = event_json.text;
    }
}

close_random.addEventListener('click', () => {
    event_modal.style.display = 'none';
});



async function morpheus(json) {
    event_modal.style.display = 'block';
    close_random.style.display = 'none';
    event_text.innerText = json.text;
    const agree = document.createElement('button');
    const disagree = document.createElement('button');
    agree.textContent = 'Yea baby!';
    disagree.textContent = 'Nope';
    agree.className = 'button';
    disagree.className = 'button';
    event_modal.style.display = 'block';
    event_text.innerText = json.text;
    event_buttons.appendChild(agree);
    event_buttons.appendChild(disagree);
    agree.addEventListener('click', async (evt) => {
        await pill_taking();
    });
    disagree.addEventListener('click', async (evt) => {
        event_modal.style.display = 'none';
    });

}

async function pill_taking() {
    const result = await fetch('http://127.0.0.1:4000/random/morpheus_pill');
    const result_json = await result.json();
    random_image.style.display = 'flex';
    random_image.src = '../html/image/morpheus.jpg';
    event_text.innerText = 'Witch pill do you want to take?';
    const red_pill = document.createElement('button');
    const blue_pill = document.createElement('button');
    red_pill.textContent = 'Red pill';
    blue_pill.textContent = 'Blue pill';
    red_pill.className = 'button';
    blue_pill.className = 'button';
    close_random.style.display = 'none';
    event_buttons.removeChild(event_buttons.lastChild);
    event_buttons.removeChild(event_buttons.lastChild);
    event_buttons.appendChild(red_pill);
    event_buttons.appendChild(blue_pill);
    red_pill.addEventListener('click', async (evt) => {
        if (result_json.bad_pill == 'red') {
            ending('bad_pill');
        } else {
            ending('good_pill');
        }
    });
    blue_pill.addEventListener('click', async (evt) => {
        if (result_json.bad_pill == 'blue') {
            ending('bad_pill');
        } else {
            ending('good_pill');
        }
    });
}

async function shark_gets_hit(name_player) {
    event_text.innerText = 'You hit the shark with a magical object, he is transported back 3 airports!'
    shark_moving(name_player, -3)
} 