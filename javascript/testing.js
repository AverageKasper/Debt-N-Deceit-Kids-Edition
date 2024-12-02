//http://127.0.0.1:4000/sql/check_name/<name>
//http://127.0.0.1:4000/sql/fly/<airport_type>
//http://127.0.0.1:4000/random/event
//http://127.0.0.1:4000/small/dive
//http://127.0.0.1:4000/start/start_game/<name>/<difficulty>



'use strict';

const testing_p = document.getElementById('testing_p');
const testing_button = document.getElementById('testing_button');

testing_button.addEventListener('click', async (evt) => {
    const response = await fetch('http://127.0.0.1:4000/start/start_game/testing/EASY');
    const data = await response.json();
    console.log(data);



});