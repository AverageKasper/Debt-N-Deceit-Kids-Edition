'use strict';

const start_modal = document.getElementById('start-modal');
const kbButtons = document.querySelectorAll('div.difficulty-buttons button');
const player_name_input = document.getElementById('player-name');
const error_p = document.getElementById('error');
const button_1 = document.getElementById('button-1');
const button_2 = document.getElementById('button-2')

const stat_block = document.getElementById('stat-block')
const main_buttons_div = document.getElementById('main-buttons');

// Modals
const pp_modal = document.getElementById('pp-modal');
const diving_modal = document.getElementById('diving-modal');
const gambling_modal = document.getElementById('gambling-modal');
// Map init
let map_point;
let map = L.map('map', {
    minZoom: 3.5,
    maxZoom: 3.5,
    zoomControl: false
});

let cartodbAttribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/attribution">CARTO</a>';

let positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
    attribution: cartodbAttribution
}).addTo(map);


async function update_stats() {
    const player_name = player_name_input.value;
    let player_stats = await fetch(`http://127.0.0.1:4000/sql/player_stats/${player_name}`);
    let player_data = await player_stats.json();
    stat_block.innerHTML = `<p>Name: ${player_name}<br>Money: ${player_data.money}<br>Debt: ${10000 - player_data.money}<br>
    Carbon: ${player_data.carbon}<br>Shark: ${player_data.shark} steps behind<br>Inventory: ${player_data.inventory}`
    return player_data
}

async function use_carbon(name_of_player, amount) {
    await fetch(`http://127.0.0.1:4000/sql/carbon/${name_of_player}/${amount}`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json' }
    }
    ).then(response => response.json())
    .catch(error => {
        console.error('Error fetching balance:', error);
    });
}
// fix this shit i have no idea why this works
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
        try {
            let airport = await fetch(`http://127.0.0.1:4000/sql/fly/${type}`)
            if (!airport.ok) {
                throw new Error(`Failed to fetch ${type}: ${airport.statusText}`);
            }
            let airport_data = await airport.json()
            if (airport_data.latitude_deg && airport_data.longitude_deg) {
                let latitude = airport_data.latitude_deg;
                let longitude = airport_data.longitude_deg;
                map_point = L.marker([latitude, longitude]).addTo(map);
                map_point.bindPopup(`<b>${airport_data.name}</b>`);
                next_airports['airport_' + i] = airport_data;
            } else {
                console.error(`Airport data for ${type} is missing latitude or longitude`);
            }
        } catch (error) {
            console.error(`Error fetching ${type}:`, error);
        }
    }
    return next_airports
}

async function small_tasks() {
    main_buttons_div.innerHTML = '';
    const small_button_1 = document.createElement('button')
    small_button_1.textContent = 'Pickpocketing'
    small_button_1.className = 'button'
    small_button_1.addEventListener('click', async (evt) => {
        await pp_init();
        await shark_moving(player_name_input.value, -1);
        await update_stats();
        pp_modal.style.display = 'block';
    });

    const small_button_2 = document.createElement('button')
    small_button_2.textContent = 'Dumpster diving'
    small_button_2.className = 'button'
    small_button_2.addEventListener('click', async (evt) => {
        await get_diving();
        await shark_moving(player_name_input.value, -1);
        await update_stats();
        diving_modal.style.display = 'block';
    });

    const small_button_3 = document.createElement('button')
    small_button_3.textContent = 'Go to the next airport'
    small_button_3.className = 'button'
    small_button_3.addEventListener('click', async (evt) => {
        clear_map();
        button_to_airport();

    });
    
    main_buttons_div.appendChild(small_button_1)
    main_buttons_div.appendChild(small_button_2)
    main_buttons_div.appendChild(small_button_3)
}

async function medium_tasks() {
    main_buttons_div.innerHTML = '';
    const medium_button_1 = document.createElement('button')
    medium_button_1.textContent = 'Trivia'
    medium_button_1.className = 'button'
    medium_button_1.addEventListener('click', async (evt) => {
        await get_trivia_category();
        await shark_moving(player_name_input.value, -1);
    });

    const medium_button_2 = document.createElement('button')
    medium_button_2.textContent = 'Go to the next airport'
    medium_button_2.className = 'button'
    medium_button_2.addEventListener('click', async (evt) => {
        clear_map();
        button_to_airport();
    });
    
    main_buttons_div.appendChild(medium_button_1)
    main_buttons_div.appendChild(medium_button_2)
}




async function large_tasks() {
    main_buttons_div.innerHTML = '';
    const large_button_1 = document.createElement('button')
    large_button_1.textContent = 'Gambling'
    large_button_1.className = 'button'
    large_button_1.addEventListener('click', async (evt) => {
        await getBalance();
        await shark_moving(player_name_input.value, -1);
        gambling_modal.style.display = 'block';
    });

    // const large_button_2 = document.createElement('button')
    // large_button_2.textContent = 'Lollipop'
    // large_button_2.className = 'button'
    // large_button_2.addEventListener('click', async (evt) => {
        
    //     await shark_moving(player_name_input.value, -1);
    //     return;
    // });

    const large_button_3 = document.createElement('button')
    large_button_3.textContent = 'Go to the next airport'
    large_button_3.className = 'button'
    large_button_3.addEventListener('click', async (evt) => {
        clear_map();
        button_to_airport();
    });
    
    main_buttons_div.appendChild(large_button_1)
    // main_buttons_div.appendChild(large_button_2)
    main_buttons_div.appendChild(large_button_3)
}

async function check_shark() {
    let current_stats = await update_stats();
    if (current_stats.shark <= 0) {
        if (current_stats.inventory > 0) {
            shark_gets_hit(current_stats.name);
        }
        else if (current_stats.money < 10000) {
            ending('bad_shark')
        } else {
            ending('good_shark')
        }
    }
}

async function button_to_airport() {
    main_buttons_div.innerHTML = '';
    
    const airport_list = await airport_selection()
    const airport_1_button = document.createElement('button')
    airport_1_button.textContent = airport_list.airport_1.name
    airport_1_button.className = 'button'
    airport_1_button.addEventListener('click', async (evt) => {
        await random_event();
        await shark_moving(player_name_input.value, 1);
        
        await update_stats();
        
        small_tasks();
        
        
    })
    const airport_2_button = document.createElement('button')
    airport_2_button.textContent = airport_list.airport_2.name
    airport_2_button.className = 'button'
    airport_2_button.addEventListener('click', async (evt) => {
        await random_event();
        await shark_moving(player_name_input.value, 1);

        await update_stats();
        medium_tasks();
    })
    const airport_3_button = document.createElement('button')
    airport_3_button.textContent = airport_list.airport_3.name
    airport_3_button.className = 'button'
    airport_3_button.addEventListener('click', async (evt) => {
        await random_event();
        await shark_moving(player_name_input.value, 1);
        await update_stats();
        large_tasks();
    })
    main_buttons_div.appendChild(airport_1_button)
    main_buttons_div.appendChild(airport_2_button)
    main_buttons_div.appendChild(airport_3_button)
    await check_shark();
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
        if (name_taken.exists == true) {
            error_p.textContent = ('Name already taken, please choose another name');
            return;
        } else if (player_name == '') {
            error_p.textContent = ('Please enter a name');
            return;
        } else {
            error_p.textContent = '';
            const start_game = await fetch(`http://127.0.0.1:4000/start/start_game/${player_name}/${difficulty}`);
            const start_game_json = await start_game.json();
            start_modal.style.display = 'none';
            await update_stats();
            await button_to_airport();
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
