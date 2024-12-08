'use strict';


const pp_button_1 = document.getElementById('pp_button_1');
const pp_button_2 = document.getElementById('pp_button_2');
const pp_button_3 = document.getElementById('pp_button_3');

const pickpocket_result = document.getElementById('pickpocket_result');
const close_button = document.getElementById('close');
const pp_modal_pp = document.getElementById('pp-modal');


async function pp_init() {
    const victims = await fetch('http://127.0.0.1:4000/small/pp/victims_list');
    const viclims_json = await victims.json();
    console.log(viclims_json);
    pp_button_1.name = viclims_json[0].victim_1.name;
    pp_button_1.value = viclims_json[0].victim_1.difficulty;
    pp_button_1.textContent = viclims_json[0].victim_1.name;
    pp_button_2.name = viclims_json[0].victim_2.name;
    pp_button_2.value = viclims_json[0].victim_2.difficulty;
    pp_button_2.textContent = viclims_json[0].victim_2.name;
    pp_button_3.name = viclims_json[0].victim_3.name;
    pp_button_3.value = viclims_json[0].victim_3.difficulty;
    pp_button_3.textContent = viclims_json[0].victim_3.name;
    pp_button_1.style.display = 'block';
    pp_button_2.style.display = 'block';
    pp_button_3.style.display = 'block';
    pickpocket_result.innerText = '';
}

pp_button_1.addEventListener('click', async (evt) => {
    const victim = pp_button_1.name;
    const difficulty = pp_button_1.value;
    const result = await fetch(`http://127.0.0.1:4000/small/pp/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
    pp_button_1.style.display = 'none';
    update_stats();
});

pp_button_2.addEventListener('click', async (evt) => {
    const victim = pp_button_2.name;
    const difficulty = pp_button_2.value;
    const result = await fetch(`http://127.0.0.1:4000/small/pp/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
    pp_button_2.style.display = 'none';
    update_stats();
});

pp_button_3.addEventListener('click', async (evt) => {
    const victim = pp_button_3.name;
    const difficulty = pp_button_3.value;
    const result = await fetch(`http://127.0.0.1:4000/small/pp/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
    pp_button_3.style.display = 'none';
    update_stats();
});

close_button.addEventListener('click', async (evt) => {
    pp_modal_pp.style.display = 'none';
});