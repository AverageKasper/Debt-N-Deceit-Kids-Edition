'use strict';


const button_1 = document.getElementById('button_1');
const button_2 = document.getElementById('button_2');
const button_3 = document.getElementById('button_3');

const pickpocket_result = document.getElementById('pickpocket_result');

async function getData(url) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return data;
}


const victims = getData('http://127.0.0.1:4000/pickpocket/victims_list').then(async data => {
    console.log(data);
    if (Array.isArray(data) && data.length > 0 && data[0].victim_1 && data[0].victim_2 && data[0].victim_3) {
        button_1.innerHTML = `Victim 1:${data[0].victim_1.name}<br>Difficulty:${data[0].victim_1.difficulty}`;
        button_1.name = data[0].victim_1.name;
        button_1.value = data[0].victim_1.difficulty;

        button_2.innerHTML = `Victim 2:${data[0].victim_2.name}<br>Difficulty:${data[0].victim_2.difficulty}`;
        button_2.name = data[0].victim_2.name;
        button_2.value = data[0].victim_2.difficulty;

        button_3.innerHTML = `Victim 3:${data[0].victim_3.name}<br>Difficulty:${data[0].victim_3.difficulty}`;
        button_3.name = data[0].victim_3.name;
        button_3.value = data[0].victim_3.difficulty;
    } else {
        console.error('Invalid data structure:', data);
    }
});

button_1.addEventListener('click', async (evt) => {
    const victim = button_1.name;
    const difficulty = button_1.value;
    const result = await fetch(`http://127.0.0.1:4000/pickpocket/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
});

button_2.addEventListener('click', async (evt) => {
    const victim = button_2.name;
    const difficulty = button_2.value;
    const result = await fetch(`http://127.0.0.1:4000/pickpocket/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
});

button_3.addEventListener('click', async (evt) => {
    const victim = button_3.name;
    const difficulty = button_3.value;
    const result = await fetch(`http://127.0.0.1:4000/pickpocket/${victim}/${difficulty}`)
    const result_json = await result.json();
    console.log(result_json);
    pickpocket_result.innerText = result_json.message;
});