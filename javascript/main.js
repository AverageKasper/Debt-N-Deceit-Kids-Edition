'use strict';

const start_modal = document.getElementById('start-modal');
const kbButtons = document.querySelectorAll('div.difficulty-buttons button');
const player_name_input = document.getElementById('player-name');
const error_p = document.getElementById('error');
const button_1 = document.getElementById('button-1');
const button_2 = document.getElementById('button-2')
const pp_modal = document.getElementById('pp-modal');
const stat_block = document.getElementById('stat-block')
const main_buttons_div = document.getElementById('main-buttons');

// Map init
let map_point;
let map = L.map('map', {
    minZoom: 3.5,
    maxZoom: 3.5
});

let cartodbAttribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attribution">CARTO</a>';

let positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: cartodbAttribution
}).addTo(map);


async function update_stats() {
    const player_name = player_name_input.value;
    let player_stats = await fetch(`http://127.0.0.1:4000/sql/player_stats/${player_name}`);
    let player_data = await player_stats.json();
    console.log(player_data);
    stat_block.innerHTML = `<p>Name: ${player_name}<br>Money: ${player_data.money}<br>Debt: ${10000 - player_data.money}<br>
    Shark: ${player_data.shark} steps behind<br>Inventory: ${player_data.inventory}`

}

async function airport_selection() {
    let next_airports = {}
    for (let i = 1; i < 4; i++) {
        let type = 'heliport'
        if (i == 1) {
            type = 'small_airport'
        } else if (i == 2) {
            type = 'medium_airport'
        } else {
            type = 'large_airport'
        }
        let airport = await fetch(`http://127.0.0.1:4000/sql/fly/${type}`)
        let airport_data = await airport.json()
        map_point = L.marker([airport_data.latitude_deg, airport_data.longitude_deg]).addTo(map);
        map_point.bindPopup(`<b>${airport_data.name}</b>`)
        console.log(airport_data)
        next_airports['airport_' + i] = airport_data
        console.log(next_airports)
    }
    return next_airports
}

async function button_to_airport() {
    main_buttons_div.innerHTML = '';
    const airport_list = await airport_selection()
    console.log(airport_list)
    const airport_1_button = document.createElement('button')
    airport_1_button.textContent = airport_list.airport_1.name
    airport_1_button.className = 'button'
    airport_1_button.addEventListener('click', async (evt) => {
        console.log('1 clicked')
    })
    const airport_2_button = document.createElement('button')
    airport_2_button.textContent = airport_list.airport_2.name
    airport_2_button.className = 'button'
    airport_2_button.addEventListener('click', async (evt) => {
        console.log('2 clicked')
    })
    const airport_3_button = document.createElement('button')
    airport_3_button.textContent = airport_list.airport_3.name
    airport_3_button.className = 'button'
    airport_3_button.addEventListener('click', async (evt) => {
        console.log('3 clicked')
    })
    main_buttons_div.appendChild(airport_1_button)
    main_buttons_div.appendChild(airport_2_button)
    main_buttons_div.appendChild(airport_3_button)
}

function clear_map() {
    map.eachLayer((layer) => {
        if (layer instanceof L.Marker) {
           layer.remove();
        }
      });
}

kbButtons.forEach((button) => {
    button.addEventListener('click', async function () {
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
            update_stats();
            button_to_airport();
        }
    });
});


map.setView([57.7089, 11.9746], 0);
map.dragging.disable();
map.touchZoom.disable();
map.doubleClickZoom.disable();
map.scrollWheelZoom.disable();
map.boxZoom.disable();
map.keyboard.disable();
if (map.tap) map.tap.disable();

button_1.addEventListener('click', async (evt) => {
    const result = await fetch('http://127.0.0.1:4000/small/pp/victims_list')
    const data = await result.json()
    console.log(data);

    pp_button_1.style.display = '';
    pp_button_1.innerHTML = `Victim 1:${data[0].victim_1.name}<br>Difficulty:${data[0].victim_1.difficulty}`;
    pp_button_1.name = data[0].victim_1.name;
    pp_button_1.value = data[0].victim_1.difficulty;

    pp_button_2.style.display = '';
    pp_button_2.innerHTML = `Victim 2:${data[0].victim_2.name}<br>Difficulty:${data[0].victim_2.difficulty}`;
    pp_button_2.name = data[0].victim_2.name;
    pp_button_2.value = data[0].victim_2.difficulty;

    pp_button_3.style.display = '';
    pp_button_3.innerHTML = `Victim 3:${data[0].victim_3.name}<br>Difficulty:${data[0].victim_3.difficulty}`;
    pp_button_3.name = data[0].victim_3.name;
    pp_button_3.value = data[0].victim_3.difficulty;




    pp_modal.style.display = 'block';
});

button_2.addEventListener('click', async (evt) => {
    clear_map()
    airport_selection();
});