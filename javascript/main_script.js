'use strict';


const button_1 = document.getElementById('button_1');
const button_2 = document.getElementById('button_2');
const button_3 = document.getElementById('button_3');

async function getData(url) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return data;
} 
 
const victims = getData('http://127.0.0.1:4000/pickpocket_victims').then(data => {
    console.log(data);
    button_1.innerHTML = `Victim 1:${data[0].victim_1.name}<br>Difficulty:${data[0].victim_1.difficulty}`;
    button_2.innerHTML = `Victim 2:${data[0].victim_2.name}<br>Difficulty:${data[0].victim_2.difficulty}`;
    button_3.innerHTML = `Victim 3:${data[0].victim_3.name}<br>Difficulty:${data[0].victim_3.difficulty}`;
});;

button_1.addEventListener('click', () => {
    console.log('Victim 1 clicked');
});