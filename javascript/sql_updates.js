'use strict';
async function shark_moving(player_name, amount) {
    const response = await fetch(`http://127.0.0.1:4000/sql/update_shark/${player_name}/${amount}`, {
        method: 'POST'
    });
    const shark_json = await response.json();
    console.log(shark_json);
}