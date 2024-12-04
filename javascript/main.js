'use strict';

const start_modal = document.getElementById('start-modal');
const kbButtons = document.querySelectorAll('div.difficulty-buttons button');
const player_name_input = document.getElementById('player-name');
const error_p = document.getElementById('error');



kbButtons.forEach((button) => {
    button.addEventListener('click',async function() {
        const difficulty = button.id;
        const player_name = player_name_input.value;
        const result = await fetch(`http://127.0.0.1:4000/sql/check_name/${player_name}`);
        const name_taken = await result.json();
        console.log(name_taken);
        if (name_taken.exists == true) {
            error_p.textContent = ('Name already taken, please choose another name');
            return; 
        } else {
            error_p.textContent = '';
            const start_game = await fetch(`http://127.0.0.1:4000/start/start_game/${player_name}/${difficulty}`);
            const start_game_json = await start_game.json();
            console.log(start_game_json);
            start_modal.style.display = 'none';
        }
    });
});

var map = L.map('map', {
    minZoom: 3.5,
    maxZoom: 3.5
});

var cartodbAttribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attribution">CARTO</a>';

var positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: cartodbAttribution
}).addTo(map);

map.setView([57.7089, 11.9746], 0);
map.dragging.disable();
map.touchZoom.disable();
map.doubleClickZoom.disable();
map.scrollWheelZoom.disable();
map.boxZoom.disable();
map.keyboard.disable();
if (map.tap) map.tap.disable();